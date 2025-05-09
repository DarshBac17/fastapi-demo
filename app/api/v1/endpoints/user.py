from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=list[UserOut])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_users(db, skip, limit)

@router.get("/{user_id}", response_model=UserOut)
def read(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated = user_service.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", response_model=UserOut)
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = user_service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
