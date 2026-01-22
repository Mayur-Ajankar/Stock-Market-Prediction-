import pandas as pd
import ta

DATA_PATH = "data/raw/nifty_latest.parquet"

def load_market_data() -> pd.DataFrame:
    df = pd.read_parquet(DATA_PATH)

    # Standardize column names
    df.columns = [c.lower() for c in df.columns]

    # Ensure datetime
    df["date"] = pd.to_datetime(df["date"])

    # Sort properly
    df = df.sort_values(["symbol", "date"])

    return df

    
