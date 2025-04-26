#!/bin/bash

# Получаем порт из переменной окружения или используем 8000 по умолчанию
export PORT=${PORT:-8000}
echo "Using port: $PORT"

# Создаём директории если они не существуют
mkdir -p /app/static /app/media /app/logs

# Применяем миграции
echo "Applying database migrations..."
python manage.py migrate

# Компилируем переводы
echo "Compiling translations..."
python manage.py compilemessages

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Создаём суперпользователя если он не существует
echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD');
    print('Superuser created.');
else:
    print('Superuser already exists.')
"

# Запускаем Gunicorn
echo "Starting Gunicorn server on port $PORT..."
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:$PORT --workers=2 --timeout=30