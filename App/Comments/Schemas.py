from typing import List, Optional
from pydantic import EmailStr, BaseModel
from datetime import date, datetime, time, timedelta


class createComment(BaseModel):
    userId: int
    content: str
    postId:int


class editComment(BaseModel):
    id:int
    userId: int
    content: str
    postId:int

class deleteComment(BaseModel):
    id:int
    userId: int
    postId:int

class allComments(BaseModel):
    userId: int
