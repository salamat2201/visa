FROM python:3.11-slim

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . /app/

# Создаём директории
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Даём права на исполнение entrypoint
RUN chmod +x /app/docker-entrypoint.sh

# Открываем порт (Railway использует PORT из переменных окружения)
EXPOSE 8000

# Запускаем entrypoint скрипт
ENTRYPOINT ["/app/docker-entrypoint.sh"]