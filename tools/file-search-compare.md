**How Does This Compare to What We Built Earlier?**

In Module 1, we built our own RAG pipeline using LangChain, ChromaDB, and OpenAI.

That gave us control over the different components. With Gemini File Search, Google manages those components for us.

| Component | DIY RAG (Module 1) | Gemini File Search |
|---|---|---|
| **Document chunking** | Configure a text splitter | Automatically handled, with some configuration options |
| **Embeddings** | Select and call an embedding model | Generated automatically |
| **Vector database** | Configure ChromaDB or Pinecone | Managed internally by Google |
| **Retrieval** | Implement similarity search or a retriever | Managed by File Search |
| **LLM integration** | Connect retrieval to the LLM | Gemini retrieves and generates responses |
| **Infrastructure** | You manage the components | Google manages the retrieval infrastructure |
| **Flexibility** | Greater control and customisation | Simpler setup with less control |

!!! important
    Gemini File Search does **not** replace traditional RAG architectures. It provides another way to build RAG applications, particularly when we want to reduce complexity.

**What's New? Multimodal File Search**

Google has extended File Search to support **Gemini Embedding 2**.

This means File Search can work with text and supported image/multimodal content using a shared embedding space.

For example, imagine uploading a hotel brochure containing descriptions and photographs. A user could ask a question about the hotel's facilities, and the system could retrieve relevant information from the indexed content.

!!! note
    Although the standalone Gemini Embedding 2 model supports text, images, audio, video and PDFs, Gemini File Search currently does **not** support audio or video file formats.

**Why Use Gemini File Search?**

* **Simplicity**: upload documents, let Google index them, and ask questions.
* **No external vector database**: Google manages the searchable index.
* **Managed retrieval**: no need to implement your own vector similarity search.
* **Grounded responses**: Gemini can use retrieved content and provide source citations.
* **Faster development**: spend more time building your application and less time configuring retrieval infrastructure.

**Pricing and Supported Models**

Gemini File Search supports multiple Gemini models, including models in the **Gemini 3** and **Gemini 4** families. Availability depends on the model and API.

File Search also supports two embedding models:

* `gemini-embedding-001`: text-focused embeddings
* `gemini-embedding-2`: multimodal embeddings

| Component | Pricing |
|---|---|
| File Search storage | Free |
| Query-time embeddings | Free |
| Initial indexing with Gemini Embedding 001 | $0.15 per 1 million tokens (paid tier) |
| Initial text indexing with Gemini Embedding 2 | $0.20 per 1 million tokens (paid tier) |
| Retrieved context and answer generation | Charged according to the selected Gemini model |

!!! info "Prices may change"
    These are published rates as of October 2026 and may change. Check Google's official <a href="https://ai.google.dev/gemini-api/docs/pricing" target="_blank">pricing page</a> before deploying production applications. See also: <a href="https://ai.google.dev/gemini-api/docs/tokens" target="_blank">Token info</a>.

!!! tip "Key takeaway"
    **DIY RAG gives us control. Gemini File Search gives us simplicity.**

    Both approaches use the same fundamental concept: retrieving relevant information and providing it to an LLM to generate an answer. The main difference is **who manages the retrieval pipeline**.

In the next exercise, we'll create our own File Search store, upload a document, and ask Gemini questions about its contents.

