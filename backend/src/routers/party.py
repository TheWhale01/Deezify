from fastapi import APIRouter

router = APIRouter(
	prefix='/party'
)

@router.post('/create')
def create_party():
	pass
