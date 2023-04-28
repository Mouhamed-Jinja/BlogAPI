from fastapi import APIRouter, Depends
from app.blog import schemas
from sqlalchemy.orm import Session 
from app.blog.database import get_db
from app.blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"] 
)

@router.post("/", response_model = schemas.ShowUser)
def new_user(user_request : schemas.User, db:Session = Depends(get_db)):
    return user.create_user(user_request, db)

@router.get("/{id}", response_model= schemas.ShowUser)
def printUsers(id:int, db:Session = Depends(get_db)):
    return user.get_user_witID(id,db)