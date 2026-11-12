
import pandas as pd


def preprocess_movies(df: pd.DataFrame) -> pd.DataFrame:
    processed = df.copy()

    processed["title"] = processed["title"].str.strip()
    processed["genre"] = processed["genre"].str.strip()

    processed["estimated_profit_million"] = (
        processed["revenue_million"]
        - processed["budget_million"]
    )

    processed["roi_percentage"] = (
        processed["estimated_profit_million"]
        / processed["budget_million"].replace(0, float("nan"))
    ) * 100

    processed["decade"] = (
        processed["year"] // 10
    ) * 10

    return processed
