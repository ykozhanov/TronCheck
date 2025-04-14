from fastapi import FastAPI
from src.app.utils import add_routers, add_exception_handlers

app = FastAPI(
    title="TronInfo",
    description="Микросервис для получения информации о кошельках в сети Tron (TRX), "
    "включая баланс, bandwidth и energy, с сохранением истории запросов.",
    version="0.1.0",
)

add_exception_handlers(app)
add_routers(app)
