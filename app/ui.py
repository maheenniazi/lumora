# ui.py — everything the user sees and interacts with

import streamlit as st
import tempfile, os
from ingest import ingest_pdf, list_courses, get_all_chunks, save_notes, list_notes, load_note
from rag import build_rag_chain
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(page_title="Lumora", page_icon="🌙", layout="wide")

# ── Session State Setup ───────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state["messages"] = {}
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = {}
if "chain" not in st.session_state:
    st.session_state["chain"] = {}
if "view" not in st.session_state:
    st.session_state["view"] = "chat"  # either "chat" or "note"
if "current_note" not in st.session_state:
    st.session_state["current_note"] = None

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.title("🌙 Lumora")

    # Course creation
    st.header("📚 Courses")
    new_course = st.text_input("New course name (e.g. MAT136)")
    if st.button("Create Course") and new_course.strip():
        os.makedirs(f"chroma_db/{new_course.strip().replace(' ', '_')}", exist_ok=True)
        st.success(f"Course '{new_course}' created!")
        st.rerun()

    courses = list_courses()
    if courses:
        selected_course = st.selectbox("Select course", courses)
    else:
        selected_course = None
        st.info("Create a course above to get started.")

    st.divider()

    # PDF upload — only shown if a course is selected
    if selected_course:
        st.subheader(f"Upload to {selected_course}")
        uploaded_file = st.file_uploader("Choose PDFs", type="pdf", accept_multiple_files=True)
        if uploaded_file and st.button("Ingest PDFs"):
            total_chunks = 0
            with st.spinner("Reading and embedding your notes..."):
                for file in uploaded_file:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(file.read())
                        tmp_path = tmp.name
                    total_chunks += ingest_pdf(tmp_path, selected_course)
                    os.unlink(tmp_path)
            st.success(f"Done! Ingested {len(uploaded_file)} files, {total_chunks} total chunks.")
            if "chain" in st.session_state:
                del st.session_state["chain"]

    st.divider()

    # Saved notes history — shows all previously generated notes for this course
    if selected_course:
        st.subheader("📒 Saved Notes")
        saved = list_notes(selected_course)
        if saved:
            for note_file in saved:
                # clean up the filename for display
                display = note_file.replace("_", " ").replace(".md", "")
                if st.button(display, key=note_file):
                    st.session_state["current_note"] = load_note(selected_course, note_file)
                    st.session_state["view"] = "note"
                    st.rerun()
        else:
            st.caption("No saved notes yet. Generate some in the Notes tab!")

    st.divider()

    # Button to go back to chat from note view
    if st.button("💬 Back to Chat"):
        st.session_state["view"] = "chat"
        st.rerun()

# ── Stop if no course selected ────────────────────────────────
if not selected_course:
    st.info("Create and select a course in the sidebar to get started.")
    st.stop()

# ── Note View ─────────────────────────────────────────────────
# If user clicked a saved note, show it full screen
if st.session_state["view"] == "note" and st.session_state["current_note"]:
    st.markdown(st.session_state["current_note"])
    st.download_button(
        label="⬇️ Download as Markdown",
        data=st.session_state["current_note"],
        file_name=f"{selected_course}_notes.md",
        mime="text/markdown"
    )
    st.stop()  # don't show anything else

# ── Chat View ─────────────────────────────────────────────────
st.title(f"🌙 {selected_course}")

# Two tabs: Chat and Generate Notes
tab1, tab2 = st.tabs(["💬 Chat", "📝 Generate Notes"])

# ── Tab 1: Chat ───────────────────────────────────────────────
with tab1:

    # Build the RAG chain for this course if not already built
    if selected_course not in st.session_state["chain"]:
        try:
            st.session_state["chain"][selected_course] = build_rag_chain(selected_course)
            st.session_state["messages"][selected_course] = []
            st.session_state["chat_history"][selected_course] = []
        except Exception:
            st.warning("No notes ingested yet. Upload a PDF in the sidebar first.")
            st.stop()

    # Show all previous messages for this course
    for msg in st.session_state["messages"].get(selected_course, []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box at the bottom
    if query := st.chat_input(f"Ask anything about {selected_course}..."):
        msgs = st.session_state["messages"][selected_course]
        history = st.session_state["chat_history"][selected_course]
        chain, retriever = st.session_state["chain"][selected_course]

        msgs.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                sources = retriever.invoke(query)
                answer = chain.invoke({"question": query, "chat_history": history})
            st.markdown(answer)

            with st.expander("📎 Source chunks used"):
                for i, doc in enumerate(sources):
                    st.markdown(f"**Chunk {i+1}** (page {doc.metadata.get('page', '?')})")
                    st.caption(doc.page_content[:300] + "...")

        msgs.append({"role": "assistant", "content": answer})
        history.extend([HumanMessage(content=query), AIMessage(content=answer)])

# ── Tab 2: Generate Notes ─────────────────────────────────────
with tab2:
    st.subheader(f"Generate detailed notes for {selected_course}")
    st.caption("Be specific — e.g. 'Week 3 U-Substitution' pulls more relevant content than just 'week 3'")

    note_title = st.text_input(
        "What do you want notes on?",
        placeholder="e.g. Week 1 — Integration Intro, or Week 3 U-Substitution"
    )

    if st.button("✨ Generate Notes"):
        if not note_title.strip():
            st.warning("Please enter a topic before generating.")
        else:
            chunks = get_all_chunks(selected_course, keyword=note_title)
            if not chunks:
                st.warning("No notes found. Upload a PDF first.")
            else:
                # sort by page so content is in order
                chunks = sorted(chunks, key=lambda x: x.metadata.get("page", 0))

                # combine all chunks into one block — no batching
                all_text = "\n\n".join([
                    f"[Page {c.metadata.get('page', '?')}]\n{c.page_content}"
                    for c in chunks
                ])

                # cap at 12000 chars (fits in llama3.2 context window)
                all_text = all_text[:12000]

                llm = ChatOllama(model="llama3.2", temperature=0.1, num_ctx=8192)

                prompt = ChatPromptTemplate.from_messages([
                    ("system", """You are an expert academic note-taker for university students.
Create ONE set of detailed, well-organized study notes from ALL the lecture content below.
Do NOT repeat yourself. Each concept, example, and formula should appear exactly once.
Only use information from the lecture content — do not invent anything.
Preserve all math notation exactly as written.

FORMAT:
# {topic}

## 📌 Overview
What this lecture covers in 3-4 sentences.

## 📖 Key Definitions
- **Term**: definition (one per line)

## 🧠 Main Concepts
### [Concept Name]
Full explanation. Sub-points as bullets.

## 📐 Formulas & Theorems
- **Name**: exact formula or theorem statement

## ✏️ Worked Examples
### Example [n]: [brief description]
Step-by-step exactly as in the lecture.

## ⭐ Key Takeaways
- Most important points, no repetition

Lecture content:
{content}"""),
                    ("human", "Generate one complete set of study notes for: {topic}")
                ])

                with st.spinner("Generating notes... this takes 1-2 minutes ☕"):
                    response = (prompt | llm).invoke({
                        "content": all_text,
                        "topic": note_title
                    })
                    full_notes = response.content

                st.markdown("---")
                st.markdown(full_notes)

                save_notes(selected_course, note_title, full_notes)
                st.success("✅ Notes saved! Find them in the sidebar anytime.")

                st.download_button(
                    label="⬇️ Download Notes",
                    data=full_notes,
                    file_name=f"{note_title.replace(' ', '_')}.md",
                    mime="text/markdown"
                )