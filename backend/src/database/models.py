from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.base import Mapped
from database.db import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    token = Column(String, unique=True, index=True, nullable=False)
    service = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    party_id = Column(Integer, ForeignKey('parties.id'))

    owned_party = relationship("Party", back_populates='owner', uselist=False)

class Party(BaseModel):
	__tablename__ = 'parties'

	name = Column(String, unique=True, nullable=False, index=True)
	owner_id = Column(Integer, ForeignKey('users.id'))

	owner = relationship("User", back_populates='owned_party')
	members = relationship("User")
