from fastapi import FastAPI
from app.entities import models
from app.database.config import engine
from app.database import router

trader.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def home():
    return "Welcome SecondStaxx FX Trading"

app.include_router(router.router,prefix="/trade", tags=["FX-Trade"])