from http import HTTPStatus
from typing import Union
from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, name: str, status_code: Union[HTTPStatus, int] = HTTPStatus.BAD_REQUEST):
        self.name = name
        self.status_code = status_code if status_code else HTTPStatus.BAD_REQUEST


class BaseAppException(Exception):
    def __init__(self, name: str):
        self.name = name


class NotFoundException(BaseAppException):
    pass


class ConflictException(BaseAppException):
    pass


class UnauthorizedException(BaseAppException):
    pass