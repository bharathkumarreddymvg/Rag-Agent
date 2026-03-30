from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.config import EMBED_MODEL
import os

DATA_PATH = "data/pdfs"
DB_PATH = "data/chroma"

embedding = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL
)

def ingest():

    docs = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            path = os.path.join(DATA_PATH, file)
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

    print(f"Loaded documents: {len(docs)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)

    print(f"Created chunks: {len(chunks)}")

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    vectordb.add_documents(chunks)
    vectordb.persist()

    print("Documents indexed successfully:", len(chunks))


if __name__ == "__main__":
    ingest()