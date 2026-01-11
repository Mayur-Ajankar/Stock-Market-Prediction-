import os
import pandas as pd
from datetime import datetime, timedelta
from ingestion.stock_APIs.yahoo_api import YahooFinanceAPI

# Config
NIFTY_50 = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

DATA_DIR = "data/raw"
os.makedirs(DATA_DIR, exist_ok=True)


def fetch_market_data():
    api = YahooFinanceAPI()
    frames = []

    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=40)).strftime("%Y-%m-%d")

    for symbol in NIFTY_50:
        try:
            print(f"Fetching {symbol}")
            df = api.fetch_historical_data(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date
            )
            frames.append(df)
        except Exception as e:
            print(f"❌ Failed for {symbol}: {e}")

    if not frames:
        raise RuntimeError("No market data fetched")

    df_all = pd.concat(frames, ignore_index=True)
    print(df_all.head())

    # Save locally (later → DB)
    file_path = f"{DATA_DIR}/nifty_latest.parquet"
    df_all.to_parquet(file_path, index=False)

    print(f"✅ Data saved to {file_path}")
    return df_all


if __name__ == "__main__":
    fetch_market_data()


