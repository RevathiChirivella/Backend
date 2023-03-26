from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import mysql.connector


# Define the product catalog database connection
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Revath*12",
    database="product_catalog"
)

# Define the FastAPI instance
app = FastAPI()

# Define the Product Catalog Model
class ProductCatalog(BaseModel):
    id: Optional[int]
    name: str

# Define the API endpoint to create a new category
@app.post("/category")
def create_category(category: ProductCatalog):
    cursor = db_conn.cursor()
    query = "INSERT INTO categories (name) VALUES (%s)"
    val = (category.name,)
    cursor.execute(query, val)
    db_conn.commit()
    cursor.close()
    return {"message": "Category created successfully!"}

# Define the API endpoint to get all categories
@app.get("/categories")
def get_all_categories():
    cursor = db_conn.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    return categories

# Define the API endpoint to get a category by ID
@app.get("/category/{category_id}")
def get_category_by_id(category_id: int):
    cursor = db_conn.cursor()
    query = "SELECT * FROM categories WHERE id = %s"
    val = (category_id,)
    cursor.execute(query, val)
    category = cursor.fetchone()
    cursor.close()
    if category is None:
        return JSONResponse(status_code=404, content={"message": "Category not found!"})
    else:
        return category
    


@app.get("/category/name/{category_name}")
def get_category_by_id(category_name: str):
    cursor = db_conn.cursor()
    query = "SELECT * FROM categories WHERE name = %s"
    val = (category_name,)
    cursor.execute(query, val)
    category = cursor.fetchone()
    cursor.close()
    if category is None:
        return JSONResponse(status_code=404, content={"message": "Category not found!"})
    else:
        return category


# Define the API endpoint to update a category by ID
@app.put("/category/{category_id}")
def update_category_by_id(category_id: int, category: ProductCatalog):
    cursor = db_conn.cursor()
    query = "UPDATE categories SET name = %s WHERE id = %s"
    val = (category.name, category_id)
    cursor.execute(query, val)
    db_conn.commit()
    cursor.close()
    return {"message": "Category updated successfully!"}


# Define the API endpoint to delete a category by ID
@app.delete("/category/{category_id}")
def delete_category_by_id(category_id: int):
    cursor = db_conn.cursor()
    query = "DELETE FROM categories WHERE id = %s"
    val = (category_id,)
    cursor.execute(query, val)
    db_conn.commit()
    cursor.close()
    return {"message": "Category deleted successfully!"}