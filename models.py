import json
from statistics import mean
import pandas as pd
import streamlit as st

class Movie:
    def __init__(self, id, title, original_title, overview, release_date, poster_path, backdrop_path, vote_average, vote_count, popularity, adult, genre_ids, video, original_language):
        self.id = id
        self.title = title
        self.original_title = original_title
        self.overview = overview
        self.release_date = release_date
        self.poster_path = poster_path
        self.backdrop_path = backdrop_path
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.popularity = popularity
        self.adult = adult
        self.genre_ids = genre_ids
        self.video = video
        self.original_language = original_language

    def get_genres(self):
        return sorted([str(genre_id) for genre_id in self.genre_ids])

class Actor:
    def __init__(self, name, profile, actor_id, total_pages, movies):
        self.name = name
        self.profile = profile
        self.actor_id = actor_id
        self.total_pages = total_pages
        self.movies = [Movie(**movie) for movie in movies]

    def __str__(self):
        return f"Actor: {self.name} (ID: {self.actor_id})"

    def list_movies(self):
        return self.movies

    def get_first_movie(self):
        return sorted(self.movies, key=lambda m: m.release_date[:4])[0]

    def get_last_movie(self):
        return sorted(self.movies, key=lambda m: m.release_date[:4])[-1]

    def get_movies_per_year(self):
        years = [movie.release_date[:4] for movie in self.movies]
        return years
    
    def get_average_vote(self):
        return mean(movie.vote_average for movie in self.movies) if self.movies else 0

    def get_genre_distribution(self, genres_dict):
        genre_counts = []
        for movie in self.movies:
            for genre in movie.get_genres():
                genre_counts.append(genres_dict[genre])
        
        genre_counts = pd.DataFrame(genre_counts).value_counts()
        #genre_counts.columns=["genre", "count"]
        return genre_counts

@st.cache_data
def load_data():
    with open('data/actors.json', 'r') as file:
        data = json.load(file)

    actors = {name: Actor(name, data[name]["profile"], data[name]["id"], data[name]["total_pages"], data[name]["movies"]) for name in data}
    
    return actors

@st.cache_data
def load_genres():
    with open('data/genres.json', 'r') as file:
        genres = json.load(file)
    return genres
