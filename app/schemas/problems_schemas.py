from typing import Any, Dict, List
from pydantic import BaseModel

class ProblemSchema(BaseModel):
    id: int
    name: str
    category: str
    difficulty: str
    description: str
    recommended_time_complexity: str
    recommended_space_complexity: str
    testcases: List[Dict[str, Any]]

    class Config:
        from_attributes = True


class CodeSubmission(BaseModel):
    code: str