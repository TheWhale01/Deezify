from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.db import get_db
from enums.services import Services
from music_service.deezer import DeezerService
from database.schemas import user as user_schema
from crud import user as crud
import os

router = APIRouter(
        prefix='/login/deezer'
)

dz_service = DeezerService()

@router.get('/')
def login():
    return dz_service.login(dz_service.auth_url)

@router.get('/callback')
def callback(request: Request, db: Session = Depends(get_db)):
    token = dz_service.callback(request)
    username: str = dz_service.get_user('/user/me')
    user: user_schema.UserCreate = user_schema.UserCreate(token=token.access_token, service=Services.DEEZER, username=username)
    db_user = crud.create_user(db, user)
    response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
    response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite=None)
    response.set_cookie(key='user_id', value=str(db_user.id), httponly=True, samesite='lax')
    return response
