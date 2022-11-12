from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


@app.get('/')
def index():
    return {
        'data': "blog page"
    }


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    return {
        'data': id
    }


@app.get('/blog_limit')
def limitBlog(limit=15, published: bool = True):
    if published:
        return {'blog': {f'{limit} published blogs from db'}}
    else:
        return {'blog': {"all published blog from from db"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[false]


@app.post('/blog')
def createBlog(request: Blog):
    return {'data': f'{request.title} is blog is created and {request.body}'}
