from typing import List, Optional
from pydantic import EmailStr, BaseModel
from datetime import date, datetime, time, timedelta


class editPost(BaseModel):
    id: Optional[int]
    content: Optional[dict]
    recommendations: Optional[dict]


class createPost(BaseModel):
    pageId:int
    content: Optional[dict]
    recommendations: Optional[dict]


class getPost(BaseModel):
    id: Optional[int]
