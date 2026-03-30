from app.config import EMBED_MODEL, VECTOR_DB_PATH

vectordb = None


def get_vectordb():
    global vectordb

    if vectordb is None:
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_chroma import Chroma

        embedding = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

        vectordb = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=embedding
        )

    return vectordb


def vector_search(query, k=5):
    db = get_vectordb()
    docs = db.similarity_search(query, k=k)

    return [d.page_content for d in docs]