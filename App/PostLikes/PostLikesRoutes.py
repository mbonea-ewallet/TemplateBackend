from fastapi import APIRouter, Depends
from .Schemas import addLike,deleteLike
from .Model import PostLike
from App.Users.Model import User
from App.Post.Model import Post
from App.utils import get_user_and_post
import asyncio
postLike_router = APIRouter(tags=["PostLikes"])




@postLike_router.post("/postLike/add")
async def add_postLike(post: addLike):
    user,_post=await get_user_and_post(post) #validate if both the post and user exist
    previos =await PostLike.objects.filter(user=user).filter(post=_post).first()
    if previos:
        return {"code": 400, "message": "you already liked it", "payload": None}
    
    data=await PostLike.objects.create(post=_post,user=user)
    return {"code": 200, "message": "success", "payload": data.__dict__}

@postLike_router.post("/postLike/delete")
async def create_post(post: deleteLike):
    user,_post=await get_user_and_post(post)
    data=await PostLike.objects.filter(id=post.id).first()
    if not data:
        return {"code": 400, "message": "Does not exist", "payload": None}
    if user.id == data.user.id and _post.id == data.post.id:
        await data.delete()
        return {"code": 200, "message": "success", "payload": None}


@postLike_router.post("/postLike/get")
async def create_post(post: deleteLike):
    user,_post=await get_user_and_post(post)
    data=await PostLike.objects.filter(id=post.id).first()
    if not data:
        return {"code": 400, "message": "Does not exist", "payload": None}
    if user.id == data.user.id and _post.id == data.post.user.id:
        return {"code": 200, "message": "success", "payload": data.__dict__}
