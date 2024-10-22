from fastapi import APIRouter

from app.core.user import auth_backend, fastapi_users
from app.schemas import UserCreate, UserRead, UserUpdate

user_router = APIRouter()

user_router.include_router(
    # В роутер аутентификации
    # передается объект бэкенда аутентификации.
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)

user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)

users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
# Exclude the unnecessary handle from the list of router endpoints.
users_router.routes = [
    rout for rout in users_router.routes if rout.name not in [
        'users:delete_user', 'users:patch_user'
    ]
]
user_router.include_router(
    users_router,
    prefix='/users',
    tags=['users'],
)
