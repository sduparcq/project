# %% imports
import pandas as pd
import Context
import DataAccesser
from typing import List
import importlib
import numpy as np


importlib.reload(Context)
importlib.reload(DataAccesser)


# %% DATA LOADING
ref_dict = {
    "ADA": "",
    "AVAX": "",
    "BNB": "",
    "BTC": "",
    "ETH": "",
    "LTC": "",
    "SOL": "",
    "XRP": ""
}

for key in list(ref_dict.keys()):
    ref_dict[key] = f"{key}__USDT"

ctx = Context.Context(ref_dict=ref_dict)
ax = DataAccesser.DataAccesser()
df = ax.generate_data_frame(universe=ctx.universe)
df_save = df.copy()


# %% FEATURE ENG
df = df['2023-01': '2025-09']
symbols = df.columns
n_udl = len(symbols)

period = 24 * 20 # periode de 20 jours

for symbol in symbols:
    df[f"{symbol}_momentum"] = df[symbol].pct_change(periods=period)


def create_momentum(symbols: List[str], short: int, long: int):
    for symbol in symbols:
        df[f"{symbol}_momentum"] = df[symbol].rolling(short).mean() - df[symbol].rolling(long).mean()
        df[f"{symbol}_momentum"] = (df[f"{symbol}_momentum"] - df[f"{symbol}_momentum"].mean()) / df[f"{symbol}_momentum"].std()

create_momentum(
    symbols=symbols,
    short=20,
    long=100
)

# %% ANALYSIS
df.describe()

def create_signal(symbols: List[str]):
    for symbol in symbols:
        df[f"{symbol}_signal"] = df[f"{symbol}_momentum"].apply(np.sign)

create_signal(
    symbols=symbols
)

df.head(-1)


# %% BACKTEST





