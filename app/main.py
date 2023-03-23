from fastapi import FastAPI
from config import engine
import models

app = FastAPI()

@app.get('/')
async def home():
    return "Welcome SecondStaxx FX Trading"

