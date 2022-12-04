import pymongo
from fastapi import APIRouter, HTTPException, status
from backend.app.schemas.user_schema import UserAuth
from backend.app.services.user_service import UserService

user_router = APIRouter()


@user_router.post("/create", summary="Create new user")
async def create_user(data: UserAuth):
    try:
        await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )
