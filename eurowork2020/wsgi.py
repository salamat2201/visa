# eurowork2020/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eurowork2020.settings')

# Печать для отладки
print("Initializing WSGI application...")

application = get_wsgi_application()

# Печать для подтверждения, что WSGI приложение создано
print("WSGI application initialized successfully")