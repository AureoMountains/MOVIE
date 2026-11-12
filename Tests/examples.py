
from movie_analysis.data import MOVIES

from movie_analysis.analysis import (
    movies_by_genre,
    top_movies_by_revenue
)


print("Top 3 movies:")

for movie in top_movies_by_revenue(MOVIES, 3):
    print(movie["title"])


print("\nMovies by genre:")

for genre, movies in sorted(movies_by_genre(MOVIES).items()):
    print(f"{genre}: {len(movies)}")
