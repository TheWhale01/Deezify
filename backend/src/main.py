from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.login.spotify import auth as sp_auth
from routers.login.deezer import auth as dz_auth
from routers import user
from routers import party
from routers import search
from routers import song
from database.db import engine, Base
from socket_events import origins, sio
import socketio
import uvicorn
import os
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_origins=origins,
)

Base.metadata.create_all(bind=engine)

app.include_router(dz_auth.router)
app.include_router(sp_auth.router)
app.include_router(user.router)
app.include_router(party.router)
app.include_router(search.router)
app.include_router(song.router)

sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

if __name__ == '__main__':
    uvicorn.run(app="main:sio_app", port=int(os.getenv('PORT')), host=os.getenv('HOST'), reload=True)
