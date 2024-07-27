from fastapi import APIRouter, Depends
from dependancies.user import get_user
from music_service import instance

router = APIRouter()

@router.get('/search')
def search(q: str, user = Depends(get_user)):
	return instance.service.search(q)