from sqlalchemy import Column, Integer,String
from database import Base

class userdb(Base):
    __tablename__ = "logincustomers"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(255))
    email = Column(String(255))
    password = Column(String (255))