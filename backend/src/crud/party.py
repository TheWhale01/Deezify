from sqlalchemy.orm import Session
from database import models
from database.schemas import party as party_schema

def create_party(db: Session, party: party_schema.PartyCreate, user_id: int):
	db_party = models.Party(**party.dict(), owner_id=user_id)
	db.add(db_party)
	db.commit()
	db.refresh(db_party)
	return db_party

def get_party(db: Session, party_id: int):
	return db.query(models.Party).filter(models.Party.id == party_id).first()
