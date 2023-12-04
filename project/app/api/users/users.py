from fastapi import APIRouter
from app.schemas.users import UserCreateSchema,UserCreationResponse
from app.api.users import repository

router = APIRouter()


@router.post("/create",response_model=UserCreationResponse,status_code=201)
async def create_user(request : UserCreateSchema)-> UserCreationResponse:
    user = await repository.create(request)
    return {    
        "user_name": user.user_name,
        "email": user.email}

