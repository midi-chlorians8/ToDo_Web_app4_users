from sqlalchemy import sql
from app.models.user import User
from app.shemas.user import UserSchemaCreate
from app.auth.security import hash_password

from app.base_repository import BaseRepository


class UserRepository(BaseRepository):
    async def get_by_email_or_none(self, email: str) -> list or None:
        query = sql.select(User).where(User.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return user

    async def create_user(self, data: UserSchemaCreate) -> str:
        user = UserSchemaCreate(
            fullname=data.fullname,
            email=data.email,
            psw=hash_password(data.psw)
        )
        values = {**user.dict()}
        query = sql.insert(User).values(**values).returning(
            User.email,
        )
        resp = await self.database.fetch_one(query=query)
        return resp.email

    async def change_password(self, email: str, psw: str) -> str:
        upd_user = sql.update(User).where(User.email == email).values(psw=hash_password(psw))
        await self.database.execute(query=upd_user)
        return True
