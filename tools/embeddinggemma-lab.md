
<p class="eyebrow sub">Module 4 · Task 4C</p>

### BONUS LAB: EmbeddingGemma 2 { #module-4c data-toc-label="4c · BONUS: EmbeddingGemma 2" data-task="4c" }

!!! info "New model: announced 6 October 2026"
    Google DeepMind introduced **EmbeddingGemma 2** on **6 October 2026**. It is a compact, open-weight **740-million-parameter** multimodal embedding model based on Gemma 4. It embeds text, code, images, audio and video into a shared **768-dimensional** space. Unlike the hosted **Gemini Embedding 2** API you just used, EmbeddingGemma 2 can run **locally**, with model weights downloaded to your Colab runtime or your own computer. It is released under the Apache 2.0 license.

    * <a href="https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/" target="_blank">Official announcement</a>
    * <a href="https://developers.googleblog.com/en/embeddinggemma-2-the-developer-guide/" target="_blank">Official getting-started guide</a>

#### Introduction: Why should we try another embedding model?

So far, our Gemini Embedding 2 exercise sent text, images and audio through **Google's hosted API**. This bonus task demonstrates a different deployment choice: **run an embedding model yourself**. This task creates its own small examples, so it doesn't need any data from [Task 4B](#module-4b), and you can focus on what changed.

**Key differences**

| | Gemini Embedding 2 | EmbeddingGemma 2 |
|---|---|---|
| How we run it | Hosted Gemini API | Download weights and run locally |
| Model identifier | `gemini-embedding-2` | `google/embeddinggemma-2` |
| Default vector dimensions | 3,072 | 768 |
| Need a Gemini API key? | Yes | No Gemini API key required |
| Hardware | API handles inference | Colab GPU recommended for this full multimodal exercise |
| Multimodal inputs | Text, image, audio, video and PDFs | Text/code, images, audio, video and interleaved inputs |

!!! warning "Important"
    These are **different models and different embedding spaces**. Do not compare their vectors directly, even if you reduce them to the same number of dimensions. Re-embed both documents and queries with the model you are searching with.

---

**Step 1: Prepare your Colab runtime**

!!! important "Do not open a new notebook"
    Continue in the **same Google Colab notebook you used for Task 4B**. Add the new cells for this task below the Task 4B cells.

    That notebook is already connected to the **GPU runtime** you set up in Task 4B, so you don't need to change anything. The full multimodal model can be much slower on CPU.

!!! tip "What just happened?"
    We are allocating compute to run the model locally. Unlike the Gemini API, the model's calculations happen within this runtime.

---

**Step 2: Install the libraries**

!!! note "Local model setup (EmbeddingGemma 2)"
    Unlike Gemini Embedding 2, which runs on Google's cloud through an API, **EmbeddingGemma 2 runs locally within your Google Colab environment.**

    This means we need to install the necessary libraries and download the model onto the Colab runtime before we can generate embeddings.

    **Please note:**

    * The installation and initial model download may take several minutes, depending on your Colab environment and network connection.
    * The model is downloaded when we load it in a later step, not during the `pip install` command.
    * Make sure you have selected a **GPU runtime** in Google Colab for better performance.
    * Once the model is loaded, subsequent embeddings can be generated locally without making calls to the Gemini API.
    * If you restart or disconnect from your Colab runtime, you may need to load or download the model again.

    **Key takeaway:** We're setting up our own embedding model rather than relying on Google's cloud API. This gives us greater control over where and how our data is processed.

Run this in a Colab code cell:

```py
%pip install -q "sentence-transformers>=6.1.0" transformers Pillow soundfile
```

After it finishes, run this in a new Colab code cell:

```py
%pip install --no-cache-dir --force-reinstall "numpy==2.2.6"
```

!!! note
    If Colab asks you to restart the runtime after upgrading packages, restart it, then continue with Step 3.

!!! tip "What just happened?"
    `sentence-transformers` provides a convenient way to download EmbeddingGemma 2 and turn our content into vectors. `transformers` supplies the underlying model implementation.

---

**Step 3: Load EmbeddingGemma 2**

```py linenums="1"
import torch
from sentence_transformers import SentenceTransformer

MODEL_ID = "google/embeddinggemma-2"

# Use bfloat16 on supported GPUs; float32 elsewhere.
# Avoid float16 with this model.
dtype = (torch.bfloat16 if torch.cuda.is_available()
         and torch.cuda.is_bf16_supported() else torch.float32)

local_model = SentenceTransformer(
    MODEL_ID,
    model_kwargs={"torch_dtype": dtype},
)

print("✅ Loaded:", MODEL_ID)
print("📐 Default embedding dimension:", local_model.get_sentence_embedding_dimension())
```

!!! success "Expected"
    Embedding dimension **768**. This is still a substantial model and may require a GPU and download time. By disabling the audio encoder, we avoid loading components not needed in this exercise.

!!! tip "What just happened?"
    The model weights were downloaded and loaded onto your Colab runtime. From now on, embedding calculations happen there, rather than being sent to the Gemini API.

---

**Step 4: Create two sample documents (no Task 4B data needed)**

```py linenums="1"
places = {
    "Machu Picchu": "Ancient Inca stone ruins high in the Andes mountains of Peru.",
    "Great Barrier Reef": "Tropical underwater coral reefs, colourful fish and snorkelling in Australia.",
}

# These are the searchable document embeddings.
local_text_vectors = {
    name: local_model.encode(
        description,
        prompt_name="Document",
        normalize_embeddings=True,
    )
    for name, description in places.items()
}

print("✅ Created", len(local_text_vectors), "document embeddings")
```

!!! tip "What just happened?"
    We created two small travel descriptions and converted them to vectors using the local model. `Document` tells the model these inputs are content to be searched.

---

**Step 5: Ask a question and retrieve a matching document**

```py linenums="1"
import numpy as np

question = "Where can I explore ancient ruins high in the mountains?"
question_vector = local_model.encode(
    question,
    prompt_name="SearchQuery",
    normalize_embeddings=True,
)

ranked = sorted(
    [
        (name, float(np.dot(question_vector, vector)))
        for name, vector in local_text_vectors.items()
    ],
    key=lambda item: item[1],
    reverse=True,
)

for name, score in ranked:
    print(f"{name}: {score:.3f}")
```

!!! success "What to look for"
    **Machu Picchu** should normally be the stronger match. The exact scores are model-dependent.

!!! tip "What just happened?"
    The question was embedded locally and its vector was compared with both saved document vectors. We used a dot product, which gives cosine similarity when both vectors are normalized. This is **retrieval**, not an LLM-generated answer.

---

**Step 6: Bonus: create an image locally and search it with text**

This image is a simple illustration, not a real travel photograph. We create it in Colab using Pillow, so there is no external image URL or file from Task 4B to download. The goal is to demonstrate cross-modal similarity, not to benchmark model accuracy.

```py linenums="1"
from PIL import Image, ImageDraw
from IPython.display import display

# Draw a simple mountain scene in memory.
img = Image.new("RGB", (512, 320), (130, 190, 230))
draw = ImageDraw.Draw(img)
draw.polygon([(0, 285), (150, 90), (310, 285)], fill=(95, 110, 105))
draw.polygon([(170, 285), (340, 70), (512, 285)], fill=(75, 95, 95))
draw.polygon([(105, 148), (150, 90), (194, 148)], fill="white")
draw.polygon([(291, 132), (340, 70), (389, 132)], fill="white")
draw.rectangle([(0, 285), (511, 319)], fill=(55, 125, 65))
img.save("mountains.png")
display(img)

# Embed the image using the same local model.
image_vector = local_model.encode(
    {"image": "mountains.png"},
    normalize_embeddings=True,
)

# Compare two text queries against the one image embedding.
queries = [
    "Snow-capped mountain peaks",
    "Colourful tropical coral reef underwater",
]

for query in queries:
    query_vector = local_model.encode(
        query, prompt_name="SearchQuery", normalize_embeddings=True
    )
    score = float(np.dot(query_vector, image_vector))
    print(f"{query}: {score:.3f}")
```

!!! success "What to look for"
    The mountain query should plausibly score higher than the coral-reef query, although a synthetic drawing may not behave as reliably as a real photograph. If it doesn't, discuss that as a useful model-evaluation result rather than a lab failure.

---

**What just happened? Understanding your results**

Congratulations! You have successfully demonstrated multimodal embeddings running locally with EmbeddingGemma 2.

In this exercise, you:

1. Created a simple snow-capped mountain illustration using Python and Pillow.
2. Converted the image into a numerical embedding using the locally loaded EmbeddingGemma 2 model.
3. Converted two text descriptions into embeddings using the same model.
4. Compared the image embedding with each text embedding using cosine similarity.

**Example results from the lab**

| Text description | Example similarity score |
|---|---|
| Snow-capped mountain peaks | 0.727 |
| Colourful tropical coral reef underwater | 0.528 |

Your actual scores may differ. In this example, the snow-capped mountain description scores higher, which is the sensible match for the illustration.

!!! info "Why does this matter?"
    You did not manually label the image as a mountain for the model. The model processed the image pixels into a vector, and processed each text description into a vector in a shared embedding space. This lets us compare different types of content directly: **cross-modal semantic similarity**.

!!! warning "Important"
    These numbers are **similarity scores, not accuracy percentages or probabilities**. A score of 0.727 does not mean the model is 72.7% certain. It means that, in this comparison, the mountain description is more similar to the image embedding than the coral-reef description. If both scores are unexpectedly close, that's an opportunity to discuss the limitations of simple synthetic illustrations and model evaluation.

**Why is this useful in a real application?**

Imagine a collection of thousands of images. Someone types “snow-covered mountains” and the application returns matching photos, even when no one manually assigned those exact words as tags. The same technique can support product image search, visual document discovery and multimodal RAG retrieval.

Because this exercise uses EmbeddingGemma 2 locally, the embeddings are generated in the Colab runtime rather than by sending the image to the hosted Gemini embedding API. (Colab itself is cloud-hosted. Running in Colab is not the same as running on your own laptop.)

!!! tip "Key takeaway"
    One locally loaded multimodal embedding model can represent both images and text in a shared vector space, making text-to-image retrieval possible.

!!! question "Optional discussion question"
    What would change if we stored embeddings for three different images and then searched them using a single text query? We could rank and return the closest image instead of only comparing one image against two descriptions.

---

**Quick troubleshooting**

| Problem | What to do |
|---|---|
| `NameError: local_model is not defined` | Step 3 did not complete in this runtime. Rerun Step 3. Do not install everything again unless packages are missing. |
| `NameError: local_text_vectors is not defined` | Rerun Step 4, then Step 5. |
| NumPy import error (`_blas_supports_fpe`) | Stop and start a fresh Colab runtime, then run only the two installation cells in Step 2. Restarting without correcting conflicting installed packages may not be enough. |
| Out of GPU memory | Confirm a GPU is selected, close other notebooks using GPU memory, and make sure `config_kwargs={"audio_config": None}` is present. A CPU runtime may be very slow. |
| Cannot access model weights | Visit <a href="https://huggingface.co/google/embeddinggemma-2" target="_blank">huggingface.co/google/embeddinggemma-2</a> to check access terms and authentication. |

---

**Wrap-up: What you should remember**

* **Gemini Embedding 2:** embeddings are generated by a hosted Google API.
* **EmbeddingGemma 2:** the model runs in your Colab runtime (or your own machine), after its weights are downloaded.

Both models generate vectors rather than final written answers, and their embedding spaces must not be mixed. This bonus is intentionally small and doesn't depend on Task 4B data, so it still works even after your runtime restarts.

!!! question "Think about it"
    Why might an organisation prefer to generate embeddings on its own infrastructure rather than send documents to a hosted API?

**References**

* <a href="https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2" target="_blank">EmbeddingGemma 2 model card</a>
* <a href="https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/" target="_blank">EmbeddingGemma 2 developer guide</a>

