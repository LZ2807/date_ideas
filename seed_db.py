from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import DateIdeaRepository


init_db()

repo = DateIdeaRepository()

dummy_ideas = [
    {
        "title": "Go Stargazing",
        "description": "Drive somewhere dark, bring blankets and snacks.",
        "status": DateStatus.IDEA,
    },
    {
        "title": "Pottery Painting",
        "description": "Paint some questionable pottery for each other.",
        "status": DateStatus.PLANNED,
    },
    {
        "title": "Cook Homemade Pizza",
        "description": "Make pizza completely from scratch.",
        "status": DateStatus.DONE,
    },
    {
        "title": "Visit the Zoo",
        "description": "Spend the afternoon at the zoo.",
        "status": DateStatus.IDEA,
    },
    {
        "title": "Movie Marathon",
        "description": "Pick three movies, get snacks and stay on the couch all day.",
        "status": DateStatus.DONE,
    },
    {
        "title": "Hiking Trip",
        "description": "Find a nice trail and pack lunch for the top.",
        "status": DateStatus.PLANNED,
    },
]


for idea in dummy_ideas:
    repo.create(**idea)

print(f"Added {len(dummy_ideas)} dummy date ideas.")