from fastapi import APIRouter, Depends

from src.services import AsyncHistoryService, AsyncTronInfoService
from src.app.dependencies import get_async_history_service, get_async_tron_info_service
from src.schemas import (
    TronInfoCreateSchema,
    TronInfoRequest,
    ExceptionSchema,
    ResponseSchema,
)

router = APIRouter()


@router.post(
    "/",
    summary="Получить основную информацию об аккаунте",
    response_model=TronInfoCreateSchema,
    responses={
        200: {"description": "Успешный запрос"},
        400: {"description": "Некорректный адрес", "model": ExceptionSchema},
        404: {"description": "Адрес не найден", "model": ExceptionSchema},
        422: {"description": "Ошибка валидации данных", "model": ExceptionSchema},
        500: {"description": "Внутренняя ошибка сервера", "model": ResponseSchema},
    },
)
async def get_tron_info(
    tron_info_request: TronInfoRequest,
    tron_info_service: AsyncTronInfoService = Depends(get_async_tron_info_service),
    history_info_service: AsyncHistoryService = Depends(get_async_history_service),
) -> TronInfoCreateSchema:
    """Получить основную информацию об аккаунте: баланс, пропускная способность, энергия"""
    tron_info = await tron_info_service.get_base_info(tron_info_request.address)
    await history_info_service.create(tron_info)
    return tron_info
