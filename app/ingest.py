from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os

CHROMA_DIR = "chroma_db"

def ingest_pdf(pdf_path: str):
    """Load a PDF, chunk it, embed it, and store in ChromaDB."""

    # 1. Load the PDF
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       # each chunk is ~500 characters
        chunk_overlap=50,     # chunks overlap by 50 chars so context isn't lost at edges
    )
    chunks = splitter.split_documents(documents)

    # 3. Embed and store in ChromaDB
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    return len(chunks)

def load_vectorstore():
    """Load an existing ChromaDB vectorstore from disk."""
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )