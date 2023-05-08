from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import String
from sqlalchemy.sql.schema import Column
from pydantic import EmailStr
from app.models.posts import Posts


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(sa_column=Column("email", String, unique=True))
    psw: str
    posts: List['Posts'] = Relationship()
