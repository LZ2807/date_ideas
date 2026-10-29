import streamlit as st

from database.db import init_db
import database.models

init_db()

pages = {
    "Views": [
        st.Page("pages/overview.py", title="Overview"),
        st.Page("pages/planned.py", title="Planned"),
        st.Page("pages/done.py", title="Done"),
        st.Page("pages/map.py", title="Map"),

        st.Page("pages/date_detail.py", title="Date Details", visibility="hidden"),
    ]
}

pg = st.navigation(pages)
pg.run()