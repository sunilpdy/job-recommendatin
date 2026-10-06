# AI Job Recommendation System

An AI-powered **Job Recommendation and Matching System** that analyzes a candidate's skills, education, experience, and resume content to recommend the most relevant job opportunities.

The system combines **skill-based matching, education matching, experience matching, and semantic text similarity** to calculate an overall job compatibility score and rank jobs accordingly.

---

## Features

* Candidate profile-based job recommendations
* Resume text analysis
* Automatic skill extraction
* Skill matching between candidate and job requirements
* Education compatibility analysis
* Experience-level matching
* TF-IDF-based semantic similarity
* Weighted final matching score
* Matched and missing skills identification
* Ranked job recommendations
* REST API using FastAPI
* Pydantic data validation
* Modular and extensible architecture
* JSON-based job dataset
* Swagger/OpenAPI API documentation

---

## Recommendation Algorithm

The system calculates a final job matching score using four major components:

| Component           | Weight |
| ------------------- | -----: |
| Skills              |    40% |
| Education           |    20% |
| Experience          |    20% |
| Semantic Similarity |    20% |

### Final Score

```text
Final Score =
    (Skill Score × 0.40)
  + (Education Score × 0.20)
  + (Experience Score × 0.20)
  + (Semantic Score × 0.20)
```

For example:

```text
Skill Score        = 80%
Education Score    = 100%
Experience Score   = 75%
Semantic Score     = 72%

Final Score =
(80 × 0.40) +
(100 × 0.20) +
(75 × 0.20) +
(72 × 0.20)

= 81.4%
```

---

## System Architecture

```text
                    Candidate
                       |
                       v
              +----------------+
              | Resume / Input |
              +-------+--------+
                      |
                      v
              +---------------+
              | Text Processing|
              +-------+-------+
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Skills     Education   Experience
          |           |           |
          +-----------+-----------+
                      |
                      v
             +-------------------+
             | Matching Engine   |
             +---------+---------+
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
   Skill Match    Experience     Semantic
                  Match          Similarity
        |              |              |
        +--------------+--------------+
                       |
                       v
               Final Match Score
                       |
                       v
              Ranked Job Results
```

---

## Project Structure

```text
job_recommendation_system/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   └── jobs.json
│
├── models/
│   └── schemas.py
│
├── services/
│   ├── text_processor.py
│   ├── skill_extractor.py
│   ├── similarity.py
│   ├── scoring.py
│   └── recommender.py
│
└── tests/
    └── test_recommender.py
```

---

## Technologies Used

### Programming Language

* Python 3.10+

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Machine Learning / NLP

* Scikit-learn
* TF-IDF
* Cosine Similarity

### Data Processing

* JSON
* Python standard library

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd job_recommendation_system
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoint

### `POST /recommend`

Returns the most relevant jobs for a candidate.

### Request

```json
{
    "name": "John Doe",
    "skills": [
        "Python",
        "FastAPI",
        "MongoDB",
        "Docker",
        "Git"
    ],
    "education": [
        "Computer Engineering"
    ],
    "experience_years": 2,
    "experience_text": "Python backend development and REST API development",
    "resume_text": "Experienced Python backend developer with experience in FastAPI, MongoDB, Docker and REST APIs."
}
```

### Response

```json
[
    {
        "job_id": 1,
        "title": "Python Backend Developer",
        "company": "Tech Solutions",
        "location": "Kathmandu",
        "skill_score": 75.0,
        "education_score": 100.0,
        "experience_score": 100.0,
        "semantic_score": 71.32,
        "final_score": 84.26,
        "matched_skills": [
            "docker",
            "fastapi",
            "git",
            "mongodb",
            "python",
            "rest api"
        ],
        "missing_skills": [
            "django",
            "postgresql"
        ]
    }
]
```

---

## How Matching Works

### 1. Skill Matching

The system compares the candidate's skills against the skills required by each job.

For example:

```text
Candidate Skills:
Python
FastAPI
MongoDB
Docker
Git

Job Requirements:
Python
FastAPI
Django
MongoDB
PostgreSQL
Docker
Git
```

Matched skills:

```text
Python
FastAPI
MongoDB
Docker
Git
```

Missing skills:

```text
Django
PostgreSQL
```

The skill score is calculated based on the percentage of required skills that the candidate possesses.

---

### 2. Education Matching

The system compares the candidate's educational background with the education requirements of the job.

Example:

```text
Candidate:
Computer Engineering

Job:
Computer Science
Computer Engineering
Software Engineering
```

Since `Computer Engineering` matches one of the accepted educational backgrounds, the candidate receives an education score.

---

### 3. Experience Matching

The system compares the candidate's experience with the minimum experience required for the position.

Example:

```text
Candidate Experience: 2 years
Required Experience: 2 years

Experience Score: 100%
```

If the candidate has less experience:

```text
Candidate Experience: 1 year
Required Experience: 2 years

Experience Score: 50%
```

---

### 4. Semantic Similarity

The system uses **TF-IDF vectorization and cosine similarity** to compare the candidate's profile with job descriptions.

This helps identify similarity between the overall candidate profile and job requirements rather than relying only on exact skill matches.

---

## Skill Extraction

The system can automatically identify predefined skills from resume text.

Example:

```text
Resume:

"Experienced Python developer with FastAPI, MongoDB,
Docker and REST API development experience."
```

Extracted skills:

```text
Python
FastAPI
MongoDB
Docker
REST API
```

Skill aliases are also supported.

For example:

```text
"python3"       → Python
"mongo db"      → MongoDB
"restful api"   → REST API
"k8s"           → Kubernetes
"sklearn"       → Scikit-learn
```

---

## Recommendation Output

For each recommended job, the system provides:

```text
Job Title
Company
Location
Skill Score
Education Score
Experience Score
Semantic Score
Final Score
Matched Skills
Missing Skills
```

This makes the recommendation more transparent and explainable.

---

## Example Recommendation

```text
==================================================
Recommended Job
==================================================

Position:
Python Backend Developer

Company:
Tech Solutions

Location:
Kathmandu

Skill Score:
75%

Education Score:
100%

Experience Score:
100%

Semantic Score:
71.32%

Final Match:
84.26%

Matched Skills:
✓ Python
✓ FastAPI
✓ MongoDB
✓ Docker
✓ Git
✓ REST API

Missing Skills:
✗ Django
✗ PostgreSQL
```

---

## Future Improvements

The current implementation provides a foundation for an AI-based job recommendation platform. Future versions can include:

### Advanced NLP

* Sentence Transformers
* BERT
* Word embeddings
* Semantic skill matching
* Context-aware resume analysis

### Resume Processing

* PDF resume upload
* DOCX resume support
* Automatic resume parsing
* Named Entity Recognition
* Email and phone extraction
* Education extraction
* Work experience extraction
* Certification extraction

### Database

Replace the JSON job database with:

```text
MySQL
PostgreSQL
MongoDB
```

### Advanced Recommendation

Future versions can consider:

* Candidate preferences
* Salary expectations
* Job location
* Remote/hybrid preference
* Industry
* Job seniority
* Career history
* Certifications
* Courses
* Company preferences

### Machine Learning

A future recommendation engine could learn from:

```text
Job views
Applications
Saved jobs
Rejected jobs
Interview selections
Successful hires
```

and use this information to personalize recommendations.

---

## Planned Production Architecture

```text
                    +------------------+
                    |    Web / Mobile  |
                    |     Frontend     |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |    FastAPI API    |
                    +--------+---------+
                             |
             +---------------+---------------+
             |               |               |
             v               v               v
       Resume Parser    Job Service    Recommendation
             |               |               |
             v               v               v
        NLP Engine       Database       ML/NLP Engine
             |               |               |
             +---------------+---------------+
                             |
                             v
                    +------------------+
                    | Ranked Job List  |
                    +------------------+
```

---

## Testing

Run tests using:

```bash
pytest
```

Example:

```bash
pytest tests/
```

---

## Error Handling

The application validates:

* Candidate input
* Missing candidate skills/resume
* Invalid `top_n`
* Missing job dataset
* Invalid job data
* Empty text fields

FastAPI also provides automatic validation through Pydantic models.

---

## Security Considerations

For a production deployment, the following should be added:

* Authentication and authorization
* API rate limiting
* Input validation
* File upload restrictions
* Resume privacy protection
* Secure database credentials
* Environment variables
* HTTPS
* Logging and monitoring

---

## License

This project is intended for educational and research purposes.

A production implementation should include an appropriate open-source or commercial license depending on how the project is distributed.

---

## Author

**AI Job Recommendation System**

Developed as a Python-based AI/NLP project for intelligent resume-to-job matching and personalized job recommendations.
