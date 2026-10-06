from typing import List

from services.text_processor import TextProcessor


class SkillExtractor:

    SKILL_ALIASES = {
        "python": ["python", "python3"],
        "fastapi": ["fastapi"],
        "django": ["django"],
        "rest api": ["rest api", "restful api", "rest"],
        "mongodb": ["mongodb", "mongo db", "mongo"],
        "postgresql": ["postgresql", "postgres"],
        "mysql": ["mysql"],
        "docker": ["docker", "docker container"],
        "kubernetes": ["kubernetes", "k8s"],
        "aws": ["aws", "amazon web services"],
        "git": ["git", "github", "gitlab"],
        "machine learning": [
            "machine learning",
            "ml"
        ],
        "tensorflow": ["tensorflow"],
        "pytorch": ["pytorch"],
        "numpy": ["numpy"],
        "pandas": ["pandas"],
        "scikit-learn": [
            "scikit-learn",
            "sklearn"
        ],
        "javascript": [
            "javascript",
            "js"
        ],
        "typescript": ["typescript", "ts"],
        "react": ["react", "reactjs"],
        "html": ["html"],
        "css": ["css"],
        "linux": ["linux"],
        "jenkins": ["jenkins"],
        "terraform": ["terraform"],
        "ci/cd": [
            "ci/cd",
            "continuous integration",
            "continuous deployment"
        ]
    }

    @classmethod
    def extract(cls, text: str) -> List[str]:

        text = TextProcessor.clean_text(text)

        detected_skills = []

        for skill, aliases in cls.SKILL_ALIASES.items():

            for alias in aliases:

                if alias.lower() in text:

                    detected_skills.append(skill)

                    break

        return sorted(set(detected_skills))
