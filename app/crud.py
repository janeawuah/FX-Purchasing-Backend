from sqlalchemy.orm import Session
from models import Trade,Trader,Account
from schemas import TraderSchema,TradeSchema,AccountSchema, RequestTrade, Request,Response

#crud for trader
def get_trader(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Trader).offset(skip).limit(limit).all()

def get_trader_by_id(db: Session, trader_id: int):
    return db.query(Trader).filter(Trader.id == trader_id).first()

def get_trader_by_email(db: Session, trader_email: str):
    return db.query(Trader).filter(Trader.email == trader_email).first()

def create_trader(db: Session, trader:TraderSchema):
    _trader= Trader(full_name=trader.full_name,email=trader.email, disabled = trader.disabled)
    db.add(_trader)
    db.commit()
    db.refresh(_trader)
    return _trader

def remove_trader(db: Session, trader_id: int):
    _trader = get_trader_by_id(db=db, trader_id=trader_id)
    db.delete(_trader)
    db.commit()

def update_trader_details(db: Session, trader_id: int, full_name: str, email: str, disabled: bool):
    _trader= get_trader_by_id(db=db, trader_id=trader_id)
    _trader.full_name = full_name
    _trader.email = email
    _trader.disabled = disabled
    db.commit()
    db.refresh(_trader)
    return _trader

#crud for trade
def get_trade(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Trade).offset(skip).limit(limit).all()

def get_trade_by_id(db: Session, trade_id: int):
    return db.query(Trade).filter(Trade.id == trade_id).first()

def create_trade(db: Session, trade:TradeSchema):
    _trade= Trade(date=trade.date,trader_id=trade.trader_id,currencies=trade.currencies, source_amount=trade.source_amount,target_amount=trade.target_amount, status=trade.status)
    db.add(_trade)
    db.commit()
    db.refresh(_trade)
    return _trade

def remove_trade(db: Session, trade_id: int):
    _trade = get_trade_by_id(db=db, trade_id=trade_id)
    db.delete(_trade)
    db.commit()

def update_trade_details(db: Session, trade_id: int, date: str, currencies: str,source_amount:str,target_amount:str,status:str):
    _trade= get_trade_by_id(db=db, trade_id=trade_id)
    _trade.date = date
    _trade.trader = trade_id
    _trade.currencies = currencies
    _trade.source_amount = source_amount
    _trade.target_amount = target_amount
    _trade.status = status
    
    db.commit()
    db.refresh(_trade)
    return _trade

def update_trade_status(db: Session, trade_id: int, status:str):
    _account=get_trade_by_id(db=db, trade_id=trade_id)
    _account.status = status
    db.commit()
    db.refresh(_account)
    return _account

def get_trade_status(db:Session,trade_id:int):
    _trader=db.query(Trade).filter(Trade.id == trade_id).first()
    _trader_dict=_trader.__dict__
    return _trader_dict["status"]

#crud for account
def get_account(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Account).offset(skip).limit(limit).all()

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first().status

def create_account(db: Session, account:AccountSchema):
    _account=Account(account_balance=account.account_balance, currency=account.currency, trader_id = account.trader_id)
    db.add(_account)
    db.commit()
    db.refresh(_account)
    return _account

def update_account_balance(db: Session, account_id: int, account_balance:int):
    _account=get_account_by_id(db=db, account_id=account_id)
    _account.account_balance = account_balance
    db.commit()
    db.refresh(_account)
    return _account
    

def remove_account(db: Session, account_id: int):
    _account = get_account_by_id(db=db, account_id=account_id)
    db.delete(_account)
    db.commit()

def update_account_details(db: Session, account_id: int, account_balance: int=None, currency: str=None, trader_id: int=None,status:str=None):
    _account= get_account_by_id(db=db, account_id=account_id)
    if account_balance!=None:
        _account.account_balance = account_balance
    if currency!=None:
        _account.currency = currency
    if trader_id!=None:
        _account.trader_id = trader_id
    if status!=None:
        _account.status = status
    db.commit()
    db.refresh(_account)
    return _account