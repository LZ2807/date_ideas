import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.title("Countries Visited 🌍")

# Example data — replace this with your database query
visited_countries = {
    "DEU",  # Germany
    "CZE",  # Czechia
}

world = px.data.gapminder()[["iso_alpha", "country"]].drop_duplicates()
world = world[world["iso_alpha"] != " - "].copy()

world["visited"] = world["iso_alpha"].isin(visited_countries)
world["color"] = world["visited"].map({
    True: "Visited",
    False: "Not visited",
})

fig = px.choropleth(
    world,
    locations="iso_alpha",
    color="color",
    hover_name="country",
    color_discrete_map={
        "Visited": "#e53935",
        "Not visited": "#171717",
    },
    projection="natural earth",
    center={"lat": 49.460983, "lon": 11.0618},
)
fig.update_layout(
    height=1000,
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),
)
fig.update_layout(
    geo=dict(
        showframe=False,
        projection_type="natural earth",    
        showcoastlines=True,
        coastlinecolor="#777777",
        showocean=True,
        oceancolor="#eeeeee",
        showland=True,
        landcolor="#171717",
        bgcolor="rgba(0,0,0,0)",
        lataxis_range=[25, 72],
        lonaxis_range=[-25, 45],
    ),
    margin=dict(l=0, r=0, t=0, b=0),
    legend_title_text="",
)

st.plotly_chart(fig, height=1000,config={"responsive": True})