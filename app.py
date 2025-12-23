import os
import streamlit as st

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Streamlit setup to Display
st.set_page_config(page_title="Multi‑PDF RAG", layout="wide")
st.title("📄 Multi‑PDF RAG Application")

# API Key setup
api_key = st.text_input("Enter OpenAI API Key", type="password")
if not api_key:
    st.warning("API key required")
    st.stop()
os.environ["OPENAI_API_KEY"] = api_key


# Multiple File uploads
uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type="pdf",
    accept_multiple_files=True
)
if not uploaded_files:
    st.info("Upload PDFs to begin")
    st.stop()


# Save PDFs for Query
os.makedirs("data", exist_ok=True)
pdf_paths = []

for file in uploaded_files:
    path = os.path.join("data", file.name)
    with open(path, "wb") as f:
        f.write(file.getbuffer())
    pdf_paths.append(path)


# Load documents
documents = []
for path in pdf_paths:
    loader = PyPDFLoader(path)
    documents.extend(loader.load())


# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)


# Embeddings + Vector Store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})


# Prompt
prompt = ChatPromptTemplate.from_template(
    """
You are a precise assistant.
Answer ONLY using the context below.
If the answer is not in the context, say "I don't know.".

Context:
{context}

Question:
{question}
"""
)


# LLM
llm = ChatOpenAI(temperature=0)


# RAG Chain (Runnable-based)
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

# User Query
question = st.text_input("Ask a question about the PDFs")

if question:
    with st.spinner("Thinking..."):
        answer = rag_chain.invoke(question)
    st.markdown("### Answer")
    st.write(answer)