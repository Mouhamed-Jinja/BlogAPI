from fastapi import APIRouter, Depends, HTTPException, status
from app.blog import  models,token
from fastapi.security import OAuth2PasswordRequestForm


from sqlalchemy.orm import session
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    tags=["Logins"]
)
@router.post("/login")
def login(request : OAuth2PasswordRequestForm = Depends(), db:session = Depends(get_db)):
    match_user = db.query(models.Users).filter(models.Users.user_name == request.username).first()
    if not match_user:
        return "not valied"
  
    
    if not Hash.verify(request.password , match_user.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Password is wrong")
           
 
    access_token = token.create_access_token(data={"sub": match_user.user_name})
    return {"access_token": access_token, "token_type": "bearer"}