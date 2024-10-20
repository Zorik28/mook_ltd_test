from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from app.core.config import settings


class PreBase:
    """
    The class with common attributes for future inheritance.

    The `__tablename__` will be the model name in lowercase.

    An `id` field will be added to all tables.
    """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)  # Base class for future models.

engine = create_async_engine(url=settings.database_url)

# Multiple session creation.
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
