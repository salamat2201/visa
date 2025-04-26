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

# Запуск Gunicorn
echo "Запуск Gunicorn..."
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2 --timeout 120