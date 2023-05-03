from fastapi import APIRouter, Depends, HTTPException, Response, status
from typing import List
from app.auth.auth_handler import get_current_user_id
from app.controllers.posts import PostsAPIController
from app.core.posts import PostsRepository
from app.repositories.posts import get_posts_repository
from app.shemas.posts import PostSchema, PostSchemaCreate


posts_route = APIRouter()


@posts_route .get("/sec_posts_query", tags=["posts"], response_model=List[PostSchema])  # Покажет записи в заданном диапазоне залогиненного юзера
async def get_posts(
        current_user_id: int = Depends(get_current_user_id),
        session: PostsRepository = Depends(get_posts_repository)
):
    response = await PostsAPIController.controller_get_all_user_posts(user_id=current_user_id, posts=session)
    return response


@posts_route.post("/posts", tags=["posts"], response_model=PostSchema)
async def add_post(data: PostSchemaCreate, current_user_id: int = Depends(get_current_user_id),
                   session: PostsRepository = Depends(get_posts_repository)) -> dict:
    if current_user_id != data.user_id:
        raise HTTPException(status_code=422, detail='current user id and body id mismatch')
    response = await PostsAPIController.controller_create_user_post(data, posts=session)
    return response


@posts_route.delete("/posts/{post_id}", tags=["posts"])
async def delete_post(post_id: int, current_user_id: int = Depends(get_current_user_id),
                      session: PostsRepository = Depends(get_posts_repository)):
    response = await PostsAPIController.controller_delete_user_post(post_id, current_user_id, posts=session)
    if response:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
