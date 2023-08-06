from itertools import zip_longest
import pandas as pd
from pandas.core.frame import DataFrame


def pairwise_explode(df, columns):

    df1 = (
        df.apply(
            lambda x: tuple(zip_longest(*[x[y] for y in columns], fillvalue=pd.NA)),
            axis=1,
        )
        .explode()
        .apply(lambda x: pd.Series(x, index=columns))
        .groupby(level=0)
        .ffill()
    )
    dfne = (df[[x for x in df.columns if x not in columns]].join(df1)).filter(
        df.columns
    )
    return dfne.copy()


def pd_add_pairwise_explode():
    DataFrame.d_pairwise_explode = pairwise_explode
