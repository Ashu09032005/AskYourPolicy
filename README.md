# PolicyQA – Smart Question Answering from PDF Insurance Documents

**PolicyQA** is an intelligent document assistant developed as part of **Bajaj HackRx 6** (Hackathon by Bajaj).  
It allows users to ask questions from lengthy insurance policy PDFs (e.g., Arogya Sanjeevani) and get precise answers – instantly.

This project reads the PDF, splits it into meaningful chunks, converts them to embeddings, and retrieves the most relevant answers using **FAISS**, a high-performance vector store for similarity search.


---

## 🔍 Key Features

- ✅ Extracts and preprocesses large policy PDFs
- 📄 Splits documents into semantically meaningful chunks
- 🔐 Uses **vector embeddings** to represent text
- ⚡ Uses **FAISS** for fast nearest-neighbor vector retrieval
- 🤖 Provides accurate, contextually relevant answers to user questions
- 🏷️ Handles medical, legal, and insurance-specific terminologies

---

## 🚀 How It Works

1. **PDF Parsing**  
   Reads and extracts raw text from policy PDFs.

2. **Chunking**  
   Splits the document into overlapping or clean segments to retain context. You can customize chunk size (e.g., 500 tokens).

3. **Embedding**  
   Each chunk is converted into a high-dimensional vector using a sentence-transformer or OpenAI embedding model.

4. **Indexing with FAISS**  
   Chunks are indexed in FAISS – a fast similarity search engine.

5. **QA via Vector Search**  
   When a user asks a question:
   - The question is embedded
   - Nearest chunks are retrieved from FAISS
   - A rule-based answer extractor forms the final answer

---

## 💡 What Makes PolicyQA Different

- **Insurance-Specific Optimization**  
  Tailored to read real policy PDFs (e.g., Arogya Sanjeevani), unlike generic document bots.

- **Chunking Strategy Matters**  
  Uses smart chunking to preserve legal clause context, avoiding out-of-context answers.

- **Performance-First with FAISS**  
  Outperforms traditional keyword-based QA using semantic search.

- **Modular Design**  
  Easily switch embedding models, chunking logic, or answer generation pipeline.

- **Scalable**  
  Can handle multi-page, multi-policy document collections with ease.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| PyMuPDF | PDF text extraction |
| FAISS | Vector similarity search |
| Transformers / Sentence Transformers | Text embeddings |
| Flask  | Backend framework for API endpoints |

---


