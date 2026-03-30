from app.tools.vector_search import vector_search
from app.tools.web_search import web_search

def hybrid_search(query):

    vector_docs = vector_search(query)

    web_docs = web_search(query)

    # normalize web results
    web_texts = [d["content"] for d in web_docs]

    return vector_docs + web_texts