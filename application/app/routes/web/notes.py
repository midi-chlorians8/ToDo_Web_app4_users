# from fastapi import APIRouter, Depends
# from app.core.user import UsersRepository
# from app.repositories.users import get_users_repository
# from app.shemas.user import SchemaUserData, SchemaUserInfo
# from fastapi import FastAPI, Body, Depends, HTTPException, Query
#
# from app.model import PostSchema, UserSchema, UserLoginSchema
# from app.auth.auth_bearer import JWTBearer
# from app.auth.auth_handler import signJWT, decodeJWT
# from app.model import PasswordResetSchema, PasswordUpdateSchema
#
#
# notes_web_route = APIRouter()
#
# @notes_web_route.get("/new_page2", response_class=HTMLResponse)
# async def page_notes(
#     request: Request,
#     fullname: str = Query("Anonim"),
#     current_user: Optional[UserSchema] = Depends(get_current_user_cook),
# ):
#     return templates.TemplateResponse("notes_body.html", {"request": request, "fullname": fullname})