from fastapi import APIRouter, Depends
from dependancies.user import get_user
from music_service import instance

router = APIRouter(
    prefix='/search',
    dependencies=[
        Depends(get_user),
    ],
)

@router.get('')
def search(q: str):
	return instance.service.search(q)
