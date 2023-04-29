from app.core.user import UserRepository
from app.core.db import database


def get_user_repository() -> UserRepository:
    return UserRepository(database)
