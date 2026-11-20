# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-20
- **Generated at:** 2026-11-20T15:07:56Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 197

General-purpose generative LLMs, including general-purpose multimodal models. Task-specific OCR, translation, RAG, coding, math/proof, decision and function-calling specialists are excluded, alongside auxiliary models.

Historical snapshots retain their original scope; changes across the scope correction on 2026-11-16 also reflect the removed repositories.

## Charts

![Top models by 30-day downloads](docs/charts/top-models-30d.png)

![Organizations by best single model (30-day downloads)](docs/charts/orgs-best-single-model-30d.png)

![Best single model per organization (30-day downloads, log scale)](docs/charts/orgs-best-single-model-30d-log.png)

### Trends over time

From daily snapshots in `data/metrics/timeseries.jsonl` (top 15 models / top 10 orgs by latest-day volume). Rolling-30d charts use a symlog y-axis (0 at zero, log compression above).

Rolling-30-day charts omit incomplete model observations; organization totals have a gap if any member model is incomplete. Complete zero observations remain zero.

Daily estimates omit intervals where the catalog changed, its identity is unknown, or a fetch was incomplete; they resume after two complete observations of the same catalog. This avoids counting newly added models’ lifetime downloads as daily growth.

![Top models: rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-top-models-30d.png)

![Top models: estimated daily downloads (Δ all-time)](docs/charts/timeseries-top-models-daily.png)

![Top organizations: summed rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-orgs-30d.png)

![Top organizations: estimated daily downloads (Δ all-time)](docs/charts/timeseries-orgs-daily.png)

| Rank | Model | Country | Developer | Org | Downloads (30d) | Δ 30d | All-time | Momentum | Params | Repos |
| ---: | --- | :---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,041,702 | +1,673 | 61,042,848 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,054,362 | -17,102 | 67,100,742 | 1.6% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 654,245 | +5,901 | 4,660,293 | 13.7% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 546,199 | -4,504 | 46,607,317 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 348,560 | -5,526 | 32,904,699 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 260,373 | +1,275 | 2,609,235 | 9.6% | 8.92B | 6 |
| 7 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 228,846 | +9,576 | 348,392 | 51.0% | 12.77B | 4 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 212,703 | +2,182 | 5,964,418 | 3.5% | 3.85B | 7 |
| 9 | Voxtral Mini 3B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190,459 | +26,044 | 6,693,998 | 2.8% | 4.68B | 1 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 155,686 | +4,664 | 5,073,092 | 3.0% | 24.01B | 2 |
| 11 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 149,678 | -13,514 | 4,702,868 | 3.1% | 8.05B | 2 |
| 12 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 135,562 | -297 | 4,305,159 | 3.1% | 11.34B | 10 |
| 13 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 126,733 | +776 | 16,701,108 | 0.8% | 12.25B | 3 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 111,149 | +557 | 5,679,673 | 1.9% | 24.01B | 1 |
| 15 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 97,220 | -2,182 | 7,744,915 | 1.2% | 23.57B | 2 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,373 | -62 | 8,618,803 | 0.7% | 8.02B | 1 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,171 | -364 | 11,305,835 | 0.4% | 140.63B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 36,151 | -86 | 756,399 | 4.2% | 119.40B | 3 |
| 19 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 34,674 | -534 | 740,637 | 4.1% | 7.77B | 5 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 29,374 | -2,332 | 808,347 | 3.2% | 23.57B | 2 |
| 21 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 21,581 | +564 | 21,662 | 17.7% | — | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,183 | +258 | 949,595 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 17,562 | +24 | 805,487 | 1.9% | 11.25B | 10 |
| 24 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,009 | -1,374 | 374,556 | 3.6% | 24.01B | 2 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,217 | -37 | 751,469 | 1.8% | 8.90B | 5 |
| 26 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,082 | +14 | 1,125,650 | 1.2% | 127.70B | 2 |
| 27 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,817 | +110 | 4,948,344 | 0.3% | 122.61B | 1 |
| 28 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,692 | +229 | 251,671 | 3.9% | — | 1 |
| 29 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 12,195 | -97 | 37,054 | 8.9% | 78.10B | 2 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,015 | -82 | 500,949 | 1.8% | 9.15B | 1 |
| 31 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,622 | +147 | 527,405 | 1.7% | 7.24B | 8 |
| 32 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,460 | +20 | 5,393,381 | 0.2% | 22.25B | 1 |
| 33 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,155 | +366 | 264,523 | 2.5% | 4.76B | 8 |
| 34 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,109 | +650 | 9,109 | 8.3% | 11.17B | 8 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,549 | +288 | 90,469 | 4.5% | — | 5 |
| 36 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,395 | +73 | 24,905 | 6.7% | 3.83B | 5 |
| 37 | Pixtral 12B (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,931 | +199 | 145,026 | 3.2% | — | 2 |
| 38 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,843 | +1,236 | 163,869 | 3.0% | 9.15B | 1 |
| 39 | Voxtral Small 24B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,652 | +621 | 1,000,131 | 0.7% | 24.26B | 1 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,598 | -37 | 37,466 | 5.5% | 72.01B | 4 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,551 | +233 | 18,351 | 6.4% | 1.51B | 6 |
| 42 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,958 | +76 | 58,550 | 4.4% | 8.03B | 7 |
| 43 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,600 | +57 | 606,327 | 0.9% | 22.64B | 1 |
| 44 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,439 | -171 | 121,114 | 2.9% | 8.42B | 7 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,162 | +356 | 154,580 | 2.4% | 2.25B | 7 |
| 46 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,161 | -262 | 25,045 | 4.9% | 572.6M | 5 |
| 47 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,840 | +15 | 139,339 | 2.4% | 2.89B | 1 |
| 48 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,773 | -210 | 553,213 | 0.9% | 70.60B | 2 |
| 49 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,643 | +8 | 160,348 | 2.2% | 351.6M | 1 |
| 50 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,438 | +110 | 66,063 | 3.3% | 1.60B | 9 |
| 51 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 5,048 | -5 | 40,093 | 3.6% | 56.7M | 1 |
| 52 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,979 | +321 | 30,430 | 3.8% | 22.64B | 1 |
| 53 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,818 | +10 | 46,638 | 3.3% | 13.29B | 3 |
| 54 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,413 | +12 | 156,082 | 1.7% | 7.24B | 4 |
| 55 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,178 | -20 | 125,773 | 1.9% | 8.54B | 2 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,146 | -20 | 379,474 | 0.9% | 7.24B | 8 |
| 57 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,136 | +3 | 141,721 | 1.7% | 7.40B | 3 |
| 58 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,059 | +35 | 12,818 | 3.6% | 40.43B | 2 |
| 59 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,909 | +26 | 132,227 | 1.7% | 7.48B | 9 |
| 60 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,769 | +20 | 55,698 | 2.4% | 7.77B | 3 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,668 | -51 | 42,109 | 2.6% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,548 | -5,141 | 5,048,351 | 0.1% | 122.61B | 1 |
| 63 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,481 | -270 | 3,919 | 3.3% | 3.93B | 2 |
| 64 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,393 | +43 | 13,737 | 3.0% | 9.15B | 1 |
| 65 | OpenEuroLLM Prelude-base 9B | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 3,344 | +82 | 79,398 | 1.9% | 9.09B | 1 |
| 66 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,237 | +15 | 97,278 | 1.6% | 2.89B | 1 |
| 67 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,227 | -69 | 23,009 | 2.6% | 27.43B | 3 |
| 68 | AI Sweden Llama 3 8B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3,033 | +46 | 96,354 | 1.5% | 8.03B | 10 |
| 69 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,033 | +44 | 170,954 | 1.1% | 11.17B | 16 |
| 70 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2,905 | +2,351 | 14,939 | 2.5% | 31.59B | 6 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,811 | +57 | 21,712 | 2.3% | 12.19B | 2 |
| 72 | Velvet 14B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,811 | +8 | 70,948 | 1.6% | 14.08B | 1 |
| 73 | Velvet 2B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,759 | +10 | 89,812 | 1.5% | 2.22B | 1 |
| 74 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,697 | +13 | 87,187 | 1.4% | 9.15B | 1 |
| 75 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,361 | +61 | 23,783 | 1.9% | 4.30B | 2 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,277 | +3 | 103,274 | 1.1% | 30.68B | 1 |
| 77 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,182 | -60 | 231,298 | 0.7% | 35.13B | 4 |
| 78 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,115 | +14 | 81,601 | 1.2% | 7.45B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,085 | +5 | 359,234 | 0.5% | — | 3 |
| 80 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,080 | +7 | 52,598 | 1.4% | 9.24B | 4 |
| 81 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,051 | -10 | 455,078 | 0.4% | 40.43B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,031 | +7 | 160,803 | 0.8% | 1.10B | 1 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,002 | +8 | 109,112 | 1.0% | 7.45B | 1 |
| 84 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,919 | +9 | 187,523 | 0.7% | 6.74B | 1 |
| 85 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,914 | +36 | 420,641 | 0.4% | 353.4M | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,913 | +5 | 304,192 | 0.5% | 6.74B | 2 |
| 87 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,905 | -5 | 35,750 | 1.4% | 22.64B | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,855 | +9 | 148,239 | 0.7% | 13.02B | 1 |
| 89 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,787 | +29 | 402,059 | 0.4% | 3.21B | 1 |
| 90 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,782 | +25 | 417,204 | 0.3% | 1.20B | 1 |
| 91 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,768 | -18 | 10,628 | 1.6% | 9.82B | 1 |
| 92 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,759 | +6 | 180,461 | 0.6% | 12.25B | 6 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,581 | -17 | 802,804 | 0.2% | — | 3 |
| 94 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,559 | -353 | 157,606 | 0.6% | 23.57B | 2 |
| 95 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,535 | +8 | 55,306 | 1.0% | 7.24B | 5 |
| 96 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,482 | -55 | 41,261 | 1.0% | 70.55B | 3 |
| 97 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,471 | +3 | 54,044 | 1.0% | 7.24B | 1 |
| 98 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,430 | -16 | 34,841 | 1.1% | 14.03B | 1 |
| 99 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,248 | -58 | 45,056 | 0.9% | 12.25B | 3 |
| 100 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,193 | +22 | 57,134 | 0.8% | 7.55B | 1 |
| 101 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,176 | +16 | 175,595 | 0.4% | 11.51B | 9 |
| 102 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,149 | -24 | 9,909 | 1.0% | 4.30B | 3 |
| 103 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,046 | +23 | 59,129 | 0.7% | 1.35B | 3 |
| 104 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,027 | +9 | 45,466 | 0.7% | 12.19B | 2 |
| 105 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,022 | -10 | 32,022 | 0.8% | 33.12B | 1 |
| 106 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,019 | 0 | 9,648 | 0.9% | 28.84B | 3 |
| 107 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,001 | +2 | 671,693 | 0.1% | 7.45B | 2 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 999 | -2 | 15,326 | 0.9% | 4.33B | 3 |
| 109 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 956 | +27 | 219,421 | 0.3% | 12.19B | 3 |
| 110 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 867 | +18 | 96,943 | 0.4% | 1.35B | 8 |
| 111 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 856 | +12 | 24,325 | 0.7% | 11.17B | 5 |
| 112 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 856 | -20 | 233,746 | 0.3% | — | 2 |
| 113 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 851 | +2 | 1,912 | 0.8% | 608.3M | 1 |
| 114 | EuroVLM 9B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 791 | -34 | 8,640 | 0.7% | 9.57B | 1 |
| 115 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 771 | +63 | 1,650 | 0.8% | 9.15B | 2 |
| 116 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 760 | -15 | 82,185 | 0.4% | 7.04B | 4 |
| 117 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 703 | -5 | 32,053 | 0.5% | 11.17B | 5 |
| 118 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 696 | +4 | 112,628 | 0.3% | 7.29B | 2 |
| 119 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 672 | -19 | 17,228 | 0.6% | 1.54B | 4 |
| 120 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 667 | +6 | 21,015 | 0.6% | 3.20B | 2 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 588 | +3 | 28,093 | 0.5% | 9.24B | 2 |
| 122 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 581 | -8 | 3,885 | 0.6% | 30.68B | 1 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 540 | 0 | 1,809 | 0.5% | 852,480 | 2 |
| 124 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 467 | +3 | 22,299 | 0.4% | 9.24B | 2 |
| 125 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 448 | -15 | 5,840 | 0.4% | 11.51B | 5 |
| 126 | OpenEuroLLM Prelude-long 9B | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 447 | +56 | 447 | 0.4% | 9.09B | 1 |
| 127 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 441 | -12 | 4,596 | 0.4% | 8.03B | 3 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 391 | +33 | 38,096 | 0.3% | 27.23B | 3 |
| 129 | OpenEuroLLM Prelude SFT Excellent v0.2 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 379 | +27 | 379 | 0.4% | 9.09B | 1 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 347 | +17 | 22,331 | 0.3% | 2.61B | 2 |
| 131 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 340 | -5 | 12,329 | 0.3% | 27.23B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 317 | +4 | 70,715 | 0.2% | 8.03B | 3 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 279 | +3 | 107,401 | 0.1% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 242 | -2 | 2,889 | 0.2% | 4.02B | 2 |
| 135 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 240 | +7 | 29,904 | 0.2% | 1.01B | 1 |
| 136 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 234 | -7 | 33,010 | 0.2% | 40.43B | 2 |
| 137 | Mambaoutai 1.6B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 234 | -5 | 1,402 | 0.2% | 1.62B | 1 |
| 138 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 221 | +7 | 42,042 | 0.2% | 11.17B | 1 |
| 139 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 209 | +5 | 322,393 | 0.0% | 7.24B | 2 |
| 140 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 191 | 0 | 3,010 | 0.2% | 31.59B | 6 |
| 141 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 187 | +2 | 16,745 | 0.2% | 7.29B | 2 |
| 142 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 182 | +13 | 39,502 | 0.1% | 7.48B | 2 |
| 143 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 178 | -4 | 19,786 | 0.1% | 68.98B | 2 |
| 144 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 171 | +4 | 28,533 | 0.1% | 46.70B | 6 |
| 145 | Velvet2 3B Speech | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 165 | -4 | 204 | 0.2% | 4.55B | 1 |
| 146 | Alfred 40B (1023) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 161 | -1 | 78,655 | 0.1% | — | 1 |
| 147 | Pixtral Large (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 159 | -6 | 4,497 | 0.2% | — | 1 |
| 148 | PAGnol xl | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 157 | -4 | 1,648 | 0.2% | 1.64B | 1 |
| 149 | TowerVision 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 151 | +2 | 2,794 | 0.1% | 3.02B | 1 |
| 150 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 148 | -2 | 44,739 | 0.1% | 7.70B | 5 |
| 151 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 137 | +1 | 2,974 | 0.1% | 40.43B | 2 |
| 152 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 133 | +3 | 12,797 | 0.1% | 70.55B | 2 |
| 153 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 133 | +4 | 5,249 | 0.1% | 437.8M | 1 |
| 154 | GPT-SW3 1.3B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 131 | +2 | 306,787 | 0.0% | 1.47B | 4 |
| 155 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 124 | +8 | 2,624 | 0.1% | — | 1 |
| 156 | Velvet2 3B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 117 | +2 | 136 | 0.1% | 3.89B | 1 |
| 157 | Salamandra VL 7B (2512) | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 113 | -2 | 2,107 | 0.1% | 8.90B | 1 |
| 158 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 107 | +5 | 5,123 | 0.1% | 70.55B | 3 |
| 159 | PAGnol medium | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 106 | 0 | 1,170 | 0.1% | 380.0M | 1 |
| 160 | GPT-sl Base | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 95 | +2 | 1,843 | 0.1% | — | 1 |
| 161 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 95 | +3 | 38,788 | 0.1% | 70.55B | 3 |
| 162 | Alfred 40B (0723) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 93 | +4 | 5,552 | 0.1% | — | 1 |
| 163 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 93 | -1 | 479 | 0.1% | 437.8M | 1 |
| 164 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 90 | +1 | 7,512 | 0.1% | 31.59B | 6 |
| 165 | EuroVLM 1.7B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 88 | -1 | 3,046 | 0.1% | 2.06B | 1 |
| 166 | CroissantCool v0.2 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 82 | -4 | 14,817 | 0.1% | 1.35B | 1 |
| 167 | TowerVision 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 80 | 0 | 1,387 | 0.1% | 9.66B | 1 |
| 168 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 73 | +6 | 225 | 0.1% | 437.8M | 1 |
| 169 | PAGnol small | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 69 | -2 | 4,672 | 0.1% | — | 1 |
| 170 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 68 | +3 | 282 | 0.1% | 437.8M | 1 |
| 171 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 61 | +1 | 1,340 | 0.1% | 560.9M | 1 |
| 172 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 61 | +4 | 328 | 0.1% | 437.8M | 1 |
| 173 | PAGnol large | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 49 | -2 | 895 | 0.0% | — | 1 |
| 174 | TowerVideo 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 47 | +1 | 487 | 0.0% | 9.66B | 1 |
| 175 | Salamandra 7B Vision | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 42 | +2 | 3,723 | 0.0% | 8.19B | 1 |
| 176 | TowerVideo 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 40 | +1 | 1,133 | 0.0% | 3.02B | 1 |
| 177 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 39 | +2 | 629 | 0.0% | 6.25B | 2 |
| 178 | OpenEuroLLM Prelude SFT Excellent v0.1 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 39 | -1 | 59 | 0.0% | 9.10B | 1 |
| 179 | Velvet2 3B Vision | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 37 | +14 | 92 | 0.0% | 4.33B | 1 |
| 180 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 36 | +2 | 1,469 | 0.0% | 8.03B | 1 |
| 181 | NorwAI Magistral 24B reasoning | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 31 | 0 | 547,892 | 0.0% | 23.85B | 1 |
| 182 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | +1 | 158 | 0.0% | 7.24B | 1 |
| 183 | CroissantCool v0.1 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 27 | -1 | 608 | 0.0% | 1.35B | 1 |
| 184 | NorwAI Mistral-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 25 | 0 | 111,668 | 0.0% | 7.54B | 3 |
| 185 | GPT-SW3 20B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 24 | +2 | 141,985 | 0.0% | 20.92B | 5 |
| 186 | Tyr 7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 24 | +3 | 919 | 0.0% | 7.24B | 1 |
| 187 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 20 | +3 | 384 | 0.0% | 12.25B | 1 |
| 188 | GPT-SW3 126M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 10 | 0 | 893,762 | 0.0% | 186.1M | 4 |
| 189 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 9 | +5 | 6,176 | 0.0% | 12.25B | 3 |
| 190 | GPT-SW3 6.7B v2 | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 7 | 0 | 262,851 | 0.0% | 7.11B | 5 |
| 191 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 6 | -2 | 1,509 | 0.0% | 31.58B | 2 |
| 192 | GPT-SW3 40B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 5 | +2 | 59,798 | 0.0% | 39.93B | 2 |
| 193 | NorwAI Mixtral-8x7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 3 | 0 | 2,175 | 0.0% | 47.00B | 2 |
| 194 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 195 | GPT-SW3 356M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 334,511 | 0.0% | 470.6M | 4 |
| 196 | GPT-SW3 6.7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 68,906 | 0.0% | 7.11B | 1 |
| 197 | NorwAI Llama2-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | 0 | 65,548 | 0.0% | 7.03B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,077,807 | 302,581,395 | 27 | 2.0% |
| 2 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 233,291 | 480,981 | 7 | 40.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 200,373 | 6,113,317 | 7 | 3.2% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 197,794 | 6,560,782 | 13 | 3.0% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 78,067 | 2,703,385 | 18 | 2.8% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 51,280 | 1,461,254 | 10 | 3.3% |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,037 | 597,085 | 5 | 2.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,200 | 1,328,547 | 6 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,025 | 572,790 | 13 | 2.2% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,267 | 455,106 | 6 | 2.6% |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 12,955 | 119,239 | 2 | 5.9% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,416 | 373,668 | 13 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,769 | 205,355 | 3 | 2.2% |
| 14 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Almawave | IT | 5,889 | 161,192 | 5 | 2.3% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,805 | 496,565 | 3 | 1.0% |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,485 | 404,007 | 12 | 1.1% |
| 17 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 5,249 | 14,547 | 2 | 4.6% |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,118 | 862,406 | 3 | 0.5% |
| 19 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,355 | 701,867 | 2 | 0.5% |
| 20 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 4,209 | 80,283 | 4 | 2.3% |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,998 | 663,426 | 2 | 0.5% |
| 22 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden | SE | 3,234 | 2,165,873 | 9 | 0.1% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,192 | 26,970 | 4 | 2.5% |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,894 | 1,163,737 | 4 | 0.2% |
| 25 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,858 | 107,159 | 2 | 1.4% |
| 26 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,022 | 171,497 | 4 | 0.7% |
| 27 | [lightonai](https://huggingface.co/lightonai) | LightOn | FR | 869 | 93,994 | 7 | 0.4% |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI / NTNU | NO | 59 | 727,283 | 4 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,041,702 | 61,042,848 | 1 |
| 2 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 228,846 | 348,392 | 7 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 149,678 | 4,702,868 | 11 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 135,562 | 4,305,159 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 34,674 | 740,637 | 19 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 20,183 | 949,595 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 12,195 | 37,054 | 29 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,958 | 58,550 | 42 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,439 | 121,114 | 44 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,840 | 139,339 | 47 |
| 11 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 5,048 | 40,093 | 51 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,413 | 156,082 | 54 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,146 | 379,474 | 56 |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,481 | 3,919 | 63 |
| 15 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude-base 9B | 3,344 | 79,398 | 65 |
| 16 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,227 | 23,009 | 67 |
| 17 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden Llama 3 8B | 3,033 | 96,354 | 68 |
| 18 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 2,905 | 14,939 | 70 |
| 19 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Velvet 14B | 2,811 | 70,948 | 72 |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,277 | 103,274 | 76 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,115 | 81,601 | 78 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,085 | 359,234 | 79 |
| 23 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,031 | 160,803 | 82 |
| 24 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,759 | 180,461 | 92 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,581 | 802,804 | 93 |
| 26 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,046 | 59,129 | 103 |
| 27 | [lightonai](https://huggingface.co/lightonai) | Mambaoutai 1.6B | 234 | 1,402 | 137 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI Magistral 24B reasoning | 31 | 547,892 | 181 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 40.2% | 233,291 | 480,981 | 2 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5.9% | 12,955 | 119,239 | 11 |
| 3 | [domyn](https://huggingface.co/domyn) | 4.6% | 5,249 | 14,547 | 17 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.3% | 51,280 | 1,461,254 | 6 |
| 5 | [swiss-ai](https://huggingface.co/swiss-ai) | 3.2% | 200,373 | 6,113,317 | 3 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 3.0% | 197,794 | 6,560,782 | 4 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,037 | 597,085 | 7 |
| 8 | [utter-project](https://huggingface.co/utter-project) | 2.8% | 78,067 | 2,703,385 | 5 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,267 | 455,106 | 10 |
| 10 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.5% | 3,192 | 26,970 | 23 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,416 | 373,668 | 12 |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | 2.3% | 4,209 | 80,283 | 20 |
| 13 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2.3% | 5,889 | 161,192 | 14 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 15,025 | 572,790 | 9 |
| 15 | [ilsp](https://huggingface.co/ilsp) | 2.2% | 6,769 | 205,355 | 13 |
| 16 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,077,807 | 302,581,395 | 1 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,858 | 107,159 | 25 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,200 | 1,328,547 | 8 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.1% | 5,485 | 404,007 | 16 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,805 | 496,565 | 15 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 2,022 | 171,497 | 26 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,355 | 701,867 | 19 |
| 23 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,118 | 862,406 | 18 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,998 | 663,426 | 21 |
| 25 | [lightonai](https://huggingface.co/lightonai) | 0.4% | 869 | 93,994 | 27 |
| 26 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,894 | 1,163,737 | 24 |
| 27 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0.1% | 3,234 | 2,165,873 | 22 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | 0.0% | 59 | 727,283 | 28 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
