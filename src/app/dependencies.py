from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from src.repositories import (
    AsyncTronpyTronInfoRepository,
    AsyncSQLAlchemyHistoryRepository,
)
from src.services import AsyncHistoryService, AsyncTronInfoService
from src.core.db import get_session
from src.core.config import get_settings

settings = get_settings()


def get_async_history_service(
    db: AsyncSession = Depends(get_session),
) -> AsyncHistoryService:
    async_history_repository = AsyncSQLAlchemyHistoryRepository(db)
    return AsyncHistoryService(async_history_repository)


def get_async_tron_info_service() -> AsyncTronInfoService:
    async_tron_client = AsyncTron(AsyncHTTPProvider(
        endpoint_uri=settings.API_TRON_URL,
        api_key=settings.API_TRON_KEY
    ))
    async_tron_info_repository = AsyncTronpyTronInfoRepository(async_tron_client)
    return AsyncTronInfoService(async_tron_info_repository)
