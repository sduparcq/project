from abc import ABC, abstractmethod
import pandas as pd
from typing import List
import numpy as np

class Strategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def gen_signal(self) -> pd.DataFrame:
        """
        method to create buy sell signal on the dataframe
        """ 
        pass

    # =============================================
    # BASE FEATURE ENG
    def __gen_price_diff(self, symbols: List[str], df: pd.DataFrame):
        for symbol in symbols:
            df[f"{symbol}_price_diff"] = df[symbol] - df[symbol].shift(1)

    def __gen_log_returns(self, symbols: List[str], df: pd.DataFrame):
        for symbol in symbols:
            df[f"{symbol}_log_return"] = np.log(
                df[symbol] / df[symbol].shift(1)
            )


