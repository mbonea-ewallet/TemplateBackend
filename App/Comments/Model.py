import asyncio
import orm
import psycopg2
import datetime
import pydantic
from App.modelInit import database, models
from App.Users.Model import User


class Comment(orm.Model):
    tablename = "comments"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "user": orm.ForeignKey(User, on_delete=orm.CASCADE),
        "post": orm.ForeignKey(User, on_delete=orm.CASCADE),
        "content": orm.String(max_length=100),
        "likes": orm.Integer(index=True, default=0),
        "createdAt": orm.DateTime(index=True, default=datetime.datetime.now),
        "updatedAt": orm.DateTime(index=True, default=datetime.datetime.now),
    }
