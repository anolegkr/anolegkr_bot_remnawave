import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.core.config import settings
from app.core.database import init_db
from app.bot.handlers import start, donate

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


async def main():
    # Инициализация БД
    await init_db()
    
    # Создание бота
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    
    dp = Dispatcher()
    
    # Регистрация роутеров
    dp.include_router(start.router)
    dp.include_router(donate.router)
    
    # Установка webhook (если нужен)
    if settings.WEBHOOK_URL:
        await bot.set_webhook(settings.WEBHOOK_URL)
        logger.info(f"Webhook установлен: {settings.WEBHOOK_URL}")
    else:
        await bot.delete_webhook()
        logger.info("Webhook удалён, используем polling")
    
    # Запуск
    logger.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
