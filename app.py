from pathlib import Path

import pandas as pd
import streamlit as st

logo_path = Path(__file__).parent / "logo.jpg"
if logo_path.is_file():
    _, logo_column, _ = st.columns([1, 2, 1])
    with logo_column:
        st.image(str(logo_path), width=180)
else:
    st.warning("Add logo.jpg to the project folder to display the logo.")

st.title("Vacation Planner")

st.header("Plan Your Dream Vacation")
st.write("Use this app to plan your perfect vacation. Select your destination, activities, and budget to get started!")

hotels_path = Path(__file__).parent / "hotels.csv"
hotels = pd.read_csv(hotels_path)
destinations = sorted(hotels["destination"].unique())

destination = st.selectbox(
    "Choose your destination:",
    destinations,
    index=None,
    placeholder="Select a destination",
)

if destination is not None:
    suggestions = hotels[hotels["destination"] == destination]
    st.subheader(f"Hotel suggestions in {destination}")
    for hotel in suggestions.itertuples(index=False):
        stars = "★" * int(hotel.rating_stars) + "☆" * (5 - int(hotel.rating_stars))
        st.markdown(f"**{hotel.hotel_name}**  \n${hotel.price_per_night:.0f} per night · {stars} ({hotel.rating_stars}/5)")
