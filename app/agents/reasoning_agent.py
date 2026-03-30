from langchain_ollama.llms import OllamaLLM
from app.config import OLLAMA_MODEL, OLLAMA_BASE_URL

llm = OllamaLLM(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL
)

def generate_answer(query, context):

    prompt = f"""
You are an expert AI assistant.

Use the evidence below to answer.

Evidence:
{context}

Question:
{query}

Provide a clear answer with sources.
"""

    return llm.invoke(prompt)