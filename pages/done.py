import streamlit as st

from components.date_card import render_date_card
from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import DateIdeaRepository

init_db()



repo = DateIdeaRepository()
statuses = list(DateStatus)

# ----- Helper Functions -----
def handle_status_change(idea_id: int):
    new_status = st.session_state[f"status_{idea_id}"]
    repo.update_status(idea_id, new_status)
def handle_rating_change(idea_id: int):
    new_rating = st.session_state[f"rating_{idea_id}"]
    repo.update_rating(idea_id, new_rating)


st.title("❤️ Done Dates") 


with st.container(wrap=True):
    ideas = repo.get_all()
    done = [idea for idea in ideas if idea.status == DateStatus.DONE.value]
    for idea in done:
        render_date_card(idea, repo)


