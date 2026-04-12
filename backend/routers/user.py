from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db
from ..services.user_service import create_user_service, get_users_service

router = APIRouter()

@router.post("/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    return create_user_service(db, name, email)

@router.get("/")
def get_users(
    skip: int = 0,
    limit: int = 10,
    name: str = None,
    db: Session = Depends(get_db)
):
    return get_users_service(db, skip, limit, name)