from fastapi import FastAPI
from src.app.utils import add_routers

app = FastAPI()

add_routers(app)
