from app.core.db import database
from app.core.user import UserRepository


def get_user_repository() -> UserRepository:
    return UserRepository(database)
