from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    token = Column(String, unique=True, index=True, nullable=False)
    service = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    party_id: Mapped[int] = mapped_column(ForeignKey('parties.id', ondelete="SET NULL"), nullable=True)
    
    party: Mapped["Party"] = relationship(back_populates='members', foreign_keys=[party_id])
    owned_party: Mapped["Party"] = relationship(back_populates='owner', uselist=False, foreign_keys="[Party.owner_id]", cascade='all, delete')


class Party(BaseModel):
    __tablename__ = 'parties'

    name = Column(String, unique=True, nullable=False, index=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, unique=True)
    
    owner: Mapped[User] = relationship(back_populates='owned_party', foreign_keys=[owner_id])
    members: Mapped[list[User]] = relationship(back_populates='party', foreign_keys='[User.party_id]')
    queue: Mapped['Queue'] = relationship(back_populates='party', foreign_keys='[Queue.party_id]', uselist=False, cascade='all, delete')

class Queue(BaseModel):
    __tablename__ = 'queues'

    party_id: Mapped[int] = mapped_column(ForeignKey('parties.id'), nullable=False, unique=True)

    party: Mapped[Party] = relationship(back_populates='queue', uselist=False, cascade="all, delete")
    songs: Mapped[list["Song"]] = relationship(back_populates='queue', foreign_keys='[Song.queue_id]', cascade='all, delete')

class Song(BaseModel):
    __tablename__ = 'songs'

    song_id: Mapped[str] = mapped_column(nullable=False)
    service: Mapped[int] = mapped_column()
    queue_id: Mapped[Queue] = mapped_column(ForeignKey('queues.id', ondelete='CASCADE'), nullable=True)

    queue: Mapped[Queue] = relationship(back_populates='', foreign_keys=[queue_id])
