from typing import List, Optional
from pydantic import EmailStr, BaseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class BaseRequest(BaseModel):
    email: EmailStr
    name: str
    password: str
    phoneNumber: Optional[str]

    def hash_password(self):
        self.password = pwd_context.hash(self.password)
