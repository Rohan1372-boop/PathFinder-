from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PathFinder AI API")

# -----------------------------
# CORS (IMPORTANT for GitHub Pages frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Model
# -----------------------------
class QuizSubmission(BaseModel):
    answers: Dict[str, int] = Field(..., example={
        "R1": 8, "R2": 7, "R3": 6,
        "I1": 9, "I2": 8, "I3": 7,
        "A1": 5, "A2": 6, "A3": 5,
        "S1": 4, "S2": 5, "S3": 6,
        "E1": 7, "E2": 6, "E3": 7,
        "C1": 5, "C2": 6, "C3": 5
    })

# -----------------------------
# Career Database (Expandable)
# -----------------------------
career_database = {
    "Realistic": [
        {
            "career": "Mechanical Engineer",
            "roadmap": {
                "Foundation": [
                    "Complete 12th with PCM",
                    "Prepare for JEE/CET"
                ],
                "Skill Development": [
                    "Learn CAD software",
                    "Understand manufacturing processes"
                ],
                "Experience": [
                    "Intern in manufacturing companies",
                    "Work on practical projects"
                ],
                "Advanced Growth": [
                    "Learn automation",
                    "Pursue M.Tech or specialize"
                ]
            }
        }
    ],
    "Investigative": [
        {
            "career": "Data Scientist",
            "roadmap": {
                "Foundation": [
                    "Learn Python",
                    "Study Statistics & Mathematics"
                ],
                "Skill Development": [
                    "Learn Machine Learning",
                    "Work on real datasets"
                ],
                "Experience": [
                    "Build ML portfolio projects",
                    "Participate in hackathons"
                ],
                "Advanced Growth": [
                    "Learn Deep Learning",
                    "Deploy ML models"
                ]
            }
        }
    ],
    "Artistic": [
        {
            "career": "UI/UX Designer",
            "roadmap": {
                "Foundation": [
                    "Learn design basics",
                    "Understand color theory"
                ],
                "Skill Development": [
                    "Learn Figma",
                    "Design case studies"
                ],
                "Experience": [
                    "Build portfolio",
                    "Freelance projects"
                ],
                "Advanced Growth": [
                    "Work with startups",
                    "Specialize in product design"
                ]
            }
        }
    ],
    "Social": [
        {
            "career": "Psychologist",
            "roadmap": {
                "Foundation": [
                    "Study Psychology",
                    "Complete Bachelor's degree"
                ],
                "Skill Development": [
                    "Learn counseling techniques"
                ],
                "Experience": [
                    "Intern at clinics"
                ],
                "Advanced Growth": [
                    "Complete Master's",
                    "Get licensed"
                ]
            }
        }
    ],
    "Enterprising": [
        {
            "career": "Entrepreneur",
            "roadmap": {
                "Foundation": [
                    "Learn business fundamentals"
                ],
                "Skill Development": [
                    "Validate startup ideas",
                    "Build MVP"
                ],
                "Experience": [
                    "Launch startup",
                    "Get early users"
                ],
                "Advanced Growth": [
                    "Scale business",
                    "Seek investment"
                ]
            }
        }
    ],
    "Conventional": [
        {
            "career": "Chartered Accountant",
            "roadmap": {
                "Foundation": [
                    "Register for CA Foundation"
                ],
                "Skill Development": [
                    "Clear Inter exams",
                    "Complete articleship"
                ],
                "Experience": [
                    "Work with CA firm"
                ],
                "Advanced Growth": [
                    "Clear Final",
                    "Start practice or join firm"
                ]
            }
        }
    ]
}

# -----------------------------
# Trait Mapping
# -----------------------------
trait_map = {
    "R": "Realistic",
    "I": "Investigative",
    "A": "Artistic",
    "S": "Social",
    "E": "Enterprising",
    "C": "Conventional"
}

# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(data: QuizSubmission):

    trait_scores = {
        "Realistic": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Social": 0,
        "Enterprising": 0,
        "Conventional": 0
    }

    # Calculate scores
    for question, score in data.answers.items():
        trait_letter = question[0]  # R1 -> R
        trait_name = trait_map[trait_letter]
        trait_scores[trait_name] += score

    # Sort traits
    sorted_traits = sorted(trait_scores.items(), key=lambda x: x[1], reverse=True)

    dominant_trait = sorted_traits[0][0]
    total_score = sum(trait_scores.values())

    confidence = round((sorted_traits[0][1] / total_score) * 100, 2)

    recommended_careers = career_database[dominant_trait]

    return {
        "dominant_trait": dominant_trait,
        "confidence_percentage": confidence,
        "recommended_careers": recommended_careers,
        "all_scores": trait_scores
    }
