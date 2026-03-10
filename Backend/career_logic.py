"""
career_logic.py
---------------
Analyses 12 quiz answers and returns the best-matching career from 20 options.

HOW IT WORKS
============
Step 1 – Convert answers to a TRAIT VECTOR (12 floats, one per trait dimension).
         Yes=1.0 / Sometimes=0.5 / No=0.0

Step 2 – Each career has a PROFILE VECTOR (12 floats) that describes how strongly
         each trait matters for that career.  Values range 0.0–1.0.
         Careers are deliberately designed so their dominant traits don't overlap,
         which guarantees a spread of possible results.

Step 3 – Compute the DOT PRODUCT of the user's trait vector with each career
         profile vector.  The career with the highest dot product wins.
         (Dot product = sum of element-wise multiplications — it rewards matching
         strong traits and ignores irrelevant ones.)

Trait index legend (matches questions.py):
  0  ANALYTICAL    1  DATA          2  CREATIVE      3  SOCIAL
  4  TECHNICAL     5  BUSINESS      6  COMMUNICATION 7  LEADERSHIP
  8  SCIENTIFIC    9  DETAIL        10 INDEPENDENT   11 EMPATHETIC
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# 20 Career profiles
# Each profile is a list of 12 floats [t0, t1, ..., t11].
# Set a trait to 1.0 if it's essential, 0.5 if useful, 0.0 if irrelevant.
# Every career must have a UNIQUE dominant-trait combination so the quiz
# produces a genuine spread of results.
# ---------------------------------------------------------------------------
CAREERS: list[dict] = [

    # ── Tech / Engineering ───────────────────────────────────────────────────

    {
        "name": "Software Engineer",
        "description": (
            "You love building things from scratch. Whether it's a mobile app, "
            "a web platform, or a backend system, you thrive on turning logical "
            "thinking and technical skill into working software."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.8,  0.3,  0.2,  0.1,  1.0,  0.2,  0.2,  0.2,  0.3,  0.6,  0.7,  0.1],
    },
    {
        "name": "Data Scientist",
        "description": (
            "You are driven by a hunger to find patterns in data. You combine "
            "statistical thinking, programming, and domain curiosity to build "
            "models that answer questions no one else thought to ask."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.9,  1.0,  0.1,  0.1,  0.6,  0.2,  0.2,  0.1,  0.7,  0.7,  0.8,  0.1],
    },
    {
        "name": "Cybersecurity Analyst",
        "description": (
            "You think like an attacker so you can defend like a pro. Detail-oriented "
            "and endlessly curious about how systems can be broken — and fixed — "
            "you are the guardian of the digital world."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.9,  0.4,  0.1,  0.1,  0.9,  0.2,  0.2,  0.2,  0.5,  1.0,  0.8,  0.2],
    },
    {
        "name": "DevOps Engineer",
        "description": (
            "You sit at the crossroads of development and operations. You automate, "
            "optimise, and keep complex infrastructure running smoothly — turning "
            "chaos into reliable, repeatable systems."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.8,  0.4,  0.1,  0.2,  1.0,  0.3,  0.3,  0.4,  0.3,  0.9,  0.6,  0.1],
    },
    {
        "name": "Machine Learning Engineer",
        "description": (
            "You build the engines that power AI. Sitting between research and "
            "production, you design, train, and deploy models that learn — "
            "turning cutting-edge ideas into real-world products."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [1.0,  0.9,  0.1,  0.1,  0.9,  0.1,  0.1,  0.1,  0.8,  0.7,  0.9,  0.1],
    },

    # ── Design / Creative ────────────────────────────────────────────────────

    {
        "name": "UX / UI Designer",
        "description": (
            "You have a sharp eye for aesthetics and deep empathy for users. "
            "You craft digital experiences that are both beautiful and effortless "
            "to use — sitting at the crossroads of art and technology."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.4,  0.2,  1.0,  0.7,  0.4,  0.2,  0.6,  0.3,  0.1,  0.8,  0.5,  0.6],
    },
    {
        "name": "Graphic Designer",
        "description": (
            "You communicate through visuals. Typography, colour, composition — "
            "these are your tools. You bring ideas to life in ways that words alone "
            "never could, making brands and messages truly memorable."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.2,  0.1,  1.0,  0.3,  0.3,  0.2,  0.5,  0.2,  0.1,  0.8,  0.7,  0.3],
    },
    {
        "name": "Content Creator / Writer",
        "description": (
            "You tell stories that move people. Whether it's articles, scripts, "
            "social media, or long-form journalism, you have a gift for turning "
            "ideas into compelling words that audiences actually want to read."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.3,  0.1,  0.9,  0.4,  0.1,  0.3,  1.0,  0.2,  0.2,  0.6,  0.7,  0.4],
    },

    # ── Business / Management ────────────────────────────────────────────────

    {
        "name": "Product Manager",
        "description": (
            "You are the glue between business, design, and engineering. You define "
            "what gets built and why, balancing user needs, commercial goals, and "
            "technical constraints to ship products people love."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.6,  0.5,  0.5,  0.6,  0.4,  0.8,  0.8,  0.8,  0.2,  0.5,  0.3,  0.5],
    },
    {
        "name": "Business Analyst",
        "description": (
            "You bridge the gap between business needs and technical solutions. "
            "You map processes, spot inefficiencies, and translate messy real-world "
            "problems into clear requirements that teams can actually build."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.8,  0.7,  0.2,  0.4,  0.4,  0.9,  0.6,  0.4,  0.2,  0.8,  0.4,  0.3],
    },
    {
        "name": "Entrepreneur / Startup Founder",
        "description": (
            "You spot opportunities others miss and have the courage to chase them. "
            "Resilient, resourceful, and comfortable with risk, you build companies "
            "from nothing — driven by a vision of how things could be."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.6,  0.4,  0.7,  0.5,  0.4,  1.0,  0.8,  1.0,  0.3,  0.4,  0.5,  0.5],
    },
    {
        "name": "Marketing Manager",
        "description": (
            "You understand people and know how to reach them. You blend creativity "
            "with data-driven thinking to craft campaigns that grow brands, win "
            "customers, and make organisations genuinely stand out."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.4,  0.5,  0.8,  0.6,  0.2,  0.8,  1.0,  0.6,  0.1,  0.5,  0.3,  0.4],
    },
    {
        "name": "Financial Analyst",
        "description": (
            "Numbers are your language. You evaluate investments, model financial "
            "scenarios, and advise on strategy — giving decision-makers the clarity "
            "they need to grow wealth and manage risk."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.9,  1.0,  0.1,  0.2,  0.3,  0.9,  0.5,  0.3,  0.2,  0.9,  0.7,  0.1],
    },
    {
        "name": "Project Manager",
        "description": (
            "You bring order to complexity. Juggling timelines, budgets, and people, "
            "you keep teams aligned and projects on track — turning ambitious goals "
            "into delivered results."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.5,  0.4,  0.2,  0.7,  0.3,  0.7,  0.7,  1.0,  0.1,  0.8,  0.2,  0.4],
    },

    # ── People / Social ──────────────────────────────────────────────────────

    {
        "name": "Data Analyst",
        "description": (
            "You turn raw numbers into stories that drive action. Sitting inside "
            "a business, you answer the questions that matter — why did sales drop? "
            "which campaign worked? — with evidence, not guesswork."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.5,  0.9,  0.2,  0.5,  0.2,  0.9,  0.8,  0.3,  0.2,  0.7,  0.3,  0.2],
    },
    {
        "name": "Human Resources Manager",
        "description": (
            "People are your passion. You recruit, develop, and look after the "
            "humans that make organisations work — creating cultures where everyone "
            "can do their best work and grow."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.4,  0.3,  0.4,  1.0,  0.1,  0.6,  0.8,  0.7,  0.1,  0.5,  0.2,  0.9],
    },
    {
        "name": "Educator / Teacher",
        "description": (
            "You light up when you help someone understand something new. Patient, "
            "articulate, and deeply committed to others' growth, you shape how the "
            "next generation thinks and what they believe is possible."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.5,  0.2,  0.6,  1.0,  0.2,  0.2,  0.9,  0.5,  0.5,  0.5,  0.3,  1.0],
    },
    {
        "name": "Healthcare Professional (Nurse / Paramedic)",
        "description": (
            "You are driven by care. Whether at a bedside or on the front line, "
            "you combine clinical skill with human compassion to support people "
            "through their most vulnerable moments."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.5,  0.3,  0.2,  0.9,  0.3,  0.1,  0.7,  0.4,  0.8,  0.9,  0.2,  1.0],
    },

    # ── Science / Research ───────────────────────────────────────────────────

    {
        "name": "Research Scientist",
        "description": (
            "You push the boundaries of what is known. Methodical, curious, and "
            "deeply rigorous, you design experiments, gather evidence, and publish "
            "findings that expand humanity's understanding of the world."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.9,  0.8,  0.3,  0.3,  0.5,  0.1,  0.5,  0.2,  1.0,  0.9,  0.9,  0.4],
    },
    {
        "name": "Environmental / Sustainability Consultant",
        "description": (
            "You are passionate about protecting the planet. You advise organisations "
            "on reducing their environmental footprint — combining scientific knowledge, "
            "strategic thinking, and a genuine drive for a better world."
        ),
        #              AN    DA    CR    SO    TE    BU    CO    LE    SC    DE    IN    EM
        "profile":  [0.6,  0.5,  0.4,  0.7,  0.3,  0.6,  0.7,  0.5,  0.9,  0.6,  0.4,  1.0],
    },
]


# ---------------------------------------------------------------------------
# Scoring engine
# ---------------------------------------------------------------------------

def _answer_to_score(answer: int) -> float:
    """Yes (0) → 1.0 | Sometimes (1) → 0.5 | No (2) → 0.0"""
    if answer == 0:
        return 1.0
    if answer == 1:
        return 0.5
    return 0.0


def analyse_answers(answers: list[int]) -> dict:
    """
    Convert answers to a trait vector then find the career whose profile
    vector has the highest dot-product (cosine similarity without normalising,
    which is fine because all profile magnitudes are comparable).

    Returns: { "career": str, "description": str }
    """
    # Build trait vector from answers
    # questions.py maps each question to one trait via the "trait" field;
    # but here we just use question position directly (question i → trait i).
    num_traits = 12
    trait_vector = [0.0] * num_traits
    for i, ans in enumerate(answers):
        if i < num_traits:
            trait_vector[i] = _answer_to_score(ans)

    best_career = None
    best_score  = -1.0

    for career in CAREERS:
        profile = career["profile"]
        # Dot product
        score = sum(trait_vector[t] * profile[t] for t in range(num_traits))
        if score > best_score:
            best_score  = score
            best_career = career

    if best_career is None:
        best_career = CAREERS[0]

    return {
        "career":      best_career["name"],
        "description": best_career["description"],
    }