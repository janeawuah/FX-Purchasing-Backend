from fastapi import FastAPI
from config import engine
import models
from routers.route_trader import trade_router

app = FastAPI()

@app.get('/')
async def home():
    return "Welcome SecondStaxx FX Trading"

app.include_router(trade_router, prefix="/trader", tags=['trader'])
# app.include_router(router, prefix="/trader", tags=['trader'])