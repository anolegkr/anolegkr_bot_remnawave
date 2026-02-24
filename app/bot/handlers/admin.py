from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from app.core.config import settings
from app.bot.keyboards.main_menu import get_admin_keyboard

router = Router()


@router.command("admin")
async def cmd_admin(message: Message):
    if message.from_user.id not in settings.admin_ids_list:
        await message.answer("❌ Доступ запрещён")
        return
    
    await message.answer(
        text="🎛️ **Админ-панель**\n\n"
             "Выберите действие:",
        reply_markup=get_admin_keyboard(),
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "admin_users")
async def admin_users(callback: CallbackQuery):
    if callback.from_user.id not in settings.admin_ids_list:
        await callback.answer("❌ Доступ запрещён", show_alert=True)
        return
    
    # TODO: Получить список пользователей из БД
    await callback.message.edit_text(
        text="👥 **Пользователи**\n\n"
             "Загрузка списка...\n\n"
             "📊 Всего: 0\n"
             "🟢 Активных: 0\n"
             "🔴 Неактивных: 0",
        reply_markup=get_admin_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "admin_broadcast")
async def admin_broadcast(callback: CallbackQuery):
    if callback.from_user.id not in settings.admin_ids_list:
        await callback.answer("❌ Доступ запрещён", show_alert=True)
        return
    
    await callback.message.edit_text(
        text="📢 **Рассылка**\n\n"
             "Отправьте сообщение, которое нужно разослать всем пользователям.\n\n"
             "🔙 Нажмите «Назад» для отмены.",
        reply_markup=get_admin_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data == "admin_stats")
async def admin_stats(callback: CallbackQuery):
    if callback.from_user.id not in settings.admin_ids_list:
        await callback.answer("❌ Доступ запрещён", show_alert=True)
        return
    
    await callback.message.edit_text(
        text="📈 **Статистика бота**\n\n"
             "👥 Пользователей: 0\n"
             "💰 Доход за месяц: 0₽\n"
             "🔑 Активных подписок: 0\n"
             "📊 Запросов к API: 0",
        reply_markup=get_admin_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()
