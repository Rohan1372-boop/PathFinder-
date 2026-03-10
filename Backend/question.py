"""
questions.py
------------
12 personality questions, each targeting a distinct trait dimension.
Having more questions (12 vs 10) gives the scoring engine more signal
and reduces ties between careers.

Trait dimensions covered (index → trait):
  0  – ANALYTICAL   : loves logic, reasoning, problem-solving
  1  – DATA         : comfortable with numbers, statistics, spreadsheets
  2  – CREATIVE     : drawn to art, design, storytelling, aesthetics
  3  – SOCIAL       : energised by helping, teaching, collaborating
  4  – TECHNICAL    : enjoys building, coding, engineering, fixing things
  5  – BUSINESS     : interested in strategy, markets, organisations
  6  – COMMUNICATION: confident presenting, writing, persuading
  7  – LEADERSHIP   : likes managing people, projects, and direction
  8  – SCIENTIFIC   : curious about how the natural/physical world works
  9  – DETAIL       : meticulous, process-oriented, quality-focused
  10 – INDEPENDENT  : prefers solo deep-work over constant collaboration
  11 – EMPATHETIC   : motivated by human wellbeing and social impact
"""

QUESTIONS = [
    # Trait 0 – ANALYTICAL
    {
        "id": 1,
        "text": "Do you enjoy breaking down complex problems step by step to find a logical solution?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 0
    },
    # Trait 1 – DATA
    {
        "id": 2,
        "text": "Do you feel comfortable working with numbers, statistics, or spreadsheets?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 1
    },
    # Trait 2 – CREATIVE
    {
        "id": 3,
        "text": "Are you drawn to creative work — design, art, writing, or visual storytelling?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 2
    },
    # Trait 3 – SOCIAL
    {
        "id": 4,
        "text": "Do you genuinely enjoy helping, teaching, or mentoring other people?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 3
    },
    # Trait 4 – TECHNICAL
    {
        "id": 5,
        "text": "Do you love building or fixing things — software, hardware, or systems?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 4
    },
    # Trait 5 – BUSINESS
    {
        "id": 6,
        "text": "Are you interested in how businesses, markets, and organisations operate?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 5
    },
    # Trait 6 – COMMUNICATION
    {
        "id": 7,
        "text": "Do you enjoy presenting ideas, writing persuasively, or speaking in front of others?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 6
    },
    # Trait 7 – LEADERSHIP
    {
        "id": 8,
        "text": "Do you like taking charge — organising teams, setting goals, and driving projects forward?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 7
    },
    # Trait 8 – SCIENTIFIC
    {
        "id": 9,
        "text": "Are you fascinated by how the natural or physical world works — science, biology, or engineering?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 8
    },
    # Trait 9 – DETAIL
    {
        "id": 10,
        "text": "Do you take pride in precision and accuracy — noticing errors others might miss?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 9
    },
    # Trait 10 – INDEPENDENT
    {
        "id": 11,
        "text": "Do you do your best work alone, preferring deep focus over constant collaboration?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 10
    },
    # Trait 11 – EMPATHETIC
    {
        "id": 12,
        "text": "Are you motivated by making a real difference to people's lives or to society?",
        "options": ["Yes", "Sometimes", "No"],
        "trait": 11
    },
]