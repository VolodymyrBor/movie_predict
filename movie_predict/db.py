from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncConnection,
    create_async_engine,
)

from configs import CONFIG

engine = create_async_engine(
    CONFIG.POSTGRES_DB.build_url().build(),
)


async def init_db():
    async with engine.begin() as conn:  # type: AsyncConnection
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    session_fabric = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with session_fabric() as session:
        yield session
