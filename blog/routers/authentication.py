from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemes, db, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

routers = APIRouter(tags=["Authentication"])


@routers.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    user = db.query(models.NewUser).filter(
        models.NewUser.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='No user found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
