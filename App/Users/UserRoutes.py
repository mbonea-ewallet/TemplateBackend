from fastapi import APIRouter, status
from .Schemas import BaseRequest
from .Model import User
from sqlalchemy import and_
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")
user_router = APIRouter(tags=["User"])


@user_router.post("/user/register")
async def register_user(user: BaseRequest):
    data = await User.objects.filter(email=user.email).first()
    if data != None:
        return {"code": 400, "message": "user exists", "payload": None}
    else:
        user.hash_password()
    sample = await User.objects.create(**user.dict())
    return {"code": 200, "message": "success", "payload": None}


@user_router.post("/user/login")
async def register_user(user: BaseRequest):
    db_user = await User.objects.filter(email=user.email).first()
    if db_user.verify_password(user.password):
        return {"code": 200, "message": "success", "payload": db_user.__dict__}
    return {"code": 401, "message": "Invalid Credentials", "payload": None}
