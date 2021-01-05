import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYjdmOGNiY2JiYWQ5YWJmYjA4MDZkYmE4MmMzZDM2YiIsInN1YiI6IjVmZDNiMz" \
                "BkMmVmZTRlMDA0MDRmYTcyNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o1_" \
                "2fkbIMctxp8vWGYaW9jtT6SMP5R_1O18ObVrZU_4"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
