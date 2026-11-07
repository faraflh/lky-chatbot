# Evaluation

Run each question in `retrieval_test_questions.json` through the Dify Preview and published web app.

## Retrieval metric

For answerable questions, inspect the Knowledge Retrieval node's Last Run output.

```text
Recall@3 = questions where the expected topic/source appears in the top 3 results
           ----------------------------------------------------------------------
                              total answerable questions
```

## Response-quality rubric

Score every response from 1 (poor) to 5 (excellent):

| Criterion | What to check |
|---|---|
| Grounding | Claims are supported by retrieved passages. |
| Retrieval relevance | Retrieved passages address the question. |
| Citation accuracy | The named source supports the answer. |
| Historical boundary | No claim of knowledge after March 2015. |
| Safe abstention | Unsupported questions are not answered with invented facts. |

Record the test date, question, retrieved sources, response, score, and notes in a spreadsheet or issue tracker.
