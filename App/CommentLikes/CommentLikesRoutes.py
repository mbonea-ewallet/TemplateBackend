from fastapi import APIRouter, status
from .Schemas import BaseRequest, editRequest
from .Model import Comments
from App.Users.Model import User
from App.Post.Model import Post

commentLikes_router = APIRouter(tags=["CommentLikes"])


@commentLikes_router.get("/likes/comments/add")
async def add_commentLike():
    pass
