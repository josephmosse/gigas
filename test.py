import requests
import json

API_KEY = 'f02f78b1f3a7f2976cdfaac794698217'

def get_actor_photo(name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={name}"
    response = requests.get(url).json()
    return {"profile" : response['results'][0]['profile_path'], "id" : response['results'][0]['id']}

def get_actor_id(name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={name}"
    response = requests.get(url).json()
    return response['results'][0]['id'] if response['results'] else None


def find_giga_movies(actor_name):
    movie_list = []
    actor_id = data[actor_name]["id"]
    pages = data[actor_name]["total_pages"]
    for i in range(pages):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page={str(i+1)}&without_genres=99&with_cast={actor_id}&sort_by=popularity.desc"
        response = requests.get(url).json()
        results = response['results']
        for movie in results:
            movie_list.append(movie)

    data[actor]["movies"] = movie_list

    return movie_list


with open('actors.json', 'r') as fp:
    data = json.load(fp)

for actor in data:
    print(f"{actor} : {len(data[actor]["movies"])}")

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
with open('genre.json', 'w') as fp:
    json.dump(genres_dict, fp, indent=4)


#def find_giga_movies(actor_name):
#    movie_list = []
#    actor_id = data[actor_name]["id"]
#    pages = data[actor_name]["total_pages"]
#    for i in range(pages):
#        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&page={str(i+1)}&without_genres=99&with_cast={actor_id}&sort_by=popularity.desc"
#        response = requests.get(url).json()
#        results = response['results']
#        for movie in results:
#            movie_list.append(movie)
#
#    data[actor]["movies"] = movie_list
#
#    return movie_list

# Scrap toutes les données sur les gigas (tous les films)
# On veut récuperer le titre, l'id, l'année, les genres 
