from App.Users.Model import User
from App.Post.Model import Post
import asyncio
from fastapi import HTTPException

async def get_user_and_post(content):
    try:
    #    user = None
    #    post = await Post.objects.get(id=content.postId)
    #    print(post.id)
        user,post = await asyncio.gather(*[User.objects.get(id=content.userId), Post.objects.get(id=content.postId)])
    except:
        raise HTTPException(status_code=400, detail="Invalid data")
    return user,post