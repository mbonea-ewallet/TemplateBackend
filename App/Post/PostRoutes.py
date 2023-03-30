from fastapi import APIRouter, status
from .Schemas import createPost,editPost,getPost
from .Model import Post

post_router = APIRouter(tags=["Posts"])


@post_router.post("/post/create")
async def create_post(post: createPost):
    data=await Post.objects.create(**post.dict())
    return {"code": 200, "message": "success", "payload": data.__dict__}

@post_router.post("/post/update")
async def create_post(post: editPost):
    temp=await Post.objects.get(id= post.id)
    data=await temp.update(recommendations=post.recommendations,content=post.content)
    # data=await Post.objects.update(**post.dict())
    return {"code": 200, "message": "success", "payload": temp.__dict__}


@post_router.post("/post/get")
async def create_post(post: getPost):
    data=await Post.objects.get(id=post.id)
    return {"code": 200, "message": "success", "payload": data.__dict__}