import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from aiogram import Bot, Dispatcher
from aiogram.types import Message, User


@pytest.fixture
def bot():
    return Bot(token="test_token")


@pytest.fixture
def dp():
    return Dispatcher()


@pytest.fixture
def mock_user():
    return User(
        id=123456789,
        is_bot=False,
        first_name="Test",
        username="testuser"
    )


@pytest.fixture
def mock_message(bot, mock_user):
    return Message(
        message_id=1,
        date=1234567890,
        chat=mock_user,
        from_user=mock_user,
        text="/start"
    )


def test_bot_initialization(bot):
    assert bot is not None
    assert bot.token == "test_token"


def test_dispatcher_initialization(dp):
    assert dp is not None


@pytest.mark.asyncio
async def test_start_command(mock_message):
    # Тест команды /start
    assert mock_message.text == "/start"
    assert mock_message.from_user.id == 123456789


@pytest.mark.asyncio
async def test_database_connection():
    # Тест подключения к БД
    from app.core.database import engine
    assert engine is not None


@pytest.mark.asyncio
async def test_config_loading():
    # Тест загрузки конфига
    from app.core.config import settings
    assert settings.BOT_TOKEN is not None
    assert settings.DATABASE_URL is not None
