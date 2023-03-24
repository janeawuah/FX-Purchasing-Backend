from sqlalchemy.orm import Session
from models import Trader
from schemas import TraderSchema, RequestTrader,Request,Response

def get_trader(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Trader).offset(skip).limit(limit).all()

def get_trader_by_id(db: Session, trader_id: int):
    return db.query(Trader).filter(Trader.id == trader_id).first()

def create_trader(db: Session, trader:TraderSchema):
    _trader= Trader(name=trader.name,email=trader.email, phone_number = trader.phone_number)
    db.add(_trader)
    db.commit()
    db.refresh(_trader)
    return _trader

def remove_trader(db: Session, trader_id: int):
    _trader = get_trader_by_id(db=db, trader_id=trader_id)
    db.delete(_trader)
    db.commit()


def update_trader_details(db: Session, trader_id: int, name: str, email: str, phone_number: str):
    _trader= get_trader_by_id(db=db, trader_id=trader_id)
    _trader.name = name
    _trader.email = email
    _trader.phone_number = phone_number
    db.commit()
    db.refresh(_trader)
    return _trader