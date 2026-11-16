# Model catalog verification — 2026-11-16

## Scope and qualification

Reviewed `DEVELOPMENT.md`, the config, resolver, fetcher and both workflows. The
existing scope is European-developed generative language models, including
European continued pretraining / fine-tuning of foreign base models. Only repos
under each row's official publisher count; third-party conversions do not.
There is no minimum download or parameter threshold in the project config.
This update does not change the counting code, rolling 30-day window, parameter
aggregation, momentum formula, or existing stable row IDs.

## Changes and primary sources

The public Hub organization catalogs were retrieved on 2026-11-16 through
`https://huggingface.co/api/models?author=ORG&limit=1000&full=true`. All configured
publishers were scanned again with the project's resolver (including pagination).
Model cards and the following official publisher pages support the additions:

| Change | Source and reason |
| --- | --- |
| Repair Velvet 14B / 2B publisher from `Almawave` to `AlmawaveLabs`; preserve row IDs | [Current Velvet 14B](https://huggingface.co/AlmawaveLabs/Velvet-14B), [Velvet 2B](https://huggingface.co/AlmawaveLabs/Velvet-2B); old organization catalog is empty |
| Add Velvet2 3B | [Official model card](https://huggingface.co/AlmawaveLabs/Velvet2-3B), multilingual text generation |
| Repair Prelude matcher from `prelude` to `prelude-base`; preserve row ID | [Prelude-base card](https://huggingface.co/openeurollm/prelude-base), identifies the 9B training run and branch checkpoints; main intentionally has no final weights |
| Add Prelude-long and Prelude SFT Excellent v0.1 / v0.2 as separate rows | [Publisher catalog](https://huggingface.co/openeurollm/models), [long](https://huggingface.co/openeurollm/prelude-long), [SFT v0.1](https://huggingface.co/openeurollm/Prelude-SFT-Excellent-v0.1), [SFT v0.2](https://huggingface.co/openeurollm/Prelude-SFT-Excellent-v0.2) |
| Add AI Sweden: GPT-SW3 126M, 356M, 1.3B, 6.7B, 20B, 40B, 6.7B v2 and Nordic Llama 3 8B | [Official catalog](https://huggingface.co/AI-Sweden-Models/models), [GPT-SW3](https://huggingface.co/AI-Sweden-Models/gpt-sw3-126m), [Llama 3 card](https://huggingface.co/AI-Sweden-Models/Llama-3-8B); base/instruct and official GGUF/GPTQ variants grouped within the same version |
| Add NorwAI Llama2 7B, Mistral 7B, Mixtral 8x7B and Magistral 24B reasoning | [Official NTNU organization](https://huggingface.co/NorwAI), [Mistral card](https://huggingface.co/NorwAI/NorwAI-Mistral-7B); exclude the separate one-third-epoch research checkpoint |
| Add LightOn Alfred 40B releases 0723 and 1023 | [0723](https://huggingface.co/lightonai/alfred-40b-0723), [1023](https://huggingface.co/lightonai/alfred-40b-1023); LightOn-developed generative fine-tunes, separate release rows; exclude tokenizer-only repo |
| Add Bielik-One 11B v3.0 r1, 11B v3.1 r1 and 7B v3.0 r1 | [Official publisher](https://huggingface.co/speakleash/models), [11B v3.1 card](https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1), [7B card](https://huggingface.co/speakleash/Bielik-One-7B-v3.0-r1); cards identify merged generative weights; exclude Adapter-only repos |

Config: 186 → 207 rows (+21). Organizations: 25 → 28 (replace Almawave;
add AI Sweden, NorwAI, LightOn). Manifest: 502 → 578 repo IDs (+77, −1).
The removed ID is the obsolete Prelude ID. No overlapping row matches were
found in the retrieved catalogs; no duplicate JSON keys or assigned repo IDs.
The old published README had only 158 rows; regeneration also brings already
configured releases into the public view.

## Validation and reproduction

Run from the worktree with the project's Python environment, without installing
packages. `PYTHONDONTWRITEBYTECODE=1` and a worktree-local `HF_HOME` keep temporary
writes inside this checkout.

```bash
python scripts/resolve_model_repos.py --validate-config
python scripts/resolve_model_repos.py --audit --diff
python scripts/fetch_download_stats.py --concurrency 8 --max-retries 3
python scripts/render_charts.py
python scripts/render_timeseries_charts.py
python scripts/render_leaderboard_md.py
```

Additional data checks: unique JSON keys; no regex overlaps on current catalogs;
each row has a repo; every assigned ID belongs to its row's official organization;
no ID assigned twice; manifest config/content hashes; output row totals equal
member-repo counters; organization totals equal their model totals; snapshot
completeness and renderer execution. No automated test suite exists in this repo.

## Limits and deployment

This is a reviewed catalog update, not an exhaustive inventory of every European
research checkpoint. Unmatched publisher repos remain recorded in the manifest
for later review. Tokenizers, adapters, classifiers, embeddings, experimental
ablations and speech/vision-only families were not added in this pass. Existing
rows and eligibility choices were retained. Prelude remains a research artifact
with checkpoints on branches. Some parameter counts can be absent in the Hub API;
that does not make download counters unavailable. Downloads can change during a
run, and Hugging Face counters are not unique users.

No publication is performed here. The public site is the repository README;
there is no separate website deployment workflow. After owner review and the
approved merge path, run **Resolve model repos** and wait for success, then run
**Fetch download stats** (or let the next daily run execute). Workflows are
independent, so fetch must follow resolve. Generated files in this checkout also
provide a reviewable current snapshot; historical snapshots are preserved.

Validation result: config validation and live resolution succeeded; 207 nonempty
rows, 578 unique repos, 28 publishers. Full stats fetch completed with **578 OK,
0 errors**, without `--allow-partial`; every output model row is complete.
All model totals and organization totals were checked against the snapshot.
All three render commands completed successfully. CSV JSON row counts and values
were cross-checked. `git -c core.whitespace=cr-at-eol diff --check` passes; plain
`git diff --check` flags the existing CSV writer's standard CRLF line endings.
No counting or CSV writer changes were introduced. No browser/image visual
review or public deployment was performed.


### Conflict resolution and time-series interpretation

The PR now incorporates the current main branch, preserving all 107 existing
history records byte-for-byte, including the snapshots from November 12–15.
The new November 16 record is appended, bringing the history to 108 records.
Output deltas are recalculated against November 15, rather than November 11,
and README, CSV/JSON outputs and all seven charts are regenerated offline from
the retained snapshot. Download counters and the model catalog are unchanged.

The existing "estimated daily" charts still plot differences between snapshots,
not unique users. Catalog membership changes can affect aggregate deltas; the
renderer and counting method remain unchanged.

## Standalone LLM scope correction

After catalog expansion, model-card review removed 12 DFlash draft helpers
and the Salamandra Guard classification-adapter repository. The corrected
manifest has 565 repo IDs and still 207 rows. Multimodal generative LLMs remain.
Current counters were recomputed using the same downloaded statistics; older
history records were preserved byte for byte. The exclusions are enforced by
the resolver and audited in the manifest.

## Completeness recheck: user-facing generative models

Rechecked all 1,233 public model IDs from the 28 configured publishers via the
Hugging Face organization API with pagination, metadata, architecture and file
lists. Retrieved 473 candidate model cards (including repos with absent or
misleading pipeline tags); inspected candidate releases and exclusion categories,
plus public gated-card pages where raw READMEs were unavailable. This is not
a claim of a line-by-line manual review of every retrieved card.
This is coverage of these publishers, not a claim of all European publishers.
The owner confirmed inclusion of usable specialist models and exclusion of
comparison-only research series. Final paper-associated releases remain eligible.

The correction adds 46 rows / 57 repositories: 207 → 253 rows and
565 → 622 repositories. The existing 207 row definitions remain unchanged.
New families use exact matching to avoid admitting a new adapter or auxiliary
model merely because its name shares a prefix. The fixture records all 57
newly reviewed repo-to-row assignments and representative excluded examples.

Existing 565 repo counters are preserved from the earlier same-day fetch.
Counters for all 57 added repos were retrieved from the public API without
a token; the current snapshot records both collection timestamps in
`catalog_update`. Only the current timeseries record is replaced; all earlier
records and snapshots are preserved. Generated model/org tables and charts
are rebuilt with the same aggregation and ranking formulas.

### Newly admitted families and primary cards

- [Pixtral 12B (2409)](https://huggingface.co/mistralai/Pixtral-12B-2409)
- [Pixtral Large (2411)](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411)
- [Voxtral Mini 3B (2507)](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)
- [Voxtral Small 24B (2507)](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)
- [Velvet2 3B Vision](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Vision)
- [Bielik-One 4B r1](https://huggingface.co/speakleash/Bielik-One-4B-r1)
- [Salamandra 7B Vision](https://huggingface.co/BSC-LT/salamandra-7b-vision)
- [Salamandra VL 7B (2512)](https://huggingface.co/BSC-LT/Salamandra-VL-7B-2512)
- [SalamandraTA 7B](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct)
- [SalamandraTA 2B](https://huggingface.co/BSC-LT/salamandraTA-2b-instruct)
- [Salamandra TAV 7B](https://huggingface.co/BSC-LT/salamandra-TAV-7b)
- [EuroVLM 1.7B Preview](https://huggingface.co/utter-project/EuroVLM-1.7B-Preview)
- [EuroVLM 9B Preview](https://huggingface.co/utter-project/EuroVLM-9B-Preview)
- [TowerVision 2B](https://huggingface.co/utter-project/TowerVision-2B)
- [TowerVision 9B](https://huggingface.co/utter-project/TowerVision-9B)
- [LightOnOCR 0.9B 16k (1025)](https://huggingface.co/lightonai/LightOnOCR-0.9B-16k-1025)
- [LightOnOCR 0.9B 32k (1025)](https://huggingface.co/lightonai/LightOnOCR-0.9B-32k-1025)
- [LightOnOCR 1B (1025)](https://huggingface.co/lightonai/LightOnOCR-1B-1025)
- [LightOnOCR 2 1B](https://huggingface.co/lightonai/LightOnOCR-2-1B)
- [LightOnOCR 3 0.8B](https://huggingface.co/lightonai/LightOnOCR-3-0.8B)
- [LightOnOCR 3 1B](https://huggingface.co/lightonai/LightOnOCR-3-1B)
- [LightOnOCR 3 4B](https://huggingface.co/lightonai/LightOnOCR-3-4B)
- [PAGnol small](https://huggingface.co/lightonai/pagnol-small)
- [PAGnol medium](https://huggingface.co/lightonai/pagnol-medium)
- [PAGnol large](https://huggingface.co/lightonai/pagnol-large)
- [PAGnol xl](https://huggingface.co/lightonai/pagnol-xl)
- [Mambaoutai 1.6B](https://huggingface.co/lightonai/mambaoutai)
- [ColGrep Agent 2B](https://huggingface.co/lightonai/colgrep-agent-2B)
- [OriOn Mistral 24B](https://huggingface.co/lightonai/OriOn-Mistral)
- [OriOn Qwen 32B](https://huggingface.co/lightonai/OriOn-Qwen)
- [OriOn Qwen 32B SR1](https://huggingface.co/lightonai/OriOn-Qwen-SR1)
- [Tyr 7B](https://huggingface.co/AI-Sweden-Models/tyr)
- [Cassandre RAG 8B](https://huggingface.co/PleIAs/Cassandre-RAG)
- [GPT-sl Base](https://huggingface.co/cjvt/gpt-sl-base)
- [T5-sl small](https://huggingface.co/cjvt/t5-sl-small)
- [T5-sl large](https://huggingface.co/cjvt/t5-sl-large)
- [GaMS DPO Translator](https://huggingface.co/cjvt/GaMS-DPO-Translator)
- [TowerVideo 2B](https://huggingface.co/utter-project/TowerVideo-2B)
- [TowerVideo 9B](https://huggingface.co/utter-project/TowerVideo-9B)
- [CroissantCool v0.1](https://huggingface.co/croissantllm/CroissantCool-v0.1)
- [CroissantCool v0.2](https://huggingface.co/croissantllm/CroissantCool-v0.2)
- [Spire 7B](https://huggingface.co/utter-project/SpireBase)
- [VLT5 Base Keywords](https://huggingface.co/Voicelab/vlt5-base-keywords)
- [Krikri 8B Ancient to Modern Greek](https://huggingface.co/ilsp/llama-krikri-8b-ag-mg-full-ft)
- [M2M100 1.2B Ancient to Modern Greek](https://huggingface.co/ilsp/m2m100-1.2B-ag-mg-full-ft)
- [Velvet2 3B Speech](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Speech)

### Deliberately excluded examples

- ModernColBERT / ColBERT / DenseOn / LateOn: embedding/retrieval representations.
- LightOn-rerank, despite image-text-to-text tags: relevance scoring, not text generation.
- RITA: protein sequence models, not natural-language/code LLMs.
- Shieldstral, Bielik Guard and Salamandra Guard: classification/guardrails.
- Voxtral Realtime / Whisper and Voxtral TTS: speech-only ASR/TTS releases.
- DFlash and adapter-only Bielik-One/MixAT packages: not standalone models.
- Qwen3-8B language/Pivot/Swap series, data-mixture/scaling-law studies and
  Spire NoBlocks/NoPseudo: comparison-only experiments.
- Croissant base_5k…185k: intermediate checkpoints. CroissantCool final
  cooldown releases are included, as are the published Spire Base/Full models.

Borderline specialist cases are qualified by their outputs: VLT5 generates
keywords rather than embeddings; SalamandraTA, Krikri AG→MG and M2M100 AG→MG
generate translations; ColGrep generates tool calls; Velvet Speech supports
spoken QA and summarization as well as ASR. They are usable final generators.

### Validation of the completeness correction

Eight offline unit tests pass, including all 57 admitted IDs, negative controls
and unique row matching. Config hash, unique repository IDs, per-row aggregates
and unchanged old counters were checked independently. The first 107 historical
timeseries records remain byte-identical. Seven charts and the README regenerate.

The expanded catalog exposed a pre-existing chart bug: a publisher first present
in a later snapshot had a shorter value series than the date axis. Organization
series now retain missing earlier observations as gaps, and daily deltas are
unknown across a gap instead of inventing first-day growth. Two regression
tests cover late entry, missing days and a genuine zero observation.
