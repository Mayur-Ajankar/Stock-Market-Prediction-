Stock APIs (Yahoo / Alpha --> QQAH4T6YTANCIV8O )
   ↓
Azure Function (fetch_data)
   ↓
Feature Engineering (technicals.py)
   ↓
Signal Agent
   ↓
Risk Agent
   ↓
Strategy Agent (LangGraph + LLM)
   ↓
PostgreSQL
   ↓
FastAPI
   ↓
Streamlit UI


Yahoo Finance (NSE)
      ↓
Azure Function (fetch_data)
      ↓
PostgreSQL (market data)
      ↓
Indicators (TA)
      ↓
Signal Agent (rules)
      ↓
Risk Agent (SL/Target)
      ↓
Strategy Agent (LLM reasoning)
      ↓
FastAPI (API layer)
      ↓
Streamlit (UI)

