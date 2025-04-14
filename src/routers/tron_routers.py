from typing import Optional, Annotated

from fastapi import APIRouter, Depends, Query

from src.services import AsyncHistoryService, AsyncTronInfoService
from src.app.dependencies import get_async_history_service, get_async_tron_info_service
from src.schemas import TronInfoCreateSchema, TronInfoRequest, HistoryResponseSchema

router = APIRouter()


@router.get(
    "/",
    response_model=HistoryResponseSchema,
    responses={
        200: {"description": "Успешный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_history_query(
    offset: Annotated[
        Optional[int],
        Query(
            description="Для пагинации. Сколько записей пропустить. По умолчанию 0 - не пропускать записи."
        ),
    ] = 0,
    limit: Annotated[
        Optional[int],
        Query(
            description="Для пагинации. Сколько записей получить. По умолчанию None - получить все записи."
        ),
    ] = None,
    history_info_service: AsyncHistoryService = Depends(get_async_history_service),
) -> HistoryResponseSchema:
    return await history_info_service.get_all(offset, limit)


@router.post(
    "/",
    response_model=TronInfoCreateSchema,
    responses={
        200: {"description": "Успешный запрос"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_tron_info(
    tron_info_request: TronInfoRequest,
    tron_info_service: AsyncTronInfoService = Depends(get_async_tron_info_service),
    history_info_service: AsyncHistoryService = Depends(get_async_history_service),
) -> TronInfoCreateSchema:
    tron_info = await tron_info_service.get_base_info(tron_info_request.address)
    await history_info_service.create(tron_info)
    return tron_info
