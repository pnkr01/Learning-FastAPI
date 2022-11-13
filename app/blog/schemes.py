from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str


class ParentBlog(Blog):
    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ParentBlog] = []

    class Config():
        orm_mode = True


class ShowModel(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class NewUser(BaseModel):
    name: str
    email: str
    password: str


class LogIn(BaseModel):
    username:str 
    password:str 


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str