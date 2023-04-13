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
    return templates.TemplateResponse("test_body18m_https.html", {"request": request, "fullname": fullname})



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


