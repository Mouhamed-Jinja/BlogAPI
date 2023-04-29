from sqlalchemy.orm import session
from blog import hashing, models
from fastapi import HTTPException, status


def create_user(user_request, db:session):
    new_acc= models.Users(user_name = user_request.user_name ,password =hashing.Hash.bcrypt(user_request.password))
    db.add(new_acc)
    db.commit()
    db.refresh(new_acc)
    return new_acc

def get_user_witID(id: int , db:session):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return user
    
  


