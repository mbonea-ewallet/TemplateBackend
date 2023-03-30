import asyncio
import orm
import psycopg2
import datetime
import pydantic
from passlib.context import CryptContext
from App.modelInit import database, models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(orm.Model):
    tablename = "users"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True),
        "name": orm.String(max_length=100, index=True),
        "email": orm.String(max_length=100, index=True, unique=True),
        "password": orm.String(max_length=100, index=True),
        "phoneNumber": orm.String(max_length=100, index=True, allow_null=True),
        "account_type": orm.Integer(index=True, default=1),
        "createdAt": orm.DateTime(index=True, default=datetime.datetime.now),
        "updatedAt": orm.DateTime(index=True, default=datetime.datetime.now),
        "lastLogin": orm.DateTime(index=True, default=datetime.datetime.now),
    }

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)
