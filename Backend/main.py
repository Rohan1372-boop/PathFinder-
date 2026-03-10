"""
main.py
-------
FastAPI application entry-point for Pathfinder.

Run with:
    uvicorn main:app --reload

Then open the frontend via VS Code Live Server (default: http://127.0.0.1:5500).
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from questions import QUESTIONS
from career_logic import analyse_answers
from roadmaps import get_roadmap

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(title="Pathfinder API", version="1.0.0")

# Allow any origin so the frontend (served via Live Server) can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------
class AnswersPayload(BaseModel):
    answers: list[int]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/")
def root():
    """Health-check – confirms the API is running."""
    return {"message": "Pathfinder API is running 🚀"}


@app.get("/api/questions")
def api_get_questions():
    """
    GET /api/questions
    Returns the list of 10 personality quiz questions.
    """
    return {"questions": QUESTIONS}


@app.post("/api/submitQuiz")
def api_submit_quiz(payload: AnswersPayload):
    """
    POST /api/submitQuiz
    Accepts a JSON body: { "answers": [0, 1, 2, ...] }
    Returns a career recommendation: { "career": "...", "description": "..." }
    """
    if len(payload.answers) != 12:
        raise HTTPException(
            status_code=400,
            detail=f"Expected 12 answers, received {len(payload.answers)}."
        )

    for i, ans in enumerate(payload.answers):
        if ans not in (0, 1, 2):
            raise HTTPException(
                status_code=400,
                detail=f"Answer at index {i} is invalid: {ans}. Must be 0, 1, or 2."
            )

    result = analyse_answers(payload.answers)
    return result


@app.get("/api/roadmap/{career}")
def api_get_roadmap(career: str):
    """
    GET /api/roadmap/{career}
    Returns the learning roadmap for the given career name.
    Example: GET /api/roadmap/Data Scientist
    """
    roadmap = get_roadmap(career)
    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail=f"No roadmap found for career: '{career}'"
        )
    return roadmap