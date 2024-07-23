from sqlalchemy.orm import Session
from database import models
from database.schemas import user as user_schema

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: user_schema.UserCreate):
    # Do I have to hash token ?
    db_user = models.User(token=user.token, service=user.service, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_from_token(db: Session, access_token: str):
	user = db.query(models.User).filter(models.User.token == access_token).first()
	db.delete(user)
	db.commit()
