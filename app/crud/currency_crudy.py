from sqlalchemy.orm import Session
from models import Currency
from schemas import CurrencySchema, RequestCurrency,Request,Response

def get_all_currency(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Currency).offset(skip).limit(limit).all()

def get_currency_by_id(db: Session, currency_id: int):
    return db.query(Currency).filter(Currency.id == currency_id).first()

def create_currency(db: Session, currency:CurrencySchema):
    _currency= currency(name=currency.name)
    db.add(_currency)
    db.commit()
    db.refresh(_currency)
    return _currency

def remove_currency(db: Session, currency_id: int):
    _currency = get_currency_by_id(db=db, currency_id=currency_id)
    db.delete(_currency)
    db.commit()


def update_currency_details(db: Session, currency_id: int, name: str):
    _currency= get_currency_by_id(db=db, currency_id=currency_id)
    _currency.name = name
    db.commit()
    db.refresh(_currency)
    return _currency