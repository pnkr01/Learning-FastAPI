from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemes, db, models,oAuth2
from typing import List
from sqlalchemy.orm import Session
from ..repo import blog

get_db = db.get_db
routers = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@routers.get('/', response_model=list[schemes.ShowModel])
def get_all_blogs(db: Session = Depends(db.get_db),current_user: schemes.NewUser = Depends(oAuth2.get_current_user)):
    return blog.get_all(db)


@routers.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemes.Blog, db: Session = Depends(get_db),current_user: schemes.NewUser = Depends(oAuth2.get_current_user)):
    return blog.create(request, db)


@routers.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog_at(id, db: Session = Depends(get_db),current_user: schemes.NewUser = Depends(oAuth2.get_current_user)):
    return blog.delete(db)


@routers.put("/update/{id}")
def update_Blog(id, request: schemes.Blog, db: Session = Depends(get_db),current_user: schemes.NewUser = Depends(oAuth2.get_current_user)):
    return blog.update(db)



@routers.get('/{id}', status_code=200, response_model=schemes.ShowModel)
def show_blog_At(id, db: Session = Depends(get_db),current_user: schemes.NewUser = Depends(oAuth2.get_current_user)):
    blog.show(db)
