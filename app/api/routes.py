from fastapi import APIRouter
from app.agents.planner_agent import plan_query
from app.retriever.hybrid_search import hybrid_search
from app.agents.reasoning_agent import generate_answer
from app.memory.conversation_memory import add_memory

router = APIRouter()

@router.get("/ask")
def ask(query: str):

    plan = plan_query(query)

    docs = hybrid_search(query)

    context = "\n".join(docs[:5])

    answer = generate_answer(query, context)

    add_memory(query, answer)

    return {
        "plan": plan,
        "answer": answer,
        "sources": docs[:3]
    }