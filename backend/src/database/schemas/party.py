from pydantic import BaseModel

class User(BaseModel):
	id: int
	token: str
	service: int
	username: str

	class Config:
		from_attributes = True

class PartyBase(BaseModel):
	name: str

class PartyCreate(PartyBase):
	pass

class Party(PartyCreate):
	id: int
	device_id: str

	class Config:
		from_attributes = True
