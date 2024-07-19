from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    service = Column(Integer)
    username = Column(String)

class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True)

