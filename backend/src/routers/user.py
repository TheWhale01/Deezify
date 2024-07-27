from fastapi import APIRouter, Depends, Response, Request, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse
from database.db import get_db
from crud import user as crud
import os

router = APIRouter(
	prefix="/user"
)

@router.delete('/logout')
def logout(request: Request, response: Response, db: Session = Depends(get_db)):
	access_token = request.cookies.get('access_token')
	if access_token is None:
		raise HTTPException(status_code=401, detail='No access token provided')
	crud.delete_user_from_token(db, access_token)
	response.delete_cookie('access_token', httponly=True, samesite=None)
	return {'ok': True}

@router.get('/me')
def get_user(request: Request, response: Response, db: Session = Depends(get_db)):
	access_token = request.cookies.get('access_token')
	if access_token is None:
		raise HTTPException(status_code=401, detail='No access token provided')
	db_user = crud.get_user_by_token(db, access_token)
	if db_user is None:
		raise HTTPException(status_code=401, detail='Invalid access token')
	return {'user': db_user}