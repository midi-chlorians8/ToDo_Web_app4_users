from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostSchemaCreate(BaseModel):
    title: Optional[str]
    content: str
    created_at: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens....",
                "created_at": "2023-05-01T15:02:35.123456"
            }
        }


class PostSchema(PostSchemaCreate):
    post_id: int



class NewPost(BaseModel):
    created_at: datetime
    title: Optional[str]
    content: str
    user_id: int

