import streamlit as st
import requests
import random
import json
# Remplacez par votre clé API TMDb
API_KEY = 'f02f78b1f3a7f2976cdfaac794698217'
actors=""
directors=""
actors_ids_select = []
directors_ids_select = []
actors_ids_text = []
directors_ids_text = []

st.cache_data
def load_data():
    with open('data/data.json', 'r') as fp:
        gigas = json.load(fp)
    
    with open('data/genres.json', 'r') as fp:
        genres_dict = json.load(fp)

    with open('data/genres.json', 'r') as fp:
        gigas_directors = json.load(fp)
    return gigas, genres_dict, gigas_directors

gigas, genres_dict, gigas_directors = load_data()

sort_dict={
    "Date":"primary_release_date.asc",
    "Popularity":"popularity.desc",
    "Note":"vote_average.desc"}

def get_giga_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url).json()
    return response

def find_giga_movies(actor_ids, director_ids, sorting):

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by={sort_dict[sorting]}&without_genres=99&with_cast={actor_ids}&with_crew={director_ids}"
    response = requests.get(url).json()

    results = response['results']
    if results:
        for movie in results:
            st.markdown(f"## **{movie['original_title']}** - {movie['release_date'][:4]}")
            st.image(f"https://image.tmdb.org/t/p/original{movie['backdrop_path']}")
            st.markdown(f"### {' | '.join([genres_dict[str(genre)] for genre in movie['genre_ids']])}")
            st.markdown(movie["overview"])
            st.divider()
        with st.expander("See result"):
            st.write(response['results'])

    else:
        st.markdown("#### Trop GIGA pour exister")


st.markdown("# :movie_camera: GIGAS")
with st.form("gigas"):
    actors_select = st.multiselect(
        "Select Actors :",
        gigas.keys(),
    )

    directors_select = st.multiselect(
        "Select Directors :",
        gigas_directors.keys(),
    )
    with st.expander("Click to add more GIGAS by text"):
        others_actors = st.text_input("Input actors by text (separate with comma)")
        others_directors = st.text_input("Input directors or crew member by text (separate with comma)")

    sort = st.radio("Sort by :", ["Popularity", "Date", "Note"], horizontal=True)

    submitted=st.form_submit_button("Search :mag:")

if submitted:
    if not (actors_select or others_actors or directors_select or others_directors):
        st.error("You need to input GIGAS")
    else :
        if actors_select or directors_select:
            actors_ids_select = [gigas[actor]["id"] for actor in actors_select]
            directors_ids_select = [gigas_directors[director] for director in directors_select]

        if others_actors or others_directors:
            actors_ids_text = [str(get_actor_id(name.strip())) for name in others_actors.split(",") if name.strip()]
            directors_ids_text = [str(get_actor_id(name.strip())) for name in others_directors.split(",") if name.strip()]
        
        actors_ids = actors_ids_select + actors_ids_text
        directors_ids = directors_ids_select + directors_ids_text

        actors = ','.join(actors_ids)
        directors = ','.join(directors_ids)

        try:
            find_giga_movies(actors, directors, sort)
        except SyntaxError and NameError:
            st.write('You need to input GIGAS')


left_co, cent_co,last_co = st.columns(3)

pict_list = ["Jean Gabin","Lino Ventura", "Bernard Blier", "Yves Montand", "Romy Schneider", "Alain Delon", "Jean-Paul Belmondo", "Paul Meurisse", "Simone Signoret"]
with cent_co:
    st.image(f"https://image.tmdb.org/t/p/original{gigas[random.choice(pict_list)]['profile']}", width=200)
