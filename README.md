<h1 align="center">📚 TalkDocs</h1>
<p align="center">
  <b>Chat with multiple PDFs using AI</b><br/>
  <i>Retrieval-Augmented Generation (RAG) powered document assistant</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-%23FF4B4B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq%20LLaMA3-0b7285?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" />
</p>

---

## 🌟 Overview

TalkDocs is a powerful PDF assistant that allows you to upload **multiple PDF documents** and chat with them in real-time. It uses **RAG (Retrieval-Augmented Generation)** to give you precise, context-aware answers.

> Ask questions. Get document-grounded answers. Instantly.

---

## ✨ Features

- 💬 Chat interface powered by **LLaMA 3.3 via Groq**
- 📁 Supports **multiple PDFs** at once
- ⚡ Fast semantic search with **FAISS**
- 🧠 Keeps chat **context** with memory
- 🧩 Modular codebase – easy to extend/customize
- 🎨 Beautiful Streamlit UI with chat avatars

---

## 🛠️ Tech Stack

| 🧩 Component        | 🔧 Tool / Library                      |
|--------------------|----------------------------------------|
| UI                 | Streamlit                              |
| PDF Parsing        | PyPDF2                                 |
| Text Splitting     | LangChain TextSplitter                 |
| Embedding Model    | HuggingFace (MiniLM-L6-v2)             |
| Vector Store       | FAISS                                  |
| LLM Backend        | Groq LLaMA 3.3                         |
| Memory             | LangChain ConversationBufferMemory     |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/TalkDocs.git
cd TalkDocs
```
### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt

```
### 4. Configure Environment
Create a ```.env``` file in the root directory with the following:
```bash
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING_v2=true
LANGSMITH_PROJECT=TalkDocs
LANGSMITH_ENDPOINT=https://api.langchain.plus
GROQ_API_KEY=your_groq_api_key
```
### ▶️ Run the App

```bash
streamlit run app.py
```
Then open your browser at http://localhost:8501

---
## 🖼️ Preview
<p align="center"> <img src="preview.png" width="95%" alt="TalkDocs Screenshot"/> </p>

---
## 📁 Project Structure
```bash
TalkDocs/
├── app.py                # Main Streamlit application
├── htmlTemplates.py      # UI styling and message HTML
├── requirements.txt      # Python package dependencies
├── .env.example          # Example environment variables
└── README.md             # Project documentation

```
## 📄 License
This project is licensed under the [MIT License](https://opensource.org/license/MIT).

---
<p align="center"> <b>Talk smarter with your documents – Use TalkDocs 🚀</b> </p>

---
