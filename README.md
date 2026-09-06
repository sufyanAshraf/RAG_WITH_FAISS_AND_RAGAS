# RAG API

A minimal FastAPI project.

## Setup

The project-local `.venv` is configured for Python 3.13. Install dependencies with:

```powershell
.venv\Scripts\python.exe -m pip install -e .
```

Create a `.env` file in the project root and add your key:

```env
API_KEY=your-api-key
```

Never commit `.env` or put real keys in source code. Use `.env.example` as the template.

## Run

```powershell
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.
