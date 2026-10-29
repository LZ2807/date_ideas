import streamlit as st

from components.comment_section import render_comment_section
from database.db import init_db

from database.models import DateStatus
from database.repositories import CommentRepository, DateIdeaRepository

init_db()



repo = DateIdeaRepository()
repo_comment = CommentRepository()
statuses = list(DateStatus)


st.title("❤️ Date") 

idea_id = st.query_params.get("id")
if idea_id is None:
    st.error("No date selected.")
    st.stop()
else:
    idea = repo.get_by_id(idea_id)
    st.write("Test")
    if idea:
        st.write(f"Title: {idea.title}")
        st.write(f"Description: {idea.description}")
        st.write(f"Duration: {idea.duration} hours")
        st.write(f"Status: {idea.status.capitalize()}")
        
        # Render comments section
        render_comment_section(idea, repo_comment)


