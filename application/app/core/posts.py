from sqlalchemy import sql
from datetime import datetime
from app.base_repository import BaseRepository
from app.models.posts import Posts
from app.shemas.posts import PostSchemaCreate, PostSchema, NewPost


class PostsRepository(BaseRepository):
    async def get_all_user_posts(self, user_id: int) -> list or None:
        query = sql.select(Posts).where(Posts.user_id == user_id).order_by(Posts.created_at)
        return await self.database.fetch_all(query=query)

    async def create_post(
            self,
            data: PostSchemaCreate,
            current_user_id: int) -> PostSchema:
        new_post = NewPost(
            created_at=data.created_at if data.created_at else datetime.now(),
            title=data.title if data.title else None,
            content=data.content,
            user_id=current_user_id
        )
        values = {**new_post.dict()}
        query = sql.insert(Posts).values(**values).returning(
            Posts.created_at,
            Posts.user_id,
            Posts.post_id,
            Posts.title,
            Posts.content
        )
        return await self.database.fetch_one(query=query)

    async def get_by_id_or_none(self, id: int) -> PostSchema or None:
        query = sql.select(Posts).where(Posts.post_id == id)
        return await self.database.fetch_one(query=query)

    async def delete_post(self, id: int) -> bool:
        query = sql.delete(Posts).where(
            Posts.post_id == id)
        await self.database.execute(query)
        return True

    async def create_first_post(self, user_id: int):
        new_post = NewPost(
            created_at=datetime.now(),
            title= None,
            content="""Welcome to our note-taking app! Elon Musk once said, "When there's nothing to lose, there's only winning left." Plan your victories and successes with our application.""",
            user_id=user_id
        )
        values = {**new_post.dict()}
        query = sql.insert(Posts).values(**values)
        await self.database.execute(query)
        return True
