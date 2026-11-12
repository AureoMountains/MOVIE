
from collections import defaultdict
from collections.abc import Iterable

from .data import Movie


def average_rating(movies: Iterable[Movie]) -> float:
    if not movies:
        raise ValueError("Empty movie collection.")

    return sum(m["rating"] for m in movies) / len(movies)


def best_rated_movie(movies: Iterable[Movie]) -> Movie:
    if not movies:
        raise ValueError("Empty movie collection.")

    return max(movies, key=lambda m: m["rating"])


def top_movies_by_revenue(
    movies: Iterable[Movie],
    limit: int = 5
) -> list[Movie]:

    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    return sorted(
        movies,
        key=lambda m: m["revenue_million"],
        reverse=True
    )[:limit]


def movies_by_genre(
    movies: Iterable[Movie]
) -> dict[str, list[Movie]]:

    grouped = defaultdict(list)

    for movie in movies:
        grouped[movie["genre"]].append(movie)

    return dict(grouped)


def estimated_profit_million(movie: Movie) -> float:
    return movie["revenue_million"] - movie["budget_million"]
