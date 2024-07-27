from fastapi import APIRouter, Depends
from database import models
from database.db import get_db
from crud import party as crud
from database.schemas import party as party_schema
from database.schemas import user as user_schema
from sqlalchemy.orm import Session
from dependancies.user import get_user

router = APIRouter(
	prefix='/party'
)

@router.get('/{party_id}')
def get_party(
	party_id: int,
	db: Session = Depends(get_db),
	user: user_schema.User = Depends(get_user)
):
	return crud.get_party(db, party_id)

@router.post('/create')
def create_party(
	party: party_schema.PartyCreate,
	db: Session = Depends(get_db),
	user: user_schema.User = Depends(get_user)
):
	return crud.create_party(db, party, user.id)
