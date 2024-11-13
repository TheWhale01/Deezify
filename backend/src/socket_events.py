import socketio
import sys
from crud import song
from crud import user
from database.db import get_db
from sqlalchemy.orm import Session

origins = ['https://deezify.duckdns.org', 'https://api.deezify.duckdns.org']

sio = socketio.AsyncServer(cors_allowed_origins=origins, async_mode='asgi')

party_room_prefix = 'party_'

@sio.event
async def connect(sid, environ, auth):
    return True

@sio.event
async def disconnect(sid):
    return True

@sio.event
async def join_party(sid, data):
    party_id: int = data['party_id']
    await sio.enter_room(sid, f'{party_room_prefix}{party_id}')

@sio.event
async def add_track(sid, data):
    party_id: int = data['party_id']
    track_id: str = data['track_id']
    db: Session = next(get_db())
    track = song.get_songs_by_track_id(db, track_id).to_dict()
    user_db = user.get_user_by_id(db, track['added_by_user']).to_dict()
    track.update({'added_by': user_db})
    await sio.emit('track_added', data=track, skip_sid=sid, room=f'{party_room_prefix}{party_id}')

@sio.event
async def remove_track(sid, data):
    party_id: int = data['party_id']
    await sio.emit('track_removed', skip_sid=sid, room=f'{party_room_prefix}{party_id}')
