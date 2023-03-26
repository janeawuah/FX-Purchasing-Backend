from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')



class CurrencySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True


class RequestCurrency(BaseModel):
    parameter: CurrencySchema = Field(...)
    
 
class ExchangeRateSchema(BaseModel):
    id: Optional[int] = None
    source_currency: Optional[int] = None
    target_currency: Optional[int] = None
    rate: Optional[int] = None

    class Config:
        orm_mode = True


class RequestExchangeRate(BaseModel):
    parameter: ExchangeRateSchema = Field(...)
    

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
    trader:Optional[str]=None
    exchange_rate: Optional[int] = None
    source_total: Optional[int] = None
    target_total: Optional[int] = None

    class Config:
        orm_mode = True
        
class RequestTrade(BaseModel):
    parameter: TradeSchema = Field(...)
    
class AccountSchema(BaseModel):
    id: Optional[int] = None
    account_balance: Optional[int] = None
    currency: Optional[str] = None
    trader_id: Optional[str] = None

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
