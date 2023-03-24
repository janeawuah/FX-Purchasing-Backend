from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import TraderSchema,RequestTrader,Request,Response
from crud import trader_crud

trade_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close 
        

@trade_router.post('/create_trader')
def create(request:RequestTrader,db:Session=Depends(get_db)):
    trader_crud.create_trader(db,trader=request.parameter)
    return Response(code=200, status="OK", message= "Trader created successfully").dict(exclude_none=True)


@trade_router.get('/get_traders')
def get(db:Session=Depends(get_db)):
    __trader =trader_crud.get_trader(db,0,100)
    return Response(code=200,status="OK", message= "Success, fetched all traders",result= __trader).dict(exclude_none=True)


@trade_router.get('/')
def get_by_id(id:int,db:Session=Depends(get_db)):
    __trader = trader_crud.get_trader_by_id(db,id)
    return Response(code=200,status="Ok", message= "Success, get data",result= __trader).dict(exclude_none=True)

@trade_router.post("/update")
def update_trader(request:RequestTrader,db:Session = Depends(get_db)):
    __trader= trader_crud.update_trader_details(db, trader_id=request.parameter.id,name=request.parameter.name,email=request.parameter.email, phone_number=request.parameter.phone_number)
    return Response(code=200,status="OK",message="Successfully updated trader details", result =__trader)

@trade_router.delete("/delete")
def delete(id:int,db:Session =Depends(get_db)):
    trader_crud.remove_trader(db,trader_id=id)
    return Response(code=200, status="OK", message="Success, data deleted").dict(exclude_none=True)