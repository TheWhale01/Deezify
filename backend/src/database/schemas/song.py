from pydantic import BaseModel

class SongBase(BaseModel):
    song_id: str
    queue_id: int
    service: int
    added_by_user: int
    title: str
    artist: str
    cover: str

class SongCreate(SongBase):
    pass

class Song(SongCreate):
    id: int

    class Config:
        from_attributes = True
