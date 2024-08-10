import streamlit as st
from models import load_data, load_genres

# Charger les données des acteurs et des genres
actors = load_data()
genres_dict = load_genres()

sort_dict={
    "Date":"primary_release_date.asc",
    "Popularity":"popularity.desc",
    "Note":"vote_average.desc"}

with st.sidebar:
    selected_actor = st.selectbox("Select an Actor", options=actors.keys())

    actor = actors[selected_actor]
    movies = actor.list_movies()

    st.image(f"https://image.tmdb.org/t/p/original{actor.profile}",use_column_width=True, caption=f"Giga {actor.name}")

    sort_criteria = st.selectbox(
    "Sort Movies By",
    options=["Popularity", "Date", "Note"]
)

st.markdown(f'# {actor.name} - Movies')


if selected_actor:
    actor = actors[selected_actor]


    if sort_criteria == "Popularity":
        sorted_movies = sorted(actor.list_movies(), key=lambda m: m.popularity, reverse=True)
    elif sort_criteria == "Date":
        sorted_movies = sorted(actor.list_movies(), key=lambda m: m.release_date, reverse=False)
    elif sort_criteria == "Note":
        sorted_movies = sorted(actor.list_movies(), key=lambda m: m.vote_average, reverse=True)

    
    for movie in sorted_movies:
        st.markdown(f"## **{movie.original_title}** - {movie.release_date[:4]}")
        st.image(f"https://image.tmdb.org/t/p/original{movie.backdrop_path}")
        st.markdown(f"### {' | '.join([genres_dict[str(genre)] for genre in movie.genre_ids])}")
        st.markdown(movie.popularity)
        st.markdown(movie.overview)
        st.divider()