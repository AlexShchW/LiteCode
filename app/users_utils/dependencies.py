import datetime
from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError

from app.DAO.users_DAO import UsersDAO
from app.config import JWT_SECRET_KEY, JWT_ALGORITHM


def get_token(request: Request):
    token = request.cookies.get("litecode_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get('exp')
    if not expire or int(expire) < datetime.datetime.now(datetime.timezone.utc).timestamp():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return user