        # What Would Lee Kuan Yew Do?

An educational Retrieval-Augmented Generation (RAG) chatbot that helps users explore Lee Kuan Yew's documented perspectives on nation-building, leadership, economic development, multiracialism, and geopolitics.

The chatbot is implemented in Dify Cloud. It retrieves relevant passages from a curated knowledge base before generating an answer. It is a historically grounded simulation, **not** Lee Kuan Yew and not an authoritative historical source.

## Links

- Live Dify demo: https://udify.app/chat/ZNWDj15LtjXgtBGx
- Assessment workflow evidence: [`dify/README.md`](dify/README.md)
- Source manifest: [`data/source_manifest.csv`](data/source_manifest.csv)
- Evaluation plan: [`eval/README.md`](eval/README.md)

## Architecture

```text
Approved source documents
        ↓
Colab preparation: extract text, OCR if needed, clean, preserve metadata
        ↓
Dify Knowledge Base: chunking, embeddings, vector indexing, retrieval
        ↓
Dify Chatflow: Start → Knowledge Retrieval → LLM → Answer
        ↓
Source-grounded response
```

The active Dify configuration uses:

- Chunking: 1,000 characters with 120-character overlap
- Indexing: High Quality
- Search: Hybrid Search with `qwen3-rerank`
- Retrieval: top 3 chunks; score threshold initially disabled
- Generation model: GPT-4.1 mini through Dify Cloud

## Safety and scope

- The chatbot must not claim to be Lee Kuan Yew.
- It must not invent quotations, sources, events, dates, or views.
- It must not imply knowledge after March 2015.
- Current-events answers must be framed as historically grounded inference.
- When sources are insufficient, the chatbot must say so.

See [`docs/data-rights.md`](docs/data-rights.md) before adding source material. Full copyrighted books and unlicensed PDFs are intentionally excluded from this repository.

## Reproduce the project

1. Follow [`docs/setup-guide.md`](docs/setup-guide.md) to prepare and index approved source text.
2. Create a Dify Chatflow with `Start → Knowledge Retrieval → LLM → Answer`.
3. Copy [`dify/system-prompt.md`](dify/system-prompt.md) into the LLM System message.
4. Map LLM **Context** to the Knowledge Retrieval result and LLM **User** to `Start / query`.
5. Run the tests in [`eval/retrieval_test_questions.json`](eval/retrieval_test_questions.json).

## Repository contents

- `dify/`: prompt and workflow-export instructions
- `scripts/`: source-cleaning utility
- `data/`: metadata-only source manifest
- `eval/`: retrieval and response-quality evaluation materials
- `docs/`: architecture, setup, and data-rights documentation

## Licence

The project code and documentation may be reused under the MIT licence. Source texts retain their respective copyright and usage restrictions.
