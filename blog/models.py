
from app.blog.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    owner_id= Column(Integer , ForeignKey("Users.id"))
    creator = relationship("Users", back_populates="blogs")

    
class Users(Base):
    __tablename__ = "Users"
    id= Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="creator")
    
