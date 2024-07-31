from sqlalchemy.orm import Session
from database.schemas import queue as queue_schema
from database import models

def create_queue(db: Session, queue: queue_schema.QueueCreate):
    db_queue = models.Queue(**queue.model_dump())
    db.add(db_queue)
    db.commit()
    db.refresh(db_queue)
    return db_queue
