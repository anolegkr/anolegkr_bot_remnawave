import httpx
from app.core.config import settings
from typing import Optional, Dict, Any


class RemnawaveClient:
    def __init__(self):
        self.base_url = settings.REMNAWAVE_API_URL
        self.api_key = settings.REMNAWAVE_API_KEY
        self.verify_ssl = settings.REMNAWAVE_VERIFY_SSL
    
    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient(verify=self.verify_ssl) as client:
            response = await client.request(
                method,
                f"{self.base_url}{endpoint}",
                headers=headers,
                **kwargs
            )
            response.raise_for_status()
            return response.json()
    
    async def create_user(self, telegram_id: int, username: str) -> Dict[str, Any]:
        return await self._request("POST", "/users", json={
            "telegram_id": telegram_id,
            "username": username
        })
    
    async def get_user_keys(self, user_id: int) -> Dict[str, Any]:
        return await self._request("GET", f"/users/{user_id}/keys")
    
    async def create_subscription(self, user_id: int, plan: str) -> Dict[str, Any]:
        return await self._request("POST", "/subscriptions", json={
            "user_id": user_id,
            "plan": plan
        })
    
    async def get_stats(self) -> Dict[str, Any]:
        return await self._request("GET", "/stats")


remnawave = RemnawaveClient()
