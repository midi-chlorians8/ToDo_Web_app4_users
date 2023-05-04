from app.core.db import database
from app.core.posts import PostsRepository


def get_posts_repository() -> PostsRepository:
    return PostsRepository(database)
