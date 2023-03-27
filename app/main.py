from fastapi import Depends,FastAPI
from config import engine
from routers import router
from config import engine
import models
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from models import Trade 

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

models.Base.metadata.create_all(bind=engine)

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

def fake_decode_token(token):
    return Trade(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: Annotated[Trade, Depends(get_current_user)]):
    return current_user



# app.include_router(router, prefix="/FX-trade", tags=['trade'])