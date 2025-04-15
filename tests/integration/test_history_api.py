from src.models import TronInfo


async def test_get_empty_all(client, setup_db):
    response = await client.get("/api/history/")
    assert response.status_code == 200
    data = response.json()
    history = data["history"]
    assert isinstance(history, list)


async def test_get_all(client, setup_db, session, tron_data):
    tron_model = TronInfo(**tron_data)
    session.add(tron_model)
    await session.commit()

    response = await client.get("/api/history/")
    assert response.status_code == 200

    data = response.json()
    history = data["history"]

    assert len(history) == 1
    assert history[0].get("address") == tron_model.address
