import streamlit as st
from models import load_data, load_genres
import plotly.express as px
import pandas as pd

actors = load_data()
genres_dict = load_genres()

with st.sidebar:
    selected_actor = st.selectbox("Select an Actor", options=actors.keys())

    actor = actors[selected_actor]
    movies = actor.list_movies()

    st.image(f"https://image.tmdb.org/t/p/original{actor.profile}",use_column_width=True, caption=f"Giga {actor.name}")

st.markdown(f'# {actor.name} - Stats')

metric1, metric2 ,metric3 = st.columns(3)

metric1.metric('Movies',len(actor.list_movies()))
metric2.metric('Average Movie Rating', f"{actor.get_average_vote():.2f}")
metric3.metric('Carrer Span', f"{actor.get_first_movie().release_date[:4]} - {actor.get_last_movie().release_date[:4]}")

st.markdown("### Release date distribution")

years_fig = px.histogram(actor.get_movies_per_year(), title=f"{selected_actor} Filmography", nbins=20
                        labels={"y": "Number of Movies", "value": "Date"})
years_fig.update_traces(showlegend=False, )
st.plotly_chart(years_fig)

st.markdown("### Popularity And Average Note")

df = pd.DataFrame(
    {'popularity' : [movie.popularity for movie in movies],
        'votes' : [movie.vote_average for movie in movies],
        'name' : [movie.original_title for movie in movies]})

# Créer un DataFrame pour Plotly
# Tracer le nuage de points avec Plotly
fig = px.scatter(df, x='popularity', y='votes',hover_name='name', title='Popularité vs Note Moyenne', trendline='ols')
st.plotly_chart(fig)


st.markdown("### Genre Comparison")

actors_multiselect = st.multiselect("Choose two actors", options=actors.keys(),
                                    default=[selected_actor, "Alain Delon"],
                                    max_selections=2)
if actors_multiselect:
    actors_to_compare = pd.DataFrame()

    for actor_selected in actors_multiselect:
        actors_to_compare[actor_selected] = actors[actor_selected].get_genre_distribution(genres_dict)

    actors_to_compare = actors_to_compare.dropna()
    actors_to_compare["total"] = actors_to_compare.sum(axis=1) 
    actors_to_compare = actors_to_compare.query('total  > 5').reset_index(names="genre")
    actors_to_compare = actors_to_compare.drop("total", axis=1)
    actors_to_compare = pd.melt(actors_to_compare, id_vars=['genre'], value_vars=actors_multiselect,var_name='actor', value_name='count')

    tab_radio, tab_data = st.tabs([":material/equalizer: Chart", ":material/database: Table"])

    with tab_radio:
        radar_fig = px.line_polar(actors_to_compare, r='count',
                            theta='genre',color ='actor',
                            line_close=True,
                            markers = True)
        radar_fig.update_traces(fill = 'toself', showlegend=True)
        radar_fig.update_layout(legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=-0.2,
                            xanchor="center",
                            x=0.5,
                            title=None
                        ))
        st.plotly_chart(radar_fig)

    with tab_data:
        st.dataframe(actors_to_compare)




#test =[" | ".join(i) for i in actor.get_genre_distribution2(genres_dict)]
#
#oui = pd.DataFrame(test).value_counts().reset_index()
#
#oui.columns =['genre', 'count']
#
#st.write(oui)
#
#    def get_genre_distribution2(self, genres_dict):
#        genre_counts=[]
#        for movie in self.movies:
#            genre_counts.append([genres_dict[genre] for genre in movie.get_genres()])
#        #        genre_counts.append(genres_dict[genre])
#        #
#        #genre_counts = pd.DataFrame(genre_counts).value_counts()
#        ##genre_counts.columns=["genre", "count"]
#        return genre_counts
