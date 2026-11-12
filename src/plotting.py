
from collections.abc import Sequence
from pathlib import Path

import matplotlib.pyplot as plt

from .data import Movie


def plot_revenue(
    movies: Sequence[Movie],
    output: str | Path = "movie_revenue.png"
) -> None:

    if not movies:
        raise ValueError("Empty movie collection.")

    ordered = sorted(
        movies,
        key=lambda m: m["revenue_million"]
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        [m["title"] for m in ordered],
        [m["revenue_million"] for m in ordered],
        color="steelblue"
    )

    ax.set(
        title="Movie Gross Revenue",
        xlabel="Revenue (USD millions)",
        ylabel="Movie"
    )

    ax.grid(axis="x", alpha=0.25)

    fig.tight_layout()
    fig.savefig(output, dpi=150)
    plt.close(fig)


def plot_budget_vs_revenue(
    movies: Sequence[Movie],
    output: str | Path = "movie_budget_vs_revenue.png"
) -> None:

    if not movies:
        raise ValueError("Empty movie collection.")

    fig, ax = plt.subplots(figsize=(8, 5))

    points = ax.scatter(
        [m["budget_million"] for m in movies],
        [m["revenue_million"] for m in movies],
        s=85,
        alpha=0.8,
        c=[m["rating"] for m in movies],
        cmap="viridis",
        edgecolors="black"
    )

    fig.colorbar(points, ax=ax, label="Rating")

    ax.set(
        title="Production Budget vs Revenue",
        xlabel="Budget (USD millions)",
        ylabel="Revenue (USD millions)"
    )

    ax.grid(True, alpha=0.25)

    fig.tight_layout()
    fig.savefig(output, dpi=150)
    plt.close(fig)
