FROM python:3.13-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN pip install --no-cache-dir poetry

# Копирование файлов зависимостей
COPY pyproject.toml poetry.lock* ./

# Установка Python-зависимостей
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Копирование кода
COPY . .

# Создание папки для логов
RUN mkdir -p /app/logs

# Запуск бота
CMD ["python", "-m", "app.main"]
