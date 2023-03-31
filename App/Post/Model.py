import asyncio
import orm
import psycopg2
import datetime
import pydantic
from App.modelInit import database, models
from App.Users.Model import User


class Post(orm.Model):
    tablename = "posts"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "pageId": orm.Integer(index=True, default=0),
        "content": orm.JSON(),
        "recommendations": orm.JSON(allow_null=True),
        "createdAt": orm.DateTime(index=True, default=datetime.datetime.now),
    }
