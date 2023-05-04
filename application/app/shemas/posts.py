from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostSchemaCreate(BaseModel):
    title: Optional[str]
    content: str
    user_id: int


class PostSchema(PostSchemaCreate):
    post_id: int
    created_at: datetime


class NewPost(BaseModel):
    created_at: datetime
    title: Optional[str]
    content: str
    user_id: int

