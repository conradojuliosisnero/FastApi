from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token

user_router = APIRouter()

class user(BaseModel):
    email: str
    password: str
    
# ruta de login 
@user_router.post('/login',tags=['authentication'])
def login_user(user: user):
    if user.email == "admin@gmail.com" and user.password == "1234":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200,content=token)