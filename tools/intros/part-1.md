---
title: Overview and Setup
description: "AI by Design Part 1: Responsible AI, the evolution of AI at Cisco, and lab setup (Webex token, Google Colab, Hugging Face, LangChain, Ollama)."
chip: "Part 1 of 4"
headline: "AI by Design"
standfirst: "Frameworks, Tools & Innovation. A hands-on lab exploring Generative AI and Collaboration integration, from tokenization and embeddings to RAG, multimodal AI, and beyond."
meta:
  - label: SESSION
    value: Delivered by Omer Ilyas
  - label: STACK
    value: Webex · Google Colab · Hugging Face
  - label: MODULES
    value: Overview · Module 1
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

<p class="tagline"><del>From using AI</del> <span>to understanding how it is built.</span></p>

In this hands-on lab you go through the fundamental concepts of AI, the techniques behind Generative AI, and how AI can be integrated with Collaboration to create efficient workflows. You start with Cisco's approach to Responsible AI and the evolution of AI at Cisco, set up your lab tools, and then build your way up from tokenization and embeddings to RAG, multimodal AI, GenAI frameworks and open-source models.

The lab has four parts, one page each. This page is **Part 1**: the overview and your lab setup.

### Lab at a glance { #glance data-toc-label="Lab at a glance" }

<div class="glance build" markdown>

| | Module | What you do |
|---|---|---|
|  | [Overview](#module-0) | Responsible AI, the evolution of AI at Cisco, roadmap, and the lab overview |
| 1 | [Pre-Requisites and Setup](#module-1) | Set up your lab environment, API keys, Python tooling, and verify connectivity |

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
