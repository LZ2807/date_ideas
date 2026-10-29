from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import DateIdeaRepository


init_db()

repo = DateIdeaRepository()

for idea in repo.get_all():
    repo.delete(idea.id)