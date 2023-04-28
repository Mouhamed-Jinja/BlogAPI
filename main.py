from fastapi import FastAPI
from app.blog.database import engine
from app.blog.routers import user, blog
from app.blog.repository import authentication
from app.blog import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)    
app.include_router(user.router)

     

