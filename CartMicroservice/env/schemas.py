# from pydantic import BaseModel

# class CartItemBase(BaseModel):
#     product_name: str
#     quantity: int
#     price: float

# class CartItemCreate(CartItemBase):
#     pass

# class CartItemUpdate(CartItemBase):
#     id: int

#     class Config:
#         orm_mode = True

# class CartItem(CartItemBase):
#     id: int

#     class Config:
#         orm_mode = True
