---
name: awesome-llm-apps
description: Architecture guide, template selector, and implementation cookbook for building production-grade LLM applications and AI Agents based on patterns from Shubham Saboo's awesome-llm-apps repository. Use when building RAG systems, multi-agent workflows, autonomous agents, or LLM-powered tools.
---

# Awesome LLM Apps & AI Agents Architecture Guide

This skill provides templates, architectural blueprints, and best practices for building real-world AI applications inspired by the curated collection from **Shubham Saboo's `awesome-llm-apps`**.

---

## 1. Application Archetypes & Pattern Selection

When designing an LLM-powered application, identify the correct architecture pattern first:

| Pattern | Best For | Typical Stack | Complexity |
| :--- | :--- | :--- | :--- |
| **Simple Prompt + Tool Calling** | Single-turn Q&A, calculator, API lookups | OpenAI / Gemini SDK, LiteLLM | Low |
| **Classic RAG** | Answering questions from private docs, manuals, PDFs | LangChain / LlamaIndex, Chroma / FAISS / Qdrant, BGE / OpenAI embeddings | Low-Medium |
| **Agentic / Corrective RAG (CRAG)** | Ambiguous queries requiring document grading, web fallback, query rewrite | LangGraph, LlamaIndex, Tavily / Serper | Medium |
| **Autonomous Multi-Agent Workflow** | Multi-step research, report generation, complex coding | CrewAI, LangGraph, AutoGen | Medium-High |
| **Multimodal Agents** | Document understanding (diagrams, tables), video/audio analysis | Gemini 1.5/2.0, Whisper, PyMuPDF | Medium |
| **Local Private LLM App** | Offline usage, strict data privacy, enterprise on-prem | Ollama, vLLM, LangChain, Chroma | Low-Medium |

---

## 2. Standard Project Structure for LLM Apps

Follow this isolated, modular structure for any new LLM application:

```text
my-llm-app/
├── app.py                # UI (Streamlit, Gradio, or FastAPI)
├── agent.py              # Core agent / graph definition and orchestration
├── tools/                # Custom deterministic tools (search, calculators, APIs)
│   ├── search_tools.py
│   └── custom_tools.py
├── rag/                  # Ingestion, chunking, indexing, and retriever logic
│   ├── ingest.py
│   └── retriever.py
├── config.py             # Model selection, temperature, API keys, env vars
├── requirements.txt      # Pinned dependencies
└── .env.example          # Sample environment variables
```

---

## 3. Implementation Recipes

### Recipe A: Agentic RAG with Self-Correction (LangGraph)
1. **Retrieve**: Fetch relevant chunks from vector store.
2. **Grade Documents**: Evaluates relevance. If irrelevant, rewrite query or trigger Web Search.
3. **Generate**: Synthesize answer strictly using supported citations.
4. **Hallucination Check**: Verify that answer is grounded in context before returning to user.

### Recipe B: Collaborative Multi-Agent Team (CrewAI)
1. **Define Agents**: Assign clear roles, backstories, and goal definitions.
   - Example: *Researcher* (gathers info) $\rightarrow$ *Analyst* (synthesizes findings) $\rightarrow$ *Writer* (formats final markdown/report).
2. **Define Tasks**: Specify inputs, expected outputs, and assigned agent.
3. **Execution**: Run sequentially or hierarchically with a manager LLM.

### Recipe C: Local Offline RAG (Ollama + Streamlit)
1. Pull model: `ollama run llama3.2` or `mistral`.
2. Ingest documents into ChromaDB using local HuggingFace embeddings (`all-MiniLM-L6-v2` or `bge-small`).
3. Connect local LLM via `langchain-ollama` or native Ollama API.
4. Serve via lightweight Streamlit or FastHTML interface.

---

## 4. Production Engineering Best Practices

- **Strict Schema Outputs**: Use Pydantic or structured outputs (`response_format={"type": "json_object"}`) whenever agents output data to downstream code.
- **Fail-Safe Tool Execution**: Always wrap tool calls in `try/except` blocks returning a descriptive string message so the model can self-correct instead of crashing.
- **Cost & Token Monitoring**: Track input/output tokens and latency per step.
- **Prompt Injection Defense**: Treat untrusted document input as data, never as system instructions.
