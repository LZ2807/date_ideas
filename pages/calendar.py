import streamlit as st
from streamlit_calendar import calendar
from database.db import init_db
from database.repositories import DateIdeaRepository
from database.models import DateStatus

init_db()
repo = DateIdeaRepository()
statuses = list(DateStatus)
st.set_page_config(layout="wide")

calendar_options = {
    "editable": False,
    "selectable": True,
    "height": "auto",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridWeek,dayGridMonth"
    },

    "initialView": "dayGridMonth",
}
calendar_events = []

for idea in repo.get_by_status(DateStatus.PLANNED):
    if idea.day_planned:
        calendar_events.append({
            "id": str(idea.id),
            "title": idea.title,
            "start": idea.day_planned.isoformat(),
            "allDay": True,
        })
        
custom_css="""
    .fc {
        height: 100dvh !important;
    }
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
            .fc-header-toolbar {
            display: flex !important;
            flex-direction: column !important;
            gap: 12px;
            align-items: center !important;
        }

"""

calendar_state = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )


@st.dialog("Date Details")
def show_date_details(idea_id):
    idea = repo.get_by_id(int(idea_id))

    if idea:
        st.subheader(idea.title)
        st.write(idea.description)
        st.write(f"📅 Planned for: {idea.day_planned}")
if calendar_state and calendar_state.get("callback") == "eventClick":
    event = calendar_state["eventClick"]["event"]
    show_date_details(event["id"])