import yfinance as yf
import pandas as pd
from ingestion.stock_APIs.base import StockAPIBase
from ingestion.stock_APIs.exceptions import SymbolNotFoundError, DataFetchError

class YahooFinanceAPI(StockAPIBase):

    def fetch_historical_data(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
        interval: str = "1d"
    ) -> pd.DataFrame:

        try:
            df = yf.download(
                symbol,
                start=start_date,
                end=end_date,
                interval=interval,
                progress=False
            )
        except Exception as e:
            raise DataFetchError(str(e))

        if df.empty:
            raise SymbolNotFoundError(f"No data for {symbol}")

        df = df.copy()  # 🔑 IMPORTANT

        df.reset_index(inplace=True)
        df.rename(columns={
            "Date": "date",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        }, inplace=True)

        df["symbol"] = symbol

        return df[[
            "date", "symbol",
            "open", "high", "low", "close", "volume"
        ]]
