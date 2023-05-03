from typing import Optional
from pydantic import BaseModel, Field, EmailStr



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
