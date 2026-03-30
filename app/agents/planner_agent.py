from langchain_ollama.llms import OllamaLLM
from app.prompts.planner_prompt import PLANNER_PROMPT
from app.config import OLLAMA_MODEL, OLLAMA_BASE_URL

llm = OllamaLLM(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL
)

def plan_query(query: str):
    prompt = PLANNER_PROMPT.format(query=query)
    response = llm.invoke(prompt)
    return response