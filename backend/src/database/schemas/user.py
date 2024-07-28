from pydantic import BaseModel
from typing import Optional

class Party(BaseModel):
	id: int
	name: str
	owner_id: int

	class Config:
		from_attributes = True

class UserBase(BaseModel):
	token: str
	service: int
	username: str

class UserCreate(UserBase):
	pass

class User(UserCreate):
	id: int
	owned_party_id: int

	class Config:
		from_attributes = True
