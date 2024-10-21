import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    name: str
    surename: str
    birthdate: Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    name: str
    surename: str
    birthdate: Optional[datetime.date]


class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str]
    surename: Optional[str]
    birthdate: Optional[datetime.date]
