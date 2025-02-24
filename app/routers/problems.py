from fastapi import APIRouter, HTTPException

from app.DAO.problems_DAO import ProblemsDAO
from app.schemas.problems_schemas import ProblemSchema


router = APIRouter(
    prefix="/problems",
    tags=["Problems"],
)

@router.get("/", response_model=list[ProblemSchema])
async def get_problems(category: str = None, difficulty: str = None):
    filters = {}
    if category:
        filters["category"] = category
    if difficulty:
        filters["difficulty"] = difficulty
    problems = await ProblemsDAO.find_all(**filters)
    if not problems:
        raise HTTPException(status_code=404, detail="No problems found")
    return problems


@router.get("/{problem_id}", response_model=ProblemSchema)
async def get_problem_by_id(problem_id: int):
    problem = await ProblemsDAO.find_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    return problem