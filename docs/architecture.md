# Architecture

```text
Approved archival sources
        ↓
Google Colab preparation
  - download approved PDFs
  - extract text / OCR when needed
  - clean preliminary pages
  - preserve metadata and source register
        ↓
Dify Knowledge Base
  - High Quality indexing
  - embeddings and vector index
  - Hybrid Search + qwen3-rerank
        ↓
Dify Chatflow
  Start → Knowledge Retrieval → LLM → Answer
        ↓
Published Dify Web App
```

The LLM receives the user question and the Knowledge Retrieval result through Dify's Context feature. It should generate a grounded answer with source references, or explicitly abstain when evidence is unavailable.
