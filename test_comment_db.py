from database.db import init_db

from database.models import DateStatus
from database.repositories import CommentRepository


init_db()

repo = CommentRepository()

# CREATE
comment = repo.create(
    date_idea_id=2,
    text="This looks great!"
)



# # DELETE
# repo.delete(idea.id)

# print("\nAfter delete:")
# print(repo.get_all())