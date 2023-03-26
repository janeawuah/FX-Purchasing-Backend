from sqlalchemy import Column,Integer, String,ForeignKey
from config import Base


class Trader(Base):
    __tablename__ = 'trader'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    phone_number=Column(String)
    
    
class Trade(Base):
    __tablename__ = 'trade'
    
    id=Column(Integer,primary_key=True)
    date=Column(String)
    trader_id=Column(Integer,ForeignKey("trader.id", ondelete="CASCADE"))
    currencies= Column(String)
    source_amount=Column(Integer)
    target_amount=Column(Integer)
    status=Column(String)
    
    
class Account(Base):
    __tablename__ = 'account'
    
    id=Column(Integer,primary_key=True)
    account_balance=Column(Integer)
    currency=Column(String)
    trader_id=Column(Integer, ForeignKey("trader.id", ondelete="CASCADE"))
    