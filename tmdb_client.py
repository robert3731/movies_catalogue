import json
import requests
import random
from config import API_TOKEN


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_movies():
    return call_tmdb_api("movie/popular")


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    keys = list(data["results"])
    random.shuffle(keys)
    return keys[:how_many]


def get_movie_details(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    print(json.dumps(response.json(), indent=4))
    return response.json()['cast'][:how_many]


def search(search_query):
    response = call_tmdb_api(f"search/movie/?query={search_query}")
    return response['results']
