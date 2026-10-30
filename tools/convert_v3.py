"""Convert the AI by Design v3 guide (multi-page Material site) into this
site's four single-page parts.

V3 is read only. Each page becomes a module (`##`), each `???+ blank` box a
task (`###` with data-task, so lab.js adds "Mark complete"), and each
`??? info` panel directly inside a box a `####` sub-section. Everything else
(tabs, admonitions, code, images, HTML) is copied as is, minus the box
indentation. Asset paths and cross-page links are rewritten for the new pages.

    python3 tools/convert_v3.py [path/to/AIbyDesign-v3]

The page intros (hero, About, Lab at a glance...) live in tools/intros/.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V3 = Path(sys.argv[1] if len(sys.argv) > 1 else
          ROOT.parent.parent / "Roadshow" / "AIbyDesign-v3") / "docs"
INTROS = ROOT / "tools" / "intros"

# (v3 file, module number, title, TREE label)
PARTS = {
    "index.md": [
        ("overview", "0", "Understanding AI and Its Integration with Webex", "Overview"),
        ("Task1", "1", "Pre-Requisites and Setup", "Module 1 · Setup"),
    ],
    "part-2/index.md": [
        ("Task2", "1", "AI/ML Revolution Unveiled", "Module 1 · AI/ML"),
        ("Task3", "2", "Tokenization", "Module 2 · Tokenization"),
        ("Task4", "3", "Embeddings and Vector Database", "Module 3 · Embeddings"),
        ("Task4a", "4", "Gemini Embedding 2 Multimodal Retrieval", "Module 4 · Gemini Embedding 2"),
    ],
    "part-3/index.md": [
        ("Task5", "1", "Context Windows and RAG", "Module 1 · RAG"),
        ("Task5a", "2", "RAG through File Search Tool", "Module 2 · File Search"),
        ("Task6", "3", "Multimodal RAG", "Module 3 · Multimodal RAG"),
    ],
    "part-4/index.md": [
        ("Task9", "1", "GenAI Frameworks", "Module 1 · Frameworks"),
        ("Task10", "2", "Groq and Open Source Models", "Module 2 · Groq"),
        ("Task6b", "3", "Hugging Face with OpenAI-Compatible APIs", "Module 3 · Hugging Face"),
        ("conclusion", None, "Summary of Learning", "Wrap-up"),
    ],
}
MODULE_OF = {f: (page, num) for page, mods in PARTS.items() for f, num, _, _ in mods}
# V3 numbers modules 1-11 across the whole lab; each part here restarts at 1.
# From Tokenization (Part 2, Module 2) to the end, tabs are flattened (see untab).
UNTAB = {"Task3", "Task4", "Task4a", "Task5", "Task5a", "Task6", "Task9", "Task10", "Task6b", "conclusion"}
V3_NUMBER = {str(i): f for i, f in enumerate(
    ["Task1", "Task2", "Task3", "Task4", "Task4a", "Task5", "Task5a", "Task6", "Task9", "Task10", "Task6b"], 1)}
PART_NO = {page: i for i, page in enumerate(PARTS, 1)}


# Wording changes made for this guide, applied on top of the V3 text.
EDITS = [
    ("log in to the Webex App that is pre-installed on your laptop.",
     "log in to the Webex App that is pre-installed on your laptop. If your laptop doesn't have the Webex App, "
     'browse to <a href="https://web.webex.com" target="_blank">web.webex.com</a> and log in there with the same account.'),
    # Tokenization lab 2b: missing closing parenthesis in V3.
    ("print(len(text_splitter.create_documents([text]))\n", "print(len(text_splitter.create_documents([text])))\n"),
    ("* We will upgrade nltk to version 3.9.1", "* We will update nltk to version 3.10.4"),
    # Embeddings lab: sections 4-6 (Postman + SingleStore) are cut (see CUTS), so
    # Pinecone becomes section 4 and the text no longer refers to SingleStore.
    ("###### 7. Testing with Pinecone", "###### 4. Testing with Pinecone"),
    ("we will be using Chroma, and SingleStore for its ease of use",
     "we will be using Chroma and Pinecone for their ease of use"),
    ("So far, we used **SingleStore** to demonstrate the core idea behind vector storage and similarity search. "
     "We manually generated embeddings, saved them in a database, and queried them using similarity scoring.",
     "So far, we used **ChromaDB** to demonstrate the core idea behind vector storage and similarity search. "
     "We generated embeddings, stored them in a vector database, and queried them by similarity."),
    ("Instead of manually managing vectors in a SQL table, Pinecone is designed",
     "As a managed service, Pinecone is designed"),
    ("two different vector database solutions: SingleStore and Pinecone.",
     "two different vector database solutions: ChromaDB and Pinecone."),
    ("With SingleStore, we demonstrated how embeddings can be stored in a relational database and queried using vector similarity functions.",
     "With ChromaDB, we stored embeddings and queried them by similarity in just a few lines of code."),
    ("such as **SingleStore** and **Pinecone**", "such as **ChromaDB** and **Pinecone**"),
    ("along with extra information like the original text.\n",
     "along with extra information like the original text.\n\n"
     "!!! note \"What is an upsert?\"\n"
     "    `upsert()` is a command used to store a new vector or update an existing vector in the database. "
     "The name combines **update** and **insert**. If no vector with the given `id` exists, Pinecone inserts it. "
     "If one already exists, Pinecone replaces its values and metadata. "
     "This means you can run the same upsert again without creating duplicates.\n"),
    ('<p align="right"> 👉 This concludes the task. Click the <strong>"Context Windows and Retrieval Augmented Generation (RAG) "</strong> Task on the left. </p>\n',
     ""),
    ("    Click on the index in Pinecone to see your saved embeddings and their metadata.\n",
     "    With the above command, Pinecone creates a record with the ID `webexone-1`. The record holds the embedding "
     "vector, with the original text stored as metadata.\n\n"
     "    Click on the index in Pinecone to see your saved embeddings and their metadata.\n"),
    # Embeddings lab: explain why the ChromaDB query returns the stored sentence, not an answer.
    ("retrieved_results=db.similarity_search(query)\nprint(retrieved_results)\n```\n",
     "retrieved_results=db.similarity_search(query)\nprint(retrieved_results)\n```\n" + """
* You should see output like this:

```text
[Document(metadata={}, page_content='Welcome to the basics of GenAI created by Omer Ilyas.')]
```

!!! info "Why didn't it just answer 'Omer Ilyas'?"
    This is expected. At this stage we are only doing **retrieval**, not question answering. ChromaDB turns your question into an embedding, finds the stored document whose embedding is closest in meaning, and returns that document exactly as it was stored. A vector database finds and returns text. It does not read the text or write an answer.

**What we just built: retrieval**

<ol class="flow three">
  <li><b>Your question</b>Who created the basics of GenAI?</li>
  <li><b>Embedding + ChromaDB</b>Find the most similar documents</li>
  <li><b>Retrieved document</b>Welcome to the basics of GenAI created by Omer Ilyas.</li>
</ol>

To get a direct answer, you need a **large language model (LLM)** after retrieval. The LLM reads the retrieved document together with your question and writes the answer. Retrieval followed by generation is the foundation of **Retrieval Augmented Generation (RAG)**, which we add in a later module.

**Where we are going: retrieval + an LLM (RAG)**

<ol class="flow">
  <li><b>Question</b>Who created the basics of GenAI?</li>
  <li><b>ChromaDB</b>Retrieve the matching document</li>
  <li><b>LLM (GPT)</b>Read the document and answer</li>
  <li><b>Final answer</b>Omer Ilyas</li>
</ol>
"""),
    ("#### 1. Introduction\n\n\nIn the earlier sections of this lab, we explored how embeddings",
     "> **2026 UPDATE — IMPORTANT:** This lab now uses Google's stable **`gemini-embedding-2`** model, not "
     "`gemini-embedding-2-preview`. Gemini Embedding 2 became generally available in April 2026. The model supports "
     "text, images, audio, video, and PDFs in a *unified embedding space*. Its API **does not support the `task_type` "
     "parameter**. Google instead recommends task instructions in text-only retrieval inputs. We keep the model's "
     "default 3,072 dimensions throughout this exercise.\n\n"
     "#### 1. Introduction\n\n\nIn the earlier sections of this lab, we explored how embeddings"),
    ("Use your **personal Gmail account** to sign up and generate a key.\n",
     "Use your **personal Gmail account** to sign up and generate a key. Once you log in to AI Studio, "
     "click **Dashboard** to get your API key.\n"),
    ("###### Let's build a quick RAG application\n",
     "!!! important\n"
     '    Please open a new <a href="https://colab.research.google.com/" target="_blank">Google Colab</a> notebook '
     'for this section. Click on **"File" > "New notebook"**.\n\n'
     "###### Let's build a quick RAG application\n"),
    ('<p align="right"> 👉 This concludes the task. Click the <strong>"Multimodal RAG"</strong> Task on the left. </p>\n',
     ""),
    ("print(completion.choices[0].message)\n\n```\n",
     "print(completion.choices[0].message)\n\n```\n\n"
     '!!! important "Hugging Face API credits"\n'
     "    If you encounter the following error when running this exercise:\n\n"
     "    ```text\n"
     "    402: You have no remaining credits.\n"
     "    Purchase pre-paid credits to continue using Inference Providers.\n"
     "    ```\n\n"
     "    This means your Hugging Face account has exhausted its available inference credits. "
     "As some of the accounts used in this lab have been active for quite some time, their available credits "
     "may already have been consumed.\n\n"
     "    **What should you do?**\n\n"
     "    If you're using a shared or previously provided account, we recommend creating your own Hugging Face "
     "account using your **personal email address**. Please refer to "
     "[Part 1 · Task 1c: Huggingface Hub, Creating Account](../index.md#module-1c) for instructions on creating "
     "an account and generating your API token.\n\n"
     "    **Note:** A new free account may provide a limited inference allowance, subject to Hugging Face's "
     "current limits. Creating a new account does not guarantee sufficient credits for every exercise.\n\n"
     "    If you continue to experience credit limitations, you can move on to the next exercise.\n"),
    # The Ollama snippet is reference only; students don't run it.
    ("!!! note\n    We are using Chroma dB but you have options",
     '!!! optional "Optional: for reference only, you don\'t need to run this"\n    We are using Chroma dB but you have options'),
    ("    !!! important\n\n        ``` \n        # from langchain_community.embeddings import OllamaEmbeddings\n"
     "        # embeddings = OllamaEmbeddings()\n        ``` \n",
     "    ```py\n    # from langchain_community.embeddings import OllamaEmbeddings\n"
     "    # embeddings = OllamaEmbeddings()\n    ```\n"),
    # Task 4C (EmbeddingGemma 2 bonus lab) follows the end of Task 4B.
    ('<p align="right"> 👉 This concludes the task. Click the next **Task** on the left to continue. </p>\n',
     '<p align="right"> 👉 This concludes the task. Click the next **Task** on the left to continue. </p>\n'
     + (ROOT / "tools" / "embeddinggemma-lab.md").read_text()),
]

# The Gemini Embedding 2 lab steps are rewritten for the stable model; the new text replaces v3's steps.
REPLACE = [
    ("**Step 1 — Install Dependencies**\n",
     '<p align="right"> 👉 This concludes the task. Click the next **Task** on the left to continue. </p>',
     ROOT / "tools" / "gemini-lab.md"),
    ("#### Introduction\n\n\n#### 1. Introduction\n\n\n![CW](../assets/task5a/gem.png)",
     "**How Does This Compare to What We Built in Module 1?**",
     ROOT / "tools" / "file-search-intro.md"),
    ("**How Does This Compare to What We Built in Module 1?**",
     '??? info "Supported File Types (click to expand)"',
     ROOT / "tools" / "file-search-compare.md"),
    ("**Step 1 — Install Dependencies**\n",
     '<p align="right"> 👉 This concludes the task. Click the next **Module** on the left to continue.</p>',
     ROOT / "tools" / "file-search-lab.md"),
]

# Spans removed from the V3 text: from the start heading up to (not including) the end heading.
CUTS = [
    ("###### 4. Text to Vectors — via Postman", "###### 7. Testing with Pinecone"),
]


def cut(md):
    for start, end in CUTS:
        a = md.find(start)
        if a >= 0:
            md = md[:a] + md[md.index(end, a):]
    return md


def renumber(text, page, local=True):
    """`Module 5` in V3 prose -> this part's number, or `Part 2 · Module 4`."""
    def sub(m):
        target, num = MODULE_OF[V3_NUMBER[m.group(1)]]
        return f"Module {num}" if local and target == page else f"Part {PART_NO[target]} · Module {num}"
    return re.sub(r"\bModule (\d+)\b", lambda m: sub(m) if m.group(1) in V3_NUMBER else m.group(0), text)

FENCE = re.compile(r"^\s*(```|~~~)")
BOX = re.compile(r'^\?\?\?\+? blank "(.*)"\s*$')
TAB = re.compile(r'^\s*===[!+]? "(.*)"\s*$')
INFO = re.compile(r'^\?\?\?\+? info "(.*)"\s*$')
H1 = re.compile(r"^# (.*\S)\s*$")
EMOJI = re.compile(r"[\U0001F000-\U0001FFFF☀-➿️]")
FOOTER_HACK = re.compile(r"<div>\s*<script>.*?md-footer__inner.*?</script>\s*</div>\s*", re.S)


def indent(line):
    return len(line) - len(line.lstrip(" "))


def dedent(lines, n=4):
    return [l[min(n, indent(l)):] for l in lines]


def take_block(lines, i, n=4):
    """Lines after lines[i] that belong to the block opened there (indented
    at least n, blank, or inside a fence opened inside the block)."""
    body, fence = [], None
    j = i + 1
    while j < len(lines):
        l = lines[j]
        if fence is None and l.strip() and indent(l) < n:
            break
        m = FENCE.match(l)
        if m:
            fence = None if fence else m.group(1)
        body.append(l)
        j += 1
    while body and not body[-1].strip():
        body.pop()
    return body, j


def label(title):
    t = EMOJI.sub("", re.sub(r"^\d+\s*&nbsp;\s*", "", title)).strip()
    return re.sub(r"\s+", " ", t).replace('"', "'")


def unwrap_info(body):
    """Inside a box, turn top-level `??? info "X"` panels into #### X."""
    out, i = [], 0
    while i < len(body):
        m = INFO.match(body[i])
        if m and "click to expand" not in m.group(1):
            inner, i = take_block(body, i)
            out += [f"#### {m.group(1).strip()}", ""] + dedent(inner) + [""]
            continue
        if FENCE.match(body[i]):
            j = i + 1
            while j < len(body) and not FENCE.match(body[j]):
                j += 1
            out += body[i:j + 1]
            i = j + 1
            continue
        out.append(body[i])
        i += 1
    return out


def convert_module(src, num, title, toc, page):
    text = renumber(FOOTER_HACK.sub("", (V3 / f"{src}.md").read_text()), page, local=src != "conclusion")
    lines = text.split("\n")
    if num is None:
        out = ['<p class="eyebrow">Wrap-up</p>', "",
               f'## {title} {{ #wrap-up data-toc-label="{toc}" }}', ""]
    else:
        eyebrow = "Overview" if num == "0" else f"Module {num}"
        out = [f'<p class="eyebrow">{eyebrow}</p>', "",
               f'## {title} {{ #module-{num} data-toc-label="{toc}" }}', ""]
    task_ids = []
    seen_h1 = False
    i = 0
    while i < len(lines):
        l = lines[i]
        m = H1.match(l)
        if m:
            if seen_h1:
                out += [f"### {m.group(1)}", ""]
            seen_h1 = True
            i += 1
            continue
        m = BOX.match(l)
        if m:
            body, i = take_block(lines, i)
            n = len(task_ids) + 1
            tid = f"ov{n}" if num == "0" else f"{num}{chr(96 + n)}"
            task_ids.append(tid)
            heading = re.sub(r"^\d+\s*&nbsp;\s*", "", m.group(1)).strip()
            sub = "Overview" if num == "0" else f"Module {num}"
            out += [f'<p class="eyebrow sub">{sub} · Task {tid.upper()}</p>', "",
                    f'### {heading} {{ #module-{tid} data-toc-label="{tid} · {label(heading)}" data-task="{tid}" }}', ""]
            out += unwrap_info(dedent(body)) + [""]
            continue
        if FENCE.match(l):
            j = i + 1
            while j < len(lines) and not FENCE.match(lines[j]):
                j += 1
            out += lines[i:j + 1]
            i = j + 1
            continue
        out.append(l)
        i += 1
    if src in UNTAB:
        out = untab(out)
    md = rewrite(cut("\n".join(separate_rules(out))), page)
    if src == "conclusion":
        # V3's closing lines are white-on-dark inline styles: invisible in the light theme.
        head, sep, tail = md.rpartition("</pre>")
        md = head + sep + tail.replace("rgba(255,255,255,", "rgba(var(--ink-rgb),")
    return md, task_ids


def untab(lines, depth=0):
    """`=== "X"` tabs -> a heading per tab with its content underneath, so the
    page reads top to bottom. Nested tabs go one heading level deeper."""
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        m = TAB.match(l)
        if m:
            k = indent(l)
            body, i = take_block(lines, i, k + 4)
            out += [" " * k + "#" * min(4 + depth, 6) + " " + m.group(1).strip(), ""]
            out += untab([b[:k] + b[k:][min(4, indent(b[k:])):] if b.strip() else b for b in body], depth + 1) + [""]
            continue
        if FENCE.match(l):
            j = i + 1
            while j < len(lines) and not FENCE.match(lines[j]):
                j += 1
            out += lines[i:j + 1]
            i = j + 1
            continue
        out.append(l)
        i += 1
    return out


def separate_rules(lines):
    """A `---` right under a text line makes that line a setext <h2> (an empty
    TREE entry here); v3 meant a divider, so give it a blank line first."""
    out, fence = [], False
    for l in lines:
        if FENCE.match(l):
            fence = not fence
        if not fence and l.strip() == "---" and out and out[-1].strip():
            out.append(l[:indent(l)])
        out.append(l)
    return out


def rel(page, target):
    """Relative link from one part page to another (both are index.md files)."""
    if page == target:
        return ""
    up = "../" if "/" in page else ""
    return up + target


def rewrite(md, page):
    up = "../" if "/" in page else ""
    md = re.sub(r'(\]\(|src="|href=")(?:\./)?assets/', rf"\1{up}assets/", md)

    def link(m):
        name = m.group(2)
        target, num = MODULE_OF[name]
        anchor = "#wrap-up" if num is None else f"#module-{num}"
        return f"{m.group(1)}{rel(page, target)}{anchor}"
    md = re.sub(r"(\]\()(?:\./|\.\./)?(\w+?)(?:\.md|/)(?=\))", lambda m: link(m) if m.group(2) in MODULE_OF else m.group(0), md)

    def html_link(m):
        target, num = MODULE_OF[m.group(1)]
        url = "" if target == page else up + target.replace("index.md", "")
        return f'href="{url}#{"wrap-up" if num is None else f"module-{num}"}"'
    md = re.sub(r'href="(?:\./|\.\./)?(\w+?)(?:\.md|/)"', lambda m: html_link(m) if m.group(1) in MODULE_OF else m.group(0), md)
    # Images zoom with glightbox and load lazily, as in the reference guide.
    md = re.sub(r"(!\[[^\]]*\]\([^)\s]+\))(?!\{)", r"\1{ loading=lazy }", md)
    # The Key Vault button sits next to Notes (bottom-right), not under the rail.
    md = md.replace("bottom-left", "bottom-right")
    for old, new in EDITS:
        md = md.replace(old, new)
    for start, end, path in REPLACE:
        a, b = md.find(start), md.find(end)
        if a != -1 and b > a:
            md = md[:a] + path.read_text() + md[b:]
    return md


# The guide uses no long dashes. Sentences get a rewrite; labels ("Step 1 — Install") get a colon.
DASH_SENTENCES = [
    ("for us—it's", "for us. It's"),
    ("**2026 UPDATE — IMPORTANT:**", "**IMPORTANT 2026 UPDATE:**"),
    ("Click **Create new secret key** — the key is automatically generated",
     "Click **Create new secret key**. The key is automatically generated"),
    ("Save the API Key securely — you", "Save the API Key securely. You"),
    ("and more — and it can serve", "and more, and it can serve"),
    ("using a **CPU** — it is sufficient", "using a **CPU**. It is sufficient"),
    ("Apache 2.0 license — the first open models", "Apache 2.0 license. These are the first open models"),
    ("**openai/gpt-oss-20b** model — fast and", "**openai/gpt-oss-20b** model for fast and"),
    ("key — it’s required", "key. It’s required"),
    ("same results — but now", "same results, but now"),
    ("translates back — all through", "translates back, all through"),
    ("blocks are here — the use case", "blocks are here. The use case"),
    ("tokens and chunks — the first step", "tokens and chunks, the first step"),
    (" — and ", ", and "),
    ("| — |", "| None |"),
    ("15 – 20", "15 to 20"),
    ("Language–Image", "Language-Image"),
    ("Modules 1 – ", "Modules 1 to "),
]


def undash(md):
    for old, new in DASH_SENTENCES:
        md = md.replace(old, new)
    md = md.replace(" — ", ": ")
    left = [l for l in md.splitlines() if "—" in l or "–" in l]
    if left:
        sys.exit("long dash left in the guide:\n" + "\n".join(left))
    return md


def main():
    for page, mods in PARTS.items():
        intro = (INTROS / (page.replace("/index.md", "") .replace("index.md", "part-1") + ".md")).read_text()
        chunks = [intro.rstrip()]
        for src, num, title, toc in mods:
            md, _ = convert_module(src, num, title, toc, page)
            chunks.append(md.rstrip())
        outro = INTROS / (page.replace("/index.md", "").replace("index.md", "part-1") + ".next.md")
        if outro.exists():
            chunks.append(outro.read_text().rstrip())
        dst = ROOT / "docs" / page
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(undash("\n\n\n".join(chunks)) + "\n")
        print("wrote", dst.relative_to(ROOT))


if __name__ == "__main__":
    main()
