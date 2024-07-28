from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.db import get_db
from enums.services import Services 
from music_service import instance
from database.schemas import user as user_schema
from crud import user as crud
import os

router = APIRouter(
	prefix='/login/deezer'
)

@router.get('/')
def login():
	instance.set_service(Services.DEEZER)
	return instance.service.login(instance.service.auth_url)

@router.get('/callback')
def callback(request: Request, db: Session = Depends(get_db)):
	token = instance.service.callback(request)
	username: str = instance.service.get_user()
	user: user_schema.UserCreate = user_schema.UserCreate(token=token.access_token, service=Services.DEEZER, username=username)
	try: 
		crud.get_user_by_token(db, token.access_token)
	except HTTPException:
		crud.create_user(db, user)
	response = RedirectResponse(url=os.getenv('FRONTEND_URI'))
	response.set_cookie(key='access_token', value=token.access_token, httponly=True, samesite=None)
	return response
