#!/bin/bash

set -e

# Проверка доступности базы данных
echo "Ожидание готовности базы данных..."
export PGPASSWORD=$POSTGRES_PASSWORD
until psql -h "$PGHOST" -U "$PGUSER" -d "$PGDATABASE" -c '\q'; do
  >&2 echo "База данных еще не доступна - ожидание..."
  sleep 2
done
echo "База данных готова!"

# Применение миграций
echo "Применение миграций базы данных..."
python manage.py migrate --noinput

# Сбор статических файлов
echo "Сбор статических файлов..."
python manage.py collectstatic --noinput

# Запуск Gunicorn
echo "Запуск Gunicorn..."
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2 --timeout 120