from fastapi import APIRouter
from fastapi import Depends,status
from sqlalchemy.orm import Session
from typing import List
from app.blog import schemas,OAuth2
from app.blog.database import get_db
from app.blog.repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/", response_model=List[schemas.ShowBlog])
def get_fromDB(db:Session = Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
    return blog.get_all(db)

@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, db:Session = Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
    return blog.get_withID(id, db)
    

@router.post("/") #create
def create(request : schemas.Blog, db:Session = Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
    return blog.create_blog(request, db)

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete(id, db:Session = Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
    return blog.delete_blog(id, db)


@router.put("/{id}", status_code= status.HTTP_202_ACCEPTED)
def update(id, request :schemas.Blog, db:Session= Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
   return blog.update(id, request, db)

@router.delete("/title/{title}")
def delete_with_Title(D_title:str, db:Session= Depends(get_db), current_user : schemas.User = Depends(OAuth2.get_current_user)):
    return blog.delete_with_title(D_title, db)
