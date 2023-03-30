from typing import List, Optional
from pydantic import EmailStr, BaseModel
from datetime import date, datetime, time, timedelta


class addLike (BaseModel):
    postId:int
    userId:int

class deleteLike (BaseModel):
    id:int
    postId:int
    userId:int


    