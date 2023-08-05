"""@Author: Rayane AMROUCHE

DataFrame informations methods for the Utils class for the DataManager
"""

from scipy import stats  # type: ignore

import pandas as pd  # type: ignore
import numpy as np  # type: ignore


def unique(df_: pd.DataFrame) -> pd.DataFrame:
    """Print unique values of each column of a pandas DataFrame

    Args:
        df_ (pd.DataFrame): DataFrame whose columns' uniques are to be
            displayed

    Returns:
        pd.DataFrame: Returns original DataFrame
    """
    return (
        pd.DataFrame()
        .assign(**{
            "rank": range(len(df_))
        })
        .assign(**{
            col: pd.Series(df_[col].unique()) for col in df_.columns
        })
    )


def describe(df_: pd.DataFrame) -> pd.DataFrame:
    """Print DataFrame description

    Args:
        df_ (pd.DataFrame): DataFrame whose description is to be described

    Returns:
        pd.DataFrame: Returns DataFrame description
    """
    cat_cols = df_.select_dtypes(exclude=['number']).columns
    num_cols = df_.select_dtypes(include=['number']).columns

    return (
        pd.DataFrame()
        .assign(**{
            "count": df_.count(axis=0),
            "dtypes": df_.dtypes,
            "numeric": [
                pd.api.types.is_numeric_dtype(dtype) for dtype in df_.dtypes
            ],
        })
        .assign(**{
            "nunique": df_.nunique(),
            "mode": df_.mode(dropna=False).iloc[0],
            # "freq": stats.mode(df_, keepdims=True).count[0]
        })
        .assign(**{
            "mean": np.mean(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                axis=0
            ),
            "std": np.std(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                axis=0
            ),
            "median": np.median(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                axis=0
            ),
            "quartile_1": np.percentile(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                25, axis=0
            ),
            "quartile_3": np.percentile(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                75, axis=0
            ),
            "min": np.min(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                axis=0
            ),
            "max": np.max(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                axis=0
            )
        })
        .assign(**{
            "trim_mean_01": stats.trim_mean(
                df_.assign(**{cat: np.nan for cat in cat_cols}),
                0.1
            ),
            "skew": stats.skew(
                df_.assign(**{cat: np.nan for cat in cat_cols})
            ),
            "kurtosis": stats.kurtosis(
                df_.assign(**{cat: np.nan for cat in cat_cols})
            ),
            "sem": stats.sem(
                df_.assign(**{cat: np.nan for cat in cat_cols})
            ),
            "entropy": stats.entropy(
                df_.assign(**{cat: np.nan for cat in cat_cols})
            )
        })
        .T
        .filter(items=list(num_cols) + list(cat_cols))
    )
