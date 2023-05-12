from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET: str
    JWT_RESET_SECRET_KEY: str
    ALGORITHM: str
    SQLALCHEMY_DATABASE_URL: str

    EMAIL_USER: str
    EMAIL_PASS: str
    
    class Config:
        env_file = "./.env"


CONFIG = Settings()
