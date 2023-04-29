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
# posts_route = APIRouter()
#
# users = []
#
# posts = [
#     {
#         "id": 1,
#         "title": "Pancake",
#         "content": "Lorem Ipsum ..."
#     },
#      {
#       "id": 2,
#       "title": "SaaT.",
#       "content": "Follow point my project plan",
#       "owner_id": "aa@gmail.com"
#     },
#     {
#       "id": 3,
#       "title": "Saa2T.",
#       "content": "Today I want to to 1,2,3 points",
#       "owner_id": "aa@gmail.com"
#     }
# ]
#
# @posts_route .get("/free_posts", tags=["posts"]) #Покажет все записи без логина в систему
# async def get_posts() -> dict:
#     return { "data": posts }
#
# @posts_route .get("/sec_posts", tags=["posts"]) #Покажет все записи залогиненного юзера
# async def get_posts(current_user: dict = Depends(get_current_user)) -> dict:
#     # user_id = current_user["user_id"]
#     user_id = current_user["sub"]
#     user_posts = [post for post in posts if post.get("owner_id") == user_id]
#     return {"data": user_posts}
#
#
# @posts_route .get("/sec_posts_query", tags=["posts"])  # Покажет записи в заданном диапазоне залогиненного юзера
# async def get_posts(
#         current_user: dict = Depends(get_current_user),
#         start: int = Query(0),
#         end: int = Query(10, ge=0)
# ) -> dict:
#     # user_id = current_user["user_id"]
#     user_id = current_user["sub"]
#     user_posts = [post for post in posts if post.get("owner_id") == user_id]
#
#     if start < 0:
#         user_posts = user_posts[start:end]
#     else:
#         user_posts = user_posts[start:end]
#
#     return {"data": user_posts}
#
#
#
# @posts_route .post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
# async def add_post(post: PostSchema, current_user: dict = Depends(get_current_user) ) -> dict:
#     post.id = len(posts) + 1
#     # post.owner_id = current_user["user_id"]
#     post.owner_id = current_user["sub"]
#     posts.append(post.dict())
#     return {
#         "data": "post added."
#     }
#
#
# @posts_route .delete("/posts/{post_id}", tags=["posts"])
# async def delete_post(post_id: int, current_user: dict = Depends(get_current_user)) -> dict:
#     user_id = current_user["user_id"]
#
#     post_to_delete = None
#     for post in posts:
#         if post["id"] == post_id and post["owner_id"] == user_id:
#             post_to_delete = post
#             break
#
#     if post_to_delete is not None:
#         posts.remove(post_to_delete)
#         return {"data": f"Post with ID {post_id} has been deleted."}
#     else:
#         raise HTTPException(status_code=404, detail="Post not found or not owned by the current user.")

