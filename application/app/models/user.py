from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr
from app.models.posts import Posts


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True)
    psw: str
    posts: List['Posts'] = Relationship()
