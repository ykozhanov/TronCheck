async def test_get_empty_all(client, setup_db):
    response = await client.get("/api/history/")
    assert response.status_code == 200
    data = response.json()
    history = data["history"]
    assert isinstance(history, list)


async def test_get_all(client, setup_db, session, item):
    session.add(item)
    await session.commit()

    response = await client.get("/api/history/")
    assert response.status_code == 200

    data = response.json()
    history = data["history"]

    assert len(history) == 1
    assert history[0].get("address") == item.address
