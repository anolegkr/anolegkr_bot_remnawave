from aiogram import Bot
from typing import List
import logging

logger = logging.getLogger(__name__)


async def notify_admins(bot: Bot, admin_ids: List[int], message: str, parse_mode: str = "Markdown"):
    """Отправить уведомление всем админам"""
    for admin_id in admin_ids:
        try:
            await bot.send_message(admin_id, message, parse_mode=parse_mode)
            logger.info(f"Уведомление отправлено админу {admin_id}")
        except Exception as e:
            logger.error(f"Не удалось отправить уведомление админу {admin_id}: {e}")


async def notify_user(bot: Bot, user_id: int, message: str, parse_mode: str = "Markdown"):
    """Отправить уведомление пользователю"""
    try:
        await bot.send_message(user_id, message, parse_mode=parse_mode)
        logger.info(f"Уведомление отправлено пользователю {user_id}")
    except Exception as e:
        logger.error(f"Не удалось отправить уведомление пользователю {user_id}: {e}")


async def notify_subscription_activated(bot: Bot, user_id: int, plan_name: str, end_date: str):
    """Уведомление об активации подписки"""
    message = (
        f"✅ **Подписка активирована!**\n\n"
        f"📦 Тариф: {plan_name}\n"
        f"📅 Действует до: {end_date}\n\n"
        f"🔑 Ваши ключи доступны в личном кабинете."
    )
    await notify_user(bot, user_id, message)


async def notify_subscription_expiring(bot: Bot, user_id: int, days_left: int):
    """Уведомление о скором окончании подписки"""
    message = (
        f"⚠️ **Подписка скоро закончится!**\n\n"
        f"Осталось дней: {days_left}\n\n"
        f"👉 Продлите подписку, чтобы не потерять доступ."
    )
    await notify_user(bot, user_id, message)


async def notify_new_donation(bot: Bot, admin_ids: List[int], user_id: int, amount: float, currency: str):
    """Уведомление админам о новом донате"""
    message = (
        f"💰 **Новый донат!**\n\n"
        f"👤 User ID: `{user_id}`\n"
        f"💵 Сумма: `{amount} {currency}`\n"
        f"🙏 Спасибо!"
    )
    await notify_admins(bot, admin_ids, message)