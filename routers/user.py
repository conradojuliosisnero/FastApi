from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from shemas.user import User

user_router = APIRouter()

# ruta de login 
@user_router.post('/login',tags=['authentication'])
def login_user(user: User):
    if user.email == "admin@gmail.com" and user.password == "1234":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200,content=token)