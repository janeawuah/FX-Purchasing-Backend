import datetime
from sqlalchemy import Column,Integer, String,ForeignKey
from config import Base


class Trader(Base):
    __tablename__ = 'trader'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    phone_number=Column(String)
    
    
class Currency(Base):
    __tablename__ = 'currency'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    

class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'
    
    id=Column(Integer,primary_key=True)
    source_currency=Column(String,ForeignKey("currency.name",ondelete="CASCADE"))
    target_currency=Column(String,ForeignKey("currency.name",ondelete="CASCADE"))
    date=Column(String)
    
class Trade(Base):
    __tablename__ = 'trade'
    
    id=Column(Integer,primary_key=True)
    trader=Column(Integer,ForeignKey("trader.id", ondelete="CASCADE"))
    exchange_rate= Column(Integer,ForeignKey("exchange_rates.id",ondelete="CASCADE"))
    source_total=Column(Integer)
    target_total=Column(Integer)
    
    
class Account(Base):
    __tablename__ = 'account'
    
    id=Column(Integer,primary_key=True)
    account_balance=Column(Integer)
    currency=Column(String)
    trader_id=Column(Integer, ForeignKey("trader.id", ondelete="CASCADE"))
    