from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
