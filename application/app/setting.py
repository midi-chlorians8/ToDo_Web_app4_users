from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET: str
    JWT_RESET_SECRET_KEY: str
    ALGORITHM: str
    SQLALCHEMY_DATABASE_URL: str

    class Config:
        env_file = "./.env"


CONFIG = Settings()
