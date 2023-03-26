from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Revath*12",
    database="details"
)

# Initialize FastAPI app
app = FastAPI()

# Define data models
class Cart(BaseModel):
    product_id: int
    user_id: int
    quantity: int

class UpdateCart(BaseModel):
    quantity: int

# Define API endpoints
@app.post("/cart")
def create_cart(cart: Cart):
    # Check if cart already exists for user_id and product_id
    cursor = db.cursor()
    query = "SELECT * FROM cart WHERE user_id=%s AND product_id=%s"
    values = (cart.user_id, cart.product_id)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result is not None:
        # If cart already exists, update the quantity
        query = "UPDATE cart SET quantity=quantity+%s WHERE user_id=%s AND product_id=%s"
        values = (cart.quantity, cart.user_id, cart.product_id)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Cart updated successfully."}
    else:
        # If cart does not exist, create a new cart entry
        query = "INSERT INTO cart (product_id, user_id, quantity) VALUES (%s, %s, %s)"
        values = (cart.product_id, cart.user_id, cart.quantity)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Cart created successfully."}

@app.put("/cart/{user_id}/{product_id}")
def update_cart(user_id: int, product_id: int, cart: UpdateCart):
    # Check if cart exists for user_id and product_id
    cursor = db.cursor()
    query = "SELECT * FROM cart WHERE user_id=%s AND product_id=%s"
    values = (user_id, product_id)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result is None:
        # If cart does not exist, raise an HTTP exception
        raise HTTPException(status_code=404, detail="Cart not found.")
    else:
        # If cart exists, update the quantity
        query = "UPDATE cart SET quantity=%s WHERE user_id=%s AND product_id=%s"
        values = (cart.quantity, user_id, product_id)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Cart Updated Successfully"}
    




@app.delete("/cart/{user_id}/{product_id}")
def delete_cart(user_id: int, product_id: int):
    # Check if cart exists for user_id and product_id
    cursor = db.cursor()
    query = "SELECT * FROM cart WHERE user_id=%s AND product_id=%s"
    values = (user_id, product_id)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result is None:
        # If cart does not exist, raise an HTTP exception
        raise HTTPException(status_code=404, detail="Cart not found.")
    else:
        # If cart exists, update the quantity
        query = "DELETE FROM cart WHERE user_id=%s AND product_id=%s"
        values = (user_id, product_id)
        cursor.execute(query, values)
        db.commit()
        return {"message": "Cart deleted Successfully"}
    


@app.get("/cart/{user_id}")
def get_cart(user_id: int):
    
    cursor = db.cursor()
    query = "SELECT * FROM cart WHERE user_id=%s"
    values = (user_id,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    if result is None:
        return []
    else:
        cart_items = []
        for row in result:
            cart_item = {"id":row[0], "product_id":row[1], "user_id": row[2], "quantity": row[3]}
            cart_items.append(cart_item)
        return cart_items

    














# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# from models import CartItem
# import models

# app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

# # Set up CORS
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dependency
# def get_db():
#     db = None
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

# @app.get("/cart")
# def get_cart(db: Session = Depends(get_db)):
#     cart_items = db.query(CartItem).all()
#     return cart_items

# @app.post("/cart")
# def add_to_cart(item: CartItem, db: Session = Depends(get_db)):
#     item=CartItem(product_name=item.product_name, quantity=item.quantity, price=item.price)
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item

# @app.put("/cart/{id}")
# def update_cart(id: int, item: CartItem, db: Session = Depends(get_db)):
#     db_item = db.query(CartItem).filter(CartItem.id == id).first()
#     if db_item:
#         db_item.product_name = item.product_name
#         db_item.quantity = item.quantity
#         db_item.price = item.price
#         db.commit()
#         db.refresh(db_item)
#         return db_item
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")

# @app.delete("/cart/{id}")
# def delete_from_cart(id: int, db: Session = Depends(get_db)):
#     db_item = db.query(CartItem).filter(CartItem.id == id).first()
#     if db_item:
#         db.delete(db_item)
#         db.commit()
#         return {"message": "Item deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")


