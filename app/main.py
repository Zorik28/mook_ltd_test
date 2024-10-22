from fastapi import FastAPI

from app.core.config import settings
from app.routers import user_router


app = FastAPI(title=settings.app_title)

app.include_router(user_router)
