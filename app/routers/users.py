from fastapi import APIRouter, Depends, HTTPException, Response

from app.DAO.users_DAO import UsersDAO
from app.models.users_model import Users
from app.schemas.users_schemas import UserAuthSchema
from app.users_utils.auth import authenticate_user, create_access_token, get_password_hash
from app.users_utils.dependencies import get_current_user

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@auth_router.post("/register")
async def register(user_data: UserAuthSchema):
    existing_user = await UsersDAO.find_by_email(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.create_user(email=user_data.email, hashed_password=hashed_password)

@auth_router.post("/login")
async def login(response: Response, user_data: UserAuthSchema):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="litecode_access_token", value=access_token, httponly=True)
    return {"access_token" : access_token}

@auth_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="litecode_access_token")
    return {"detail": "Logged out"}

@auth_router.get("/me")
async def me(user: Users = Depends(get_current_user)):
    current_user_email = user.email
    return {"email" : current_user_email}