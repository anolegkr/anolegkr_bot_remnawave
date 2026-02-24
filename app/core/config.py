from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Telegram
    BOT_TOKEN: str
    ADMIN_IDS: str
    
    # Database
    DATABASE_URL: str
    REDIS_URL: str
    
    # Remnawave
    REMNAWAVE_API_URL: str
    REMNAWAVE_API_KEY: str
    REMNAWAVE_VERIFY_SSL: bool = True
    
    # Payments
    CRYPTOBOT_TOKEN: str = ""
    PLATEGA_API_KEY: str = ""
    
    # Web
    WEBHOOK_URL: str = ""
    SECRET_KEY: str
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
    
    @property
    def admin_ids_list(self) -> List[int]:
        return [int(x.strip()) for x in self.ADMIN_IDS.split(",") if x.strip()]


settings = Settings()
