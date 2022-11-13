from sqlalchemy.orm import Session
from blog import models, schemes
from fastapi import HTTPException, status
from blog.hashing import Hash


def create_user(request: schemes.NewUser, db: Session):
    new_user = models.NewUser(
        name=request.name, email=request.email, password=Hash.decrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def getUser(id: int, db: Session):
    user = db.query(models.NewUser).filter(models.NewUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the user with {id} not found')
    return user
