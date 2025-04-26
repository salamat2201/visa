#!/bin/bash

set -e

# Вывод информации о подключении к базе данных для отладки
echo "Информация о подключении к базе данных:"
echo "PGHOST: $PGHOST"
echo "PGPORT: $PGPORT"
echo "PGUSER: $PGUSER"
echo "PGDATABASE: $PGDATABASE"

# Проверка доступности базы данных
echo "Ожидание готовности базы данных..."
export PGPASSWORD=$POSTGRES_PASSWORD

# Задержка перед первой проверкой
sleep 5

# Попытка подключения к базе данных
until pg_isready -h "$PGHOST" -p "$PGPORT" -U "$PGUSER"; do
  >&2 echo "База данных еще не доступна - ожидание..."
  sleep 5
done
echo "База данных готова!"

# Применение миграций
echo "Применение миграций базы данных..."
python manage.py migrate --noinput

# Сбор статических файлов
echo "Сбор статических файлов..."
python manage.py collectstatic --noinput

# Создание суперпользователя
echo "Проверка существования суперпользователя..."
python -c "
import os
from django.contrib.auth import get_user_model
User = get_user_model()
DJANGO_SUPERUSER_USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
DJANGO_SUPERUSER_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
DJANGO_SUPERUSER_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')

if not User.objects.filter(username=DJANGO_SUPERUSER_USERNAME).exists():
    print('Создание суперпользователя...')
    User.objects.create_superuser(
        username=DJANGO_SUPERUSER_USERNAME,
        email=DJANGO_SUPERUSER_EMAIL,
        password=DJANGO_SUPERUSER_PASSWORD
    )
    print(f'Суперпользователь {DJANGO_SUPERUSER_USERNAME} создан')
else:
    print(f'Суперпользователь {DJANGO_SUPERUSER_USERNAME} уже существует')
"

# Запуск Gunicorn
echo "Запуск Gunicorn..."
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2 --timeout 120