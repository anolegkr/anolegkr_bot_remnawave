import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.core.config import settings
from app.core.database import init_db
from app.core.logger import setup_logger
from app.bot.handlers import start_router, menu_router, subscribe_router, donate_router, admin_router

logger = setup_logger()


async def main():
    # Инициализация БД
    await init_db()
    logger.info("✅ База данных инициализирована")
    
    # Создание бота
    bot = Bot(
        token=settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    
    dp = Dispatcher()
    
    # Регистрация всех роутеров
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(subscribe_router)
    dp.include_router(donate_router)
    dp.include_router(admin_router)
    
    logger.info("✅ Роутеры зарегистрированы")
    
    # Установка webhook (если нужен)
    if settings.WEBHOOK_URL:
        await bot.set_webhook(settings.WEBHOOK_URL)
        logger.info(f"🔗 Webhook установлен: {settings.WEBHOOK_URL}")
    else:
        await bot.delete_webhook()
        logger.info("🔗 Webhook удалён, используем polling")
    
    # Запуск
    logger.info("🚀 Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
