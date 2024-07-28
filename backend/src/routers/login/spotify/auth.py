import os
from enums.services import Services
from sqlalchemy.orm import Session
from utils import generate_random_string
from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from crud import user as crud
from database.db import get_db
from database.schemas import user as user_schema
from music_service import instance

router = APIRouter(
    prefix='/login/spotify'
)

@router.get('/')
def login():
    instance.set_service(Services.SPOTIFY)
    state = generate_random_string(32)
    url = (
        f"{instance.service.auth_url}?response_type=code"
        f"&client_id={os.getenv('SPOTIFY_CLIENT_ID')}"
        f"&scope={os.getenv('SPOTIFY_SCOPES')}"
        f"&redirect_uri={os.getenv('SPOTIFY_CALLBACK_URL')}"
        f"&state={state}"
    )
    response = instance.service.login(url)
    return response

@router.get('/callback')
def callback(request: Request, db: Session = Depends(get_db)):
    token = instance.service.callback(request)
    username: str = instance.service.get_user()
    user: user_schema.UserCreate = user_schema.UserCreate(token=token.access_token, service=Services.SPOTIFY, username=username)
    try:
        crud.get_user_by_token(db, token.access_token)
    except HTTPException:
        crud.create_user(db, user)
    response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
    response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite='lax')
    return response
