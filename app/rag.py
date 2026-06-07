# rag.py builds the actual question-answering chain
# RAG = Retrieval Augmented Generation
# meaning: retrieve relevant notes, then generate an answer using them

from langchain_ollama import ChatOllama  # the local AI model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder  # structures the prompt
from langchain_core.output_parsers import StrOutputParser  # converts AI output to plain text
from langchain_core.runnables import RunnablePassthrough  # passes data through the chain unchanged
from langchain_core.messages import HumanMessage, AIMessage  # message types for chat history
from ingest import load_vectorstore  # our function to load a course's notes

def build_rag_chain(course: str):
    """
    Builds the full RAG pipeline for a given course.
    Returns the chain (for answering) and the retriever (for finding source chunks).
    """

    # Load this course's vector store from disk
    vectorstore = load_vectorstore(course)

    # The retriever is what searches your notes
    # k=3 means it finds the 3 most relevant chunks for each question
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # The LLM is the actual AI model that generates answers
    # temperature=0.2 means low creativity — we want factual, grounded answers
    llm = ChatOllama(model="llama3.2", temperature=0.2)

    # The prompt is the instruction we give the AI before every question
    # It tells the AI: only use the context (your notes), and remember the conversation
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful study assistant. Answer the question using only the context below.
If the answer isn't in the context, say "I couldn't find that in your notes."

Context:
{context}"""),
        MessagesPlaceholder(variable_name="chat_history"),  # inserts conversation history here
        ("human", "{question}"),  # the user's current question goes here
    ])

    # Helper function to combine multiple chunks into one block of text
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # This is the full chain — it runs left to right:
    # 1. Take the input (question + chat history)
    # 2. Retrieve relevant chunks and add them as "context"
    # 3. Feed everything into the prompt template
    # 4. Send to the LLM
    # 5. Parse the output as a plain string
    chain = (
        RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"])))
        | prompt
        | llm
        | StrOutputParser()
    )

    # Return both the chain and retriever
    # We need the retriever separately to show the source chunks in the UI
    return chain, retriever