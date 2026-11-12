
from movie_analysis.data import load_movies
from movie_analysis.validation import validate_movies
from movie_analysis.preprocessing import preprocess_movies
from movie_analysis.analysis import movies_by_genre

df = load_movies()

validate_movies(df)

df = preprocess_movies(df)

print(movies_by_genre(df))
