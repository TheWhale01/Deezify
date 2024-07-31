from pydantic import BaseModel

class SongBase(BaseModel):
    song_id: str
    queue_id: int
    service: int

class SongCreate(SongBase):
    pass

class Song(SongCreate):
    id: int

    class Config:
        from_attributes = True
