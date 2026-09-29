from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import DateIdeaRepository


init_db()

repo = DateIdeaRepository()

# CREATE
idea = repo.create(
    title="Go Stargazing",
    description="Drive somewhere dark and bring snacks.",
)

print("Created:", idea)


# READ
print("\nAll ideas:")

for idea in repo.get_all():
    print(idea)


# UPDATE
repo.update_status(
    idea.id,
    DateStatus.PLANNED,
)

print("\nAfter update:")
print(repo.get_by_id(idea.id))


# # DELETE
# repo.delete(idea.id)

# print("\nAfter delete:")
# print(repo.get_all())