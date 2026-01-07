class StockAPIError(Exception):
    pass

class SymbolNotFoundError(StockAPIError):
    pass

class DataFetchError(StockAPIError):
    pass
