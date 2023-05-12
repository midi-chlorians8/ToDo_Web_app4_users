from app.exceptions import ConflictException, NotFoundException, ApiException
from app.core.posts import PostsRepository
from app.shemas.posts import PostSchemaCreate, PostSchema
from typing import List


class PostsAPIController:
    @classmethod
    async def controller_get_all_user_posts(cls, user_id: int, posts: PostsRepository) -> List[PostSchema]:
        return await posts.get_all_user_posts(user_id)

    @classmethod
    async def controller_create_user_post(cls, data: PostSchemaCreate,
                                          current_user_id: int,
                                          posts: PostsRepository) -> PostSchema:
        return await posts.create_post(data, current_user_id)

    @classmethod
    async def controller_delete_user_post(cls, post_id: int, user_id: int, posts: PostsRepository):
        post = await posts.get_by_id_or_none(post_id)
        if post is None:
            raise NotFoundException(name="Post doesn't exist")
        if post.user_id != user_id:
            raise ConflictException(name="Current user isn't the owner")
        return await posts.delete_post(post_id)

