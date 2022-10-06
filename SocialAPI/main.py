from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException

from SocialAPI import models
from SocialAPI.db import engine, SessionLocal, get_db
from SocialAPI.schemas import Post

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.get('/posts')
async def get_posts():
    return {"data": "These are your posts"}


@app.get('/posts/{id}')
async def get_post(id_: int):
    return {'data': "This is your post"}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return {"data": post}


@app.get('/posts/{id}')
def get_post(id_: int, response: Response):
    # Not Found
    # raise HTTPExecution(status_code=status.HTTP_404_NOT_FOUND,
    #                     detail='Not found')
    #
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"message": 'Not found'}
    return {"data": id_}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id_: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('posts/{id}')
def update_post(id_: int):
    return {"data", id_}

