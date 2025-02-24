from fastapi import FastAPI

from app.routers.problems_router import router as problems_router

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to the LiteCode API! Go to /docs"}

app.include_router(problems_router)
