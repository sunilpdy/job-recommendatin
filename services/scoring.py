from typing import List, Tuple

from config import (
    SKILL_WEIGHT,
    EDUCATION_WEIGHT,
    EXPERIENCE_WEIGHT,
    SEMANTIC_WEIGHT
)


class ScoringEngine:

    @staticmethod
    def calculate_skill_score(
        candidate_skills: List[str],
        required_skills: List[str]
    ) -> Tuple[float, List[str], List[str]]:

        candidate_set = {
            skill.lower().strip()
            for skill in candidate_skills
        }

        required_set = {
            skill.lower().strip()
            for skill in required_skills
        }

        if not required_set:
            return 100.0, [], []

        matched = candidate_set.intersection(
            required_set
        )

        missing = required_set - candidate_set

        score = (
            len(matched) /
            len(required_set)
        ) * 100

        return (
            round(score, 2),
            sorted(matched),
            sorted(missing)
        )

    @staticmethod
    def calculate_education_score(
        candidate_education: List[str],
        required_education: List[str]
    ) -> float:

        if not required_education:
            return 100.0

        candidate_text = " ".join(
            candidate_education
        ).lower()

        matches = 0

        for education in required_education:

            if education.lower() in candidate_text:
                matches += 1

        score = (
            matches /
            len(required_education)
        ) * 100

        return round(score, 2)

    @staticmethod
    def calculate_experience_score(
        candidate_years: float,
        required_years: float
    ) -> float:

        if required_years <= 0:
            return 100.0

        if candidate_years >= required_years:
            return 100.0

        score = (
            candidate_years /
            required_years
        ) * 100

        return round(min(score, 100), 2)

    @staticmethod
    def calculate_final_score(
        skill_score: float,
        education_score: float,
        experience_score: float,
        semantic_score: float
    ) -> float:

        final_score = (
            skill_score * SKILL_WEIGHT +
            education_score * EDUCATION_WEIGHT +
            experience_score * EXPERIENCE_WEIGHT +
            semantic_score * SEMANTIC_WEIGHT
        )

        return round(final_score, 2)
