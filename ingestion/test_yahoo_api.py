from ingestion.stock_APIs.yahoo_api import YahooFinanceAPI


NIFTY_50_TICKERS = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]


if __name__ == "__main__":
    yahoo_api = YahooFinanceAPI()
    try:
        df = yahoo_api.fetch_historical_data(
            symbol=NIFTY_50_TICKERS,
            start_date="2025-01-01",
            end_date="2025-12-31",
            interval="1d"
        )
        print(df.head())
        print(df.tail())
        print(df)
        df.to_csv("nifty_50_january_2025.csv", index=False)
    except Exception as e:
        print(f"Error fetching data: {e}")