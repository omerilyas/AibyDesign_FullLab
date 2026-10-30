# AI by Design: full GenAI lab guide

The AI by Design v3 lab (`Roadshow/AIbyDesign-v3`) in the single-page-per-part layout of the AI by Design for Collaboration guide: hero, TREE rail, progress bar, Mark complete per task, J/K keys, Notes and the v3 Key Vault.

| Part | Page | Modules |
|---|---|---|
| 1 | `docs/index.md` | Overview, Module 1 (setup) |
| 2 | `docs/part-2/index.md` | Modules 2-5 (AI/ML, tokenization, embeddings, Gemini Embedding 2) |
| 3 | `docs/part-3/index.md` | Modules 6-8 (RAG, File Search, multimodal RAG) |
| 4 | `docs/part-4/index.md` | Modules 9-11 (frameworks, Groq, Hugging Face), summary |

Each v3 `???+ blank` box is one task. All v3 assets are in `docs/assets/` with their v3 paths.

## Run locally

```bash
source /Users/omer/VirtualEnvoirnments/Mkdocs/bin/activate
mkdocs serve        # http://127.0.0.1:8000
mkdocs build --strict
```

## Regenerate from v3

`python3 tools/convert_v3.py` rebuilds the four part pages from the v3 sources (read only) and the intros in `tools/intros/`. It overwrites `docs/index.md` and `docs/part-*/index.md`, so once you edit those pages by hand, stop using it.

`v3-unpublished/` keeps the v3 pages that were not in the v3 nav (fine-tuning tasks 7-8d, Task20, Task6_replicate). They are not part of the site.
