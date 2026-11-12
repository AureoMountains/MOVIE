
from typing import TypedDict


class Movie(TypedDict):
    title: str
    year: int
    genre: str
    rating: float
    runtime: int
    budget_million: float
    revenue_million: float


MOVIES: list[Movie] = [
    {
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8,
        "runtime": 148,
        "budget_million": 160,
        "revenue_million": 839
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "genre": "Action",
        "rating": 9.0,
        "runtime": 152,
        "budget_million": 185,
        "revenue_million": 1006
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "rating": 8.7,
        "runtime": 169,
        "budget_million": 165,
        "revenue_million": 731
    },
    {
        "title": "Parasite",
        "year": 2019,
        "genre": "Thriller",
        "rating": 8.5,
        "runtime": 132,
        "budget_million": 11,
        "revenue_million": 258
    },
    {
        "title": "Whiplash",
        "year": 2014,
        "genre": "Drama",
        "rating": 8.5,
        "runtime": 106,
        "budget_million": 3.3,
        "revenue_million": 49
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genre": "Sci-Fi",
        "rating": 8.7,
        "runtime": 136,
        "budget_million": 63,
        "revenue_million": 467
    },
    {
        "title": "Pulp Fiction",
        "year": 1994,
        "genre": "Crime",
        "rating": 8.9,
        "runtime": 154,
        "budget_million": 8.5,
        "revenue_million": 214
    },
    {
        "title": "Spirited Away",
        "year": 2001,
        "genre": "Animation",
        "rating": 8.6,
        "runtime": 125,
        "budget_million": 19,
        "revenue_million": 395
    },
    {
        "title": "Alien",
        "year": 1979,
        "genre": "Horror",
        "rating": 8.5,
        "runtime": 117,
        "budget_million": 11,
        "revenue_million": 106
    },
    {
        "title": "Blade Runner 2049",
        "year": 2017,
        "genre": "Sci-Fi",
        "rating": 8.0,
        "runtime": 164,
        "budget_million": 150,
        "revenue_million": 267
    },
    {
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "genre": "Comedy",
        "rating": 8.1,
        "runtime": 99,
        "budget_million": 25,
        "revenue_million": 172
    },
    {
        "title": "Get Out",
        "year": 2017,
        "genre": "Horror",
        "rating": 7.8,
        "runtime": 104,
        "budget_million": 4.5,
        "revenue_million": 255
    }
]
