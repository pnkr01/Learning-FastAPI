from sqlalchemy.orm import Session
from .. import models, schemes

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemes.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==
                                        id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the blog with id {id} is not found')
    db.delete(synchronize_session=False)
    db.commit()
    return "deleted sucessfully"


def update(db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with id {id} not found')
    else:
        db.query(models.Blog).filter(
            models.Blog.id == id).update(request.dict())

    db.commit()
    db.refresh(blog)
    return blog


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'this blog {id} is not found')
    return blog
