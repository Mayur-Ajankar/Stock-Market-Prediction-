from ingestion.stock_APIs.yahoo_api import YahooFinanceAPI
from ingestion.stock_APIs.utils import fetch_multiple_stocks

NIFTY_50 = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

if __name__ == "__main__":
    api = YahooFinanceAPI()

    df = fetch_multiple_stocks(
        api=api,
        symbols=NIFTY_50,
        start_date="2025-01-01",
        end_date="2025-02-01"
    )

    print(df)
    print("Rows:", len(df))
    
    df.to_csv("nifty_50_2025.csv", index=False)
