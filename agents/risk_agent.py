def risk_agent(price: float, atr: float) -> dict:
    stop_loss = round(price - (1.5 * atr), 2)
    target = round(price + (3 * atr), 2)

    rr = (target - price) / (price - stop_loss)

    return {
        "stop_loss": stop_loss,
        "target": target,
        "risk_reward": round(rr, 2),
        "approved": rr >= 1.5
    }
