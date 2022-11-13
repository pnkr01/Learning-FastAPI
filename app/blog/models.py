from blog.db import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String) 
    user_id = Column(Integer,ForeignKey('newUser.id'))
    creator = relationship("NewUser",back_populates="blogs")


class NewUser(Base):
    __tablename__ = "newUser"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog",back_populates="creator")