from fastapi import BackgroundTasks
from app.auth.auth_handler import signJWT, get_reset_password_token, get_user_email_from_reset_token
from app.shemas.user import UserSchemaCreate, UserSchemaOut, UserLoginSchema, PasswordResetSchema
from app.core.user import UserRepository
from app.exceptions import ConflictException, NotFoundException, ApiException
from app.auth.security import verify_password
from fastapi import HTTPException
from starlette import status
import jwt

from application.app.auth.utils import send_password_reset_email


class UserAPIController:
    @classmethod
    async def create_api_user(cls, data: UserSchemaCreate, user: UserRepository) -> UserSchemaOut:
        check_user = await user.get_by_email_or_none(email=data.email)
        if check_user:
            raise ConflictException(name="User already exists")
        new_user = await user.create_user(data=data)
        token = signJWT(new_user.user_id)
        return UserSchemaOut(email=new_user.email, access_token=token)

    @classmethod
    async def login_user(cls, data: UserLoginSchema, user: UserRepository):
        check_user = await user.get_by_email_or_none(email=data.email)
        if check_user is None:
            raise NotFoundException(name="User doesn't exist")
        if not verify_password(password=data.psw, hash=check_user.psw):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Incorrect password",
            )
        token = signJWT(check_user.user_id)
        return UserSchemaOut(email=check_user.email, access_token=token)

    @classmethod
    async def password_reset_user(cls, data: PasswordResetSchema,
                                  user: UserRepository,
                                  background_tasks: BackgroundTasks):
        check_user = await user.get_by_email_or_none(email=data.email)
        if check_user is None:
            raise NotFoundException(name="User")
        token = get_reset_password_token(email=check_user.email, expires_in=3600)
        print(token)
        background_tasks.add_task(send_password_reset_email, check_user.email, token)
        return {"message": 'Link was sent to email'}

    @classmethod
    async def change_api_password(cls, token: str, psw: str, user: UserRepository):
        try:
            email = await get_user_email_from_reset_token(token)
            check_user = await user.get_by_email_or_none(email=email)
        except jwt.exceptions.ExpiredSignatureError:
            raise ApiException(name="Refresh token expired", status_code=401)
        except jwt.exceptions.InvalidSignatureError:
            raise ApiException(name="Wrong token", status_code=403)
        except jwt.exceptions.DecodeError:
            raise ApiException(name="Invalid refresh token", status_code=403)
        if check_user is None:
            raise NotFoundException(name="Could not find user", status_code=404)
        await user.change_password(email=email, psw=psw)
        return {"message": "Password has been updated successfully."}
