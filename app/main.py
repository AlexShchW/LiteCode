from fastapi import FastAPI
from typing import Optional
import os
import json

from app.routers.problems_router import router as problems_router

app = FastAPI()

app.include_router(problems_router)
