import time
from typing import Dict

import jwt
from app.setting import CONFIG
from time import time
from app.shemas.user import TokenPayload
from typing import Optional
from datetime import timedelta, datetime
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2
from fastapi import Depends, Request
from app.repositories.user import get_user_repository
from app.exceptions import ConflictException, NotFoundException, ApiException

JWT_SECRET = CONFIG.SECRET
JWT_ALGORITHM = CONFIG.ALGORITHM
JWT_RESET_SECRET_KEY = CONFIG.JWT_RESET_SECRET_KEY


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise ApiException(name="Invalid authentication scheme.", status_code=403)
            verify_jwt(credentials.credentials)
            return credentials.credentials
        else:
            raise ApiException(name="Invalid authorization code.", status_code=403)


class OAuth2PasswordBearerWithCookie(OAuth2):
    async def __call__(self, request: Request) -> str:
        access_token: str = request.cookies.get("access_token")
        if access_token:
            verify_jwt(access_token)
            return access_token


def verify_jwt(token: str) -> None:
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.exceptions.ExpiredSignatureError:
        raise ApiException(name="Token expired", status_code=401)
    except jwt.exceptions.InvalidSignatureError:
        raise ApiException(name="Invalid token.", status_code=403)


def signJWT(user_email: str, expires_delta: Optional[timedelta] = None) -> Dict[str, str]: #work [ass repair]
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "user_id": user_email,  # Замените 'user_id' на 'sub'
        "expires": expire.timestamp()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


async def get_current_user_id(token: str = Depends(JWTBearer())):
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    token_data = TokenPayload(**payload)

    return token_data


def get_reset_password_token(data, user) -> str:
    check_user = UserAPIController.get_user_by_email_or_none(email=data.email, user=get_user_repository())
    if check_user is None:
        raise NotFoundException(name="User")
    return jwt.encode(
        {'sub': email, 'exp': time() + expires_in},
        JWT_RESET_SECRET_KEY, algorithm=JWT_ALGORITHM)


async def get_user_email_from_reset_token(token: str):
    payload = jwt.decode(token, JWT_RESET_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    token_data = TokenPayload(**payload)
    return token_data.sub


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
