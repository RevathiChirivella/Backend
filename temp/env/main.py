from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
import models,schemas
from database import engine,SessionLocal
from models import userdb


app= FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(db: Session, r:schemas.User):
     db_user = userdb(name=r.name, email=r.email, password=r.password)
     db.add(db_user)
     db.commit()
     db.refresh(db_user)
     return db_user


@app.post("/signup") 
def signup(r:schemas.User,db: Session= Depends (get_db)):
     db_user= db.query(userdb).filter(userdb.email == r.email).first()
     if db_user:
          raise HTTPException(status_code=400, detail="email already registered")
     elif "@gmail.com" not in r.email:
          return {"message": "email format wrong"}
     elif len(r.password) < 8:
          return {"message": "Required 8 characters"}
     else:
          return create_user(db,r)



@app.post("/login")
def login (request: schemas.User, db: Session =Depends (get_db)):
      db_user = db.query(userdb).filter(userdb.email == request.email).first()
      if not db_user:
            raise HTTPException(status_code = 401, detail="Invalid email or password")
      if db_user.password != request.password:
            raise HTTPException(status_code=401, detail="Invalid username or password")
      return {"message": "Login successful"}
