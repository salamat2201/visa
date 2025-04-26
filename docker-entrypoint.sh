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
echo "Создание суперпользователя..."
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-admin}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-admin@example.com}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-admin}

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Суперпользователь создан')
else:
    print('Суперпользователь уже существует')
"

# Запуск Gunicorn
echo "Запуск Gunicorn..."
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2 --timeout 120