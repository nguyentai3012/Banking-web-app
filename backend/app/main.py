from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from backend.app.api.api_v1.routers import router
from backend.app.core.config import settings
from backend.app.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).Banking
    await init_beanie(
        database=db_client,
        document_models=[User]
    )


app.include_router(router, prefix=settings.API_V1_STR)
