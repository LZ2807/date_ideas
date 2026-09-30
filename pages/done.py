import streamlit as st

from components.date_card import render_date_card
from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import CommentRepository, DateIdeaRepository

init_db()



repo = DateIdeaRepository()
repo_comment = CommentRepository()
statuses = list(DateStatus)


st.title("❤️ Done Dates") 


with st.container(wrap=True):
    for idea in repo.get_by_status(DateStatus.DONE):
        render_date_card(idea, repo)


