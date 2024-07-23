from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login.spotify import auth as sp_auth
from login.deezer import auth as dz_auth
from database import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        '*'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Base.metadata.create_all(bind=engine)

app.include_router(sp_auth.router)
app.include_router(dz_auth.router)
