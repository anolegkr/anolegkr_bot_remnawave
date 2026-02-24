from aiogram import Router, F
from aiogram.types import CallbackQuery, LabeledPrice
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class SubscriptionState(StatesGroup):
    waiting_for_payment = State()


PRICES = {
    "sub_1m": 299,
    "sub_3m": 799,
    "sub_6m": 1399,
    "sub_12m": 2499,
}

NAMES = {
    "sub_1m": "1 месяц",
    "sub_3m": "3 месяца",
    "sub_6m": "6 месяцев",
    "sub_12m": "12 месяцев",
}


@router.callback_query(F.data.startswith("sub_"))
async def process_subscription(callback: CallbackQuery, state: FSMContext):
    plan = callback.data
    price = PRICES.get(plan, 0)
    name = NAMES.get(plan, "Подписка")
    
    await state.update_data(plan=plan, price=price)
    
    await callback.bot.send_invoice(
        chat_id=callback.from_user.id,
        title=f"🔑 VPN Подписка — {name}",
        description=f"Доступ к VPN на {name}",
        payload=f"sub_{callback.from_user.id}_{plan}",
        provider_token="",  # Для Stars
        currency="XTR",     # Telegram Stars
        prices=[LabeledPrice(label=name, amount=price * 10)],  # Stars * 10
        start_parameter="subscribe",
    )
    await callback.answer()
    await state.set_state(SubscriptionState.waiting_for_payment)


@router.pre_checkout_query()
async def process_pre_checkout(callback: CallbackQuery):
    await callback.answer(ok=True)


@router.message(F.successful_payment)
async def process_successful_payment(message: Message, state: FSMContext):
    data = await state.get_data()
    plan = data.get("plan", "sub_1m")
    name = NAMES.get(plan, "Подписка")
    
    # TODO: Здесь вызов Remnawave API для создания ключа
    # await remnawave.create_subscription(...)
    
    await message.answer(
        f"✅ **Оплата прошла успешно!**\n\n"
        f"Тариф: {name}\n"
        f"Ключи генерируются...\n\n"
        f"⏳ Ожидайте, ключи придут в течение 1-2 минут.",
        parse_mode="Markdown"
    )
    await state.clear()
