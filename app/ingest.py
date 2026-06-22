# ingest.py handles everything related to reading PDFs and storing them
# Think of it as the "librarian" — it reads your notes and files them away

from langchain_community.document_loaders import PyMuPDFLoader  # reads PDF files
from langchain_text_splitters import RecursiveCharacterTextSplitter  # splits text into chunks
from langchain_community.vectorstores import Chroma  # our vector database (stores embeddings)
from langchain_ollama import OllamaEmbeddings  # converts text into numbers (embeddings)
import os  # lets us work with files and folders

# this is the main folder where all course notes will be stored
BASE_DIR = "chroma_db"

def get_chroma_dir(course: str) -> str:
    """
    Returns the folder path for a specific course.
    e.g. "MAT136" -> "chroma_db/MAT136"
    Creates the folder if it doesn't exist yet.
    """
    path = os.path.join(BASE_DIR, course.strip().replace(" ", "_"))
    os.makedirs(path, exist_ok=True)  # exist_ok=True means don't crash if folder already exists
    return path

def ingest_pdf(pdf_path: str, course: str):
    """
    Takes a PDF file and a course name, then:
    1. Reads the PDF
    2. Splits it into small chunks
    3. Converts each chunk into embeddings (numbers that capture meaning)
    4. Saves everything into that course's folder
    """

    # Step 1: Load the PDF — PyMuPDF reads every page and gives us the text
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()

    # Step 2: Split into chunks
    # We can't feed a whole textbook to the AI at once — it has a memory limit
    # So we break it into 500-character pieces with 50-character overlap
    # The overlap makes sure we don't lose context at the edges of chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    # Step 3: Create embeddings and store them
    # Embeddings turn text into numbers — similar text gets similar numbers
    # This is what lets us search by meaning, not just keywords
    embeddings = OllamaEmbeddings(model="nomic-embed-text")  # separate model just for embeddings
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=get_chroma_dir(course),  # save to this course's folder
    )

    # Return how many chunks were created (we show this to the user in the UI)
    return len(chunks)

def load_vectorstore(course: str):
    """
    Opens an existing course's vector store from disk.
    Called when the user selects a course to chat with.
    """
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma(
        persist_directory=get_chroma_dir(course),  # load from this course's folder
        embedding_function=embeddings,
    )

def list_courses() -> list:
    """
    Returns a list of all courses that have been created.
    Just looks at what folders exist inside chroma_db/.
    """
    if not os.path.exists(BASE_DIR):
        return []  # no courses yet
    # os.listdir gives us all items in the folder
    # we filter to only include folders (not files)
    return [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]

def get_all_chunks(course: str, keyword: str = None) -> list:
    """
    Returns chunks from a course's vector store.
    If keyword is provided (e.g. "week 3"), it searches for relevant chunks.
    Otherwise returns a broad set of chunks.
    """
    vectorstore = load_vectorstore(course)
    query = keyword if keyword else "lecture notes concepts definitions examples"
    # k=100 pulls back as many chunks as possible
    results = vectorstore.similarity_search(query, k=100)
    return results

import json
from datetime import datetime

NOTES_DIR = "saved_notes"

def save_notes(course: str, title: str, content: str):
    """Save generated notes to disk."""
    course_notes_dir = os.path.join(NOTES_DIR, course)
    os.makedirs(course_notes_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{timestamp}_{title.replace(' ', '_')}.md"
    filepath = os.path.join(course_notes_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"# {title}\n*Generated on {timestamp}*\n\n{content}")
    return filepath

def list_notes(course: str) -> list:
    """Returns all saved notes for a course, newest first."""
    course_notes_dir = os.path.join(NOTES_DIR, course)
    if not os.path.exists(course_notes_dir):
        return []
    files = [f for f in os.listdir(course_notes_dir) if f.endswith(".md")]
    return sorted(files, reverse=True)  # newest first

def load_note(course: str, filename: str) -> str:
    """Loads a saved note by filename."""
    filepath = os.path.join(NOTES_DIR, course, filename)
    with open(filepath, "r") as f:
        return f.read()

def ingest_text_chunks(chunks: list, course: str):
    """
    Ingests a list of plain text strings into a course's vector store.
    Used for Notion data which comes as text, not PDFs.
    """
    from langchain_core.documents import Document

    # Convert plain text strings into LangChain Document objects
    documents = [Document(page_content=chunk) for chunk in chunks]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=get_chroma_dir(course),
    )

def ingest_csv(csv_path: str, course: str, source_name: str = ""):
    """
    Reads a CSV file and ingests each row as a text chunk.
    Used for Notion database exports.
    """
    import csv
    chunks = []
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # convert each row to readable text
            parts = []
            for key, value in row.items():
                if value and value.strip():
                    parts.append(f"{key}: {value.strip()}")
            if parts:
                chunks.append("\n".join(parts))
    
    if chunks:
        ingest_text_chunks(chunks, course)
    
    return len(chunks)