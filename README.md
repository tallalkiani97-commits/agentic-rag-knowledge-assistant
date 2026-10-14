# Agentic RAG Knowledge Assistant

**A source-grounded AI knowledge assistant that retrieves relevant documents, plans a response, and returns cited evidence.**

This project demonstrates a practical AI engineering pattern: Retrieval-Augmented Generation (RAG) combined with an agent-style workflow. Instead of asking a language model to answer from memory, the assistant first searches a local knowledge base, selects relevant passages, and formats the response with source references.

## Why this project matters

Modern AI applications increasingly need to work with private, changing or domain-specific information. RAG addresses that need by separating the knowledge layer from the language model: documents are ingested and indexed, relevant context is retrieved at query time, and generation is grounded in that context.

This repository is intentionally transparent. The included baseline runs without a paid API and shows the retrieval and citation workflow clearly. An LLM provider can be added behind the `generate_answer` function later.

## Features

- Local Markdown knowledge base.
- Lightweight lexical retrieval baseline.
- Agent-style plan → retrieve → synthesize workflow.
- Source citations for every answer.
- Evidence snippets shown with the final response.
- Configurable top-k retrieval.
- Provider-agnostic generation boundary.
- Clear upgrade path to embeddings, vector databases and tool calling.

## Architecture

```text
Question
   ↓
Planner: identify search intent
   ↓
Retriever: score and rank document chunks
   ↓
Evidence pack: keep source path + matching passage
   ↓
Generator: synthesize only from retrieved evidence
   ↓
Answer + citations + evidence panel
```

A production version can replace the lexical retriever with embeddings and a vector database such as Qdrant or MongoDB Vector Search. The workflow still follows the same indexing → retrieval → generation pattern.

## Quick start

```bash
python3 app.py "What skills does Tallal use for AI projects?"
```

Try another query:

```bash
python3 app.py "Which projects use databases?"
```

No API key is required for the included grounded baseline.

## Example output

```text
Answer
Tallal's AI portfolio combines Python, TensorFlow, NLP, databases and web development.

Sources
[1] sample_docs/portfolio.md
```

## Project structure

```text
app.py                 # CLI entry point and agent-style workflow
rag_core.py            # chunking, retrieval and grounded synthesis
sample_docs/portfolio.md
requirements.txt       # optional production extensions
.env.example           # optional provider configuration
README.md              # project documentation
```

## Upgrade path

1. Replace lexical scoring with dense embeddings.
2. Persist vectors in Qdrant, MongoDB Vector Search or another vector store.
3. Add PDF ingestion and metadata-aware chunking.
4. Add an LLM adapter for natural-language synthesis.
5. Add tool calling for web search, calculators and structured data.
6. Add evaluation for retrieval recall, citation correctness and answer faithfulness.
7. Add observability traces and prompt/version management.

## Evaluation ideas

- **Retrieval precision:** how many returned chunks are relevant?
- **Retrieval recall:** did the system find the evidence needed to answer?
- **Citation coverage:** does each factual claim point to a source?
- **Faithfulness:** is the answer supported by the evidence pack?
- **Latency and cost:** how fast and efficiently does the assistant respond?

## Limitations

The baseline retriever uses token overlap rather than semantic embeddings. It is designed for clarity and offline execution, not production accuracy. A RAG system can still produce incorrect answers if retrieval is weak or the source data is incomplete, so evaluation and human review remain important for high-impact use cases.

## Tech stack

Python 3 · information retrieval · RAG architecture · agent workflows · citation-grounded generation

## References

- [LangChain Deep Agents RAG guide](https://docs.langchain.com/oss/python/deepagents/rag)
- [MongoDB Vector Search RAG tutorial](https://www.mongodb.com/docs/vector-search/tutorials/rag/)
- [Qdrant: Understanding RAG](https://qdrant.tech/articles/what-is-rag-in-ai/)

## Author

Built by **Tallal Kiani** as a modern AI engineering portfolio project.
