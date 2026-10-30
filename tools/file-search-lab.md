**Step 1: Install dependencies**

Run this in a Colab code cell:

```py
%pip install -q google-genai
```

!!! tip "What just happened?"
    We installed the Python SDK used to communicate with the Gemini API. The Gemini model itself is not being downloaded to Colab.

!!! warning "Dependency warning"
    Colab may display a `google-auth` version conflict during installation. That warning does not necessarily mean the SDK failed. Try Step 2 before reinstalling packages. Avoid repeatedly upgrading or downgrading dependencies if imports work.

---

**Step 2: Import libraries and configure the Gemini API key**

```py linenums="1"
from google.colab import userdata
from google import genai
from google.genai import types
import os
import time

api_key = userdata.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Add GEMINI_API_KEY in Colab Secrets and enable notebook access.")

client = genai.Client(api_key=api_key)
MODEL = "gemini-2.5-flash"  # Tested with generate_content() in this lab

print("✅ Gemini client ready")
print("🤖 Generation model:", MODEL)
```

!!! tip "What just happened?"
    We created an authenticated Gemini client without displaying the API key. `MODEL` is the generation model used to answer questions. The File Search index has its own embedding configuration.

---

**Step 3: Create or reuse a File Search store**

A **File Search store** is a persistent, server-side collection of indexed document content. We use a distinctive name for this exercise and reuse an existing matching store after a Colab restart.

```py linenums="1"
STORE_DISPLAY_NAME = "Omers-DECT-Task5A"

matching_stores = [
    store for store in client.file_search_stores.list()
    if store.display_name == STORE_DISPLAY_NAME
]

if matching_stores:
    file_search_store = matching_stores[0]
    print("♻️ Reusing existing store")
else:
    file_search_store = client.file_search_stores.create(
        config={"display_name": STORE_DISPLAY_NAME}
    )
    print("✅ Created a new store")

file_search_store_name = file_search_store.name
print("Store display name:", file_search_store.display_name)
print("Store resource ID:", file_search_store_name)

if len(matching_stores) > 1:
    print("⚠️ Multiple stores share this display name; using the first one.")
```

!!! tip "What just happened?"
    The API assigned a resource name such as `fileSearchStores/...`. We don't manually copy or hard-code this ID. A display name is not guaranteed to be unique across stores, so the code warns you if multiple matches exist.

!!! info "Embedding-model choice"
    This beginner exercise uses the store's **default embedding configuration**. For a new store that explicitly uses Gemini Embedding 2, creation can instead specify `"embedding_model": "models/gemini-embedding-2"`. Embedding settings belong to the store and should be chosen before indexing. Don't assume you can change an existing store's embeddings after upload.

---

**Step 4: Verify the store and PDF file**

```py linenums="1"
pdf_path = "/content/data/Geminidect.pdf"

print("📚 Available File Search stores:")
for store in client.file_search_stores.list():
    print(" -", store.display_name, "→", store.name)

if not os.path.isfile(pdf_path):
    raise FileNotFoundError(
        f"PDF not found at {pdf_path}. Upload Geminidect.pdf to Colab's data folder."
    )

print("\n✅ PDF found:", pdf_path)
print("Size (KB):", round(os.path.getsize(pdf_path) / 1024, 1))
```

!!! tip "What just happened?"
    We verified both requirements: a File Search store in Google's service, and a local PDF in the Colab runtime ready for upload.

---

**Step 5: Upload and index the Cisco DECT PDF**

Uploading the PDF triggers chunking, embedding and indexing. We first check whether the document is already in this store, which helps avoid accidental duplicate uploads after a restart.

```py linenums="1"
DOCUMENT_DISPLAY_NAME = "Geminidect.pdf"

existing_docs = list(
    client.file_search_stores.documents.list(parent=file_search_store_name)
)

already_indexed = any(
    getattr(doc, "display_name", None) == DOCUMENT_DISPLAY_NAME
    for doc in existing_docs
)

if already_indexed:
    print("♻️ PDF already indexed in this store; skipping upload.")
else:
    print("📤 Uploading and indexing PDF...", flush=True)

    operation = client.file_search_stores.upload_to_file_search_store(
        file=pdf_path,
        file_search_store_name=file_search_store_name,
        config={"display_name": DOCUMENT_DISPLAY_NAME},
    )

    while not operation.done:
        print("⏳ Indexing in progress...", flush=True)
        time.sleep(5)
        operation = client.operations.get(operation)

    if getattr(operation, "error", None):
        raise RuntimeError(f"Indexing failed: {operation.error}")

    print("✅ Upload/indexing operation finished")

print("\n📑 Documents in the store:")
for doc in client.file_search_stores.documents.list(parent=file_search_store_name):
    print(" -", getattr(doc, "display_name", None), doc.name)
```

!!! tip "What just happened?"
    Google processed your PDF into searchable content. You didn't call an embedding model directly or manage a separate vector index. The loop checks the long-running upload operation until it finishes.

!!! note "Troubleshooting"
    The indexing step can take some time. If you get an indexing error, check the error message and PDF path before retrying. A finished upload operation is not the same as an answered question. Retrieval and generation happen in Step 7.

---

**Step 6: Configure the File Search tool**

```py linenums="1"
file_search_tool = types.Tool(
    file_search=types.FileSearch(
        file_search_store_names=[file_search_store_name]
    )
)

print("✅ File Search tool configured for:", file_search_store_name)
```

!!! tip "What just happened?"
    We told Gemini which store it may retrieve information from. The object does not generate a response. It is passed to the model when we ask a question.

---

**Step 7: Ask a question with `generate_content()`**

```py linenums="1"
question = (
    "What kind of cells do the Cisco IP DECT 6800 Phone products support?"
)

print("🔎 Searching the Cisco DECT guide...", flush=True)
start = time.monotonic()

response = client.models.generate_content(
    model=MODEL,
    contents=(
        "Answer using only the uploaded Cisco DECT guide. "
        "If the information is not in the document, say so. "
        "Keep the answer concise. Question: " + question
    ),
    config=types.GenerateContentConfig(
        tools=[file_search_tool]
    ),
)

print("\n🤖 Gemini answer:\n")
print(response.text or "No text response returned.")
print(f"\n⏱️ Time taken: {time.monotonic() - start:.1f} seconds")
```

!!! tip "What just happened?"
    Gemini used the File Search tool to retrieve relevant context from your indexed PDF and generate a natural-language answer. The retrieved text is not the same thing as the final answer: a retrieval tool finds relevant document material, and the LLM formulates the response.

!!! important
    The exact answer depends on the modified Cisco guide used in this lab. Don't assume the result is correct just because it sounds plausible. Compare it with the PDF.

!!! note "Gemini API availability (503 error)"
    When running this exercise, you may occasionally encounter the following error:

    ```text
    503 UNAVAILABLE: This model is currently experiencing high demand.
    ```

    **Don't worry!** This usually means Google's Gemini service is temporarily experiencing high demand and cannot process your request. It does not necessarily mean there is anything wrong with your code or the document you uploaded.

    **What should you do?**

    1. Try running the query cell again after a short interval.
    2. If the error continues, move on to the next section of the lab.
    3. You can return to this exercise later without uploading or indexing the PDF again, provided your File Search store and indexed document still exist.

    **Important:** There is no need to reinstall libraries, restart Google Colab or recreate your File Search store just because you receive a 503 error.

    **Key takeaway:** When building AI applications that rely on cloud services, temporary API availability issues can occur. Handling these gracefully is an important part of building reliable AI applications.

---

**Step 8: Examine available source information**

Gemini may return grounding details identifying documents or chunks used for the answer. The exact metadata shape can vary by API and model.

```py linenums="1"
if response.candidates:
    grounding = getattr(response.candidates[0], "grounding_metadata", None)
    if grounding:
        print("📚 Grounding/source information:")
        print(grounding)
    else:
        print("ℹ️ No grounding metadata was returned in this response.")
else:
    print("ℹ️ No response candidates were returned.")
```

!!! tip "What just happened?"
    We're inspecting traceability information rather than simply trusting the answer. Not every response includes a friendly page-level citation. For critical use cases, verify claims directly against the source PDF.

**Try another question (optional)**

```py linenums="1"
another_question = "Summarise the main deployment considerations mentioned in the DECT guide."

response2 = client.models.generate_content(
    model=MODEL,
    contents=(
        "Use only the uploaded Cisco DECT guide. "
        "If the guide does not contain the answer, say so. "
        + another_question
    ),
    config=types.GenerateContentConfig(tools=[file_search_tool]),
)
print(response2.text)
```

---

**Step 9: Advanced option: custom chunking (optional)**

Gemini automatically chunks documents, but we can customise the maximum chunk size and overlap during upload. This changes indexing behaviour and is not needed for the main exercise.

```py linenums="1"
# OPTIONAL EXAMPLE: do not run unless you intentionally want
# to upload an additional indexed copy of the PDF.
#
# custom_operation = client.file_search_stores.upload_to_file_search_store(
#     file=pdf_path,
#     file_search_store_name=file_search_store_name,
#     config={
#         "display_name": "Geminidect-custom-chunks.pdf",
#         "chunking_config": {
#             "white_space_config": {
#                 "max_tokens_per_chunk": 200,
#                 "max_overlap_tokens": 20,
#             }
#         },
#     },
# )
```

!!! tip "What just happened?"
    Smaller chunks can influence how much surrounding context the retriever returns. More overlap can preserve context between adjacent chunks but may increase indexing volume. There isn't one best chunk size for every document.

---

**Step 10: Clean up (optional, destructive)**

Your File Search store persists after Colab disconnects. Deleting the store is not required to finish the exercise, but you may want to remove the lab data when finished.

```py linenums="1"
# SAFETY CHECK: Set to True only when you intentionally want
# to permanently delete this lab's File Search store.
DELETE_LAB_STORE = False

if DELETE_LAB_STORE:
    client.file_search_stores.delete(
        name=file_search_store_name,
        config={"force": True}
    )
    print("🗑️ Deleted File Search store:", file_search_store_name)
else:
    print("✅ Store retained:", file_search_store_name)
    print("Set DELETE_LAB_STORE=True only when ready to delete it.")
```

!!! tip "What just happened?"
    We provided a controlled cleanup step without deleting the store automatically. If you delete it, the indexed contents are no longer available for retrieval. You'll need to recreate and reindex the store to repeat the exercise.

---

**What we learned in this module**

In Module 1, we manually loaded a PDF, split it into chunks, generated embeddings, stored them in ChromaDB and connected retrieval to an LLM using LangChain.

In this module, we created a managed File Search store, uploaded the Cisco DECT PDF and asked Gemini to answer using the indexed material. Google managed chunking, embedding, indexing and retrieval. We still had to configure the store, upload the document, choose a generation model, ask a question and assess the answer.

!!! tip "Key takeaway"
    Both DIY and managed RAG can ground responses in external documents. **DIY RAG** offers fine-grained control. **File Search** offers a shorter development path. Neither eliminates the need for evaluation, access control or source verification.

**Troubleshooting checklist**

| Problem | What to check |
|---|---|
| `google-auth` dependency warning | Test imports and client creation before changing versions |
| API key error | Check the Colab Secret is exactly `GEMINI_API_KEY` and notebook access is enabled |
| PDF not found | Confirm `/content/data/Geminidect.pdf` exists. Colab uploads disappear when a runtime is deleted |
| `NameError` after restart | Rerun Steps 2 to 6 to recreate Python variables. The store itself may still exist |
| No documents | Rerun Step 5 and wait for indexing to finish |
| Model unsupported | Check Google's latest File Search documentation for supported model and API combinations. The tested model may be deprecated later |
| Unexpected answer | Inspect grounding details and verify against the PDF |

**Official references**

* <a href="https://ai.google.dev/gemini-api/docs/file-search" target="_blank">Google Gemini API: File Search</a>
* <a href="https://ai.google.dev/gemini-api/docs/pricing" target="_blank">Google Gemini API: Pricing</a>
* <a href="https://aistudio.google.com/api-keys" target="_blank">Google AI Studio: API keys</a>

