FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install the CPU-only build of PyTorch first so the image doesn't pull
# several GB of CUDA libraries the app never uses, then the pinned deps.
COPY requirements.txt .
RUN pip install --index-url https://download.pytorch.org/whl/cpu torch==2.12.0 \
 && pip install -r requirements.txt

COPY app/ ./app/

# The app imports its modules as top-level (e.g. `from ingest import ...`)
ENV PYTHONPATH=/app/app \
    OLLAMA_HOST=http://ollama:11434

EXPOSE 8501

CMD ["streamlit", "run", "app/ui.py", "--server.address=0.0.0.0", "--server.port=8501"]
