from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemes, db, models
from typing import List
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repo import user

get_db = db.get_db
routers = APIRouter(
    prefix="/user",
    tags=['Users']
)


@routers.post('/')
def create_user(request: schemes.NewUser, db: Session = Depends(get_db),):
    return user.create_user(request, db)


@routers.get('/{id}', status_code=202, response_model=schemes.ShowUser)
def get_User_At(id: int, db: Session = Depends(get_db)):
    return user.getUser(id, db)
