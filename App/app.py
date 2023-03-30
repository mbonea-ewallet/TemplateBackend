from fastapi import FastAPI
from .Users.UserRoutes import user_router
from .Post.PostRoutes import post_router
from .PostLikes.PostLikesRoutes import postLike_router
from .Comments.CommentRoutes import comment_router
from .modelInit import models, database

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await models.create_all()
    if not database.is_connected:
        await database.connect()
        print("connected!")


@app.get("/")
async def landing_page():
    return {"code": 200, "message": "still running"}


app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(postLike_router)


async def main():
    pass


# if __name__ == "__main__":
#     main()
#     uvicorn.run(app, host="0.0.0.0", port=8000)
