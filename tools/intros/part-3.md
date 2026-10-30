---
title: RAG
description: "AI by Design Part 3: context windows and RAG, RAG through Gemini File Search, multimodal RAG."
chip: "Part 3 of 4"
headline: "Retrieval Augmented Generation"
standfirst: "Ground LLM answers in your own data. Learn context windows, build a RAG pipeline, use Gemini File Search, and extend RAG to images."
meta:
  - label: SESSION
    value: Delivered by Omer Ilyas
  - label: STACK
    value: Python · Google Colab · Gemini
  - label: MODULES
    value: Modules 1 to 3
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

In [Part 2](../part-2/index.md) you turned text, images and audio into embeddings and searched them in vector databases. In this part you put that to work: you learn why **context windows** limit what an LLM can see, then build **Retrieval Augmented Generation (RAG)** pipelines that ground answers in real documents, first with your own vector store, then with Gemini's managed **File Search**, and finally with images in **Multimodal RAG**.

### Lab at a glance { #glance data-toc-label="Lab at a glance" }

<div class="glance build" markdown>

| | Module | What you do |
|---|---|---|
| 1 | [Context Windows and RAG](#module-1) | Build Retrieval Augmented Generation pipelines to ground LLM responses with real data |
| 2 | [RAG through File Search Tool](#module-2) | Use Gemini's managed File Search to build RAG pipelines without managing your own vector database |
| 3 | [Multimodal RAG](#module-3) | Go beyond text with vision models, image analysis, and multimodal retrieval |

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
