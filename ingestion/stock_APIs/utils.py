import pandas as pd
from typing import List

def fetch_multiple_stocks(
    api,
    symbols: List[str],
    start_date: str,
    end_date: str
) -> pd.DataFrame:

    data = []

    for symbol in symbols:
        try:
            df = api.fetch_historical_data(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date
            )
            data.append(df)
            print(f"Fetched {symbol}")
        except Exception as e:
            print(f"Skipping {symbol}: {e}")

    if not data:
        raise ValueError("No data fetched from Yahoo")

    return pd.concat(data, ignore_index=True)
