from pathlib import Path
import pandas as pd


DATA_PATH = (
    Path(__file__).resolve().parents[1] / "data" / "raw"
)

COLUMNS = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income"
]


def load_dataset() -> pd.DataFrame:
    """Load and merge the original Adult dataset files."""

    train = pd.read_csv(
        DATA_PATH / "adult.data",
        names=COLUMNS,
        skipinitialspace=True,
        na_values="?"
    )

    test = pd.read_csv(
        DATA_PATH / "adult.test",
        names=COLUMNS,
        skipinitialspace=True,
        na_values="?",
        skiprows=1
    )

    df = pd.concat(
        [train, test],
        ignore_index=True
    )

    df["income"] = (
        df["income"]
        .str.strip()
        .str.rstrip(".")
    )

    return df
