"""
defines an abstract base class (ABC) for stock market data providers. 
Its purpose is design clarity, consistency, and extensibility in your system—especially 
useful in agentic / modular AI architectures like stock-trading project.

"""

from abc import ABC, abstractmethod
import pandas as pd

class StockAPIBase(ABC):

    """Abstract base class for stock market data providers."""
    @abstractmethod
    def fetch_historical_data(
        self, 
        symbol: str, 
        start_date: str, 
        end_date: str,
        internal: str) -> pd.DataFrame:
        

        """
        Fetch historical stock data for a given symbol between start_date and end_date.

        Args:
            symbol (str): The stock symbol to fetch data for.
            start_date (str): The start date for the data in 'YYYY-MM-DD' format.
            end_date (str): The end date for the data in 'YYYY-MM-DD' format."""