# Multi-User RAG

🌐 **Multi-User RAG** is a versatile and scalable platform that enables users to interact with a Retrieval-Augmented Generation (RAG) system. It is deployed on [Streamlit Cloud](https://multi-user-rag.streamlit.app/) to provide a seamless user experience for document uploads, data processing, and intelligent querying.

---

## 🚀 Features

- **Multi-User Support**: Simultaneous interactions for multiple users.
- **Session Management**:
  - Uses **Gemini** and **PostgreSQL** for session handling and user tracking.
  - Prisma ORM for seamless database operations.
- **Document Handling**:
  - Upload and process `.pdf`, `.docx`, `.html`, and image files.
  - Automatic text extraction using OCR for images.
- **Efficient Data Retrieval**:
  - Embedded document vectors for fast and accurate querying.
  - Integration with **ChromaDB** for vector storage and retrieval.
- **Real-Time Interaction**:
  - Instant feedback and results through Streamlit's interactive UI.

---

## 📖 How It Works

1. **Upload a Document**: Users can upload files in supported formats.
2. **Process the Document**:
   - Text is extracted and split into manageable chunks.
   - Embeddings are created for each chunk.
   - Data is indexed into the vector database.
3. **Query the Document**: Users can input queries, and the RAG system retrieves relevant information.

---

## 💡 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, FastAPI (optional for API integration)
- **Session Management**: Gemini and PostgreSQL
- **ORM**: Prisma
- **Database**: ChromaDB (for vector storage)
- **Text Extraction**: PyPDFLoader, Docx2txtLoader, UnstructuredHTMLLoader, pytesseract (for OCR)
- **Embedding Model**: OpenAI, Hugging Face, or custom embedding models

---

## 🌈 Key Highlights

- ⚡ **Fast and Scalable**: Optimized for real-time performance.
- 📂 **Flexible Document Types**: Handles PDFs, Word documents, HTML files, and images.
- 🔍 **Intelligent Search**: Combines text embeddings and metadata for precise results.
- 🔒 **Secure and Reliable**: Built with multi-user concurrency in mind.

---

## 📋 How to Use

1. Visit the live app: [multi-user-rag.streamlit.app](https://multi-user-rag.streamlit.app/).
2. Upload a document in any of the supported formats.
3. Enter a query related to the uploaded document.
4. View instant, intelligent results based on the document content.

---

## 📦 Installation (For Local Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/multi-user-rag.git
   cd multi-user-rag
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

---

## 💡 Future Improvements

- 🔧 Add advanced query filtering and summarization.
- 📊 Visualize document embeddings and query results.
- 🌍 Support multilingual documents.

---

## 🧑‍💻 Contributors

- [Your Name](https://github.com/your-profile)

---

## 📝 License

This project is licensed under the MIT License.

---

<div align="center">
    <h3>🌟 Thank you for using Multi-User RAG! 🌟</h3>
</div>
