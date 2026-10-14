# Lumora

[![CI](https://github.com/maheenniazi/lumora/actions/workflows/ci.yml/badge.svg)](https://github.com/maheenniazi/lumora/actions/workflows/ci.yml)

Chat with your own course notes using a local LLM and RAG pipeline. Upload any PDF — lecture slides, textbook chapters, your own notes — and ask it questions in plain English. It answers using only your material and shows you exactly which chunk it pulled from.

## Demo
<!-- Add a GIF here once you record one -->

## How it works

1. **Ingest** — Your PDF is chunked into 500-character segments and embedded using Ollama's embedding model
2. **Retrieve** — When you ask a question, the top 3 most semantically similar chunks are retrieved from ChromaDB
3. **Generate** — The chunks + your question are passed to a local Llama 3.2 model which generates a grounded answer
4. **Memory** — Conversation history is maintained so follow-up questions work naturally

## Tech stack

- [LangChain](https://langchain.com) — RAG orchestration
- [Ollama](https://ollama.ai) — Local LLM inference (Llama 3.2)
- [ChromaDB](https://trychroma.com) — Vector store
- [Streamlit](https://streamlit.io) — UI
- [PyMuPDF](https://pymupdf.readthedocs.io) — PDF parsing

## Setup

1. Install [Ollama](https://ollama.ai) and pull the model:
```bash
   ollama pull llama3.2
```
2. Clone the repo and install dependencies:
```bash
   git clone git@github.com:maheenniazi/lumora.git
   cd lumora
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
```
3. Run:
```bash
   ollama serve &
   PYTHONPATH=./app streamlit run app/ui.py
```

### Run with Docker

Docker Compose starts Lumora and an Ollama server together:

```bash
docker compose up -d --build
docker compose exec ollama ollama pull llama3.2
docker compose exec ollama ollama pull nomic-embed-text
```

Then open http://localhost:8501. Your courses and saved notes persist in `./chroma_db` and `./saved_notes`. To use the "generate notes" feature, set `ANTHROPIC_API_KEY` in your shell before running `docker compose up`.

## Development

```bash
pip install -r requirements-dev.txt
ruff check .
pytest
```

GitHub Actions runs linting and the test suite on every push and pull request, then builds the Docker image and smoke-tests it.

## Technical decisions

- **Local LLM over API** — No cost, no data leaves your machine, works offline
- **RAG over fine-tuning** — Grounding the model in your actual notes dramatically reduces hallucinations
- **ChromaDB** — Lightweight, file-based vector store, no separate server needed
- **Chunk overlap** — 50-character overlap between chunks prevents context being cut off at boundaries