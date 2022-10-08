from fastapi import FastAPI

from SocialAPI import models
from SocialAPI.Routers import posts, users, auth
from SocialAPI.db import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
async def root():
    return {'message': "Hello World"}
