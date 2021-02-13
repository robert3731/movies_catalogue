from flask import Flask, render_template, request
import tmdb_client
import random
import datetime

app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list = request.args.get("list_type", "popular")
    list_types = ['popular', 'now_playing', 'top_rated', 'upcoming']
    if selected_list not in list_types:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, list_types=list_types)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_movie_details(movie_id)
    images = tmdb_client.get_movie_images(movie_id)
    if images['backdrops']:
        selected_backdrop = random.choice(images['backdrops'])
        backdrop = selected_backdrop['file_path']
    else:
        backdrop = []
    cast = tmdb_client.get_single_movie_cast(movie_id, how_many=4)
    return render_template("movie_details.html", movie=movie, cast=cast, selected_backdrop=backdrop)


@app.route("/search")
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)


@app.route('/today')
def airing_today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("airing_today.html", movies=movies, today=today)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
