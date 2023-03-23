import datetime
from sqlalchemy import Column,Integer, String,ForeignKey
from config import Base



class currency(Base):
    __tablename__ = 'currency'
    
    id=Column(Integer,primary_key=True)
    name=Column
    

class ExchangeRates(Base):
    __tablename__ = 'exchange_rates'
    
    id=Column(Integer,primary_key=True)
    source_currency=Column(str,ForeignKey("currency.name",ondelete="CASCADE"))
    target_currency=Column(str,ForeignKey("currency.name",ondelete="CASCADE"))
    date=Column(datetime)

class Trader(Base):
    __tablename__ = 'trader'
    
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    phone_number=Column(String)
    
class Order(Base):
    __tablename__ = 'order'
    
    id=Column(Integer,primary_key=True)
    customer_id=Column(Integer,ForeignKey("customer.id", ondelete="CASCADE"))
    book_id=Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    quantity=Column(Integer)
    price=Column(Integer)
    
    
class Account(Base):
    __tablename__ = 'account'
    
    id=Column(Integer,primary_key=True)
    account_balance=Column(Integer)
    currency=Column(String)
    customer_id=Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"))
    
    