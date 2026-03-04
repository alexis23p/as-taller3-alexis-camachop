from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image_url: Optional[str] = None


class ProductOut(ProductBase):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CartOut(BaseModel):
    id: int
    user_id: int
    items: List[CartItemBase] = []

    class Config:
        orm_mode = True
