
import pandas as pd


REQUIRED_COLUMNS = {
    "title",
    "year",
    "genre",
    "rating",
    "runtime",
    "budget_million",
    "revenue_million",
}


def validate_movies(df: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {sorted(missing_columns)}"
        )

    if df.empty:
        raise ValueError("Dataset is empty.")

    if df[list(REQUIRED_COLUMNS)].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    if not df["rating"].between(0, 10).all():
        raise ValueError("Ratings must be between 0 and 10.")

    if (df["runtime"] <= 0).any():
        raise ValueError("Runtime must be positive.")

    if (df["budget_million"] < 0).any():
        raise ValueError("Budget cannot be negative.")

    if (df["revenue_million"] < 0).any():
        raise ValueError("Revenue cannot be negative.")

    if df["title"].duplicated().any():
        raise ValueError("Duplicate movie titles detected.")
