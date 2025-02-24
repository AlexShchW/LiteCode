from fastapi import FastAPI

from app.routers.problems import router as problems_router
from app.routers.users import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(problems_router)
@app.get("/")
async def root():
    return {"message": "Welcome to the LiteCode API! Go to /docs"}
