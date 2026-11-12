
from .data import MOVIES
from .analysis import (
    average_rating,
    best_rated_movie,
    top_movies_by_revenue,
    estimated_profit_million
)
from .plotting import (
    plot_revenue,
    plot_budget_vs_revenue
)


def main():

    print(f"Movies: {len(MOVIES)}")
    print(f"Average rating: {average_rating(MOVIES):.2f}")

    best = best_rated_movie(MOVIES)

    print(
        f"Best rated movie: {best['title']} "
        f"({best['rating']}/10)"
    )

    print("\nTop 5 movies by revenue:")

    for movie in top_movies_by_revenue(MOVIES):

        profit = estimated_profit_million(movie)

        print(
            f"{movie['title']}: "
            f"${movie['revenue_million']}M "
            f"(Revenue - Budget: ${profit:.2f}M)"
        )

    plot_revenue(MOVIES)
    plot_budget_vs_revenue(MOVIES)


if __name__ == "__main__":
    main()
