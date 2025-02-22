from sqlalchemy import JSON, Column, Integer, String
from app.database.database_access import Base

class Problems(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String, index=True)
    difficulty = Column(String, index=True)
    description = Column(String)
    recommended_time_complexity = Column(String)
    recommended_space_complexity = Column(String)
    testcases = Column(JSON)