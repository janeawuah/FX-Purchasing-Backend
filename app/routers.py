from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestTrader,RequestAccount,RequestTrade,Response
import crud

router = APIRouter()


def get_db():
    print("connecting to db")
    db = SessionLocal()
    print("connected to db")
    try:
        yield db
    finally:
        db.close 
        
             
#Trader
@router.post('/create_trader')
def create(request:RequestTrader,db:Session=Depends(get_db)):
    _trader = crud.get_trader_by_email(db, trader_email = request.parameter.email)
    if _trader:
        raise HTTPException(status_code=400, detail="Email already registered")
    crud.create_trader(db,trader=request.parameter)
    return Response(code=200, status="OK", message= "Trader created successfully").dict(exclude_none=True)


@router.get('/get_traders')
def get(db:Session=Depends(get_db)):
    __trader =crud.get_trader(db,0,100)
    return Response(code=200,status="OK", message= "Success, fetched all traders",result= __trader).dict(exclude_none=True)


@router.get('/get_trader')
def get_by_id(id:int,db:Session=Depends(get_db)):
    __trader = crud.get_trader_by_id(db,id)
    return Response(code=200,status="Ok", message= "Success, get data",result= __trader).dict(exclude_none=True)

@router.post("/update_trader")
def update_trader(request:RequestTrader,db:Session = Depends(get_db)):
    __trader= crud.update_trader_details(db, trader_id=request.parameter.id,name=request.parameter.name,email=request.parameter.email, phone_number=request.parameter.phone_number)
    return Response(code=200,status="OK",message="Successfully updated trader details", result =__trader)

@router.delete("/delete_trader")
def delete(id:int,db:Session =Depends(get_db)):
    crud.remove_trader(db,trader_id=id)
    return Response(code=200, status="OK", message="Success, data deleted").dict(exclude_none=True)  
        
#Trade
@router.post('/create_trade')
def create(request:RequestTrade,db:Session=Depends(get_db)):
    crud.create_trade(db,trade=request.parameter)
    return Response(code=200, status="OK", message= "Trade created successfully").dict(exclude_none=True)


@router.get('/get_trades')
def get(db:Session=Depends(get_db)):
    __trade =crud.get_trade(db,0,100)
    return Response(code=200,status="OK", message= "Success, fetched all trades",result= __trade).dict(exclude_none=True)


@router.get('/get_trade_status')
def get_trade_status(id:int,db:Session=Depends(get_db)):
    __trade = crud.get_trade_status(db,id)
    return Response(code=200,status="Ok", message= "Success, get data",result= __trade).dict(exclude_none=True)

@router.get('/get_trade')
def get_by_id(id:int,db:Session=Depends(get_db)):
    __trade = crud.get_trade_by_id(db,id)
    return Response(code=200,status="Ok", message= "Success, get data",result= __trade).dict(exclude_none=True)

@router.post("/update_trade")
def update_trade(request:RequestTrade,db:Session = Depends(get_db)):
    __trade= crud.update_trade_details(db, trade_id=request.parameter.id,date=request.parameter.date,trader=request.parameter.trader,
        source_amount=request.parameter.source_amount,target_amount=request.parameter.target_amount,status=request.parameter.status)
    return Response(code=200,status="OK",message="Successfully updated trade details", result =__trade)


@router.post("/update_trade_status")
def update_trade_status(request:RequestTrade,db:Session = Depends(get_db)):
    __trade_status= crud.update_trade_status(db, status=request.parameter.status)
    return Response(code=200,status="OK",message="Successfully updated trade details", result =__trade_status)

@router.delete("/delete_trade")
def delete(id:int,db:Session =Depends(get_db)):
    crud.remove_trade(db,trade_id=id)
    return Response(code=200, status="OK", message="Success, data deleted").dict(exclude_none=True)

#Account
@router.post('/create_account')
def create(request:RequestAccount,db:Session=Depends(get_db)):
    crud.create_account(db,account=request.parameter)
    return Response(code=200, status="OK", message= "Account created successfully").dict(exclude_none=True)


@router.get('/get_accounts')
def get(db:Session=Depends(get_db)):
    __account =crud.get_account(db,0,100)
    return Response(code=200,status="OK", message= "Success, fetched all Accounts",result= __account).dict(exclude_none=True)


@router.get('/get_account')
def get_by_id(id:int,db:Session=Depends(get_db)):
    __account = crud.get_account_by_id(db,id)
    return Response(code=200,status="Ok", message= "Success, get account details",result= __account).dict(exclude_none=True)

@router.post("/update_account_balance")
def update_account_balance(request:RequestAccount,db:Session = Depends(get_db)):
    __account_balance= crud.update_account_balance(db, account_id=request.parameter.id,account_balance=request.parameter.account_balance)
    return Response(code=200,status="OK",message="Successfully updated account balance", result =__account_balance)

@router.post("/update_account")
def update_account(request:RequestAccount,db:Session = Depends(get_db)):
    __account= crud.update_account_details(db, account_id=request.parameter.id,name=request.parameter.name,email=request.parameter.email, phone_number=request.parameter.phone_number)
    return Response(code=200,status="OK",message="Successfully updated account details", result =__account)

@router.delete("/delete_account")
def delete(id:int,db:Session =Depends(get_db)):
    crud.remove_account(db,account_id=id)
    return Response(code=200, status="OK", message="Success, data deleted").dict(exclude_none=True)