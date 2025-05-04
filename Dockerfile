FROM python:3.11-slim

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Установка рабочей директории
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    netcat-traditional \
    libpq-dev \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копирование проекта
COPY . /app/

# Убедимся, что директория для статических файлов существует
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Компиляция файлов переводов
RUN django-admin compilemessages

# Настройка entrypoint
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]