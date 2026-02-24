from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from app.bot.keyboards.main_menu import get_main_menu_keyboard
from app.models.user import User
from app.core.database import async_session_maker
from sqlalchemy import select

router = Router()


@router.command("start")
async def cmd_start(message: Message):
    # Сохраняем пользователя в БД
    async with async_session_maker() as session:
        result = await session.execute(
            select(User).where(User.telegram_id == message.from_user.id)
        )
        user = result.scalar_one_or_none()
        
        if not user:
            user = User(
                telegram_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name
            )
            session.add(user)
            await session.commit()
    
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я бот для управления VPN-подписками на базе Remnawave.\n\n"
        "Выберите действие в меню ниже 👇",
        reply_markup=get_main_menu_keyboard()
    )


@router.callback_query(F.data == "main_menu")
async def show_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="📱 Главное меню\n\nВыберите действие:",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()
