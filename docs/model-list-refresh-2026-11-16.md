# General-purpose European LLM catalog verification — 2026-11-16

## Final scope

Only general-purpose generative language models: open-ended text generation,
broad instruction/chat and reasoning across domains. General-purpose base models
and general-purpose multimodal LLMs remain eligible. There is no parameter floor.
Specialist releases are excluded even if their base architecture retains some
chat capability. The former broader specialist scope has been superseded.

## Coverage and result

The public Hugging Face catalogs of all 28 configured publishers were retrieved
with pagination: 1,233 model IDs, architecture/task metadata and weight-file lists.
Candidate model cards were retrieved and borderline intended-use cases checked
against official cards. This is not a claim of every European publisher or a
line-by-line reading of every card.

The final catalog contains 197 rows and 532 repositories. Narrowing the previous
253-row/622-repository catalog removes 56 specialist rows and 90 repositories.
No intermediate manifest archive is added. Previous history remains in Git.

## Qualification examples and primary sources

Retained general-purpose families include:

- [Pixtral](https://huggingface.co/mistralai/Pixtral-12B-2409): broad text and visual capabilities.
- [Voxtral](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507): retains general text performance while adding audio understanding.
- [Magistral](https://huggingface.co/mistralai/Magistral-Small-2509): broad reasoning; not a math-only specialist.
- [Nesso 4B](https://huggingface.co/mii-llm/nesso-4B): everyday assistant across diverse tasks; distinguish narrow Agentic releases.
- [TowerVision](https://huggingface.co/utter-project/TowerVision-2B): captioning, visual understanding, summaries and QA.
- [Velvet Vision](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Vision) and [Velvet Speech](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Speech): multimodal QA and broader understanding.
- General-purpose Bielik, PLLuM, Mistral, EuroLLM, Apertus and other base/chat families.

Excluded specialist releases include:

- [LightOnOCR](https://huggingface.co/lightonai/LightOnOCR-2-1B) and [OCRonos](https://huggingface.co/PleIAs/OCRonos): OCR / post-correction.
- [VLT5 Keywords](https://huggingface.co/Voicelab/vlt5-base-keywords): keyword generation.
- [Pleias Pico](https://huggingface.co/PleIAs/Pleias-Pico), Nano and RAG families, Cassandre and OriOn: retrieval/document specialists.
- [SalamandraTA](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct), Salamandra TAV, Spire, Tilde WMT, GaMS DPO Translator and Greek translation fine-tunes: translation specialists.
- [Codestral](https://huggingface.co/mistralai/Codestral-22B-v0.1), Devstral and ColGrep: software/code specialists.
- [Mathstral](https://huggingface.co/mistralai/Mathstral-7B-v0.1) and Leanstral: math/proof specialists.
- [Domyn teachers](https://huggingface.co/domyn/Domyn-Edge-Teacher-IF): cards explicitly say they are not general-purpose assistants.
- [Bielik-One](https://huggingface.co/speakleash/Bielik-One-4B-r1): structured decisions; incidental chat does not change its intended use.
- Dedicated ALIA/Salamandra Function Calling and Nesso Agentic releases; their general base/instruct siblings remain.
- T5-sl denoising checkpoints rather than open-ended general-purpose generators.

Embedding/reranking/classification, protein-only, speech-only ASR/TTS, draft
helpers, adapter-only packages, intermediate checkpoints and comparison-only
research series remain excluded. Translator variants within otherwise general GaMS/GPT-SW3 families and two
dedicated Salamandra Tools variants are also excluded. General conversational
AinaHack variants remain eligible.

The retained family definitions plus reviewed
negative controls enforce the scope without trusting pipeline tags alone.

## Data and validation

Retained repo counters are unchanged. The snapshot's `catalog_update` records
the two original counter-collection timestamps and eligible repo counts. Only
the current 2026-11-16 snapshot and last timeseries record are recomputed.
Earlier snapshots and the first 107 timeseries records are preserved byte for
byte. Cross-scope changes in totals/rank are catalog corrections, not demand.

All model/org tables, CSV, README and seven charts are regenerated with the
existing aggregation and ranking formulas. The missing-history chart fix is
retained: absent observations stay gaps and do not invent first-day growth.
Scope and chart regression tests run offline.
