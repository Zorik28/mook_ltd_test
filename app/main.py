from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(title=settings.app_title)


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
