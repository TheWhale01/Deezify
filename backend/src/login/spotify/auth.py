import os
from enums.services import Services
from sqlalchemy.orm import Session
from utils import generate_random_string
from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
import crud
import schemas
from database import get_db
from music_service.spotify import SpotifyService

router = APIRouter(
    prefix='/login/spotify'
)

sp_service = SpotifyService()

@router.get('/')
def login():
    state = generate_random_string(32)
    url = (
        f"{sp_service.auth_url}?response_type=code"
        f"&client_id={os.getenv('SPOTIFY_CLIENT_ID')}"
        f"&scope={os.getenv('SPOTIFY_SCOPES')}"
        f"&redirect_uri={os.getenv('SPOTIFY_CALLBACK_URL')}"
        f"&state={state}"
    )
    response = sp_service.login(url)
    return response

@router.get('/callback')
def callback(request: Request, db: Session = Depends(get_db)):
    token = sp_service.callback(request)
    username: str = sp_service.get_user('/me')
    user: schemas.UserCreate = schemas.UserCreate(token=token.access_token, service=Services.SPOTIFY, username=username)
    crud.create_user(db ,user)
    response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
    response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite='lax')
    return response
