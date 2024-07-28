from fastapi import APIRouter, Depends
import sys
from database import models
from database.db import get_db
from crud import party as crud
from database.schemas import party as party_schema
from sqlalchemy.orm import Session
from dependancies.user import get_user

router = APIRouter(
	prefix='/party'
)

@router.get('/{party_id}')
def get_party(
	party_id: int,
	db: Session = Depends(get_db),
	user: models.User = Depends(get_user)
):
	db_party = crud.get_party(db, party_id)
	return {
		'id': db_party.id,
		'name': db_party.name,
		'owner': user.id == db_party.owner.id
	}

@router.post('/create')
def create_party(
	party: party_schema.PartyCreate,
	db: Session = Depends(get_db),
	user: models.User = Depends(get_user)
):
	return crud.create_party(db, party, user.id)

@router.delete('/{party_id}')
def delete_party(
	party_id: int,
	db: Session = Depends(get_db),
	user: models.User = Depends(get_user)
):
	crud.delete_party(db, party_id, user=user)
	return {'ok': True}

@router.put('/{party_id}/add_user')
def add_user_to_party(
	party_id: int,
	db: Session = Depends(get_db),
	user: models.User = Depends(get_user)
):
	crud.add_user(db, party_id, user.id)
