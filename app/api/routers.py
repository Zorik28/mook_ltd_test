from fastapi import APIRouter

from app.api.user import router


main_router = APIRouter()

main_router.include_router(router)
