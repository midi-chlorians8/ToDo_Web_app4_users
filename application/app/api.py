from fastapi import FastAPI, Body, Depends, HTTPException, Query


from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT, decodeJWT


posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

users = []

app = FastAPI()


# helpers

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!"}





# @app.get("/posts/{id}", tags=["posts"])
# async def get_single_post(id: int) -> dict:
#     if id > len(posts):
#         return {
#             "error": "No such post with the supplied ID."
#         }

#     for post in posts:
#         if post["id"] == id:
#             return {
#                 "data": post
#             }













async def get_current_user(token: str = Depends(JWTBearer())) -> dict:
    payload = decodeJWT(token)
    if payload:
        return payload
    else:
        raise HTTPException(status_code=401, detail="Invalid token or token has expired")

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









@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)


# @app.post("/user/login", tags=["user"])
# async def user_login(user: UserLoginSchema = Body(...)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }
@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    raise HTTPException(status_code=401, detail="Wrong login details!")