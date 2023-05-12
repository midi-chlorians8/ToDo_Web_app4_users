from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostSchemaCreate(BaseModel):
    title: Optional[str]
    content: str

    class Config:
        schema_extra = {
            "example": {
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens....",
            }
        }


class PostSchema(PostSchemaCreate):
    post_id: int
    created_at: datetime


class NewPost(BaseModel):
    created_at: datetime
    title: Optional[str]
    content: str
    user_id: int

