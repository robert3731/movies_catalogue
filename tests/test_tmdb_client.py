from unittest.mock import Mock
import tmdb_client


def test_get_poster_url_uses_default_size():
    poster_api_path="some-poster-path"
    expected_default_size='w342'
    poster_url=tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list=tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list_type_top_rated():
    movies_list=tmdb_client.get_movies_list(list_type="top_rated")
    assert movies_list is not None


def test_get_movies_list_type_upcoming():
    movies_list=tmdb_client.get_movies_list(list_type="upcoming")
    assert movies_list is not None


def test_get_movies_list_type_now_playing():
    movies_list=tmdb_client.get_movies_list(list_type="now_playing")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']

    movies_mock = Mock()
    response = movies_mock.return_value
    response.json.return_value=mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", movies_mock)

    movies_list=tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_movie_details(monkeypatch):
    mock_single_movie = ["Reksio"]
    single_movie_mock = Mock()

    response = single_movie_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.requests.get", single_movie_mock)
    single_movie = tmdb_client.get_movie_details(500)
    assert single_movie == mock_single_movie


def get_single_movie_cast(monkeypatch):
    mock_movie_cast = "Random cast"
    single_movie_cast_mock = Mock()

    response = single_movie_cast_mock.return_value
    response.json.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", single_movie_cast_mock)
    single_movie_cast = tmdb_client.get_single_movie_cast(500, 4)
    assert single_movie_cast == mock_movie_cast


def get_single_movie_image(monkeypatch):
    mock_movie_image = "Image.jpg"
    single_movie_image_mock = Mock()

    response = single_movie_image_mock.return_value
    response.json.return_value = mock_movie_image
    monkeypatch.setattr("tmdb_client.requests.get", single_movie_image_mock)
    single_movie_image = tmdb_client.get_movie_images(500)
    assert single_movie_image == single_movie_image_mock
