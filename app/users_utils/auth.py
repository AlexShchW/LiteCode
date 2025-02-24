import datetime
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.DAO.users_DAO import UsersDAO
from app.config import JWT_ALGORITHM, JWT_SECRET_KEY

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire =  datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_by_email(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
    