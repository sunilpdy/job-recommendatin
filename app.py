from fastapi import FastAPI, HTTPException

from config import JOBS_FILE

from models.schemas import (
    Candidate,
    Recommendation
)

from services.recommender import JobRecommender


app = FastAPI(
    title="AI Job Recommendation System",
    version="1.0.0"
)


recommender = JobRecommender(
    str(JOBS_FILE)
)


@app.get("/")
def home():

    return {
        "message": "AI Job Recommendation System",
        "status": "running"
    }


@app.post(
    "/recommend",
    response_model=list[Recommendation]
)
def recommend_jobs(
    candidate: Candidate,
    top_n: int = 10
):

    if top_n <= 0:
        raise HTTPException(
            status_code=400,
            detail="top_n must be greater than 0"
        )

    if not candidate.skills and not candidate.resume_text:
        raise HTTPException(
            status_code=400,
            detail="Candidate skills or resume text is required"
        )

    return recommender.recommend(
        candidate,
        top_n=top_n
    )
