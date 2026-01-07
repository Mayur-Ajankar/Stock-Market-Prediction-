from langchain_community.llms import Ollama

def load_llm(model_name: str = "llama3"):
    """
    Loads open-source LLM via Ollama
    """
    return Ollama(
        model=model_name,
        temperature=0.2
    )
