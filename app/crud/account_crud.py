from sqlalchemy.orm import Session
from models import Account
from schemas import AccountSchema, RequestAccount,Request,Response

def get_account(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Account).offset(skip).limit(limit).all()

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def create_account(db: Session, account:AccountSchema):
    _account= account(name=account.name,email=account.email, phone_number = account.phone_number)
    db.add(_account)
    db.commit()
    db.refresh(_account)
    return _account

def remove_account(db: Session, account_id: int):
    _account = get_account_by_id(db=db, account_id=account_id)
    db.delete(_account)
    db.commit()


def update_account_details(db: Session, account_id: int, name: str, email: str, phone_number: str):
    _account= get_account_by_id(db=db, account_id=account_id)
    _account.name = name
    _account.email = email
    _account.phone_number = phone_number
    db.commit()
    db.refresh(_account)
    return _account