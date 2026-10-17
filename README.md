# 🌙 Lumora

**Chat with your own course notes, privately and on your own machine.**

Upload your lecture slides, textbook chapters or notes, then ask questions in plain English. Lumora answers **only from your material** and shows the chunks (with page numbers) it used for each answer. If the answer isn't in your notes, it says so instead of making something up.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C)
![Ollama](https://img.shields.io/badge/Ollama-Llama%203.2-000000)
![ChromaDB](https://img.shields.io/badge/ChromaDB-vector%20store-FF6F61)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit&logoColor=white)

---

## ✨ Features

- **📚 One space per course.** Each course (e.g. `MAT136`) gets its own vector store, so answers never mix subjects.
- **📄 PDF + CSV ingestion.** Drop in several PDFs at once. CSV exports, such as a Notion database, work too: each row becomes a searchable chunk.
- **💬 Grounded chat with memory.** Ask follow-up questions naturally, and open **📎 Source chunks used** to see exactly where an answer came from.
- **🛡️ Hallucination guardrail.** When the context doesn't cover your question, it replies *"I couldn't find that in your notes."*
- **📝 Study-note generator (optional).** Pick a topic ("Week 3 U-Substitution") and get structured notes: overview, definitions, concepts, formulas, worked examples and key takeaways. Notes are saved per course in `saved_notes/` and can be downloaded as Markdown.

## 🧠 How it works

```
 PDF / CSV ──► PyMuPDF ──► 500-char chunks (50 overlap) ──► nomic-embed-text ──► ChromaDB (per course)
                                                                                     │
 your question ──────────────────────────────► top-3 similar chunks ◄────────────────┘
                                                      │
                          chat history + chunks ──► Llama 3.2 (Ollama, temp 0.2) ──► answer + sources
```

1. **Ingest:** PDFs are parsed with PyMuPDF and split into 500-character chunks with a 50-character overlap, so ideas aren't cut off at chunk edges.
2. **Embed:** each chunk is embedded locally with Ollama's `nomic-embed-text` and stored in `chroma_db/<course>/`.
3. **Retrieve:** your question pulls the 3 most semantically similar chunks.
4. **Generate:** the chunks, your chat history and the question go to a local Llama 3.2 model, which is told to answer only from that context.

## 🚀 Getting started

**Prerequisites:** Python 3.10+ and [Ollama](https://ollama.com).

```bash
# 1. Pull the chat model and the embedding model
ollama pull llama3.2
ollama pull nomic-embed-text

# 2. Clone and install
git clone https://github.com/maheenniazi/lumora.git
cd lumora
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Run
ollama serve &            # skip if the Ollama app is already running
streamlit run app/ui.py
```

Then in the sidebar: **create a course → upload PDFs → Ingest → start asking.**

### Optional: note generation

The **📝 Generate Notes** tab uses the Claude API, because long notes need a bigger context window than Llama 3.2 has. Chat works fully offline without it.

```bash
pip install anthropic
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

## 📁 Project structure

```
app/
  ui.py        Streamlit app: courses, uploads, chat, note generator, saved notes
  ingest.py    PDF/CSV loading, chunking, embeddings, per-course Chroma stores, saved notes
  rag.py       Retrieval chain: retriever (k=3) → prompt → Llama 3.2 → answer
chroma_db/     local vector stores, one folder per course (git-ignored)
saved_notes/   generated notes, one folder per course
```

## 🧩 Design decisions

| Decision | Why |
|---|---|
| **Local LLM instead of an API** | It's free, it works offline, and your notes never leave your machine. |
| **RAG instead of fine-tuning** | Grounding answers in your actual notes reduces hallucinations, and new material works as soon as you upload it. |
| **ChromaDB** | A lightweight, file-based vector store with no separate server to run. |
| **One store per course** | Retrieval stays focused, so a calculus question never pulls in biology notes. |
| **Low temperature (0.2)** | Answers stay factual and close to the source. |

## 🗺️ Roadmap

- [ ] Record a demo GIF
- [ ] Support more file types (DOCX, slides)
- [ ] Run the note generator on a local model as well
