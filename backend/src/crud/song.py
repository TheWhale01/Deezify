from sqlalchemy.orm import Session
from database.schemas import song as song_schema
from database import models

def create_song(db: Session, song: song_schema.SongCreate):
    db_song = models.Song(**song.model_dump())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

