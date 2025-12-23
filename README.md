# 📄 Multi-PDF RAG Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)

**Ask questions across multiple PDFs using AI**

</div>

---

## ✨ Features

- 📤 Upload multiple PDFs at once
- 🧠 AI-powered answers using GPT-4
- 🎯 Context-aware responses from your documents only
- ⚡ Fast semantic search with FAISS

## 🚀 Quick Start
```bash
# Clone repo
git clone https://github.com/moizishere-droid/Multi-PDF-RAG-Application.git
cd Multi-PDF-RAG-Application

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## 💡 Usage

1. Enter your OpenAI API key
2. Upload one or more PDFs
3. Ask questions about your documents
4. Get instant AI-powered answers

## 🏗️ How It Works
```
PDFs → Text Extraction → Chunking → Embeddings → Vector Store → Retrieval → LLM → Answer
```

## ⚙️ Configuration
```python
chunk_size=1000        # Text chunk size
chunk_overlap=200      # Chunk overlap
search_kwargs={"k": 4} # Retrieved chunks
temperature=0          # LLM creativity
```
---

<div align="center">

Made with ❤️ | ⭐ Star if helpful!

</div>
