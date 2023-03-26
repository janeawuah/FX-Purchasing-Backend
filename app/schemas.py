import datetime
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class TraderSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True


class RequestTrader(BaseModel):
    parameter: TraderSchema = Field(...)
    
class TradeSchema(BaseModel):
    id:Optional[int]
    date:Optional[str]
    trader_id:Optional[int]=None
    currencies: Optional[str] = None
    source_amount: Optional[int] = None
    target_amount: Optional[int] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True
        
class RequestTrade(BaseModel):
    parameter: TradeSchema = Field(...)
    
class AccountSchema(BaseModel):
    id: Optional[int] = None
    account_balance: Optional[int] = None
    currency: Optional[str] = None
    trader_id: Optional[int] = None

    class Config:
        orm_mode = True
        
class RequestAccount(BaseModel):
    parameter: AccountSchema = Field(...)


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
