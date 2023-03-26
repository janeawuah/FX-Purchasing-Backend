from sqlalchemy.orm import Session
from models import ExchangeRate
from schemas import ExchangeRateSchema, RequestExchangeRate,Request,Response

def get_exchangerate(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExchangeRate).offset(skip).limit(limit).all()

def get_exchangerate_by_id(db: Session, exchangerate_id: int):
    return db.query(ExchangeRate).filter(ExchangeRate.id == exchangerate_id).first()

def create_exchangerate(db: Session, exchangerate:ExchangeRateSchema):
    _exchangerate= exchangerate(source_currencey=exchangerate.source_currency,target_currencey=exchangerate.target_currency, rate = exchangerate.rate)
    db.add(_exchangerate)
    db.commit()
    db.refresh(_exchangerate)
    return _exchangerate

def remove_exchangerate(db: Session, exchangerate_id: int):
    _exchangerate = get_exchangerate_by_id(db=db, exchangerate_id=exchangerate_id)
    db.delete(_exchangerate)
    db.commit()


def update_exchangerate_details(db: Session, exchangerate_id: int, source_currencey: int, target_currencey: int, rate: int):
    _exchangerate= get_exchangerate_by_id(db=db, exchangerate_id=exchangerate_id)
    _exchangerate.source_currencey = source_currencey
    _exchangerate.target_currencey = target_currencey
    _exchangerate.rate = rate
    db.commit()
    db.refresh(_exchangerate)
    return _exchangerate