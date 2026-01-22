def signal_agent(row: dict) -> dict:
    signal = "HOLD"
    confidence = 0.5

    if row["rsi"] < 30 and row["macd"] > 0 and row["volume"] > row["volume_ma"]:
        signal = "BUY"
        confidence = 0.75

    elif row["rsi"] > 70 and row["ema_9"] < row["ema_21"]:
        signal = "SELL"
        confidence = 0.70

    return {
        "signal": signal,
        "confidence": confidence
    }
