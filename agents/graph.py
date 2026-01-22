from agents.signal_agent import signal_agent
from agents.risk_agent import risk_agent
from agents.strategy_agent import strategy_agent

def run_agents(df):
    results = []

    for symbol, stock_df in df.groupby("symbol"):
        latest = stock_df.iloc[-1].to_dict()

        signal = signal_agent(latest)

        risk = risk_agent(
            price=latest["close"],
            atr=latest["atr"]
        )

        if not risk["approved"]:
            continue

        state = {
            "symbol": symbol,
            "signal": signal["signal"],
            "indicators": {
                "rsi": latest["rsi"],
                "macd": latest["macd"],
                "ema_9": latest["ema_9"],
                "ema_21": latest["ema_21"],
            },
            "risk": risk
        }

        strategy = strategy_agent(state)

        results.append({
            "symbol": symbol,
            "signal": strategy["final_decision"],
            "stop_loss": risk["stop_loss"],
            "target": risk["target"],
            "reason": strategy["reason"]
        })

    return results
