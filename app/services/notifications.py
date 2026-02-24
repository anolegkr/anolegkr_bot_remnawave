from aiogram import Bot
from typing import List
import logging

logger = logging.getLogger(__name__)


async def notify_admins(bot: Bot, admin_ids: List[int], message: str):
    """Отправить уведомление всем админам"""
    for admin_id in admin_ids:
        try:
            await bot.send_message(admin_id, message, parse_mode="Markdown")
        except Exception as e:
            logger.error(f"Не удалось отправить уведомление админу {admin_id}: {e}")


async def notify_user(bot: Bot, user_id: int, message: str, parse_mode: str = "Markdown"):
    """Отправить уведомление пользователю"""
    try:
        await bot.send_message(user_id, message, parse_mode=parse_mode)
    except Exception as e:
        logger.error(f"Не удалось отправить уведомление пользователю {user_id}: {e}")
