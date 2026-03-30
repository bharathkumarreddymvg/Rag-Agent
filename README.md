# RAG Agent System

A modular Retrieval-Augmented Generation (RAG) system built with FastAPI, LangChain, and ChromaDB. This project combines document retrieval, web search, and LLM-based reasoning to answer user queries intelligently.

---

## Overview

This system follows an agent-based architecture:

* Planner Agent decides how to handle the query
* Retriever fetches relevant information from documents and the web
* Reasoning Agent generates the final answer using context
* Memory stores recent interactions

---

## Features

* FastAPI-based REST API
* Hybrid search (vector search + web search)
* Modular agent design (planner and reasoning agents)
* Local vector database using ChromaDB
* PDF ingestion and chunking pipeline
* Conversation memory support

---

## Project Structure

```
rag-agent-pro/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── agents/
│   │   ├── planner_agent.py
│   │   └── reasoning_agent.py
│   │
│   ├── retriever/
│   │   └── hybrid_search.py
│   │
│   ├── tools/
│   │   ├── vector_search.py
│   │   ├── web_search.py
│   │   └── calculator.py
│   │
│   ├── memory/
│   │   └── conversation_memory.py
│   │
│   ├── prompts/
│   │   └── planner_prompt.py
│   │
│   └── config.py
│
├── data/
│   ├── pdfs/
│   └── chroma/
│
├── ingest.py
├── run.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/bharathkumarreddymvg/Rag-Agent.git
cd Rag-Agent
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Data Ingestion

Place your PDF files inside:

```
data/pdfs/
```

Run ingestion:

```
python ingest.py
```

This will:

* Load PDFs
* Split into chunks
* Store embeddings in ChromaDB

---

## Running the Application

Start the FastAPI server:

```
uvicorn run:app --reload
```

Open in browser:

```
http://localhost:8000/docs
```

---

## API Usage

### Ask a question

```
GET /ask?query=your_question
```

Example:

```
http://localhost:8000/ask?query=what is machine learning
```

Response includes:

* Plan (steps from planner agent)
* Answer (generated response)
* Sources (retrieved documents)

---

## Technologies Used

* FastAPI
* LangChain
* ChromaDB
* HuggingFace Embeddings
* DuckDuckGo Search
* Python

---

## Configuration

Key settings in `app/config.py`:

* LLM model
* Embedding model
* Vector database path

---

## Notes

* Ensure embedding model is consistent across ingestion and retrieval
* ChromaDB must be cleared if embedding model changes
* Web search depends on internet availability

---

## Future Improvements

* Add frontend UI
* Deploy using cloud services
* Add streaming responses
* Improve memory handling
* Add authentication

---

## Author

Bharath Kumar Reddy

---
