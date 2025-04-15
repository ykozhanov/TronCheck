from typing import Optional, Annotated

from fastapi import APIRouter, Depends, Query

from src.services import AsyncHistoryService
from src.app.dependencies import get_async_history_service
from src.schemas import (
    HistoryResponseSchema,
    ExceptionSchema,
    ResponseSchema,
)
from src.exceptions import HistoryPaginatorBadRequestException

router = APIRouter()


@router.get(
    "/",
    summary="Получить историю запросов",
    response_model=HistoryResponseSchema,
    responses={
        200: {"description": "Успешный запрос"},
        400: {"description": "Некорректный запрос", "model": ExceptionSchema},
        422: {"description": "Ошибка валидации данных", "model": ExceptionSchema},
        500: {"description": "Внутренняя ошибка сервера", "model": ResponseSchema},
    },
)
async def get_history_query(
    offset: Annotated[
        Optional[int],
        Query(
            description="Для пагинации.\n\n\nСколько записей пропустить.\n\nПо умолчанию 0 - не пропускать записи."
        ),
    ] = 0,
    limit: Annotated[
        Optional[int],
        Query(
            description="Для пагинации.\n\n\nСколько записей получить.\n\nПо умолчанию null - получить все записи."
        ),
    ] = None,
    history_info_service: AsyncHistoryService = Depends(get_async_history_service),
) -> HistoryResponseSchema:
    """Получить историю запросов информации о Tron аккаунте"""
    if offset < 0:
        raise HistoryPaginatorBadRequestException(offset=offset, info="Offset не может быть меньше 0")
    if limit and limit <= 0:
        raise HistoryPaginatorBadRequestException(limit=limit, info="Limit не может быть меньше 1")

    return await history_info_service.get_all(offset, limit)
