import streamlit as st
import requests
import random

# Remplacez par votre clé API TMDb
API_KEY = 'f02f78b1f3a7f2976cdfaac794698217'
actors=""
directors=""
actors_ids_select = []
directors_ids_select = []
actors_ids_text = []
directors_ids_text = []
genres_dict = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}


gigas = {
  "Jean Gabin": {
    "profile": "/pmFuOVTQvYdgmN7cYOuyJHPfMRt.jpg",
    "id": "11544"
  },
  "Alain Delon": {
    "profile": "/jmu91SQe5qSmvpAnEVQTuP33FNd.jpg",
    "id": "15135"
  },
  "Jean-Paul Belmondo": {
    "profile": "/hXAM7zTXGWVAv0VLGGrnxAJJbca.jpg",
    "id": "3829"
  },
  "Lino Ventura": {
    "profile": "/j8D4ox5jSavrB7G8KrlxEIxivEq.jpg",
    "id": "15397"
  },
  "Bernard Blier": {
    "profile": "/6xRHGb7CNDa83rcTzCp3LeIvU2s.jpg",
    "id": "24379"
  },
  "Gérard Depardieu": {
    "profile": "/fLYH1pcEX49x6ikfoKkLC8L5lBO.jpg",
    "id": "16927"
  },
  "Yves Montand": {
    "profile": "/wewmvQm200D2jD14G4YjSmg0WVb.jpg",
    "id": "2565"
  },
  "Paul Meurisse": {
    "profile": "/9QtiJ4jRC2NWoAzaUGW5xMQaCMX.jpg",
    "id": "12267"
  },
  "Patrick Dewaere": {
    "profile": "/iQ1Khy341bDFWUNmmVFpytwpk2w.jpg",
    "id": "34581"
  },
  "Serge Reggiani": {
    "profile": "/7URSpmWp6SDIfLhKoPExc2oueet.jpg",
    "id": "15137"
  },
  "Michel Serrault": {
    "profile": "/aaSFvOVwf5tQObbRfdh2mmJuFLQ.jpg",
    "id": "12270"
  },
  "Jean-Louis Trintignant": {
    "profile": "/xZjgsgOGVo8sub6tf0CxclwJ9wR.jpg",
    "id": "1352"
  },
  "Louis de Funès": {
    "profile": "/8R8WVggSEKxxT4n2HRKHjxHrIQZ.jpg",
    "id": "11187"
  },
  "Jean Marais": {
    "profile": "/68SthRQ494vF0GzXTpXflTCY8LP.jpg",
    "id": "9741"
  },
  "Jean Bouise": {
    "profile": "/oRUMbNX21qfcTmxodcn3SRqkoe6.jpg",
    "id": "2168"
  },
  "Bourvil": {
    "profile": "/h9eYqmgnBhRoccnTFKo0Y05dI8b.jpg",
    "id": "37131"
  },
  "Pierre Richard": {
    "profile": "/2hTxDJOdBrvqJy8yFHnLzqG4yBe.jpg",
    "id": "24501"
  },
  "Michel Piccoli": {
    "profile": "/6yZaIIeMfYgQtcdNo4dubL2N5YT.jpg",
    "id": "3784"
  },
  "Daniel Auteuil": {
    "profile": "/5asrvkdSnlYlHap3ldDNyE5opeI.jpg",
    "id": "6012"
  },
  "Jean Rochefort": {
    "profile": "/wyvdO0ih9mwLE3UHCy8GudqnKTK.jpg",
    "id": "24421"
  },
  "Sami Frey": {
    "profile": "/7yb6JIdlMNWxc6SKhRVxauxa9wW.jpg",
    "id": "17578"
  },
  "Francis Blanche": {
    "profile": "/tqHH6RNErwSPk8avbIzQKkQPc7e.jpg",
    "id": "39645"
  },
  "Charles Vanel": {
    "profile": "/dznVyOfBuL2cTDucr0xOpzp6iGT.jpg",
    "id": "2566"
  },
  "Fernandel": {
    "profile": "/eiiPLZPZ0XilcexB5eNOWEbbcrm.jpg",
    "id": "69958"
  },
  "Henri Vidal": {
    "profile": "/335OqmmRefyOHRbbLrzpURoLkJS.jpg",
    "id": "545679"
  },
  "Jacques Villeret": {
    "profile": "/w4sONhPYO3c361BPxDToT4pJFpY.jpg",
    "id": "35323"
  },
  "Maurice Ronet": {
    "profile": "/kNoCaKscnlHGTUucSUwjla7QT1v.jpg",
    "id": "15395"
  },
  "Michel Galabru": {
    "profile": "/f6uvYIfc6cgQkn713rViFXIUCn0.jpg",
    "id": "24629"
  },
  "Jean Carmet": {
    "profile": "/jfWIGiDPcVR5aM7Ws2IYBYAwUju.jpg",
    "id": "24540"
  },
  "Jean Yanne": {
    "profile": "/nZAsOM0mtE0oHHj9DlbH94SxtAI.jpg",
    "id": "24381"
  },
  "Philippe Noiret": {
    "profile": "/mWPa6A0JK3tfVRQDIzCQGEao19B.jpg",
    "id": "24366"
  },
  "François Périer": {
    "profile": "/ajiLZZ2TH9fg4mm1jPGAW5yXuv7.jpg",
    "id": "27440"
  },
  "Paul Frankeur": {
    "profile": "/mbKwqRsKZv6vf1hUdCTMDDePv6T.jpg",
    "id": "24684"
  },
  "Guy Marchand": {
    "profile": "/A0txUn9cpfgLzwiiNentjkHGOw.jpg",
    "id": "38901"
  },
  "Maurice Biraud": {
    "profile": "/8Ln3zgS5TznPqLwjDjCzlv7eRhx.jpg",
    "id": "32100"
  },
  "Jean-Pierre Cassel": {
    "profile": "/iCZ9CFw55lwdERGuIEFrkpOdaBi.jpg",
    "id": "19162"
  },
  "Romy Schneider": {
    "profile": "/lAH90VMs5iU7kGJR3LSkre2Jxhe.jpg",
    "id": "6250"
  },
  "Brigitte Bardot": {
    "profile": "/58RcIEUurDXbFl43CjPAqMvC4JT.jpg",
    "id": "3783"
  },
  "Catherine Deneuve": {
    "profile": "/a6Ku0amMUmaEs4gP13lag3za5Sh.jpg",
    "id": "50"
  },
  "Jeanne Moreau": {
    "profile": "/lsIlRbcStJev5n1mypIeUUYKWuy.jpg",
    "id": "14812"
  },
  "Simone Signoret": {
    "profile": "/vRI2Vt3HX911uDrVK170waQsL8b.jpg",
    "id": "12266"
  },
  "Annie Girardot": {
    "profile": "/2njhI92RBGwQgGhGFDA9wgdGDo9.jpg",
    "id": "6014"
  },
  "Isabelle Adjani": {
    "profile": "/buIW2T5TWtGpz7vqADX6Byd0n69.jpg",
    "id": "6553"
  },
  "Claudia Cardinale": {
    "profile": "/m7iyqSEMHI1qmKx7ml4HmVyG0BC.jpg",
    "id": "4959"
  },
  "Isabelle Huppert": {
    "profile": "/3YQwWkpNKQeV5NUmdCH76Ne1gDP.jpg",
    "id": "17882"
  }
}
def get_giga_photo(name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={name}"
    response = requests.get(url).json()
    return {"profile" : response['results'][0]['profile_path'], "id" : response['results'][0]['id']}

gigas_directors = {
  "Henri Verneuil": "34580",
  "Claude Sautet": "20789",
  "Henri-Georges Clouzot": "2559",
  "Jean-Pierre Melville": "3831",
  "Jean-Luc Godard": "3776",
  "Claude Chabrol": "19069",
  "François Truffaut": "1650",
  "Louis Malle": "15389",
  "Éric Rohmer": "28615",
  "Jacques Demy": "24882",
  "Agnès Varda": "6817",
  "Jean Cocteau": "9730",
  "Marcel Carné": "25161",
  "Jean Renoir": "11528",
  "Jacques Tati": "5763",
  "Alain Resnais": "11983",
  "René Clément": "9740",
  "Georges Franju": "37302",
  "Bertrand Blier": "34262"
}
sort_dict={
    "Date":"primary_release_date.asc",
    "Popularity":"popularity.desc"}

def get_giga_id(name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={name}"
    response = requests.get(url).json()
    return response['results'][0]['id'] if response['results'] else None



@st.cache_data
def get_giga_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url).json()
    return response

@st.cache_data
def find_giga_movies(actor_ids, director_ids, sorting):

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by={sort_dict[sorting]}&without_genres=99&with_cast={actor_ids}&with_crew={director_ids}"
    response = requests.get(url).json()

    results = response['results']
    if results:
        for movie in results:
            st.markdown(f"## **{movie['original_title']}** - {movie['release_date'][:4]}")
            st.image(f"https://image.tmdb.org/t/p/original{movie['backdrop_path']}")
            st.markdown(f"### {' | '.join([genres_dict[genre] for genre in movie['genre_ids']])}")
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

    sort = st.radio("Sort by :", ["Popularity", "Date"], horizontal=True)

    submitted=st.form_submit_button("Search :mag:")

if submitted:
    if not (actors_select or others_actors or directors_select or others_directors):
        st.error("You need to input GIGAS")
    else :
        if actors_select or directors_select:
            actors_ids_select = [gigas[actor]["id"] for actor in actors_select]
            directors_ids_select = [gigas_directors[director] for director in directors_select]

        if others_actors or others_directors:
            actors_ids_text = [str(get_giga_id(name.strip())) for name in others_actors.split(",") if name.strip()]
            directors_ids_text = [str(get_giga_id(name.strip())) for name in others_directors.split(",") if name.strip()]
        
        actors_ids = actors_ids_select + actors_ids_text
        directors_ids = directors_ids_select + directors_ids_text

        actors = ','.join(actors_ids)
        directors = ','.join(directors_ids)

        try:
            find_giga_movies(actors, directors, sort)
        except SyntaxError and NameError:
            st.write('You need to input GIGAS')

#for col,actor in zip(st.columns(len(actors_select), gap="small"),actors_select):
#                with col:
#                    st.image(f"https://image.tmdb.org/t/p/original{gigas[actor]['profile']}", width=150)

left_co, cent_co,last_co = st.columns(3)
#with cent_co:
#    st.image(f"https://image.tmdb.org/t/p/original{gigas[random.choice(list(gigas.keys()))]['profile']}", width=200)

pict_list = ["Jean Gabin","Lino Ventura", "Bernard Blier", "Yves Montand", "Romy Schneider", "Alain Delon", "Jean-Paul Belmondo", "Paul Meurisse", "Simone Signoret"]
with cent_co:
    st.image(f"https://image.tmdb.org/t/p/original{gigas[random.choice(pict_list)]['profile']}", width=200)
