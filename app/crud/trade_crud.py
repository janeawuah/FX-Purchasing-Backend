from sqlalchemy.orm import Session
from models import Trade
from schemas import TradeSchema, RequestTrade,Request,Response

def get_trade(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Trade).offset(skip).limit(limit).all()

def get_trade_by_id(db: Session, trade_id: int):
    return db.query(Trade).filter(Trade.id == trade_id).first()

def create_trade(db: Session, trade:TradeSchema):
    _trade= Trade(exchange_rate=trade.name,email=trade.email, phone_number = trade.phone_number)
    db.add(_trade)
    db.commit()
    db.refresh(_trade)
    return _trade

def remove_trade(db: Session, trade_id: int):
    _trade = get_trade_by_id(db=db, trade_id=trade_id)
    db.delete(_trade)
    db.commit()


def update_trade_details(db: Session, trade_id: int, name: str, email: str, phone_number: str):
    _trade= get_trade_by_id(db=db, trade_id=trade_id)
    _trade.name = name
    _trade.email = email
    _trade.phone_number = phone_number
    db.commit()
    db.refresh(_trade)
    return _trade