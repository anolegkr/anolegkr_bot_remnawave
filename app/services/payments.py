from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from app.core.config import settings
import logging
import hashlib
import hmac

logger = logging.getLogger(__name__)


class PaymentProvider(ABC):
    """Базовый класс для платежных провайдеров"""
    
    @abstractmethod
    async def create_invoice(self, amount: float, currency: str, user_id: int, description: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        pass


class CryptoBotProvider(PaymentProvider):
    """CryptoBot (@CryptoBot) провайдер"""
    
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://pay.cryptobot.ru/api"
    
    async def create_invoice(self, amount: float, currency: str, user_id: int, description: str) -> Dict[str, Any]:
        """Создать инвойс в CryptoBot"""
        import httpx
        
        headers = {"X-CryptoBot-ApiToken": self.token}
        payload = {
            "amount": amount,
            "currency": currency,
            "description": description,
            "paid_btn_name": "OpenBot",
            "paid_btn_url": f"https://t.me/anolegkr_bot_remnawave"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/createInvoice",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            
            return {
                "invoice_id": data.get("result", {}).get("invoice_id"),
                "invoice_url": data.get("result", {}).get("pay_url"),
                "status": data.get("result", {}).get("status")
            }
    
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        """Проверить подпись вебхука от CryptoBot"""
        # CryptoBot использует HMAC-SHA256
        expected_signature = hmac.new(
            self.token.encode(),
            str(payload).encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(expected_signature, signature)


class PlategaProvider(PaymentProvider):
    """Platega провайдер"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.platega.com/v1"
    
    async def create_invoice(self, amount: float, currency: str, user_id: int, description: str) -> Dict[str, Any]:
        """Создать инвойс в Platega"""
        import httpx
        
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "amount": amount,
            "currency": currency,
            "description": description,
            "success_url": "https://t.me/anolegkr_bot_remnawave"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/payment",
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            
            return {
                "invoice_id": data.get("id"),
                "invoice_url": data.get("payment_url"),
                "status": data.get("status")
            }
    
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        """Проверить подпись вебхука от Platega"""
        # Platega использует HMAC-SHA256
        expected_signature = hmac.new(
            self.api_key.encode(),
            str(payload).encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(expected_signature, signature)


class TelegramStarsProvider(PaymentProvider):
    """Telegram Stars (нативные платежи)"""
    
    async def create_invoice(self, amount: float, currency: str, user_id: int, description: str) -> Dict[str, Any]:
        """Для Stars инвойсы создаются через aiogram.send_invoice()"""
        return {
            "invoice_id": f"stars_{user_id}_{int(amount)}",
            "invoice_url": None,  # Stars работают внутри Telegram
            "status": "pending"
        }
    
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        """Stars не требуют проверки подписи"""
        return True


# Фабрика для получения провайдера
def get_payment_provider(provider_name: str) -> PaymentProvider:
    if provider_name == "cryptobot":
        return CryptoBotProvider(settings.CRYPTOBOT_TOKEN)
    elif provider_name == "platega":
        return PlategaProvider(settings.PLATEGA_API_KEY)
    elif provider_name == "stars":
        return TelegramStarsProvider()
    else:
        raise ValueError(f"Unknown payment provider: {provider_name}")