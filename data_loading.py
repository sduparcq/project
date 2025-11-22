import ccxt
import pandas as pd
import time
from datetime import datetime

SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    "LTC/USDT",
    "ADA/USDT",
    "XRP/USDT",
    "SOL/USDT",
    "AVAX/USDT",
    "DOT/usdt",
    "UNI/USDT",
    "LINK/USDT",
    "BCH/USDT"
    ]

TIMEFRAME = "1h"
SINCE = int(pd.Timestamp("2020-01-01").timestamp() * 1000)
LIMIT = 1000

OUTPUT_DIR = "./data/"


def fetch_ohlcv_historical(exchange, symbol, timeframe, since, limit=1000, pause=0.2):
    all_data = []
    last_timestamp = since

    while True:
        candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=last_timestamp, limit=limit)
        if not candles:
            break

        all_data.extend(candles)
        last_timestamp = candles[-1][0] + 1

        print(f"{symbol} -> fetched {len(all_data)} row so far ...")

        time.sleep(pause)

        if len(candles) < limit:
            break

    df = pd.DataFrame(
        all_data,
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ms")

    df = df.set_index("datetime")
    df = df.drop(columns=["timestamp"])

    return df

def main():
    exchange = ccxt.binance()

    for symbol in SYMBOLS:
        print(f"\n=== Downloading historical data for {symbol} ({TIMEFRAME}) ===")
        df = fetch_ohlcv_historical(exchange, symbol, TIMEFRAME, SINCE, LIMIT)
        safe_symbol = symbol.replace("/", "__")
        path = f"{OUTPUT_DIR}{safe_symbol}_{TIMEFRAME}.parquet"

        df.to_parquet(path, engine="pyarrow", index=True)
        print(f"Saved -> {path} ({len(df)} rows)")

    print("\nAll downloads complete")



if __name__ == "__main__":
    main()




