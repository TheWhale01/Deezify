from pydantic import BaseModel

class QueueBase(BaseModel):
    party_id: int

class QueueCreate(QueueBase):
    pass

class Queue(QueueCreate):
    id: int

    class Config:
        from_attributes = True
