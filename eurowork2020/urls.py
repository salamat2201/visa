from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import views  # Импортируем наш новый файл views.py

# Сначала определяем не-i18n шаблоны URL
urlpatterns = [
    # Здесь есть маршрут для переключения языков
    path('i18n/', include('django.conf.urls.i18n')),
    # Добавляем маршрут для проверки здоровья
    path('health/', views.health_check, name='health_check'),
]

# Затем добавляем i18n шаблоны URL
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('landing.urls', namespace='landing')),
    prefix_default_language=False,
)

# Обработка статических и медиа файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)