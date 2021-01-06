import requests
import random
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYjdmOGNiY2JiYWQ5YWJmYjA4MDZkYmE4MmMzZDM2YiIsInN1YiI6IjVmZDNiMz" \
                "BkMmVmZTRlMDA0MDRmYTcyNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o1_" \
                "2fkbIMctxp8vWGYaW9jtT6SMP5R_1O18ObVrZU_4"


def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    keys = list(data["results"])
    random.shuffle(keys)
    return keys[:how_many]


def get_movie_details(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast'][:how_many]
