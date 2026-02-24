from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.bot.keyboards.main_menu import get_main_menu_keyboard

router = Router()


@router.callback_query(F.data == "my_keys")
async def show_my_keys(callback: CallbackQuery):
    await callback.message.edit_text(
        text="🔑 **Мои ключи**\n\n"
             "Здесь будут ваши VPN-ключи после оформления подписки.\n\n"
             "👉 Сначала оформите подписку в меню.",
        reply_markup=get_main_menu_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "subscription")
async def show_subscription(callback: CallbackQuery):
    await callback.message.edit_text(
        text="💳 **Подписка**\n\n"
             "Выберите тариф для подключения:\n\n"
             "• 1 месяц — 299₽\n"
             "• 3 месяца — 799₽\n"
             "• 6 месяцев — 1399₽\n"
             "• 12 месяцев — 2499₽",
        reply_markup=get_subscription_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "stats")
async def show_stats(callback: CallbackQuery):
    await callback.message.edit_text(
        text="📊 **Ваша статистика**\n\n"
             "📅 Подписка активна до: —\n"
             "📈 Трафик: 0 / 100 GB\n"
             "🔑 Ключей: 0\n\n"
             "Оформите подписку для активации.",
        reply_markup=get_main_menu_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "help")
async def show_help(callback: CallbackQuery):
    await callback.message.edit_text(
        text="
