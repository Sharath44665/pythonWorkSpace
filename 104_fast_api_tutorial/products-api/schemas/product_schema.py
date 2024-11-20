from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    title:str
    category:str
    price: float
    description: Optional[str]=None


class ProductCreate(ProductBase):
    pass 

class ProductUpdate(ProductBase):
    pass 


class Product(ProductBase):
    id: str

    class Config:
        orm_mode: True
        


