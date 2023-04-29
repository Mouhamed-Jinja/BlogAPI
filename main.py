from fastapi import FastAPI
from blog.database import engine
from blog.routers import user, blog
from blog.repository import authentication
from blog import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)    
app.include_router(user.router)

     

