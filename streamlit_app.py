import streamlit as st


gigas = st.Page(
    "pages/gigas.py", title="Gigas", icon=":material/person:", default=True
)

movies = st.Page(
    "pages/movies.py", title="Movies", icon=":material/movie:"
)

stats = st.Page(
    "pages/stats.py", title="Stats", icon=":material/query_stats:"
)
pg = st.navigation(
        {
            "Pages": [gigas, movies, stats],
        }
)

pg.run()