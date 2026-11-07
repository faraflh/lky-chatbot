# Setup guide

## 1. Prepare source text

Use the Colab notebook or `scripts/clean_book_text.py` to extract, clean, and review approved source text. Do not commit raw copyrighted source material to the public repository.

Example:

```bash
python scripts/clean_book_text.py raw_book.txt cleaned_book.txt --start-marker "[Page 12]"
```

## 2. Create a Dify Knowledge Base

Upload the approved cleaned text and use:

| Setting | Value |
|---|---|
| Chunk mode | General |
| Delimiter | `\\n\\n` |
| Maximum chunk length | 1,000 characters |
| Chunk overlap | 120 characters |
| Index method | High Quality |
| Search method | Hybrid Search |
| Reranker | `qwen3-rerank` |
| Top K | 3 |
| Score threshold | Disabled initially |

## 3. Build the Chatflow

Create and connect nodes as follows:

```text
Start → Knowledge Retrieval → LLM → Answer
```

Set the Knowledge Retrieval query input to `Start / query`.

In the LLM node:

- Set **Context** to `Knowledge Retrieval / result`.
- Insert Dify's Context variable into the System prompt.
- Set the User message to `Start / query`.
- Set model temperature near `0.2` and maximum output near 450 tokens.

Set the Answer node to output `LLM / text`.

## 4. Test and publish

Use the questions in [`../eval/retrieval_test_questions.json`](../eval/retrieval_test_questions.json). Inspect each Knowledge Retrieval Last Run result, then publish the app after the preview behaves as expected.
