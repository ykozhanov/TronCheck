from unittest.mock import AsyncMock
from src.repositories import AsyncTronpyTronInfoRepository
from tronpy import AsyncTron
from src.schemas import TronAccountInfoSchema


async def test_get_account_info_returns_data():
    mock_client = AsyncTron()
    mock_client.get_account_balance = AsyncMock(return_value={
        "balance": 100.5,
        "address": "TXXXXXX",
        "create_time": 123456789,
    })

    # Чтобы мок работал в контекстном менеджере
    mock_client.__aenter__ = AsyncMock(return_value=mock_client)
    mock_client.__aexit__ = AsyncMock(return_value=None)

    repo = AsyncTronpyTronInfoRepository(mock_client)

    result = await repo.get_account_info("TXXXXXX")

    assert isinstance(result, TronAccountInfoSchema)
    assert result.balance_sun == 100.5
