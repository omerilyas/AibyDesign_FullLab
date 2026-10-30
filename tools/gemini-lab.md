**Step 1: Install dependencies**

Run the following in a Colab cell:

```py
!pip install -q google-genai numpy matplotlib Pillow requests gTTS
```

!!! tip "What just happened?"
    We installed the Google GenAI SDK, numerical utilities, plotting and image tools, and Google Text-to-Speech (gTTS) to generate sample spoken narrations.

---

**Step 2: Configure your Gemini API key**

Run the cell below. When prompted, paste your Gemini API key and press **Enter**.

```py linenums="1"
import os
import getpass

if not os.environ.get("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass("Enter your Gemini API key: ")

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
print("✅ API key configured")
```

!!! tip "What just happened?"
    We made the key available to the notebook without printing it. For repeated labs, you can instead configure it through **Colab Secrets** and load it from `google.colab.userdata`.

---

**Step 3: Initialize Gemini and set the embedding model**

```py linenums="1"
from google import genai
from google.genai import types
from PIL import Image
from IPython.display import Audio, display
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import time
import requests

client = genai.Client(api_key=GEMINI_API_KEY)
MODEL = "gemini-embedding-2"   # ✅ Stable model, not preview
DIMENSIONS = 3072             # Default; Google also recommends 1536 or 768

print("✅ Gemini client initialized")
print("📌 Model:", MODEL)
```

!!! tip "What just happened?"
    We initialized the API client and selected the current stable embedding model. The model returns numbers, **not a chatbot response**.

!!! warning "Important change"
    Do not use `task_type="RETRIEVAL_QUERY"` or `task_type="RETRIEVAL_DOCUMENT"` with Gemini Embedding 2. That parameter is not supported.

---

**Step 4: Download destination photos**

We'll use six destinations. For reliable cross-modal results, the photos must actually show the location they represent. We try two public photo URLs for each destination, validate the downloaded images, and explicitly report failures rather than silently substituting misleading fake photos.

```py linenums="1"
from io import BytesIO

Path("data/images").mkdir(parents=True, exist_ok=True)
Path("data/audio").mkdir(parents=True, exist_ok=True)

image_sources = {
    "paris": [
        "https://cdn.pixabay.com/photo/2018/04/25/09/26/eiffel-tower-3349075_640.jpg",
        "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?w=480",
    ],
    "grand_canyon": [
        "https://cdn.pixabay.com/photo/2015/09/21/14/24/grand-canyon-949517_640.jpg",
        "https://images.pexels.com/photos/2437299/pexels-photo-2437299.jpeg?w=480",
    ],
    "kyoto": [
        "https://cdn.pixabay.com/photo/2019/07/21/07/12/temple-4352273_640.jpg",
        "https://images.pexels.com/photos/5169056/pexels-photo-5169056.jpeg?w=480",
    ],
    "great_barrier_reef": [
        "https://cdn.pixabay.com/photo/2016/11/20/08/33/coral-1842158_640.jpg",
        "https://images.pexels.com/photos/3100361/pexels-photo-3100361.jpeg?w=480",
    ],
    "machu_picchu": [
        "https://cdn.pixabay.com/photo/2012/04/26/22/48/machu-picchu-43387_640.jpg",
        "https://images.pexels.com/photos/2929906/pexels-photo-2929906.jpeg?w=480",
    ],
    "sahara": [
        "https://cdn.pixabay.com/photo/2016/11/14/04/14/sahara-1822485_640.jpg",
        "https://images.pexels.com/photos/1001435/pexels-photo-1001435.jpeg?w=480",
    ],
}

def download_photo(key, urls):
    path = Path(f"data/images/{key}.jpg")
    if path.exists():
        try:
            with Image.open(path) as im:
                im.verify()
            return str(path)
        except Exception:
            path.unlink()
    for url in urls:
        try:
            response = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            im = Image.open(BytesIO(response.content)).convert("RGB")
            im.save(path, "JPEG")
            print(f"✅ {key}")
            return str(path)
        except Exception as exc:
            print(f"⚠️ {key}: trying another image source ({type(exc).__name__})")
    raise RuntimeError(
        f"Could not download an image for {key}. Upload a real destination photo "
        f"to {path} in Colab, then rerun this cell."
    )

image_paths = {key: download_photo(key, urls) for key, urls in image_sources.items()}
print("🎉 Six destination photos are ready")
```

!!! tip "What just happened?"
    You now have a folder containing six photos. Each photo will be embedded as an image.

!!! warning "If a download fails"
    Use Colab's file browser to upload a real photograph under the expected filename. Don't use a blank gradient as a substitute, because it would distort retrieval results.

![ge3](../assets/task4/ge3.png){ loading=lazy }

---

**Step 5: Create the destination knowledge base**

```py linenums="1"
destinations = {
    "paris": {
        "name": "Paris, France",
        "description": "Romantic European city with the Eiffel Tower, the Louvre, French cuisine, art museums, and Seine River cafes.",
        "tags": ["europe", "romance", "culture", "food"],
    },
    "grand_canyon": {
        "name": "Grand Canyon, USA",
        "description": "Immense red rock canyon carved by the Colorado River with spectacular hiking and rafting adventures.",
        "tags": ["north_america", "nature", "hiking"],
    },
    "kyoto": {
        "name": "Kyoto, Japan",
        "description": "Historic Japanese city with ancient temples, shrines, bamboo groves, gardens, and traditional tea ceremonies.",
        "tags": ["asia", "culture", "temples"],
    },
    "great_barrier_reef": {
        "name": "Great Barrier Reef, Australia",
        "description": "Tropical coral reef with colourful fish and sea turtles, perfect for snorkeling and diving in warm ocean waters.",
        "tags": ["oceania", "marine", "snorkeling"],
    },
    "machu_picchu": {
        "name": "Machu Picchu, Peru",
        "description": "Ancient Incan stone ruins perched high in the Andes Mountains with terraced hillsides and mountain trekking.",
        "tags": ["south_america", "history", "mountains"],
    },
    "sahara": {
        "name": "Sahara Desert, Africa",
        "description": "Vast golden sand dunes under star-filled skies, camel treks, desert oases, and nomadic culture.",
        "tags": ["africa", "desert", "adventure"],
    },
}

for key, destination in destinations.items():
    destination["image"] = image_paths[key]
    print("🌍", destination["name"], "→", destination["image"])
```

!!! tip "What just happened?"
    We created six structured records containing readable descriptions, image paths, and tags. The *records themselves are not embeddings yet*. The next steps convert their content into vectors.

---

**Step 6: Generate audio narrations with gTTS**

```py linenums="1"
from gtts import gTTS

audio_narrations = {
    "paris": "Visit Paris for the Eiffel Tower, the Louvre, French cuisine, and romantic river cruises.",
    "grand_canyon": "Explore the Grand Canyon, a vast red rock landscape famous for hiking and rafting.",
    "kyoto": "Discover Kyoto, with ancient temples, bamboo gardens, and traditional tea ceremonies.",
    "great_barrier_reef": "Discover the Great Barrier Reef with tropical fish, coral reefs, and snorkeling.",
    "machu_picchu": "Visit Machu Picchu, the ancient Incan citadel high in the Andes Mountains.",
    "sahara": "Travel through the Sahara Desert with sand dunes, camel treks, and starlit skies.",
}

for key, narration in audio_narrations.items():
    audio_path = Path(f"data/audio/{key}.mp3")
    if not audio_path.exists():
        gTTS(text=narration, lang="en").save(str(audio_path))
    destinations[key]["audio"] = str(audio_path)
    print("🔊", audio_path)
```

!!! tip "What just happened?"
    gTTS converted written narration into MP3 audio. gTTS **generates speech**. Gemini Embedding 2 will **embed the resulting audio**. These are two different tasks. gTTS requires network access, but not a Gemini API key.

![ge4](../assets/task4/ge4.png){ loading=lazy }

---

**Step 7: Preview the multimodal content**

```py linenums="1"
fig, axes = plt.subplots(2, 3, figsize=(13, 8))
for ax, (key, dest) in zip(axes.flat, destinations.items()):
    ax.imshow(Image.open(dest["image"]))
    ax.set_title(dest["name"])
    ax.axis("off")
plt.tight_layout()
plt.show()

print("🔊 Sample narration: Paris")
display(Audio(destinations["paris"]["audio"]))
```

!!! tip "What just happened?"
    You inspected the original data: photos you can see and audio you can hear. **No embedding calculations have happened yet.** Visually confirm that each image broadly matches its destination.

---

**Step 8: Create helper functions to embed text, images, and audio**

```py linenums="1"
# Important: Gemini Embedding 2 does NOT accept a task_type argument.
# For TEXT-only search, Google recommends formatting document and query text.

def embed_text_document(title, description):
    formatted = f"title: {title} | text: {description}"
    result = client.models.embed_content(
        model=MODEL,
        contents=formatted,
        config=types.EmbedContentConfig(output_dimensionality=DIMENSIONS),
    )
    return np.asarray(result.embeddings[0].values, dtype=float)


def embed_text_query(question):
    formatted = f"task: search result | query: {question}"
    result = client.models.embed_content(
        model=MODEL,
        contents=formatted,
        config=types.EmbedContentConfig(output_dimensionality=DIMENSIONS),
    )
    return np.asarray(result.embeddings[0].values, dtype=float)


def embed_image(image_path):
    image_bytes = Path(image_path).read_bytes()
    result = client.models.embed_content(
        model=MODEL,
        contents=[types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")],
        config=types.EmbedContentConfig(output_dimensionality=DIMENSIONS),
    )
    return np.asarray(result.embeddings[0].values, dtype=float)


def embed_audio(audio_path):
    audio_bytes = Path(audio_path).read_bytes()
    result = client.models.embed_content(
        model=MODEL,
        contents=[types.Part.from_bytes(data=audio_bytes, mime_type="audio/mpeg")],
        config=types.EmbedContentConfig(output_dimensionality=DIMENSIONS),
    )
    return np.asarray(result.embeddings[0].values, dtype=float)


def cosine_sim(a, b):
    # Cosine similarity can range from -1 to +1.
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

print("✅ Four helper functions ready")
```

!!! info "What each helper does"
    * `embed_text_document` transforms a destination description into a vector.
    * `embed_text_query` transforms a user's text search into a vector.
    * `embed_image` transforms an actual photo into a vector.
    * `embed_audio` transforms an MP3 recording directly into a vector.
    * `cosine_sim` compares the direction of two vectors, where **+1 means aligned, 0 means orthogonal, and −1 means opposite directions**. These similarity scores are **not probabilities**.

!!! warning "2026 API change"
    `task_type` was used in older embedding APIs. Gemini Embedding 2 uses task-specific *text formatting* instead. In this lab, text descriptions use `title: ... | text: ...` and text queries use `task: search result | query: ...`. Image and audio embeddings don't need those text instructions.

---

**Step 9: Generate all 18 embeddings**

```py linenums="1"
embedding_db = {}

for key, dest in destinations.items():
    print(f"🔄 Embedding {dest['name']}...")

    text_vector = embed_text_document(dest["name"], dest["description"])
    time.sleep(1)
    image_vector = embed_image(dest["image"])
    time.sleep(1)
    audio_vector = embed_audio(dest["audio"])
    time.sleep(1)

    embedding_db[key] = {
        **dest,
        "text_embedding": text_vector,
        "image_embedding": image_vector,
        "audio_embedding": audio_vector,
    }
    print("✅ Dimensions:", len(text_vector), len(image_vector), len(audio_vector))

print("🎉 Destinations:", len(embedding_db))
print("📊 Total stored vectors:", len(embedding_db) * 3)
```

!!! tip "What just happened?"
    Six destinations × three modalities = **18 embeddings**. All use Gemini Embedding 2 and are the same vector length, allowing us to compare them. The `embedding_db` variable is simply a **Python dictionary**, not a production vector database. Calls incur API usage and can be delayed or rate-limited. The one-second pauses are a modest teaching precaution, not a guarantee against limits.

??? info "What does a 3,072-dimensional embedding mean? (click to expand)"
    Each item has 3,072 numerical values describing its position in a learned semantic space. Each number is not a human-readable label such as “beach” or “mountain.” You can also request **768 or 1,536 dimensions** for smaller vectors. All vectors you compare must use compatible dimensions and the same embedding model.

---

**Step 10: Build a multimodal similarity search function**

For each destination, we compare the query with its text, image, and audio vector. The exercise averages all three scores, but this is a **simple teaching heuristic**. In a real product, you may tune modality weights, select the best match per modality, or use learned ranking.

```py linenums="1"
def search_destinations(query_embedding, top_k=3, modalities=("text", "image", "audio")):
    results = []
    for key, dest in embedding_db.items():
        scores = {
            modality: cosine_sim(query_embedding, dest[f"{modality}_embedding"])
            for modality in modalities
        }
        results.append({
            "key": key,
            "name": dest["name"],
            "description": dest["description"],
            "image_path": dest["image"],
            "audio_path": dest["audio"],
            "modality_scores": scores,
            "avg_score": float(np.mean(list(scores.values()))),
        })
    return sorted(results, key=lambda x: x["avg_score"], reverse=True)[:top_k]


def display_search_results(query_label, results):
    print("\n🔎 Query:", query_label)
    fig, axes = plt.subplots(1, len(results), figsize=(5 * len(results), 4))
    if len(results) == 1:
        axes = [axes]
    for position, (ax, result) in enumerate(zip(axes, results), 1):
        ax.imshow(Image.open(result["image_path"]))
        ax.set_title(f"#{position} {result['name']}\nAverage: {result['avg_score']:.3f}")
        ax.axis("off")
        print(f"#{position} {result['name']}:",
              {m: round(s, 3) for m, s in result["modality_scores"].items()})
    plt.tight_layout()
    plt.show()

print("✅ Similarity search is ready")
```

!!! tip "What just happened?"
    We defined *how to search*. Nothing is being searched until the next step. Cosine similarity ranks related vectors, but a high score does not prove factual correctness or represent a confidence percentage.

---

**Step 11: Search with text**

```py linenums="1"
queries = [
    "I want to see ancient ruins high in the mountains",
    "Where can I go snorkeling in warm tropical water?",
    "A romantic European city with great food and art",
    "A vast empty desert landscape under the stars",
]

for question in queries:
    query_vector = embed_text_query(question)
    results = search_destinations(query_vector, top_k=3)
    display_search_results(question, results)
    time.sleep(1)
```

!!! tip "What just happened?"
    Gemini transformed each question into numbers, then our function compared those numbers with the 18 stored vectors. Expected *semantic* matches include Machu Picchu, Great Barrier Reef, Paris, and Sahara, although **exact rankings are not guaranteed**.

!!! question "Try this"
    For each result, identify which modality (text, image, or audio) contributes most to the score.

---

**Step 12: Search with a new image**

Try a new coral/ocean photograph not already in the destination database. Using a new image illustrates **retrieval by meaning**, rather than looking up the exact same file.

```py linenums="1"
query_urls = [
    "https://cdn.pixabay.com/photo/2017/01/11/15/22/turtle-1972331_640.jpg",
    "https://images.pexels.com/photos/932638/pexels-photo-932638.jpeg?w=480",
]

query_image_path = download_photo("query_coral", query_urls)
display(Image.open(query_image_path))

image_query_vector = embed_image(query_image_path)
results = search_destinations(image_query_vector, top_k=3)
display_search_results("New coral / underwater photograph", results)
```

!!! tip "What just happened?"
    The search query was an **image**, not typed text. Gemini made a vector for that photograph and compared it with the stored descriptions, photos, and narrations. Great Barrier Reef would be a sensible top result, but check the actual output.

!!! warning "If the download fails"
    Upload a real coral-reef photo named `query_coral.jpg` in `data/images`, and rerun the cell.

---

**Step 13: Search with audio (without transcription)**

```py linenums="1"
spoken_request = "I want to see beautiful coral reefs and tropical fish while snorkeling."
query_audio_path = "data/audio/query_snorkeling.mp3"

gTTS(text=spoken_request, lang="en").save(query_audio_path)
display(Audio(query_audio_path))

audio_query_vector = embed_audio(query_audio_path)
results = search_destinations(audio_query_vector, top_k=3)
display_search_results("Spoken snorkeling request", results)
```

!!! tip "What just happened?"
    We generated a spoken query with gTTS and sent the **MP3 bytes**, not a transcript, to Gemini Embedding 2. Gemini turned the audio into a vector that can be compared with stored **text, photos, and audio**. The expected destination is Great Barrier Reef, but inspect the rankings yourself.

---

**Optional Bonus: Embed text + image together (a new useful capability)**

Gemini Embedding 2 can combine multiple modalities in one request to create **one aggregated embedding** for a single item. This can be useful when a photo and its caption should be interpreted together.

```py linenums="1"
paris = destinations["paris"]
paris_image = Path(paris["image"]).read_bytes()

result = client.models.embed_content(
    model=MODEL,
    contents=[
        "A travel destination featuring the Eiffel Tower and Parisian culture",
        types.Part.from_bytes(data=paris_image, mime_type="image/jpeg"),
    ],
    config=types.EmbedContentConfig(output_dimensionality=DIMENSIONS),
)

combined_vector = np.asarray(result.embeddings[0].values)
print("✅ One combined text + image embedding:", len(combined_vector), "dimensions")
```

!!! tip "What just happened?"
    Instead of producing a separate vector for the text and another for the photo, Gemini returned **one vector representing both inputs together**. This is different from Step 9, where we deliberately stored separate vectors to show each modality's influence. For this multi-part input, we do **not** add the text-only retrieval prefix.

---

**Summary: What you should remember**

| Concept | Meaning |
| --- | --- |
| Embedding | Numeric representation of content used for similarity comparisons |
| Gemini Embedding 2 | One hosted embedding model supporting text, image, audio, video and PDFs |
| Unified vector space | Vectors from supported modalities can be compared |
| Cosine similarity | Compares the directions of vectors; possible values −1 to +1 |
| `embedding_db` | A temporary in-memory Python dictionary in this exercise |
| Pinecone / ChromaDB | Vector databases you could use to persist and query vectors at larger scale |
| LLM | A separate model that can turn retrieved information into a written answer |
| RAG | Retrieval followed by generation with an LLM |

!!! tip "The big takeaway"
    We've built a multimodal search engine. We don't need the user to type exact keywords. The model transforms descriptions, images, and audio into comparable embeddings. Our simple search compares vectors and ranks destinations. To build an assistant that writes an answer, we'd add an LLM after retrieval.

**Further learning / official documentation**

* <a href="https://ai.google.dev/gemini-api/docs/embeddings" target="_blank">Google Gemini API embeddings</a>
* <a href="https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2" target="_blank">Stable Gemini Embedding 2 model</a>
* <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2-generally-available/" target="_blank">Google's April 2026 general availability announcement</a>
* <a href="https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/" target="_blank">New EmbeddingGemma 2 (October 2026)</a>, for a separate local-model follow-up lab

