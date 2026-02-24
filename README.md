# 🤖 anolegkr_bot_remnawave

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Credits](https://img.shields.io/badge/Credits-%20CREDITS-blue)](CREDITS.md)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-3776AB.svg?logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-✅-2496ED.svg?logo=docker)](https://docker.com)
[![Remnawave API](https://img.shields.io/badge/Remnawave-API-green.svg)](https://docs.rw)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> 🚀 Современный Telegram-бот для управления VPN-подписками на базе Remnawave Panel  
> 🔐 Полностью независимая реализация с чистого листа (clean room design)

<p align="center">
  <img src="docs/assets/preview.png" alt="Bot Preview" width="600"/>
</p>

---

## 📋 Оглавление

- [✨ Особенности](#-особенности)
- [🏗️ Архитектура](#️-архитектура)
- [🚀 Быстрый старт](#-быстрый-старт)
- [⚙️ Настройка](#️-настройка)
- [🔌 Интеграции](#-интеграции)
- [🛠️ Разработка](#️-разработка)
- [🤝 Contributing](#-contributing)
- [📜 Лицензия](#-лицензия)
- [🙏 Благодарности](#-благодарности)

---

## ✨ Особенности

### 🎯 Для пользователей
| Функция | Описание |
|---------|----------|
| 📱 **Telegram MiniApp** | Удобный веб-интерфейс прямо в Telegram |
| 💳 **Гибкая оплата** | CryptoBot, Platega, YooKassa, Stripe (настраивается) |
| 🔑 **Мгновенная выдача** | Ключи VLESS/Hysteria2/Xray сразу после оплаты |
| 🌍 **Мультиязычность** | Русский 🇷🇺 / English en |
| 📊 **Личный кабинет** | Статус подписки, трафик, продление, рефералы |

### ⚙️ Для администратора
| Функция | Описание |
|---------|----------|
| 🎛️ **Админ-панель** | Управление пользователями, рассылки, статистика |
| 🔗 **Remnawave API** | Полная синхронизация через официальный REST API |
| 📈 **Метрики** | Prometheus/Grafana, логирование в JSON |
| 🔄 **Auto-deploy** | Docker Compose + GitHub Actions CI/CD |
| 🔐 **Безопасность** | Rate limiting, валидация, mTLS, secrets management |

---

## 🏗️ Архитектура

```mermaid
graph LR
    A[Telegram User] --> B[aiogram 3.x Bot]
    B --> C[FastAPI Backend]
    C --> D[(PostgreSQL)]
    C --> E[(Redis Cache)]
    C --> F[Remnawave API]
    C --> G[Payment Providers]
    F --> H[Remnawave Panel]
    G --> I[CryptoBot/Platega]
    
    style A fill:#e1f5fe
    style B fill:#fff9c4
    style C fill:#e8f5e9
    style F fill:#f3e5f5
    style H fill:#ffebee

```
## 📁 Структура проекта
my-vpn-bot/  
├── 📁 app/  
│   ├── 📁 core/          # Config, logger, database, security  
│   ├── 📁 bot/           # aiogram handlers, keyboards, filters  
│   ├── 📁 api/           # FastAPI routers (webhooks, admin)  
│   ├── 📁 services/      # Business logic: payments, remnawave, notifications  
│   ├── 📁 models/        # SQLAlchemy models + migrations  
│   └── 📁 utils/         # Helpers, validators, i18n  
├── 📁 locales/           # i18n: ru/LC_MESSAGES, en/LC_MESSAGES  
├── 📁 docs/              # Architecture diagrams, API specs  
├── 📁 tests/             # pytest + aiohttp test suite  
├── 📄 docker-compose.yml # Production-ready orchestration  
├── 📄 .env.example       # Configuration template  
├── 📄 pyproject.toml     # Poetry dependencies + linting config  
└── 📄 CREDITS.md         # Third-party attributions  

## 👥 Сообщества

Присоединяйся к нашим чатам для обсуждений, поддержки и обновлений:

| Сообщество | Описание | Ссылка |
|------------|----------|--------|
| 🤖 **Наш бот | Обсуждение бота, фичреквесты, помощь по настройке | [t.me/anolegkr_bot_remnawave](https://t.me/anolegkr_bot_remnawave) |
| ⚙️ **Remnawave Official** | Официальное сообщество панели, анонсы, документация | [t.me/remnawave](https://t.me/remnawave) |

> 💡 **Совет**: В нашем чате можно задать вопрос по интеграции, в официальном — узнать о новых функциях панели.  

🚀 Быстрый старт 
▶️ Через Docker Compose (рекомендуется)
```
# 1. Клонируй репозиторий
git clone https://github.com/anolegkr/pet-project/tree/main/telegram_bot_for_remnawave
cd telegram_bot_for_remnawave

# 2. Настрой окружение
cp .env.example .env
# 👉 Отредактируй .env под свои нужды

# 3. Запусти стек
docker compose up -d

# 4. Проверь логи
docker compose logs -f bot
```
🐍 Локальная разработка
```
# Требуется Python 3.13+ и Poetry
curl -sSL https://install.python-poetry.org | python3 -

poetry install --with dev
poetry run alembic upgrade head
poetry run python -m app.main
```
⚙️ Настройка
🔑 Основные переменные (.env)
```
# 🤖 Telegram
BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
ADMIN_IDS=123456789,987654321

# 🗄️ Database
DATABASE_URL=postgresql+asyncpg://user:pass@postgres:5432/vpnbot
REDIS_URL=redis://redis:6379/0

# 🔗 Remnawave Integration
REMNAWAVE_API_URL=https://your-panel.domain/api/v1
REMNAWAVE_API_KEY=rw_live_xxxxxxxxxxxxxx
REMNAWAVE_VERIFY_SSL=true

# 💳 Payments (включай нужные)
CRYPTOBOT_TOKEN=xxx
PLATEGA_API_KEY=xxx
# YOOKASSA_SHOP_ID=xxx

# 🌐 Web & Security
WEBHOOK_URL=https://bot.yourdomain.com/webhook
SECRET_KEY=your-super-secret-jwt-key-here
LOG_LEVEL=INFO
```
💡 Совет: Используй ```openssl rand -hex 32``` для генерации SECRET_KEY
🔄 Применение изменений
```
# Пересобрать контейнеры
docker compose up -d --build

# Применить миграции БД
docker compose exec bot alembic upgrade head

# Перезагрузить конфиг без даунтайма
docker compose exec bot pkill -HUP -f "python -m app"
```
🔌 Интеграции
Remnawave API
Бот работает только через официальный публичный API Remnawave Panel [docs.rw](https://docs.rw/)]:
```
Endpoint | Метод | Назначение
/api/v1/users | POST | Создание пользователя
/api/v1/users/{id}/keys | GET | Получение конфигураций
/api/v1/subscriptions | POST | Управление подписками
/api/v1/stats | GET| Сбор метрик для аналитики
```
🔐 Аутентификация: Bearer Token в заголовке Authorization
Платежные системы
```
# Пример подключения нового провайдера (services/payments/base.py)
class PaymentProvider(ABC):
    @abstractmethod
    async def create_invoice(self, amount: float, currency: str, user_id: int) -> Invoice: ...
    
    @abstractmethod
    async def verify_webhook(self, payload: dict, signature: str) -> bool: ...
```
✅ Готовые адаптеры: CryptoBotProvider, PlategaProvider
➕ Легко добавить: YooKassa, Stripe, Coinbase Commerce

🛠️ Разработка  
🧪 Тестирование
```
# Запустить все тесты
poetry run pytest

# С покрытием
poetry run pytest --cov=app --cov-report=html

# Линтинг
poetry run black . && poetry run ruff check .
```

🌐 Webhooks & Proxy
Для работы webhook'ов за reverse proxy (nginx/Caddy):
```
# Пример nginx location
location /webhook {
    proxy_pass http://bot:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_read_timeout 90;
}
```
🔗 Домены: Поддерживает мультидоменную настройку (bot., api., miniapp.)
📦 Обновление зависимостей
```
# Безопасное обновление
poetry update --dry-run  # сначала preview
poetry update           # затем применить

# Проверка уязвимостей
poetry run pip-audit
```
🤝 Contributing
Мы приветствуем вклад сообщества! 🙌  
Fork репозитория  
Создай feature-ветку (git checkout -b feat/amazing-feature)  
Коммить с понятными сообщениями (git commit -m 'feat: add referral system')  
Push в ветку (git push origin feat/amazing-feature)  
Открой Pull Request с описанием изменений 

📋 Checklist перед PR:  
Код отформатирован (black .)  
Пройден линтинг (ruff check .)  
Добавлены/обновлены тесты  
Обновлена документация (если нужно)  
Все тесты зелёные (pytest)  

📜 Лицензия
Этот проект распространяется под лицензией MIT — см. файл [LICENSE](https://github.com/anolegkr/pet-project/blob/main/LICENSE) для деталей.  
```
⚠️ Важно: Данный проект является независимой реализацией и не аффилирован с Remnawave или BEDOLAGA-DEV.
Интеграция с Remnawave Panel осуществляется исключительно через публичный API согласно их документации.
```
  🔍 Что это значит на практике?
| ✅ Можно | ❌ Нельзя (без отдельного соглашения)
|----------|----------|
Использовать бота для себя / своей команды | Продавать бота как SaaS-сервис
Модифицировать код под свои нужды | Брать плату за хостинг "на базе этого бота"
Делиться форками с сообществом (бесплатно) | Оказывать платную поддержку/консалтинг на основе кода
Интегрировать в свои внутренние проекты | Включать функционал бота в коммерческий продукт

## Благодарности
## 🙏 Благодарности
Подробная информация об источниках вдохновения, интеграциях и используемых библиотеках доступна в файле [CREDITS.md](CREDITS.md).

