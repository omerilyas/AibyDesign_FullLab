#### Introduction

In the previous modules, we learned how embeddings work, how to store them in vector databases such as **ChromaDB** and **Pinecone**, and how to retrieve relevant information using semantic search.

We also explored **Gemini Embedding 2** and **EmbeddingGemma 2** to understand how embeddings can work across different types of content and run either in the cloud or locally.

Now we're going to explore another approach: **Gemini File Search**, Google's fully managed Retrieval-Augmented Generation (RAG) service.

![CW](../assets/task5a/gem.png){ loading=lazy }

**What is Gemini File Search?**

Google's <a href="https://ai.google.dev/gemini-api/docs/file-search" target="_blank">File Search Tool</a> is a **fully managed RAG service** integrated into the Gemini API.

Instead of building and maintaining the entire RAG pipeline yourself, you upload your documents to a **File Search store**, and Google handles much of the underlying processing automatically.

This includes:

* Splitting documents into smaller chunks
* Generating embeddings
* Indexing and storing searchable information
* Retrieving relevant content when a question is asked
* Providing that information to the Gemini model to generate grounded answers

![ToolG](../assets/task5a/searTool.png){ loading=lazy }

!!! tip "In simple terms"
    You provide the knowledge, ask questions, and Gemini handles the retrieval process.

