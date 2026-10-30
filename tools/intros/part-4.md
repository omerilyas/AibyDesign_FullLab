---
title: Frameworks and Models
description: "AI by Design Part 4: GenAI frameworks (LangChain), Groq and open-source models, Hugging Face with OpenAI-compatible APIs."
chip: "Part 4 of 4"
headline: "GenAI Frameworks & Open Models"
standfirst: "Build with the frameworks and models behind real AI apps: LangChain use cases with Webex, Groq's LPU engine with open-source models, and Hugging Face through OpenAI-compatible APIs."
meta:
  - label: SESSION
    value: Delivered by Omer Ilyas
  - label: STACK
    value: Python · LangChain · Groq · Hugging Face
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

In [Part 3](../part-3/index.md) you built RAG pipelines. In this last part you meet the frameworks and model providers developers use to ship AI apps: **LangChain** use cases with Webex, **Groq**'s high-speed LPU engine with open-source models, and **Hugging Face** models through **OpenAI-compatible APIs**. The lab ends with a summary of everything you learned.

### Lab at a glance { #glance data-toc-label="Lab at a glance" }

<div class="glance build" markdown>

| | Module | What you do |
|---|---|---|
| 1 | [GenAI Frameworks](#module-1) | Explore popular GenAI frameworks for building AI-powered applications at scale |
| 2 | [Groq and Open Source Models](#module-2) | Use Groq's high-speed LPU engine with open-source models like GPT-OSS for cost-free inference |
| 3 | [Hugging Face and OpenAI-Compatible APIs](#module-3) | Use Hugging Face models with OpenAI-compatible endpoints for flexible integration |

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
