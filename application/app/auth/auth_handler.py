import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

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
