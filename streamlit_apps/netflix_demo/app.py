import streamlit as st
import pandas as pd

st.title("Netflix Recommendation Demo")

# Example user ratings
user_ratings = {"Stranger Things": 5, "The Crown": 4, "Breaking Bad": 5}
st.write("Your ratings:", user_ratings)

# Example recommendation
st.write("Suggested next show:", "Dark")

# Genre-based filtering
shows = pd.DataFrame({
    "Title": ["Stranger Things", "The Witcher", "The Crown", "Money Heist", "Dark"],
    "Genre": ["Sci-Fi", "Fantasy", "Drama", "Crime", "Sci-Fi"]
})

genre_filter = st.selectbox("Choose a genre", shows["Genre"].unique())
filtered_shows = shows[shows["Genre"] == genre_filter]
st.write("Shows matching your genre:", filtered_shows)


