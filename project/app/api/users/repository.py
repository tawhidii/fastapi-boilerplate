from fastapi import HTTPException
from app.models.users import Users
from app.schemas.users import UserCreateSchema
from app.utils.auth_utils import get_password_hash


async def create(request: UserCreateSchema) -> Users:
    is_user_name_exists = await Users.exists(user_name=request.user_name)
    is_email_exists = await Users.exists(email=request.email)
    if is_user_name_exists:
        raise HTTPException(status_code=400,detail="user name already exists !")
    if is_email_exists:
        raise HTTPException(status_code=400,detail="email already exists !")  
    user = await Users.create(
            user_name=request.user_name,
            email=request.email,
            password=get_password_hash(request.password)
            )
    return  user

