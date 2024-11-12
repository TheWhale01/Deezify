from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from database.schemas import song as song_schema
from database import models

def create_song(db: Session, song: song_schema.SongCreate):
  db_song = models.Song(**song.model_dump())
  db.add(db_song)
  db.commit()
  db.refresh(db_song)
  return db_song

def remove_song(db: Session, id: int):
	db_song = db.query(models.Song).filter(models.Song.id == id).first()
	if db_song is None:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="No song with such id"
		)
	db.delete(db_song)
	db.commit()

def remove_song_id(db: Session, id: str):
	db_song = db.query(models.Song).filter(models.Song.song_id == id).first()
	if db_song is None:
	    raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="No song with such id"
		)
	db.delete(db_song)
	db.commit()

def get_songs(db: Session, party_id: int):
    db_songs = db.query(models.Queue).filter(models.Queue.party_id == party_id).first()
    if db_songs is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No queue for this party id'
        )
    return db_songs.songs

def get_songs_by_track_id(db: Session, track_id: str):
    db_song = db.query(models.Song).filter(models.Song.song_id == track_id).first()
    if db_song is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No track for this track_id has been found"
        )
    return db_song
