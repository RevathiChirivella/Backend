from fastapi import FastAPI
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8000"       
#     "http://localhost:3000"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# cnx = mysql.connector.connect(user='root',password='Revath*12', host='localhost', database='details')
# cursor = cnx.cursor()

@app.get("/search/{query}")
def search(query: str):
    try:
        cnx = mysql.connector.connect(user='root',password='Revath*12', host='localhost', database='details')
        cursor = cnx.cursor()
        query=f"SELECT * FROM products WHERE name LIKE '%{query}%' or description LIKE '%{query}%' or category LIKE '%{query}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(str(e))
        return []
    finally:
        cursor.close()
        cnx.close()


    
    # query = f"%{query}%"
    # cursor.execute("SELECT * FROM products WHERE name LIKE '%s' OR description LIKE '%s', (query,query)")
    # results = [{"id":row[0], "name":row[1], "description":row[2], "price":row[3], "category":row[4], "image_url":row[5]} for row in cursor.fetchall()]
    # return {"results":results}




