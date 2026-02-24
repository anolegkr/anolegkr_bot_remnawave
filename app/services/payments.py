from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class PaymentProvider(ABC):
    @abstractmethod
    async def create_invoice(self, amount: float, currency: str, user_id: int) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        pass


class CryptoBotProvider(PaymentProvider):
    def __init__(self, token: str):
        self.token = token
    
    async def create_invoice(self, amount: float, currency: str, user_id: int) -> Dict[str, Any]:
        # TODO: Реализация через CryptoBot API
        return {"invoice_url": "https://t.me/CryptoBot"}
    
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        # TODO: Валидация подписи
        return True


class PlategaProvider(PaymentProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def create_invoice(self, amount: float, currency: str, user_id: int) -> Dict[str, Any]:
        # TODO: Реализация через Platega API
        return {"invoice_url": "https://platega.com"}
    
    async def verify_webhook(self, payload: dict, signature: str) -> bool:
        # TODO: Валидация подписи
        return True
