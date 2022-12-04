from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user name")
    password: str = Field(..., min_length=5, max_length=50, description="user password")
    first_name: str = Field(..., min_length=5, max_length=50, description="first name")
    last_name: str = Field(..., min_length=5, max_length=50, description="lastname")
    disabled: bool = Field(default=True)
