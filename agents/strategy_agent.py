from langchain_community.llms import Ollama

from llm.prompts import STRATEGY_PROMPT
#from llm.load_llm import load_llm


def strategy_agent(state: dict) -> dict:
    prompt = STRATEGY_PROMPT.format(
        market="NSE",
        stock=state["symbol"],
        signal=state["signal"],
        indicators=state["indicators"],
        risk=state["risk"]
    )

    reasoning = llm(prompt)

    return {
        "final_decision": state["signal"],
        "reason": reasoning
    }
