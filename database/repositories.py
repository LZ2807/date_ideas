from sqlalchemy import select

from database.db import SessionLocal
from database.models import DateIdea, DateStatus, Comment


class DateIdeaRepository:

    def create(
        self,
        title: str,
        description: str | None = None,
        status: DateStatus = DateStatus.IDEA,
        duration: int | None = None,
    ) -> DateIdea:

        with SessionLocal() as session:
            idea = DateIdea(
                title=title,
                description=description,
                status=status.value,
                duration=duration,
            )

            session.add(idea)
            session.commit()
            session.refresh(idea)

            return idea

    def get_all(self) -> list[DateIdea]:
        with SessionLocal() as session:
            statement = select(DateIdea)

            return list(
                session.scalars(statement).all()
            )

    def get_by_id(self, idea_id: int) -> DateIdea | None:
        with SessionLocal() as session:
            return session.get(DateIdea, idea_id)

    def get_by_status(self, status: DateStatus) -> list[DateIdea]:
        with SessionLocal() as session:
            statement = select(DateIdea).where(DateIdea.status == status.value)

            return list(
                session.scalars(statement).all()
            )

    def update_status(
        self,
        idea_id: int,
        status: DateStatus,
    ) -> DateIdea | None:

        with SessionLocal() as session:
            idea = session.get(DateIdea, idea_id)

            if idea is None:
                return None

            idea.status = status.value
            session.commit()
            session.refresh(idea)

            return idea
        
    def update_rating(
        self,
        idea_id: int,
        rating: int,
    ) -> DateIdea | None:

        with SessionLocal() as session:
            idea = session.get(DateIdea, idea_id)

            if idea is None:
                return None

            idea.rating = rating
            session.commit()
            session.refresh(idea)

            return idea
   
        
    def update(
        self,
        idea_id: int,
        title: str | None = None,
        description: str | None = None,
        status: DateStatus | None = None,
        duration: int | None = None,
    ) -> DateIdea | None:

        with SessionLocal() as session:
            idea = session.get(DateIdea, idea_id)

            if idea is None:
                return None
            
            if title is not None:
                idea.title = title
            if description is not None:
                idea.description = description
            if status is not None:
                idea.status = status.value
            if duration is not None:
                idea.duration = duration
            session.commit()
            session.refresh(idea)

            return idea

    def delete(self, idea_id: int) -> bool:
        with SessionLocal() as session:
            idea = session.get(DateIdea, idea_id)

            if idea is None:
                return False

            session.delete(idea)
            session.commit()

            return True

class CommentRepository:

    def create(
        self,
        date_idea_id: int,
        text: str,
    ) -> "Comment":

        with SessionLocal() as session:
            comment = Comment(
                date_idea_id=date_idea_id,
                text=text,
            )

            session.add(comment)
            session.commit()
            session.refresh(comment)

            return comment

    def get_by_date_idea_id(self, date_idea_id: int) -> list[Comment]:
        with SessionLocal() as session:
            statement = select(Comment).where(Comment.date_idea_id == date_idea_id)

            return list(
                session.scalars(statement).all()
            )