from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from pydantic import BaseModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Revath*12",
    database="details"
)


cursor = db.cursor(dictionary=True)


class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image_url: str
    catalog_id: int
    


@app.get("/products")
def get_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()


@app.get("/products/{id}")
def get_product(id: int):
    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/products/name/{name}")
def get_product(name: str):
    cursor.execute("SELECT * FROM products WHERE name=%s", (name,))
    product = cursor.fetchone()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/products/catalog/{catalog_id}")
def get_products_by_catalog_id(catalog_id: int):
    cursor.execute("SELECT * FROM products WHERE catalog_id=%s", (catalog_id,))
    products = cursor.fetchall()
    if not products:
        raise HTTPException(status_code=404, detail="Products not found for catalog ID")
    return products


@app.get("/products/category/{category}")
def get_products_by_category(category: str):
    cursor.execute("SELECT * FROM products WHERE category=%s", (category,))
    products = cursor.fetchall()
    if not products:
        raise HTTPException(status_code=404, detail="Products not found for this Category")
    return products


@app.post("/products")
def add_product(product: Product):
    cursor.execute("INSERT INTO products (name, description, price, category, image_url, catalog_id) VALUES (%s, %s, %s, %s, %s, %s)", (product.name, product.description, product.price, product.category, product.image_url, product.catalog_id))
    db.commit()
    return {"message": "Product added successfully"}


@app.put("/products/{id}")
def update_product(id: int, product: Product):
    cursor.execute("UPDATE products SET name=%s, description=%s, price=%s, category=%s, image_url=%s, catalog_id=%s WHERE id=%s", (product.name, product.description, product.price, product.category, product.image_url, product.catalog_id, id))
    db.commit()
    return {"message": "Product updated successfully"}


@app.delete("/products/{id}")
def delete_product(id: int):
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    db.commit()
    return {"message": "Product deleted successfully"}



