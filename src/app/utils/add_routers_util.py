from fastapi import FastAPI

from src.routers import tron_router


def add_routers(app: FastAPI) -> None:
    app.include_router(tron_router, prefix="/tron_info", tags=["Tron"])
