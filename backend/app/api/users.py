from fastapi import APIRouter
from ..core.database import db
from ..models.user import User

router = APIRouter()

@router.get('', response_model=list[User])
def list_users():
    return db.list_users()
