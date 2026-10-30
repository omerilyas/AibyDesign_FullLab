---
title: AI Foundations
description: "AI by Design Part 2: AI/ML fundamentals, tokenization, embeddings and vector databases, Gemini Embedding 2 multimodal retrieval."
chip: "Part 2 of 4"
headline: "AI Foundations: Tokens, Embeddings & Vectors"
standfirst: "Learn how AI reads language. Break text into tokens, turn meaning into vectors, store them in vector databases, and search across text, images and audio with Gemini Embedding 2."
meta:
  - label: SESSION
    value: Delivered by Omer Ilyas
  - label: STACK
    value: Python · Google Colab · Gemini
  - label: MODULES
    value: Modules 1 to 4
  - label: REVISION
    value: v3 · October 2026
links:
  - title: "Google Colab"
    url: https://colab.research.google.com
  - title: "Hugging Face"
    url: https://huggingface.co
  - title: "Webex Developer Portal"
    url: https://developer.webex.com
  - title: "LinkedIn · Omer Ilyas"
    url: https://www.linkedin.com/in/omerilyas4ccie/
---

## About this lab { #about data-toc-label="About this lab" }

In [Part 1](../index.md) you set up Google Colab, your Webex token and Room ID, and your API keys. In this part you learn the building blocks every Generative AI system relies on: how neural networks learn, how text becomes **tokens**, how meaning becomes **embeddings**, and how **vector databases** search them. You finish with **Gemini Embedding 2**, searching across text, images and audio in one vector space.

### Lab at a glance { #glance data-toc-label="Lab at a glance" }

<div class="glance build" markdown>

| | Module | What you do |
|---|---|---|
| 1 | [AI/ML Revolution Unveiled](#module-1) | Explore the foundations of AI and machine learning that power modern GenAI systems |
| 2 | [Tokenization](#module-2) | Understand how large language models break text into tokens and process language |
| 3 | [Embeddings and Vector Database](#module-3) | Represent meaning as vectors, build a vector store, and perform semantic search |
| 4 | [Gemini Embedding 2: Multimodal Retrieval](#module-4) | Explore Google's latest embedding models and multimodal retrieval techniques |

</div>

### How to use this guide { #how-to data-toc-label="How to use this guide" }

Each part of the lab lives on **one page**. Scroll down and work through it in order.

- The **TREE** on the left shows where you are. The progress bar under it fills up as you scroll.
- Press <kbd>J</kbd> / <kbd>K</kbd> to jump to the next or previous section.
- When you finish a task, click **Mark complete** at the end of it. You get a ✓ in the tree, and your progress is saved in this browser.
- Every code block has a **copy** button in its top-right corner. Paste the code into a new Colab cell and run it.
- Click any screenshot to zoom in.

### Key Vault and lab notes { #lab-notes data-toc-label="Key Vault and notes" }

Click **`$ keys`** (bottom-right) to open the **Key Vault**. Paste your Webex Bearer token, Webex Room ID, Hugging Face, LangChain, Pinecone, Gemini and Groq keys there once, and copy them from any page of the lab.

Click **Notes** (bottom-right) to open a scratchpad that stays with you on every part of the lab guide.

!!! warning "Where your keys and notes live"
    The Key Vault and the notes are saved **only in your browser** (localStorage on this device). They are **lost** if you clear your browser data, use a different browser or computer, or open the lab in a private window. On a shared machine, click **Clear All** in the Key Vault and **Clear** in the notes before you log out.

### Your lab proctor { #proctors data-toc-label="Your lab proctor" }

Need help? Raise your hand or reach out to me.

<div class="people" markdown>

<div class="person"><span class="nm">Omer Ilyas</span><span class="rl">Technical Marketing Engineer</span><span class="em">oilyas@cisco.com</span></div>

</div>
