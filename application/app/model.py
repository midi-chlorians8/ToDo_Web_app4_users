from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(...)
    content: str = Field(...)
    owner_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you'll learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens....",
                "owner_id": " "
            }
        }



class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }

#add email pass recovery
class PasswordResetSchema(BaseModel):
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com"
            }
        }

class PasswordUpdateSchema(BaseModel):
    token: str = Field(...)
    new_password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "token": "your_token_here",
                "new_password": "new_password"
            }
        }
