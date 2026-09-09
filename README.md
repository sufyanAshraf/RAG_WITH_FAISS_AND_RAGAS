# RAG Search API

A production-style Retrieval-Augmented Generation (RAG) application built with FastAPI, Groq, and Hugging Face embeddings. This project indexes local business data, retrieves relevant records via vector search, and generates grounded responses using an LLM.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.13" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-4B0082?style=for-the-badge" alt="FAISS" />
  <img src="https://img.shields.io/badge/Groq-LLM-FFD43B?style=for-the-badge" alt="Groq" />
</p>

## Overview

This project demonstrates a full RAG pipeline:

- loads structured local data
- creates embeddings for each record
- stores vectors in FAISS
- retrieves context using similarity search
- generates a final answer using a Groq-hosted language model
- includes an evaluation route for quality checks using Ragas

It is designed as a clean, portfolio-friendly backend project that can be extended for search, recommendation, customer support, and knowledge-base use cases.

## Features

- FastAPI backend with a clean API structure
- FAISS-powered vector retrieval
- Hugging Face embedding integration
- Groq model generation for response synthesis
- Local data ingestion for domain-specific knowledge
- Evaluation endpoint for RAG quality testing
- Easy local setup with a virtual environment

## Project Structure

```text
ingest_doc/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── embeddingsModel.py
│   ├── embeddingsCreator.py
│   ├── dataBase.py
│   ├── queryModel.py
│   ├── readData.py
│   ├── eval.py
│   ├── evalData.py
│   ├── evalDataPrepration.py
│   ├── logger.py
│   └── prompt.py
├── data/
├── test/
├── config.ini
├── requirements.txt
├── pyproject.toml
├── README.md
└── RAGENV/
```

## Tech Stack

- Python 3.13
- FastAPI
- FAISS
- LangChain
- Hugging Face Embeddings
- Groq API
- Ragas
- pytest

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ingest_doc.git
cd ingest_doc
```

### 2. Create and activate a virtual environment

```powershell
python -m venv RAGENV
.\RAGENV\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Update your `config.ini` file with the required API keys.

Example:

```ini
[KEYS]
groq_api_key = YOUR_GROQ_KEY
huggingface_api_key = YOUR_HUGGINGFACE_KEY
```

> Keep your API keys private and do not commit them to source control.

## Run the Application

```powershell
python -m uvicorn app.main:app --reload
```

Then open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## API Endpoints

### POST /
Send a query and receive a grounded LLM response.

Request body:

```json
{
  "query": "best restaurant near me"
}
```

Response:

```json
{
  "response": "Based on the indexed data, the best option is..."
}
```

### GET /health
Checks whether the API is running.

### GET /eval
Runs a lightweight evaluation of the retrieval and answer quality using Ragas.

## Example Use Case

This project is ideal for:

- restaurant or business search assistants
- domain-specific knowledge bots
- local recommendation systems
- internal document retrieval tools
- learning RAG architecture in practice

## Testing

```powershell
pytest -q
```

## Roadmap

- improve prompt engineering
- add async processing for large workloads
- implement database-backed vector persistence
- add authentication and rate limiting
- expand support for more document sources

## License

This project is available for learning and portfolio use. You can adapt it for your own projects.

## Author

Built as a practical RAG application demonstrating real retrieval, generation, and evaluation workflows.
 
