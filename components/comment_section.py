import streamlit as st

from database.models import DateIdea, DateStatus
from database.repositories import CommentRepository, DateIdeaRepository

def submit_comment(idea, repo_comment):
    key = f"comment_{idea.id}"
    new_comment = st.session_state[key]

    if new_comment.strip():
        repo_comment.create(
            date_idea_id=idea.id,
            text=new_comment.strip()
        )

        # Clear the input
        st.session_state[key] = ""
    else:
        st.error("Comment cannot be empty.")


def render_comment_section(idea, repo_comment):
    comments = repo_comment.get_by_date_idea_id(idea.id)

    st.subheader("Comments")

    for comment in comments:
        with st.container(horizontal_alignment="distribute", horizontal=True):
            st.write(f"- {comment.text}")
            st.button(
                "❌",
                key=f"delete_{comment.id}",
                on_click=repo_comment.delete,
                args=(comment.id,)
            )

    st.text_input(
        "Add a comment",
        key=f"comment_{idea.id}"
    )

    st.button(
        "Submit Comment",
        key=f"submit_{idea.id}",
        on_click=submit_comment,
        args=(idea, repo_comment),
    )