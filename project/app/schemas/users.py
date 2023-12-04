from typing import Dict
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    user_name: str 
    email: str
    password: str

class UserCreationResponse(BaseModel):
    user_name: str 
    email: str



