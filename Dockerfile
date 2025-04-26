FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копирование зависимостей и их установка
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . /app/

# Создание директорий для статических и медиа файлов
RUN mkdir -p /app/staticfiles /app/media

# Права на выполнение entrypoint скрипта
COPY docker-entrypoint.sh /app/
RUN chmod +x /app/docker-entrypoint.sh

# Порт, который будет доступен извне
EXPOSE 8000

# Запуск entrypoint скрипта
ENTRYPOINT ["/app/docker-entrypoint.sh"]
