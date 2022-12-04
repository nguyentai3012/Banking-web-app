from backend.app.core.security import get_password
from backend.app.models.user_model import User
from backend.app.schemas.user_schema import UserAuth


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password),
            first_name=user.first_name,
            last_name=user.last_name,
            disabled=user.disabled
        )
        await user_in.save()
        return user_in

