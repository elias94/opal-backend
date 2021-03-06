from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    name: constr(max_length=30)
    email: str


class UserCreate(UserBase):
    # available only on the user create call
    password: constr(max_length=60)


class User(UserBase):
    id: constr(max_length=12)
    display_name: constr(max_length=100)
    date_created: datetime
    last_login: datetime
    blocked: bool
    image: Optional[str]
    plan: int = 0
    onboard: bool = False

    class Config:
        orm_mode = True


class UserRestricted(BaseModel):
    id: constr(max_length=12)
    name: constr(max_length=30)
    display_name: constr(max_length=100)
    image: Optional[str]

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    user: UserRestricted
    info: Dict

    class Config:
        orm_mode = True
