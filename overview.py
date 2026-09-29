import streamlit as st

from components.date_card import render_date_card
from database.db import init_db
import database.models

from database.models import DateStatus
from database.repositories import DateIdeaRepository

init_db()



repo = DateIdeaRepository()
statuses = list(DateStatus)



st.title("❤️ Date Ideas") 

if "title" not in st.session_state:
    st.session_state.title = ""
if "description" not in st.session_state:
    st.session_state.description = ""
if "duration" not in st.session_state:
    st.session_state.duration = 0

title = st.text_input("Title", key="title")
description = st.text_input("Description", key="description")
status = st.selectbox("Status", options=statuses, key="status", format_func=lambda s: s.value.capitalize())
duration = st.slider("Duration (hours)", min_value=0, max_value=24, step=1, key="duration")

if st.button("Add Date Idea"):
    repo.create(
    title=title,
    description=description,
    status=status,
    duration=duration
)



with st.container(wrap=True):
    for idea in repo.get_all():
        render_date_card(idea, repo)
        