import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "BTC__USDT_1h.parquet"
df = pd.read_parquet(DATA_PATH)
print(df.head())
print(df.columns)
