from datetime import timedelta
from fastapi import APIRouter,Depends,HTTPException,status
from typing import Annotated
from app.schemas.token import Token,LoginPayload
from app.utils.auth_utils import authenticate_user,create_access_token




router = APIRouter()


@router.post("/token",response_model=Token,status_code=200)
async def login_for_access_token(
    request: LoginPayload
):  
    user = await authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=15)
    access_token = await create_access_token(
        data={"data": {"username":user.user_name,"email":user.email}
        }, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
