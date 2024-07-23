from pydantic import BaseModel
from typing import Optional

class Party(BaseModel):
	id: int
	name: str
	owner: 'User'
	members: list['User'] = []

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
	party: Optional[Party]

	class Config:
		from_attributes = True
