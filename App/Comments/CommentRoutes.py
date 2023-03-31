from fastapi import APIRouter, status
from .Schemas import createComment,editComment,deleteComment,allComments
from .Model import Comment
from App.Users.Model import User
from App.Post.Model import Post
from App.utils import get_user_and_post
import asyncio
postLike_router = APIRouter(tags=["PostLikes"])




comment_router = APIRouter(tags=["Comments"])


@comment_router.post("/comment/create")
async def create_comment(comment: createComment):
    user,_post = await get_user_and_post(comment)
    data = await Comment.objects.create(user=user, content=comment.content,post=_post)
    return {"code": 200, "message": "success", "payload": data.__dict__}


@comment_router.post("/comment/edit")
async def edit_comment(comment: editComment):
    # user,_post = await get_user_and_post(comment)
    db_comment = await Comment.objects.filter(id=comment.id).first()
    if not db_comment:
        return {"code": 400, "message": "Comment does not exist", "payload": None}
    if db_comment.user.id != comment.userId:
        return {
            "code": 400,
            "message": "This comment belongs to a different user",
            "payload": None,
        }
    db_data = await db_comment.update(content=comment.content)
    return {"code": 200, "message": "success", "payload": None}


@comment_router.post("/comment/all")
async def all_comments(comment: allComments):

    user = await User.objects.filter(id=comment.userId).first()
    if not user:
        return {"code": 400, "message": "User does not exist", "payload": None}
    db_comment = await Comment.objects.filter(user=user).all()

    if not db_comment:
        return {"code": 400, "message": "Comment does not exist", "payload": None}
    return {
        "code": 200,
        "message": "success",
        "payload": [i.__dict__ for i in db_comment],
    }
