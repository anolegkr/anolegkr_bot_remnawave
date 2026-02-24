from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(text="🔑 Мои ключи", callback_data="my_keys")
    builder.button(text="💳 Подписка", callback_data="subscription")
    builder.button(text="📊 Статистика", callback_data="stats")
    builder.button(text="💖 Поддержать", callback_data="donate_menu")
    builder.button(text="❓ Помощь", callback_data="help")
    
    builder.adjust(2, 2, 1)
    return builder.as_markup()


def get_admin_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(text="👥 Пользователи", callback_data="admin_users")
    builder.button(text="📢 Рассылка", callback_data="admin_broadcast")
    builder.button(text="📈 Статистика", callback_data="admin_stats")
    
    builder.adjust(2, 1)
    return builder.as_markup()
