# Personal Project — RAG Search API

A personal project focused on building a Retrieval-Augmented Generation (RAG) system with FastAPI, vector search, and language models.

This is a learning and portfolio project designed to explore how local business data can be indexed, retrieved, and used to generate grounded answers with an LLM.

## What this project does

- loads structured local data
- converts records into embeddings
- stores vectors in FAISS
- retrieves relevant context with similarity search
- generates a final response using Groq
- includes a small evaluation workflow for testing quality

## Tech stack

- Python
- FastAPI
- FAISS
- Hugging Face Embeddings
- LangChain
- Groq
- pytest

## Project status

This project is for personal learning, experimentation, and portfolio demonstration. It is not intended as a public product or reusable service for general external use.

## Local setup

```powershell
cd C:\Users\hp\work\ingest_doc
python -m venv RAGENV
.\RAGENV\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run locally

```powershell
cd C:\Users\hp\work\ingest_doc
.\RAGENV\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000/docs

## Notes

- API keys are kept in local config files only.
- This is a personal experimentation project.
- Do not expose this project or its data publicly without review.

## Purpose

The goal is to practice:

- RAG pipeline design
- embedding-based retrieval
- prompt construction
- LLM integration
- evaluation and experimentation

## License

For personal use and portfolio demonstration only.

