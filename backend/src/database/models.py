from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, index=True, nullable=False)
    service = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    owned_party = relationship("Party", back_populates='owner', cascade="all, delete")

class Party(Base):
	__tablename__ = 'parties'

	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True, nullable=False, index=True)
	owner_id = Column(Integer, ForeignKey('users.id'), unique=True, index=True, nullable=False)
	owner = relationship("User", back_populates='owned_party')
