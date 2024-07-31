from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from database import models
from database.schemas import party as party_schema
from database.schemas import queue as queue_schema
from crud.user import get_user_by_id
from crud.queue import create_queue

def create_party(db: Session, party: party_schema.PartyCreate, user_id: int):
	db_party = models.Party(**party.model_dump())
	db_user = get_user_by_id(db, user_id)
	db_party.owner_id = db_user.id
	db_party.members.append(db_user)
	db.add(db_party)
	db.commit()
	db_queue = create_queue(db, queue_schema.QueueCreate(party_id=db_party.id))
	db_party.queue = db_queue
	db.add(db_party)
	db.commit()
	db.refresh(db_party)
	return db_party

def get_party(db: Session, party_id: int):
	db_party = db.query(models.Party).filter(models.Party.id == party_id).first()
	if db_party is None:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail='No party with such id'
		)
	return db_party

def delete_party(db: Session, party_id: int, user: models.User):
	db_party = get_party(db, party_id)
	if db_party.owner_id != user.id:
		raise HTTPException(
				status_code=status.HTTP_401_UNAUTHORIZED, 
				detail="You are not the owner of this party"
		)
	db.delete(db_party)
	db.commit()

def add_user(db: Session, party_id: int, user_id: int):
	db_user = get_user_by_id(db, user_id)
	db_party = get_party(db, party_id)
	db_party.members.append(db_user)
	db.commit()
	return db_party
