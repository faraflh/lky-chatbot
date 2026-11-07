# Dify workflow evidence

The live Dify app is configured as a Chatflow:

```text
Start → Knowledge Retrieval → LLM → Answer
```

## Configuration

| Component | Setting |
|---|---|
| Knowledge Base | Lee Kuan Yew Archive |
| Chunking | General; `\\n\\n` delimiter; 1,000 characters; 120-character overlap |
| Index Method | High Quality |
| Retrieval | Hybrid Search + `qwen3-rerank`; Top K 3; score threshold off initially |
| LLM | GPT-4.1 mini |

## Export

If the Dify workspace exposes an **Export DSL** or **Download workflow** action, save the output in this directory as `lky-chatbot-workflow.yml` and commit it. Do not commit API keys, provider secrets, or Dify credentials.
