from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse

# Сначала определяем не-i18n шаблоны URL
urlpatterns = [
    # Встроенный обработчик переключения языков
    path('i18n/', include('django.conf.urls.i18n')),
]

def health_check(request):
    return HttpResponse("OK")

# Затем добавляем i18n шаблоны URL
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('', include('landing.urls', namespace='landing')),
    prefix_default_language=False,
)

# Обработка статических и медиа файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)