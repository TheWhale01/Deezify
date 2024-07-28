from fastapi.utils import get_path_param_names
from sqlalchemy.orm import Session
from fastapi import status
from starlette.exceptions import HTTPException
from database import models
from database.schemas import party as party_schema
from crud.user import get_user_by_id

def create_party(db: Session, party: party_schema.PartyCreate, user_id: int):
	db_party = models.Party(**party.dict(), owner_id=user_id)
	db.add(db_party)
	db.commit()
	db.refresh(db_party)
	return db_party

def get_party(db: Session, party_id: int):
	return db.query(models.Party).filter(models.Party.id == party_id).first()

def delete_party(db: Session, party_id: int):
	db_party = get_party(db, party_id)
	db.delete(db_party)
	db.commit()

def add_user(db: Session, party_id: int, user_id: int):
	db_user = get_user_by_id(db, user_id)
	if db_user is None:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail='No user with such id'
		)
	db_party = get_party(db, party_id)
	if db_party is None:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail='No party with such id'
		)
	db_party.members.append(db_user)
	db.commit()
	return db_party
