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
# from app.jinja_tags import templates
# from fastapi import FastAPI, Body, Depends, HTTPException, Query
#
# from app.model import PostSchema, UserSchema, UserLoginSchema
# from app.auth.auth_bearer import JWTBearer
# from app.auth.auth_handler import signJWT, decodeJWT
# from fastapi.responses import HTMLResponse, JSONResponse
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request, HTTPException
# from fastapi import Cookie
# from typing import Optional
#
#
# policy_web_route = APIRouter()
#
#
# @policy_web_route.get("/", response_class=HTMLResponse)
# async def show_policy(request: Request):
#     return templates.TemplateResponse("policy.html", {"request": request})
