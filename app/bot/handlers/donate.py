from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, LabeledPrice
from aiogram.filters import Command
from app.bot.keyboards.donate import get_donate_keyboard

router = Router()

DONATE_TEXT = """
💖 **Поддержать проект**

Этот бот развивается благодаря сообществу.
Если проект оказался полезным — вы можете отблагодарить разработчика!

Все средства идут на:
• 🖥️ Аренда серверов
• 🌐 Домены и SSL
• 🔧 API и инфраструктура
• 📚 Развитие проекта

Выберите удобный способ ниже 👇
"""


@router.command("donate")
async def cmd_donate(message: Message):
    await message.answer(
        text=DONATE_TEXT,
        reply_markup=get_donate_keyboard(),
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "donate_menu")
async def show_donate_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=DONATE_TEXT,
        reply_markup=get_donate_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()


@router.callback_query(F.data.startswith("donate_"))
async def process_donate_stars(callback: CallbackQuery):
    amount = int(callback.data.split("_")[1])
    
    await callback.bot.send_invoice(
        chat_id=callback.from_user.id,
        title="💖 Донат проекту",
        description=f"Спасибо за поддержку! {amount} Stars",
        payload=f"donate_{amount}",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="Благодарность", amount=amount)],
        start_parameter="donate"
    )
    await callback.answer()


@router.pre_checkout_query()
async def process_pre_checkout(query):
    await query.answer(ok=True)


@router.message(F.successful_payment)
async def process_payment(message: Message):
    await message.answer(
        "✅ **Спасибо за донат!**\n\n"
        "Ваша поддержка очень важна! 🙏",
        parse_mode="Markdown"
    )
