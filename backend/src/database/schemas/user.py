from pydantic import BaseModel

class Party(BaseModel):
	id: int
	name: str

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

	class Config:
		from_attributes = True
