from .start import router as start_router
from .menu import router as menu_router
from .subscribe import router as subscribe_router
from .donate import router as donate_router
from .admin import router as admin_router

__all__ = [
    "start_router",
    "menu_router",
    "subscribe_router",
    "donate_router",
    "admin_router",
]
