from fastapi import APIRouter, HTTPException
from ..models.user import User, UserCreate
from ..core.database import db

router = APIRouter()

@router.post('/login')
def login(data: UserCreate):
    user = db.get_user(data.username)
    if not user or user.password != data.password:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    return {'access_token': f'token-{user.username}', 'token_type': 'bearer'}

@router.post('/register', response_model=User)
def register(data: UserCreate):
    if db.get_user(data.username):
        raise HTTPException(status_code=400, detail='User already exists')
    return db.create_user(data)
