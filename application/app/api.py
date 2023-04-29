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
#
# # CORS
#
# origins = [
#     "http://localhost:8001",  # Adjust the port number based on where your web page is hosted
#     "http://127.0.0.1:8001",
#     "*"
# ]
#
# # CORS
#
#
#
# #templates = Jinja2Templates(directory="templates")
#
# import os
# templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
# templates = Jinja2Templates(directory=templates_dir)
#
# # from fastapi.staticfiles import StaticFiles
#
#
#
#
# # helpers
#
# async def get_current_user(token: str = Depends(JWTBearer())) -> dict:
#     payload = decodeJWT(token)
#     if payload:
#         return payload
#     else:
#         raise HTTPException(status_code=401, detail="Invalid token or token has expired")
#
#
#
#
# async def get_current_user_cook(token: Optional[str] = Cookie(None)) -> dict:
#     if token is None:
#         raise HTTPException(status_code=401, detail="No token provided")
#
#     payload = decodeJWT(token)
#     if payload:
#         return payload
#     else:
#         raise HTTPException(status_code=401, detail="Invalid token or token has expired")
#    # helpers


from typing import Optional





# see posts



# see posts








from fastapi.responses import RedirectResponse





#add email pass recovery

