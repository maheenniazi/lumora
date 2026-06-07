import streamlit as st
import tempfile, os
from ingest import ingest_pdf
from rag import build_rag_chain

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📚 AI Study Buddy")
st.caption("Upload your notes → ask anything")

# ── Sidebar: PDF upload ───────────────────────────────────────
with st.sidebar:
    st.header("Upload Notes")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

    if uploaded_file and st.button("Ingest PDF"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with st.spinner("Reading and embedding your notes..."):
            n_chunks = ingest_pdf(tmp_path)
        os.unlink(tmp_path)
        st.success(f"Done! Created {n_chunks} chunks.")
        st.session_state["ingested"] = True

# ── Main: Chat interface ──────────────────────────────────────
if "chain" not in st.session_state:
    st.session_state["chain"] = None

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if st.session_state.get("ingested") and st.session_state["chain"] is None:
    with st.spinner("Loading RAG chain..."):
        st.session_state["chain"] = build_rag_chain()

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if query := st.chat_input("Ask something about your notes..."):
    if st.session_state["chain"] is None:
        st.warning("Upload and ingest a PDF first using the sidebar.")
    else:
        # Show user message
        st.session_state["messages"].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)

        # Get answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                chain, retriever = st.session_state["chain"]
                sources = retriever.invoke(query)
                answer = chain.invoke(query)

            st.write(answer)

            # Show which chunks were cited
            with st.expander("📎 Source chunks used"):
                for i, doc in enumerate(sources):
                    st.markdown(f"**Chunk {i+1}** (page {doc.metadata.get('page', '?')})")
                    st.caption(doc.page_content[:300] + "...")

        st.session_state["messages"].append({"role": "assistant", "content": answer})