import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import dotenv
import dj_database_url

# Загрузка переменных окружения из .env файла
dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-key-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't', 'yes')

# Разрешаем доступ к приложению с Railway домена
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,*.railway.app').split(',')

# Настройка порта для Railway
PORT = int(os.environ.get('PORT', 8000))

# Application definition
INSTALLED_APPS = [
    'modeltranslation',  # Должен быть перед админкой
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Сторонние приложения
    'crispy_forms',
    'crispy_tailwind',
    
    # Наши приложения
    'landing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Для обработки статических файлов
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Для многоязычности
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eurowork2020.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eurowork2020.wsgi.application'

# Database
# Упрощенная настройка базы данных через dj-database-url
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 365  # Один год
LANGUAGE_COOKIE_PATH = '/'

# Доступные языки
LANGUAGES = (
    ('ru', _('Русский')),
    ('uz', _('Узбекский')),
    ('tg', _('Таджикский')),
    ('ky', _('Киргизский')),
)

# Пути к файлам перевода
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Модельный перевод - формат суффиксов для полей
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []

# Проверяем и добавляем директорию static если она существует
static_dir = os.path.join(BASE_DIR, 'static')
if os.path.exists(static_dir):
    STATICFILES_DIRS.append(static_dir)

# Настройка для WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройка Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Настройки сообщений
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Настройки безопасности для продакшн
if not DEBUG:
    # Дополнительные настройки безопасности для продакшена
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 год
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Настройки защиты от атак
    X_FRAME_OPTIONS = 'DENY'
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# Настройки логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# Создание директории для логов
logs_dir = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Настройки для отправки почты
EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND', 
    'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@example.com')

# Настройки кеширования
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'eurowork-cache',
    }
}

# В settings.py
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')