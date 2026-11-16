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
