import json
from pathlib import Path
from typing import List

from models.schemas import (
    Candidate,
    Job,
    Recommendation
)

from services.scoring import ScoringEngine
from services.similarity import SimilarityEngine
from services.skill_extractor import SkillExtractor


class JobRecommender:

    def __init__(self, jobs_file: str):

        self.jobs = self._load_jobs(jobs_file)

        self.similarity_engine = SimilarityEngine()

        self.scoring_engine = ScoringEngine()

    @staticmethod
    def _load_jobs(
        jobs_file: str
    ) -> List[Job]:

        path = Path(jobs_file)

        if not path.exists():
            raise FileNotFoundError(
                f"Jobs file not found: {path}"
            )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return [
            Job(**job)
            for job in data
        ]

    @staticmethod
    def _create_job_text(job: Job) -> str:

        return " ".join([
            job.title,
            " ".join(job.skills),
            " ".join(job.education),
            job.description
        ])

    @staticmethod
    def _create_candidate_text(
        candidate: Candidate
    ) -> str:

        return " ".join([
            " ".join(candidate.skills),
            " ".join(candidate.education),
            candidate.experience_text,
            candidate.resume_text
        ])

    def recommend(
        self,
        candidate: Candidate,
        top_n: int = 10
    ) -> List[Recommendation]:

        candidate_skills = candidate.skills

        # Automatically extract skills from resume
        if candidate.resume_text:

            extracted_skills = (
                SkillExtractor.extract(
                    candidate.resume_text
                )
            )

            candidate_skills = list(
                set(
                    candidate_skills +
                    extracted_skills
                )
            )

        candidate_text = self._create_candidate_text(
            candidate
        )

        job_texts = [
            self._create_job_text(job)
            for job in self.jobs
        ]

        semantic_scores = (
            self.similarity_engine.calculate_similarity(
                candidate_text,
                job_texts
            )
        )

        recommendations = []

        for index, job in enumerate(self.jobs):

            skill_score, matched, missing = (
                self.scoring_engine.calculate_skill_score(
                    candidate_skills,
                    job.skills
                )
            )

            education_score = (
                self.scoring_engine.calculate_education_score(
                    candidate.education,
                    job.education
                )
            )

            experience_score = (
                self.scoring_engine.calculate_experience_score(
                    candidate.experience_years,
                    job.experience_required
                )
            )

            semantic_score = semantic_scores[index]

            final_score = (
                self.scoring_engine.calculate_final_score(
                    skill_score,
                    education_score,
                    experience_score,
                    semantic_score
                )
            )

            recommendations.append(
                Recommendation(
                    job_id=job.id,
                    title=job.title,
                    company=job.company,
                    location=job.location,
                    skill_score=skill_score,
                    education_score=education_score,
                    experience_score=experience_score,
                    semantic_score=semantic_score,
                    final_score=final_score,
                    matched_skills=matched,
                    missing_skills=missing
                )
            )

        recommendations.sort(
            key=lambda x: x.final_score,
            reverse=True
        )

        return recommendations[:top_n]
