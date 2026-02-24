FROM python:3.13-slim

WORKDIR /app

# Установка зависимостей
RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Копирование кода
COPY . .

# Запуск
CMD ["python", "-m", "app.main"]
