from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

JOBS_FILE = DATA_DIR / "jobs.json"

# Recommendation weights
SKILL_WEIGHT = 0.40
EDUCATION_WEIGHT = 0.20
EXPERIENCE_WEIGHT = 0.20
SEMANTIC_WEIGHT = 0.20

# Minimum score required for recommendation
MIN_RECOMMENDATION_SCORE = 30.0
