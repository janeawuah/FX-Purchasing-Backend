from fastapi import Depends,FastAPI
from config import engine
from routers import router
from config import engine
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get('/')
async def home():
    return "Welcome SecondStaxx FX Trading"


app.include_router(router, prefix="/FX-trade", tags=['trade'])