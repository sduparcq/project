from _typeshed import SupportsRichComparisonT
from Strategy import Strategy
from typing import List
import pandas as pd

class MomentumStrat(Strategy):
    def __init__(self, fee: float, slippage: float, pool: int):
        self.pool = pool
        self.fee = fee
        self.slippage = slippage

    def __gen_momentum(self, df: pd.DataFrame, symbols: List[str], short: int, long: int):
        for symbol in symbols:
            df[f"{symbol}_momentum_{short}_{long}"] = df[symbol].rolling(short).mean() - df[symbol].rolling(long).mean()
            df[f"{symbol}_momentum_{short}_{long}"] = ( df[f"{symbol}_momentum_{short}_{long}"] - df[f"{symbol}_momentum_{short}_{long}"].mean()) / self.data_df[f"{symbol}_momentum_{short}_{long}"].std()
        return df

    def __gen_features(self, df: pd.DataFrame, short: int, long: int):
        return self.__gen_momentum(df=df, symbols=self.symbols, short=short, long=long)


    def gen_signal(self, df: pd.DataFrame, short: int, long: int) -> pd.DataFrame:
        df_loc = df.copy()
        df_loc = self.__gen_features(df=df_loc, short=short, long=long)
        ### generation du signal
        return df_loc




