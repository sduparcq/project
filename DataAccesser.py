import pandas as pd
from typing import List

class DataAccesser:
    def __init__(self):
        self.path = "/home/sduparcq/workspace/project/data"

    def generate_data_frame(self, universe: List[str]):
        series = {}
        for symbol in universe:
            path = self.path + f"/{symbol}__USDT_1h.parquet"
            df = pd.read_parquet(path)
            series[symbol] = df["close"]
        return pd.DataFrame(series)
