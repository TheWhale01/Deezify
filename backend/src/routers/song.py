from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import models
from database.db import get_db
from dependancies import user as user_dp
from crud import song as crud
from crud import party as crud_party
from database.schemas import song as song_schema
from music_service import instance

router = APIRouter(
	prefix='/song'
)

@router.post('')
def add_song(song_id: str, db: Session = Depends(get_db), user: models.User = Depends(user_dp.get_user)):
	track: dict = instance.service.get_track(song_id)
	party = crud_party.get_party(db, user.party_id)
	device_id: str = party.device_id
	db_song = crud.create_song(db, song_schema.SongCreate(song_id=song_id, queue_id=user.party.queue.id, service=user.service, added_by_user=user.id, title=track['title'], artist=track['artist'], cover=track['cover']))
	if len(crud.get_songs(db, user.party_id)) > 1:
		try:
			instance.service.add_to_queue(song_id, device_id, party.owner.token)
		except HTTPException as e:
			crud.remove_song(db, db_song.id)
			raise e
	return db_song

@router.get(
	'',
	response_model=list[song_schema.Song]
)
def get_songs(db: Session = Depends(get_db), user: models.User = Depends(user_dp.get_user)):
	songs = crud.get_songs(db, user.party_id)
	return songs

@router.put('/init_playback')
def init_playback(song_id: str | None = None, db: Session = Depends(get_db), user: models.User = Depends(user_dp.get_user)):
	return instance.service.init_playback(db, user.party_id, song_id)

@router.put('/pause')
def pause(user: models.User = Depends(user_dp.get_user)):
	instance.service.pause(user.party.device_id)
