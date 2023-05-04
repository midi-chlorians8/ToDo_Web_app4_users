import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


from app.routes.api.user import users_route
from app.routes.api.posts import posts_route

# from app.routes.web.notes import notes_web_route
from app.routes.web.policy import policy_web_route
from app.routes.api.helfcheck import health_route

from app.exceptions import NotFoundException, ConflictException, UnauthorizedException, ApiException

from app.core.db import database


def create_app() -> FastAPI:
    app = FastAPI()
    # app.mount("/static", StaticFiles(directory="app/static"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],  # allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(ApiException)
    async def unicorn_exception_handler(request: Request, exc: ApiException):
        status_code = exc.__dict__['status_code']
        content = exc.__dict__['name']
        return JSONResponse(
            status_code=status_code,
            content=content,
        )

    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(
            request: Request,
            exc: NotFoundException,
            status: status = status.HTTP_404_NOT_FOUND):
        status_code = status
        content = exc.__dict__['name']
        return JSONResponse(
            status_code=status_code,
            content=f'{content} not found',
        )

    @app.exception_handler(ConflictException)
    async def conflict_exception_handler(
            request: Request,
            exc: ConflictException,
            status: status = status.HTTP_409_CONFLICT):
        status_code = status
        content = exc.__dict__['name']
        return JSONResponse(
            status_code=status_code,
            content=content,
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(
            request: Request,
            exc: UnauthorizedException,
            status: status = status.HTTP_401_UNAUTHORIZED):
        status_code = status
        content = exc.__dict__['name']
        return JSONResponse(
            status_code=status_code,
            content=content,
        )

    app.include_router(router=users_route, prefix='/users', tags=["users"])
    app.include_router(router=posts_route, prefix='/posts', tags=["posts"])

    # app.include_router(router=notes_web_route, tags=["notes_web"])
    app.include_router(router=policy_web_route, prefix='/policy', tags=["other"])
    app.include_router(router=health_route, prefix='/healthcheck', tags=["healthcheck"])

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app


if __name__ == "__main__":
    uvicorn.run("main:create_app", port=8000,
                host="0.0.0.0", reload=True)
