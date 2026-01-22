from fastapi import FastAPI
from ingestion.load_data import load_market_data
from indicators.technicals import compute_indicators
from agents.graph import run_agents

app = FastAPI()

@app.get("/signals/nifty")
def get_nifty_signals():
    df = load_market_data()
    df = compute_indicators(df)

    decisions = run_agents(df)
    return decisions
