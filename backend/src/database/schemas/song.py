from pydantic import BaseModel
from database.schemas.user import User

class SongBase(BaseModel):
    song_id: str
    queue_id: int
    added_by_user: int
    service: int
    title: str
    artist: str
    cover: str

class SongCreate(SongBase):
    pass

class Song(SongCreate):
    id: int
    added_by: User

    class Config:
        from_attributes = True
