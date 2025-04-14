import pytest
from src.models import TronInfo


@pytest.mark.asyncio
async def test_get_all(client, override_get_session, item):
    async with override_get_session() as session:
        session.add(item)
        await session.commit()

    response = await client.get(
        "/api/history/",
    )

    assert response.status_code == 200
    data = response.json()
    tron_info_elem: TronInfo = data["history"][0]
    assert tron_info_elem.address == new_tron_info.address
    assert "id" in data
