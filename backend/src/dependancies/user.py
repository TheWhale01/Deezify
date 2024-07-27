from fastapi import Depends, Request, HTTPException, status
from database.db import get_db
from sqlalchemy.orm import Session
from crud import user as crud

def get_user(request: Request, db: Session = Depends(get_db)):
	token: str | None = request.cookies.get('access_token')
	if token is None:
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail='No token provided.'
		)
	db_user = crud.get_user_by_token(db, token)
	if db_user is None:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail='Invalid token.'
		)
	return db_user
