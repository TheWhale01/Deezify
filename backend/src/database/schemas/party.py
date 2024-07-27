from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
	id: int
	token: str
	service: int
	username: str
	owned_party: Optional["Party"]

	class Config:
		from_attributes = True

class PartyBase(BaseModel):
	name: str

class PartyCreate(PartyBase):
	pass

class Party(PartyCreate):
	id: int
	owner_id: int
	owner: 'User'
	# members: list['User'] = []

	class Config:
		from_attributes = True
