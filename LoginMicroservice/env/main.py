from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Revath*12",
    database="details"
)

class UserRegistrationRequest(BaseModel):
    email:str
    password:str


class UserRegistrationResponse(BaseModel):
    message:str


@app.post("/login", response_model=UserRegistrationResponse)
def login_user(user_request: UserRegistrationRequest):
    email = user_request.email
    password = user_request.password

    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s AND password = %s", (email, password))
    existing_user = cursor.fetchone()

    if existing_user:
        return {"message": "Logged In Successfully"}
    else:
        return {"message" : "User doesn't exist"}






































# from fastapi import FastAPI
# from fastapi import Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import SessionLocal
# import schemas, models, hashing,authorise


# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/loginuser')
# def Login_User(r : schemas.Login, db : Session = Depends(get_db)):
#     db_user = db.query(models.User).filter((models.User.email == r.email)).first()
#     if not db_user:
#         raise HTTPException(status_code = 401, detail = "Invalid email")
#     if (hashing.Hash.verify(r.password,db_user.password) ==  False):
#         raise HTTPException(status_code = 401, detail = "Wrong Password")
#     access_token = authorise.create_access_token(data={"sub" : db_user.email})
#     return {"access_token": access_token, "token_type": "bearer","message" : "Logged in Successfully"}
