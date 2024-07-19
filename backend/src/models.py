from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True)
    service = Column(Integer)
    username = Column(String)

    # Relationships
    party = relationship('Party')

class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("owner.id"))

    # Relationships
    owner = relationship("User")
