# %% imports
import pandas as pd
import Context
import DataAccesser

import importlib

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
df['ADA_momentum'] = df['ADA'].pct_change(periods=period)

df.head(-1)




