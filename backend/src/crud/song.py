from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.schemas import song as song_schema
from database import models

def create_song(db: Session, song: song_schema.SongCreate):
  db_song = models.Song(**song.model_dump())
  db.add(db_song)
  db.commit()
  db.refresh(db_song)
  return db_song

def get_songs(db: Session, party_id: int):
  db_songs = db.query(models.Queue).filter(models.Queue.party_id == party_id).first()
  if db_songs is None:
      raise HTTPException(
          status_code=404,
          detail='No queue for this party id'
      )
  return db_songs.songs

