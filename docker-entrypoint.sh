#!/bin/bash

# Ожидание запуска PostgreSQL
echo "Waiting for PostgreSQL to start..."
while ! pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER
do
  echo "Waiting for database connection..."
  sleep 2
done

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

# Запуск команды из docker-compose
exec "$@"
