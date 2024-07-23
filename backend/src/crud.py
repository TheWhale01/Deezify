from sqlalchemy.orm import Session
import models, schemas

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Do I have to hash token ?
    db_user = models.User(token=user.token, service=user.service, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
