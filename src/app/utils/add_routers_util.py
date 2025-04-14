from fastapi import FastAPI

from src.routers import tron_info_router, history_router


def add_routers(app: FastAPI) -> None:
    app.include_router(tron_info_router, prefix="/api/tron_info", tags=["Tron Info"])
    app.include_router(history_router, prefix="/api/history", tags=["История запросов"])
