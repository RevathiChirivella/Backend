# from pydantic import BaseModel
# from typing import Union


# class Login(BaseModel):
#     email:str
#     password:str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData_User(BaseModel):
    # email : Union[str,None] = None




# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker     


# database_url="mysql+pymysql://root:Revath*12@localhost:3306/loginn"


# engine = create_engine(database_url)
# SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

# Base = declarative_base()



# from sqlalchemy import Column, Integer, String
# from database import Base


# class User(Base):
#     __tablename__='login'


#     id=Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)