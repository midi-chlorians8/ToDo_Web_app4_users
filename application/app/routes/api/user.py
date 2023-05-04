from fastapi import APIRouter, Depends, BackgroundTasks
from app.controllers.user import UserAPIController
from app.core.user import UserRepository
from app.repositories.user import get_user_repository
from app.shemas.user import UserSchemaCreate, UserSchemaOut, UserLoginSchema, PasswordResetSchema

users_route = APIRouter()


@users_route.post("/register", response_model=UserSchemaOut)
async def user_register(data: UserSchemaCreate, session: UserRepository = Depends(get_user_repository)):
    return await UserAPIController.create_api_user(data=data, user=session)


@users_route.post("/login", response_model=UserSchemaOut)
async def user_login(data: UserLoginSchema, session: UserRepository = Depends(get_user_repository)):
    return await UserAPIController.login_user(data=data, user=session)


@users_route.post("/password-reset-request")
async def password_reset_request(password_reset: PasswordResetSchema,
                                 background_tasks: BackgroundTasks,
                                 session: UserRepository = Depends(get_user_repository)):
    return await UserAPIController.password_reset_user(data=password_reset,
                                                       user=session,
                                                       background_tasks=background_tasks)


@users_route.post("/password-reset/{token}")
async def password_reset(token: str, psw: str, session: UserRepository = Depends(get_user_repository)):
    return await UserAPIController.change_api_password(token=token, psw=psw, user=session)
