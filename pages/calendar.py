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
            "title": idea.title,
            "start": idea.day_planned.isoformat(),
            "end": idea.day_planned.isoformat(),
            "allDay": True,
        })
        
custom_css="""
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

"""

calendar = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )
