from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage
from ingest import load_vectorstore

def build_rag_chain():
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    llm = ChatOllama(model="llama3.2", temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful study assistant. Answer the question using only the context below.
If the answer isn't in the context, say "I couldn't find that in your notes."

Context:
{context}"""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_with_history(input_dict):
        docs = retriever.invoke(input_dict["question"])
        context = format_docs(docs)
        return prompt | llm | StrOutputParser()

    chain = (
        RunnablePassthrough.assign(context=lambda x: format_docs(retriever.invoke(x["question"])))
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain, retriever