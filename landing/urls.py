from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Удалена ссылка на set_language, теперь используется встроенный механизм Django
]