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


@app.post("/signup", response_model=UserRegistrationResponse)
def register_user(user_request: UserRegistrationRequest):
    email = user_request.email
    password = user_request.password
    


    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        return {"message": "User with this email already exists"}
    
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    db.commit()

    return {"message" : "created"}









































# from fastapi import FastAPI
# from fastapi import Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from database import SessionLocal,engine
# import schemas, models
# import hashing
# from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# origins = [
#     "http://localhost",
#     "http://localhost:8005"       
#     "http://localhost:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )





# @app.post('/user', response_model=schemas.ShowUser, tags=['user'])
# def create_user(request:schemas.User, db: Session = Depends(get_db)):
    
#     new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user



# @app.get('/userlist', tags=['user'])
# def get_user(db: Session = Depends(get_db)):
#     userlist = db.query(models.User).all()
#     return userlist
    


# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['user'])
# def get_user(id:int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
#     return user
    