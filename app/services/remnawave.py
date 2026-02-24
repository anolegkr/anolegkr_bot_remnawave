import httpx
from app.core.config import settings
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class RemnawaveClient:
    def __init__(self):
        self.base_url = settings.REMNAWAVE_API_URL.rstrip("/")
        self.api_key = settings.REMNAWAVE_API_KEY
        self.verify_ssl = settings.REMNAWAVE_VERIFY_SSL
        self._client: Optional[httpx.AsyncClient] = None
    
    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                verify=self.verify_ssl,
                timeout=30.0
            )
        return self._client
    
    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        client = await self._get_client()
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = await client.request(
                method,
                f"{self.base_url}{endpoint}",
                headers=headers,
                **kwargs
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Remnawave API error: {e}")
            raise
    
    async def create_user(self, telegram_id: int, username: str) -> Dict[str, Any]:
        """Создать пользователя в Remnawave"""
        return await self._request("POST", "/users", json={
            "telegram_id": telegram_id,
            "username": username
        })
    
    async def get_user(self, user_id: int) -> Dict[str, Any]:
        """Получить пользователя"""
        return await self._request("GET", f"/users/{user_id}")
    
    async def get_user_keys(self, user_id: int) -> Dict[str, Any]:
        """Получить ключи пользователя"""
        return await self._request("GET", f"/users/{user_id}/keys")
    
    async def create_key(self, user_id: int, key_name: str = "Main") -> Dict[str, Any]:
        """Создать ключ доступа"""
        return await self._request("POST", f"/users/{user_id}/keys", json={
            "name": key_name
        })
    
    async def create_subscription(self, user_id: int, plan_id: str) -> Dict[str, Any]:
        """Создать подписку"""
        return await self._request("POST", "/subscriptions", json={
            "user_id": user_id,
            "plan_id": plan_id
        })
    
    async def get_subscription(self, subscription_id: int) -> Dict[str, Any]:
        """Получить подписку"""
        return await self._request("GET", f"/subscriptions/{subscription_id}")
    
    async def get_stats(self) -> Dict[str, Any]:
        """Получить статистику панели"""
        return await self._request("GET", "/stats")
    
    async def close(self):
        """Закрыть HTTP клиент"""
        if self._client and not self._client.is_closed:
            await self._client.aclose()


# Глобальный экземпляр
remnawave = RemnawaveClient()