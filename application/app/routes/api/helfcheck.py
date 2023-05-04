from fastapi import APIRouter

health_route = APIRouter()


@health_route.get("/")
async def healthcheck() -> dict:
    return {"status": "OK", "message": "Application is running"}
