from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger, Float
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True, nullable=False)
    username = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    language_code = Column(String(10), default="ru")
    
    # Подписка
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    subscription_end = Column(DateTime, nullable=True)
    subscription_plan = Column(String(50), nullable=True)
    
    # Баланс (для внутренней системы)
    balance = Column(Float, default=0.0)
    
    # Remnawave
    remnawave_user_id = Column(Integer, nullable=True)
    
    # Статистика
    total_spent = Column(Float, default=0.0)
    referral_code = Column(String(50), unique=True, nullable=True)
    referred_by = Column(BigInteger, nullable=True)
    
    # Временные метки
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username={self.username})>"