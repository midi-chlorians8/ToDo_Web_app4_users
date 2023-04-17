from fastapi import FastAPI, Body, Depends, HTTPException, Query

from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT, decodeJWT


posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    },
     {
      "id": 2,
      "title": "SaaT.",
      "content": "Follow point my project plan",
      "owner_id": "aa@gmail.com"
    },
    {
      "id": 3,
      "title": "Saa2T.",
      "content": "Today I want to to 1,2,3 points",
      "owner_id": "aa@gmail.com"
    }
]

users = []

app = FastAPI()


# CORS
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:8001",  # Adjust the port number based on where your web page is hosted
    "http://127.0.0.1:8001", 
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# CORS

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, HTTPException

#templates = Jinja2Templates(directory="templates")

import os
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

from fastapi.staticfiles import StaticFiles
#app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse,tags=["root"])
async def matrix_login(request: Request):
    return templates.TemplateResponse("nw_v68_https.html", {"request": request})
# last ok send name



# helpers
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


async def get_current_user(token: str = Depends(JWTBearer())) -> dict:
    payload = decodeJWT(token)
    if payload:
        return payload
    else:
        raise HTTPException(status_code=401, detail="Invalid token or token has expired")
    

from fastapi import Cookie
from typing import Optional

async def get_current_user_cook(token: Optional[str] = Cookie(None)) -> dict:
    if token is None:
        raise HTTPException(status_code=401, detail="No token provided")

    payload = decodeJWT(token)
    if payload:
        return payload
    else:
        raise HTTPException(status_code=401, detail="Invalid token or token has expired")
   # helpers


from typing import Optional

@app.get("/new_page2", response_class=HTMLResponse)
async def new_page(
    request: Request,
    fullname: str = Query("Anonim"),
    current_user: Optional[UserSchema] = Depends(get_current_user_cook),
):
    return templates.TemplateResponse("test_body18m_https_adapt7.html", {"request": request, "fullname": fullname})



# see posts
@app.get("/free_posts", tags=["posts"]) #Покажет все записи без логина в систему
async def get_posts() -> dict:
    return { "data": posts }

@app.get("/sec_posts", tags=["posts"]) #Покажет все записи залогиненного юзера
async def get_posts(current_user: dict = Depends(get_current_user)) -> dict:
    user_id = current_user["user_id"]
    user_posts = [post for post in posts if post.get("owner_id") == user_id]
    return {"data": user_posts}

@app.get("/sec_posts_query", tags=["posts"]) #Покажет записи в заданном диапазоне залогиненного юзера
async def get_posts(
    current_user: dict = Depends(get_current_user),
    start: int = Query(0),
    end: int = Query(10, ge=0)
) -> dict:
    user_id = current_user["user_id"]
    user_posts = [post for post in posts if post.get("owner_id") == user_id]

    if start < 0:
        user_posts = user_posts[start:end]
    else:
        user_posts = user_posts[start:end]
    
    return {"data": user_posts}
# see posts



@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema, current_user: dict = Depends(get_current_user) ) -> dict:
    post.id = len(posts) + 1
    post.owner_id = current_user["user_id"]
    posts.append(post.dict())
    return {
        "data": "post added."
    }



@app.delete("/posts/{post_id}", tags=["posts"])
async def delete_post(post_id: int, current_user: dict = Depends(get_current_user)) -> dict:
    user_id = current_user["user_id"]

    post_to_delete = None
    for post in posts:
        if post["id"] == post_id and post["owner_id"] == user_id:
            post_to_delete = post
            break

    if post_to_delete is not None:
        posts.remove(post_to_delete)
        return {"data": f"Post with ID {post_id} has been deleted."}
    else:
        raise HTTPException(status_code=404, detail="Post not found or not owned by the current user.")


from fastapi.responses import RedirectResponse

@app.post("/user/register", tags=["user"])
async def user_register(user: UserSchema = Body(...)):
    # Check if the user already exists
    for existing_user in users:
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="User already exists")

    users.append(user)  # Add user to the users list
    return {"email": user.email, "token": signJWT(user.email)}  # Return the email and token of the registered user




@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    raise HTTPException(status_code=401, detail="Wrong login details!")



@app.get("/policy", response_class=HTMLResponse,tags=["other"])
async def matrix_login(request: Request):
    return templates.TemplateResponse("policy.html", {"request": request})


# # ============= email password recovery =============
# from aiosmtplib import send
# from email.message import EmailMessage
# import secrets

# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 587
# SMTP_USERNAME = "ilyadevops2@gmail.com"
# SMTP_PASSWORD = "Kongo321"

# @app.post("/password-reset", tags=["user"])
# async def request_password_reset(email: str, BackgroundTasks: BackgroundTasks, db: Session = Depends(get_db)):
#     # Проверьте существование пользователя
#     user = None
#     for existing_user in users:
#         if existing_user.email == email:
#             user = existing_user
#             break

#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Создайте токен сброса пароля и сохраните его в базе данных (здесь используется список для демонстрации)
#     reset_token = secrets.token_hex(20)
#     user.reset_token = reset_token

#     # Отправьте письмо с инструкциями для сброса пароля
#     message = EmailMessage()
#     message["From"] = SMTP_USERNAME
#     message["To"] = email
#     message["Subject"] = "Password Reset Request"
#     reset_url = f"http://localhost:8000/password-reset/{reset_token}"
#     message.set_content(f"Please follow the link to reset your password: {reset_url}")

#     #await send(message, hostname=SMTP_HOST, port=SMTP_PORT, username=SMTP_USERNAME, password=SMTP_PASSWORD, use_tls=True)
#     await send(
#         message,
#         hostname=SMTP_HOST,
#         port=465,  # Измените порт на 465
#         username=SMTP_USERNAME,
#         password=SMTP_PASSWORD,
#         use_ssl=True,  # Измените use_tls на use_ssl
#     )
#     return {"detail": "Password reset email sent"}




# @app.post("/password-reset/{token}", tags=["user"])
# async def reset_password(token: str, new_password: str):
#     # Проверьте токен сброса пароля
#     user_to_reset = None
#     for user in users:
#         if hasattr(user, "reset_token") and user.reset_token == token:
#             user_to_reset = user
#             break

#     if user_to_reset is None:
#         raise HTTPException(status_code=404, detail="Invalid or expired reset token")

#     # Сбросьте пароль пользователя и удалите токен сброса пароля
#     user_to_reset.password = new_password
#     del user_to_reset.reset_token

#     return {"detail": "Password reset successful"}
