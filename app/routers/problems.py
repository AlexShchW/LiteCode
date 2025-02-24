from fastapi import APIRouter, Depends, HTTPException

from app.DAO.problems_DAO import ProblemsDAO
from app.models.users_model import Users
from app.schemas.problems_schemas import CodeSubmission, ProblemSchema
from app.users_utils.dependencies import get_current_user

from app.solving_utils.process_code_utils import validate_code

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



@router.post("/{problem_id}/submit")
async def validate_solution(problem_id: int, submission: CodeSubmission, user: Users = Depends(get_current_user)):
    problem = await ProblemsDAO.find_by_id(problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")
    testcases = problem.testcases
    code = submission.code
    validation_results = await validate_code(code, testcases)
    passed_amount = sum(result["passed"] for result in validation_results)
    total_testcases = len(testcases)
    submission_result = passed_amount == total_testcases
    return {"submission_result": submission_result,
            "testcases_result": f"passed {passed_amount} out of {total_testcases} tests"}
