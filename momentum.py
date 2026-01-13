# %% imports
import Context
import DataAccesser
import DFManager

import importlib

importlib.reload(Context)
importlib.reload(DataAccesser)


# %% DATA LOADING / INSTANCIATING CLASSES ETC
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
symbols = list(ref_dict.keys())

df_manager = DFManager.DFManager(data_df=df_save, symbols=symbols)

# %% PREPARING DF 

df_manager.prepare_df()
df_manager.data_df.head(-1)
df_manager.data_df.columns
# %%
df_manager.gen_momentum(short=50, long=200)
df_manager.momentum_signal(short=50, long=200)


