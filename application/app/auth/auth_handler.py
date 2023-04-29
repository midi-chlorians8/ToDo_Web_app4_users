import time
from typing import Dict

import jwt
from app.setting import CONFIG
from time import time
from app.shemas.user import TokenPayload


JWT_SECRET = CONFIG.SECRET
JWT_ALGORITHM = CONFIG.ALGORITHM
JWT_RESET_SECRET_KEY = CONFIG.JWT_RESET_SECRET_KEY

from typing import Optional
from datetime import timedelta, datetime

def token_response(token: str):
    return {
        "access_token": token
    }

# def signJWT(user_id: str, user_email: str, expires_delta: Optional[timedelta] = None) -> Dict[str, str]:
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(hours=24)
    
#     payload = {
#         "user_id": user_id,
#         "sub": user_email,
#         "expires": expire.timestamp()
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)

def signJWT(user_email: str, expires_delta: Optional[timedelta] = None) -> Dict[str, str]: #work [ass repair]
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "sub": user_email,  # Замените 'user_id' на 'sub'
        "expires": expire.timestamp()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def get_reset_password_token(email: str, expires_in: int) -> str:
    return jwt.encode(
        {'sub': email, 'exp': time() + expires_in},
        JWT_RESET_SECRET_KEY, algorithm=JWT_ALGORITHM)


async def get_user_email_from_reset_token(token: str):
    payload = jwt.decode(token, JWT_RESET_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    token_data = TokenPayload(**payload)
    return token_data.sub

# def signJWT(user_email: str, expires_delta: Optional[timedelta] = None) -> Dict[str, str]:
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(hours=24)

#     payload = {
#         "user_id": user_email,  # Замените 'user_id' на 'user_email'
#         "expires": expire.timestamp()
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)
# def signJWT(user_id: str, expires_delta: Optional[timedelta] = None) -> Dict[str, str]:
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(hours=24)
    
#     payload = {
#         "user_id": user_id,
#         "expires": expire.timestamp()
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)

# def token_response(token: str):
#     return {
#         "access_token": token
#     }


# def signJWT(user_id: str) -> Dict[str, str]:
#     payload = {
#         "user_id": user_id,
#         #"expires": time.time() + 600
#         "expires": time.time() + 60 * 60 * 24
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
