from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, index=True)
    service = Column(Integer)
    username = Column(String)
    party_id = Column(Integer, ForeignKey('parties.id'), unique=True, nullable=True)
    party = relationship("Party", back_populates="members")

class Party(Base):
	__tablename__ = 'parties'

	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True, nullable=False, index=True)
	owner_id = Column(Integer, ForeignKey('users.id'), unique=True)
	owner = relationship("User", back_populates='party', uselist=False)
	members = relationship('User', back_populates="party", cascade='all,delete')
