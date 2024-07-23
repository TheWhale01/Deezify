from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from enums.services import Services
from music_service.deezer import DeezerService
import schemas, crud
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
    user: schemas.UserCreate = schemas.UserCreate(token=token.access_token, service=Services.DEEZER, username=username)
    crud.create_user(db, user)
    response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
    response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite='lax')
    return response
