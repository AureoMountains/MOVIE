
import pytest

from movie_analysis.data import MOVIES
from movie_analysis.analysis import (
    average_rating,
    best_rated_movie,
    top_movies_by_revenue,
    estimated_profit_million,
    movies_by_genre
)


def test_average_rating():
    assert average_rating(MOVIES[:2]) == pytest.approx(8.9)


def test_best_rated_movie():
    assert best_rated_movie(MOVIES)["title"] == "The Dark Knight"


def test_top_revenue():

    result = top_movies_by_revenue(MOVIES, 2)

    assert result[0]["title"] == "The Dark Knight"
    assert result[1]["title"] == "Inception"


def test_empty_collection():

    with pytest.raises(ValueError):
        average_rating([])


def test_negative_limit():

    with pytest.raises(ValueError):
        top_movies_by_revenue(MOVIES, -1)


def test_genre_grouping():

    grouped = movies_by_genre(MOVIES)

    assert len(grouped["Sci-Fi"]) == 4


def test_estimated_profit():

    assert estimated_profit_million(MOVIES[0]) == 679
