from sqlalchemy.orm import Session
from database import models
from database.schemas import user as user_schema
from fastapi import HTTPException, status

def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='No user with such id'
        )
    return db_user

def get_user_by_token(db: Session, access_token: str):
    db_user = db.query(models.User).filter(models.User.token == access_token).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='No user with such token'
        )
    return db_user

def create_user(db: Session, user: user_schema.UserCreate):
    # Do I have to hash token ?
    db_user = models.User(token=user.token, service=user.service, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_from_token(db: Session, access_token: str):
    user = get_user_by_token(db, access_token)
    db.delete(user)
    db.commit()
