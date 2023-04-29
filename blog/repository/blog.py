from sqlalchemy.orm import session
from fastapi import HTTPException, status
from blog import models

def get_all(db:session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_withID(id , db:session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"Error Msg" : f" ID: {id} Not Found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail={"Error Msg" : f" ID: {id} Not Found."})
    else:
        return blogs
    
def create_blog(request, db:session):
    new_blog = models.Blog(title = request.title , body = request.body, owner_id =2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def delete_blog(id, db:session):
    deleted_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not deleted_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"this id:{id} not avaliable")
    
    deleted_blog.delete(synchronize_session=False)
    db.commit()
    return"deleted"

def update(id,request, db:session):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"this id: {id} not avaliable")
    
        blog.update(request)
    db.commit()
    return f"updated to {request.title}"

def delete_with_title(D_title, db:session):
    deleted_title = db.query(models.Blog).filter(models.Blog.title ==D_title)
    if not deleted_title.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    deleted_title.delete(synchronize_session=False)
    db.commit()
    return f"{D_title} was deleted"
