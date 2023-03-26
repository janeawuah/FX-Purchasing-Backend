from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import AccountSchema,RequestAccount,Request,Response
from crud import account_crud

account_router = APIRouter()


def get_db():
    print("connecting to db")
    db = SessionLocal()
    print("connected to db")
    try:
        yield db
    finally:
        db.close 
        

@account_router.post('/create_account')
def create(request:RequestAccount,db:Session=Depends(get_db)):
    account_crud.create_account(db,account=request.parameter)
    return Response(code=200, status="OK", message= "Account created successfully").dict(exclude_none=True)


@account_router.get('/get_accounts')
def get(db:Session=Depends(get_db)):
    __account =account_crud.get_account(db,0,100)
    return Response(code=200,status="OK", message= "Success, fetched all Accounts",result= __account).dict(exclude_none=True)


@account_router.get('/')
def get_by_id(id:int,db:Session=Depends(get_db)):
    __account = account_crud.get_account_by_id(db,id)
    return Response(code=200,status="Ok", message= "Success, get account",result= __account).dict(exclude_none=True)

@account_router.post("/update")
def update_account(request:RequestAccount,db:Session = Depends(get_db)):
    __account= account_crud.update_account_details(db, account_id=request.parameter.id,name=request.parameter.name,email=request.parameter.email, phone_number=request.parameter.phone_number)
    return Response(code=200,status="OK",message="Successfully updated account details", result =__account)

@account_router.delete("/delete")
def delete(id:int,db:Session =Depends(get_db)):
    account_crud.remove_account(db,account_id=id)
    return Response(code=200, status="OK", message="Success, data deleted").dict(exclude_none=True)