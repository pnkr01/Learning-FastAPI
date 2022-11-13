from fastapi import FastAPI
from blog import models
from blog.db import engine
from blog.routers import blog,user,authentication

app = FastAPI()

app.include_router(blog.routers)
app.include_router(user.routers)
app.include_router(authentication.routers)

models.Base.metadata.create_all(engine)

