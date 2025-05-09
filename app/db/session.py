from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

ASYNC_DATABASE_URL = settings.ASYNC_DATABASE_URL
engine_async = create_async_engine(ASYNC_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AsyncSessionLocal = sessionmaker(
    bind=engine_async,
    expire_on_commit=False,
    class_=AsyncSession
)

# async
async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# sync
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()