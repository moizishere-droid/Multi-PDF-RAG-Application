# 📄 Multi‑PDF RAG Application (Streamlit)

**A Streamlit-based Retrieval-Augmented Generation (RAG) app** that lets you upload multiple PDFs and ask questions about their content. The AI answers **only using the uploaded PDFs**, making it ideal for document-focused Q&A.

---

## 🚀 Features

* **Streamlit Interface** – Easy-to-use web interface for uploading PDFs and querying them.
* **Multiple PDF Uploads** – Upload one or more PDFs to create a searchable knowledge base.
* **RAG (Retrieval-Augmented Generation)** – Uses LangChain and OpenAI embeddings to retrieve relevant chunks from PDFs and generate precise answers.
* **Context-Aware Responses** – The assistant answers **only using PDF content**. If the answer is not in the PDFs, it responds: `"I don't know."`
* **Chunked Document Processing** – PDFs are split into manageable chunks for better retrieval.
* **Vector Database** – Uses **FAISS** to store embeddings for fast semantic search.

---

## 💻 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/multi-pdf-rag.git
cd multi-pdf-rag
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 🔑 Usage

1. Enter your **OpenAI API key** in the input box.
2. Upload **one or more PDF files**.
3. Type a **question about the PDFs**.
4. Click **Enter** or press **Run**, and the AI will provide answers **based solely on the PDFs**.

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** – Web interface
* **LangChain** – RAG framework
* **OpenAI Embeddings** – Semantic search
* **FAISS** – Vector storage for fast retrieval
* **PyPDFLoader** – Load PDF content
* **RecursiveCharacterTextSplitter** – Split PDFs into chunks

---

## ✨ How It Works

1. **Upload PDFs** → Saved locally in `data/`.
2. **Load PDFs** → Using `PyPDFLoader`.
3. **Split text into chunks** → Using `RecursiveCharacterTextSplitter`.
4. **Create embeddings** → Using `OpenAIEmbeddings`.
5. **Store embeddings in FAISS** → Vector database for semantic search.
6. **Query PDFs** → User asks a question, retriever finds relevant chunks, LLM generates answer using context.

---

## 📌 Notes

* Answers are **strictly based on uploaded PDFs**.
* For large PDFs, embedding may take some time.
* The vectorstore is **in-memory**, so if the app restarts, you need to **re-upload PDFs**.

---

## 📸 Demo / Streamlit Link

Try the app live on **Streamlit**:
[**Open Multi‑PDF RAG on Streamlit**](https://share.streamlit.io/your-username/multi-pdf-rag/main/app.py)

*(Replace the link with your deployed Streamlit URL)*

---

## ✨ Future Improvements

* Persist vectorstore to disk for faster reloads.
* Support more document formats (Word, TXT).
* Improve UI/UX with file previews and upload progress.
* Multi-language PDF support.

 want me to do that?
