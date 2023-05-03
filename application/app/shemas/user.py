from pydantic import BaseModel, Field, EmailStr


class PasswordResetSchema(BaseModel):
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com"
            }
        }


class UserLoginSchema(PasswordResetSchema):
    psw: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "psw": "weakpassword"
            }
        }


class UserSchemaCreate(PasswordResetSchema):
    psw: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "psw": "weakpassword"
            }
        }


class UserSchemaOut(PasswordResetSchema):
    access_token: str


class TokenPayload(BaseModel):
    sub: EmailStr = None
    exp: int = None
