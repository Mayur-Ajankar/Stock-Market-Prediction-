# Convert price data → intelligence

import ta
import pandas as pd

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    def apply_indicators(stock_df):
        stock_df = stock_df.copy()

        stock_df["rsi"] = ta.momentum.RSIIndicator(stock_df["close"]).rsi()
        stock_df["ema_9"] = ta.trend.EMAIndicator(stock_df["close"], 9).ema_indicator()
        stock_df["ema_21"] = ta.trend.EMAIndicator(stock_df["close"], 21).ema_indicator()
        stock_df["macd"] = ta.trend.MACD(stock_df["close"]).macd()
        stock_df["atr"] = ta.volatility.AverageTrueRange(
            stock_df["high"], stock_df["low"], stock_df["close"]
        ).average_true_range()

        stock_df["volume_ma"] = stock_df["volume"].rolling(20).mean()

        return stock_df.dropna()

    return df.groupby("symbol", group_keys=False).apply(apply_indicators)
