import streamlit as st

from components.comment_section import render_comment_section
from database.models import DateIdea, DateStatus
from database.repositories import CommentRepository, DateIdeaRepository
statuses = list(DateStatus)



def render_date_card(
        idea: DateIdea,
        repo: DateIdeaRepository,
        repo_comment: CommentRepository
):
        # ----- Helper Functions -----
    def handle_status_change(idea_id: int):
        new_status = st.session_state[f"status_{idea_id}"]
        repo.update_status(idea_id, new_status)
    def handle_rating_change(idea_id: int):
        new_rating = st.session_state[f"rating_{idea_id}"]
        repo.update_rating(idea_id, new_rating)
    def handle_day_change(idea_id: int):
        new_day = st.session_state[f"day_planned_{idea_id}"]
        repo.update_day_planned(idea_id, new_day)

    edit_key = f"editing_{idea.id}"
    with st.container(border=True):
                # Date Card
                if st.button("View Details", key=f"view_{idea.id}"):
                    st.switch_page("pages/date_detail.py", query_params={"id": idea.id})
                if not st.session_state.get(edit_key, False):
                    st.write(idea.title)
                    st.write(idea.description)
                    st.write(f"Duration: {idea.duration} hours")
                    key = f"status_{idea.id}"
                    st.selectbox(
                        "Status",
                        options=statuses,
                        format_func=lambda s: s.value.capitalize(),
                        index=statuses.index(DateStatus(idea.status)),
                        key=f"status_{idea.id}",
                        on_change=handle_status_change,
                        args=(idea.id,)
                    )

                    if idea.status == DateStatus.DONE.value:
                        st.feedback(options="stars", key=f"rating_{idea.id}", default=idea.rating, on_change=handle_rating_change, args=(idea.id,))
                    
                    if idea.status == DateStatus.PLANNED.value:
                        st.date_input("Planned Day", key=f"day_planned_{idea.id}", value=idea.day_planned, on_change=handle_day_change, args=(idea.id,))

                    with st.container(wrap=True, horizontal=True):
                        st.button("❌", key=f"delete_{idea.id}", on_click=repo.delete, args=(idea.id,))
                        if st.button("✏️", key=f"edit_{idea.id}"):
                            st.session_state[edit_key] = True
                            st.rerun()
                else:
                    new_title = st.text_input("Title", value=idea.title, key=f"edit_title_{idea.id}")
                    new_description = st.text_input("Description", value=idea.description, key=f"edit_description_{idea.id}")
                    new_duration = st.slider("Duration (hours)", min_value=0, max_value=24, step=1, value=idea.duration, key=f"edit_duration_{idea.id}")
                    if st.button("💾 Save", key=f"save_{idea.id}"):
                        repo.update(
                            idea_id=idea.id,
                            title=new_title,
                            description=new_description,
                            duration=new_duration
                        )
                        st.session_state[edit_key] = False
                        st.rerun()
    
    