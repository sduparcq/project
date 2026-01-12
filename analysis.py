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
df.head()

# %% ANALYSIS

df.info()

symbols = list(ref_dict.keys())
n_symbols = len(symbols)



# %%

norm_df = df.copy()

for col in norm_df.columns:
    norm_df[col] = (norm_df[col] - norm_df[col].mean()) / norm_df[col].std()

cov_matrix = norm_df.cov()

# %%
print(cov_matrix)

# %%
df_save = df.copy()

df_save.head(-1)












