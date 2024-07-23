from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
	id: int
	token: str
	service: int
	username: str
	party: Optional["Party"]

	class Config:
		from_attributes = True

class PartyBase(BaseModel):
	name: str

class PartyCreate(PartyBase):
	owner_id: int

class Party(PartyCreate):
	id: int
	owner: 'User'
	members: list['User'] = []

	class Config:
		from_attributes = True
