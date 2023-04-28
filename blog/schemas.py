from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title : Optional[str]
    body : Optional[str]
        
class Ch_blog(Blog):
    class Config():
        orm_mode = True
        
class User(BaseModel):
    user_name:str
    password:str

class ShowUser(BaseModel):
    id :int
    user_name:str
    blogs : List[Ch_blog] = []
    class Config():
        orm_mode = True
                
class ShowBlog(BaseModel):
    title:str
    body : str
    creator: Optional[ShowUser] = None
    class Config():
        orm_mode = True
    
        
class login(BaseModel):
    user_name :str
    password : str
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_name: str | None = None


