from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine

from app.setting import CONFIG

SQLALCHEMY_DATABASE_URL = CONFIG.SQLALCHEMY_DATABASE_URL

database = Database(SQLALCHEMY_DATABASE_URL)
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
