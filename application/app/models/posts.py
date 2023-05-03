from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel
from sqlmodel import Field


class Posts(SQLModel, table=True):
    post_id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: Optional[str]
    content: str
    created_at: Optional[datetime] = None
    user_id: Optional[int] = Field(default=None, foreign_key="user.user_id")
