from enum import Enum
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="date_idea",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"DateIdea(id={self.id}, "
            f"title={self.title}, "
            f"status={self.status}, "
            f"duration={self.duration}, "
            f"rating={self.rating}, "
            f"comments={self.comments})"
        )
    
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)

    date_idea_id: Mapped[int] = mapped_column(ForeignKey("date_ideas.id"), nullable=False)

    text: Mapped[str] = mapped_column(Text)

    date_idea: Mapped["DateIdea"] = relationship(
    back_populates="comments"
    )