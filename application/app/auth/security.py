from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(psw: str) -> str:
    return pwd_context.hash(psw)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)
