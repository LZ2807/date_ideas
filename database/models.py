from enum import Enum
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base

class DateStatus(str, Enum):
    IDEA = "idea"
    PLANNED = "planned"
    DONE = "done"

class DateIdea(Base):
    __tablename__ = "date_ideas"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(200), nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    status: Mapped[str] = mapped_column(String(20), nullable=False, default=DateStatus.IDEA.value)

    duration: Mapped[int | None] = mapped_column(nullable=True, default=0)

    rating: Mapped[int | None] = mapped_column(nullable=True, default=None)

    def __repr__(self):
        return (
            f"DateIdea(id={self.id}, "
            f"title={self.title}, "
            f"status={self.status}, "
            f"duration={self.duration})"
        )