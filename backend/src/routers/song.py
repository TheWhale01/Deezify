from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import models
from database.db import get_db
from dependancies import user as user_dp
from crud import song as crud
from database.schemas import song as song_schema

router = APIRouter(
    prefix='/song'
)

@router.post('')
def add_song(song_id: str, db: Session = Depends(get_db), user: models.User = Depends(user_dp.get_user)):
    db_song = crud.create_song(db, song_schema.SongCreate(song_id=song_id, queue_id=user.party.queue.id, service=user.service))
    return db_song
