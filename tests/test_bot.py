import pytest
from aiogram import Bot, Dispatcher


@pytest.fixture
def bot():
    return Bot(token="test_token")


@pytest.fixture
def dp():
    return Dispatcher()


def test_bot_initialization(bot):
    assert bot is not None


def test_dispatcher_initialization(dp):
    assert dp is not None
