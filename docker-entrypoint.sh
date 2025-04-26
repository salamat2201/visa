#!/bin/bash

# Настройка порта для Railway
export PORT=${PORT:-8000}
echo "Using port: $PORT"

# Создание директории static если её нет
mkdir -p /app/static

# Проверка наличия DATABASE_URL (для Railway)
if [ -n "$DATABASE_URL" ]; then
    echo "Using DATABASE_URL from environment"
else
    # Ожидание запуска PostgreSQL если нет DATABASE_URL
    echo "Waiting for PostgreSQL to start..."
    while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER
    do
      echo "Waiting for database connection..."
      sleep 2
    done
    
    # Установка переменной PGPASSWORD для авторизации
    export PGPASSWORD=$DB_PASSWORD
    
    # Проверка существования базы данных и её создание, если не существует
    echo "Checking if database exists..."
    DB_EXISTS=$(psql -h $DB_HOST -p $DB_PORT -U $DB_USER -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")
    if [ "$DB_EXISTS" != "1" ]; then
      echo "Database does not exist. Creating database..."
      psql -h $DB_HOST -p $DB_PORT -U $DB_USER -c "CREATE DATABASE $DB_NAME;"
    else
      echo "Database exists."
    fi
fi

# Применение миграций
echo "Applying database migrations..."
python manage.py migrate

# Компиляция переводов
echo "Compiling translations..."
python manage.py compilemessages

# Сбор статических файлов
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Создание суперпользователя если не существует
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

# Запуск сервера Gunicorn с использованием порта из переменной окружения
echo "Starting Gunicorn server on port $PORT..."
echo "Complete environment info:"
echo "DATABASE_URL: ${DATABASE_URL:-Not set}"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "Current directory: $(pwd)"
echo "Files in current directory: $(ls -la)"

# Запускаем Django с подробными логами
exec gunicorn eurowork2020.wsgi:application --bind 0.0.0.0:$PORT --timeout 120 --log-level debug