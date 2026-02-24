from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_donate_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="💎 CryptoBot",
        url="https://t.me/CryptoBot?start=pay_anolegkr"
    )
    builder.button(
        text="💳 Platega",
        url="https://platega.com/donate/anolegkr"
    )
    builder.button(
        text="₮ USDT (TON)",
        url="https://tonviewer.com/UQCH23YxmTL24zWrKlPxLj27vjTN2iGqBBVNtlB2p3gMVUkX"
    )
    builder.button(
        text="◎ USDT (SOL)",
        url="https://solscan.io/account/8cBYzax34BiSRAMTJM3yKdmsdK8kyeDVzycNVnggCFWR"
    )
    builder.button(text="🔙 Назад", callback_data="main_menu")
    
    builder.adjust(2, 2, 1)
    return builder.as_markup()
