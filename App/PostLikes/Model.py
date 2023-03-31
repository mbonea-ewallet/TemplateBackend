import asyncio
import orm
import psycopg2
import datetime
import pydantic
from App.modelInit import database, models
from App.Users.Model import User
from App.Post.Model import Post


class PostLike(orm.Model):
    tablename = "postlikes"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "user": orm.ForeignKey(User, on_delete=orm.CASCADE),
        "post": orm.ForeignKey(Post, on_delete=orm.CASCADE),
        "createdAt": orm.DateTime(index=True, default=datetime.datetime.now),
    }
