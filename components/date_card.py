import streamlit as st

from database.models import DateIdea, DateStatus
from database.repositories import DateIdeaRepository
statuses = list(DateStatus)



def render_date_card(
        idea: DateIdea,
        repo: DateIdeaRepository,
):
        # ----- Helper Functions -----
    def handle_status_change(idea_id: int):
        new_status = st.session_state[f"status_{idea_id}"]
        repo.update_status(idea_id, new_status)
    def handle_rating_change(idea_id: int):
        new_rating = st.session_state[f"rating_{idea_id}"]
        repo.update_rating(idea_id, new_rating)

    edit_key = f"editing_{idea.id}"
    with st.container(border=True):
                # Date Card
                if not st.session_state.get(edit_key, False):
                    st.write(idea.title)
                    st.write(idea.description)
                    st.write(f"Duration: {idea.duration} hours")
                    status_key = f"status_{idea.id}"
                    idea_status=st.selectbox(
                        "Status",
                        options=statuses,
                        format_func=lambda s: s.value.capitalize(),
                        index=statuses.index(DateStatus(idea.status)),
                        key=f"status_{idea.id}",
                        on_change=handle_status_change,
                        args=(idea.id,)
                    )
                    rating = st.feedback(options="stars", key=f"rating_{idea.id}", default=idea.rating, on_change=handle_rating_change, args=(idea.id,))
    
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
    
    