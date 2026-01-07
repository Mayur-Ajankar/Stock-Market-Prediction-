import yfinance as yf
import pandas as pd
from .base import StockAPIBase



class YahooFinanceAPI(StockAPIBase):
    """Concrete implementation of StockAPIBase using Yahoo Finance."""

    def fetch_historical_data(
        self, 
        symbol: list[str], 
        start_date: str, 
        end_date: str,
        interval: str = '1d') -> pd.DataFrame:
        """
        Fetch historical stock data for a given symbol between start_date and end_date.

        Args:
            symbol (str): The stock symbol to fetch data for.
            start_date (str): The start date for the data in 'YYYY-MM-DD' format.
            end_date (str): The end date for the data in 'YYYY-MM-DD' format.
            interval (str): Data interval (e.g., '1d', '1wk', '1mo'). Default is '1d'."""

        tickers = yf.Tickers(symbol)
        df = tickers.history(start=start_date, 
                            end=end_date, 
                            interval=interval,
                            auto_adjust=True)
        
        if df.empty:
            raise ValueError(f"YAHOO, No data found for symbol: {symbol} between {start_date} and {end_date}")
        
        df.reset_index(inplace=True)

        df=df.rename(columns={'Date':'date',
                              'Open':'open',
                              'High':'high',
                                'Low':'low',
                                'Close':'close',
                                'Volume':'volume'})
        


        return df[['date', 'open', 'high', 'low', 'close', 'volume']]