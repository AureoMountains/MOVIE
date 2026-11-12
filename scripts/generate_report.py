
from pathlib import Path

from movie_analysis.data import load_movies
from movie_analysis.validation import validate_movies
from movie_analysis.preprocessing import preprocess_movies
from movie_analysis.analysis import (
    average_rating,
    best_rated_movie,
    top_movies_by_revenue,
)


ROOT = Path(__file__).resolve().parents[1]


def main():
    df = load_movies()
    validate_movies(df)
    df = preprocess_movies(df)

    output = ROOT / "reports"
    output.mkdir(exist_ok=True)

    best = best_rated_movie(df)
    top = top_movies_by_revenue(df)

    report = [
        "# Movie Analysis Report",
        "",
        f"Total movies: {len(df)}",
        f"Average rating: {average_rating(df):.2f}",
        f"Best rated movie: {best['title']}",
        "",
        "## Top 5 by revenue",
        "",
    ]

    for _, movie in top.iterrows():
        report.append(
            f"- {movie['title']}: "
            f"${movie['revenue_million']} million"
        )

    (output / "report.md").write_text(
        "\n".join(report),
        encoding="utf-8"
    )


if __name__ == "__main__":
    main()
