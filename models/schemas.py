from typing import List, Optional

from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str

    skills: List[str] = Field(default_factory=list)

    education: List[str] = Field(default_factory=list)

    experience_years: float = 0.0

    experience_text: str = ""

    resume_text: str = ""


class Job(BaseModel):
    id: int

    title: str

    company: str

    location: str

    skills: List[str] = Field(default_factory=list)

    education: List[str] = Field(default_factory=list)

    experience_required: float = 0.0

    description: str = ""

    employment_type: Optional[str] = None


class Recommendation(BaseModel):
    job_id: int

    title: str

    company: str

    location: str

    skill_score: float

    education_score: float

    experience_score: float

    semantic_score: float

    final_score: float

    matched_skills: List[str]

    missing_skills: List[str]
