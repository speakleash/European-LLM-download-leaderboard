# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-26
- **Generated at:** 2026-09-26T11:05:21Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 158

## Charts

![Top models by 30-day downloads](docs/charts/top-models-30d.png)

![Organizations by best single model (30-day downloads)](docs/charts/orgs-best-single-model-30d.png)

![Best single model per organization (30-day downloads, log scale)](docs/charts/orgs-best-single-model-30d-log.png)

### Trends over time

From daily snapshots in `data/metrics/timeseries.jsonl` (top 15 models / top 10 orgs by latest-day volume). Rolling-30d charts use a symlog y-axis (0 at zero, log compression above).

![Top models: rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-top-models-30d.png)

![Top models: estimated daily downloads (Δ all-time)](docs/charts/timeseries-top-models-daily.png)

![Top organizations: summed rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-orgs-30d.png)

![Top organizations: estimated daily downloads (Δ all-time)](docs/charts/timeseries-orgs-daily.png)

| Rank | Model | Country | Developer | Org | Downloads (30d) | Δ 30d | All-time | Momentum | Params | Repos |
| ---: | --- | :---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,444,590 | -24,158 | 57,226,327 | 4.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,790,391 | +6,238 | 64,389,911 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 615,792 | -20,493 | 3,654,293 | 16.4% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 591,429 | -8,390 | 45,653,908 | 1.3% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 510,810 | +9,478 | 4,702,265 | 10.6% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 506,970 | +24,298 | 4,152,102 | 11.9% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 470,872 | -9,304 | 16,294,214 | 2.9% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 393,636 | +37,340 | 408,444 | 77.4% | 8.90B | 1 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 335,470 | +14,751 | 533,764 | 52.9% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 307,215 | +2,375 | 2,801,957 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 286,976 | +3,279 | 5,557,791 | 5.1% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 275,393 | -4,033 | 32,306,955 | 0.8% | 46.70B | 2 |
| 13 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 221,889 | -28,491 | 416,709 | 42.9% | 353.4M | 1 |
| 14 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 220,855 | -28,305 | 413,190 | 43.0% | 1.20B | 1 |
| 15 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 215,004 | -27,256 | 398,204 | 43.2% | 3.21B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 207,503 | +6,325 | 2,172,991 | 9.1% | 8.92B | 6 |
| 17 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 202,586 | +3,946 | 5,394,184 | 3.7% | 24.01B | 1 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 175,383 | -5,166 | 4,141,399 | 4.1% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 154,462 | +2,280 | 8,501,297 | 1.8% | 8.02B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 111,414 | +6,878 | 1,061,695 | 9.6% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 95,898 | -1,328 | 528,297 | 15.3% | 70.60B | 2 |
| 22 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,064 | +272 | 716,980 | 8.9% | 23.57B | 2 |
| 23 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,765 | -8,289 | 630,433 | 9.0% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,804 | -5,376 | 7,570,938 | 0.8% | 23.57B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,736 | +92 | 745,033 | 6.8% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 51,826 | -638 | 653,259 | 6.9% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,682 | +947 | 11,201,568 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 31,195 | -533 | 676,056 | 4.0% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 28,114 | +475 | 143,235 | 11.6% | 9.15B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,058 | -991 | 479,851 | 3.5% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,431 | +126 | 5,158,518 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,731 | -8 | 25,007 | 14.2% | 72.01B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,301 | -749 | 325,702 | 3.8% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,103 | +51 | 775,827 | 1.8% | 11.25B | 10 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,298 | +179 | 71,514 | 8.3% | — | 5 |
| 36 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,263 | +1,071 | 210,653 | 4.6% | — | 1 |
| 37 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,416 | +47 | 5,300,352 | 0.2% | 7.25B | 1 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,779 | -318 | 348,555 | 2.6% | 125.03B | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,157 | +295 | 506,418 | 1.8% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 8,085 | +114 | 131,257 | 3.5% | 7.48B | 5 |
| 41 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,207 | +289 | 4,924,405 | 0.1% | 122.61B | 1 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,117 | -8 | 108,355 | 3.4% | 8.42B | 5 |
| 43 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,434 | +374 | 48,070 | 3.7% | 8.03B | 7 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,226 | -13 | 163,630 | 2.0% | 11.17B | 16 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,216 | -107 | 66,114 | 3.1% | 12.77B | 4 |
| 46 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,029 | -36 | 111,080 | 2.4% | 7.29B | 2 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,436 | -15 | 28,780 | 3.4% | 33.12B | 1 |
| 48 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,388 | -64 | 904,244 | 0.4% | 23.57B | 2 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,337 | -36 | 143,377 | 1.8% | 2.25B | 7 |
| 50 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,100 | -10 | 668,882 | 0.5% | 7.45B | 2 |
| 51 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,024 | -154 | 5,376,649 | 0.1% | 22.25B | 1 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,996 | +159 | 132,944 | 1.7% | 7.40B | 3 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,977 | +123 | 252,145 | 1.1% | 4.76B | 5 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,953 | +67 | 371,273 | 0.8% | 7.24B | 8 |
| 55 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,757 | +49 | 91,238 | 2.0% | 2.89B | 1 |
| 56 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,668 | +35 | 54,490 | 2.4% | 7.55B | 1 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,152 | +9 | 31,090 | 2.4% | 14.03B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,140 | -8 | 65,815 | 1.9% | 14.08B | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,983 | +100 | 147,645 | 1.2% | 7.24B | 4 |
| 60 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,892 | +812 | 13,028 | 2.6% | 572.6M | 5 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,880 | +94 | 34,958 | 2.1% | 2.61B | 3 |
| 62 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,720 | -32 | 57,136 | 1.7% | 1.60B | 5 |
| 63 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,687 | +11 | 84,171 | 1.5% | 9.15B | 1 |
| 64 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,565 | +31 | 5,031,689 | 0.1% | 122.61B | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,228 | +40 | 39,402 | 1.6% | 321.0M | 2 |
| 66 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,158 | +35 | 151,466 | 0.9% | 23.57B | 2 |
| 67 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,157 | +218 | 7,882 | 2.0% | 1.51B | 6 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,021 | +55 | 48,799 | 1.4% | 9.24B | 4 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,962 | +56 | 32,329 | 1.5% | 22.64B | 1 |
| 70 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,880 | +8 | 14,657 | 1.6% | 3.83B | 5 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,843 | +42 | 77,821 | 1.0% | 7.45B | 1 |
| 72 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,746 | +209 | 452,231 | 0.3% | 40.43B | 1 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,745 | +28 | 22,947 | 1.4% | 22.64B | 1 |
| 74 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,629 | +56 | 105,502 | 0.8% | 7.45B | 1 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,587 | +59 | 99,301 | 0.8% | 30.68B | 1 |
| 76 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,582 | +133 | 49,256 | 1.1% | 7.77B | 1 |
| 77 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,571 | +101 | 84,756 | 0.9% | 2.22B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,508 | +48 | 355,476 | 0.3% | — | 3 |
| 79 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,489 | +45 | 176,378 | 0.5% | 12.25B | 6 |
| 80 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,473 | +23 | 22,175 | 1.2% | 11.17B | 5 |
| 81 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,435 | +90 | 17,117 | 1.2% | 12.19B | 2 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,395 | +3 | 157,272 | 0.5% | 1.10B | 1 |
| 83 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,385 | -5 | 173,076 | 0.5% | 11.51B | 7 |
| 84 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,380 | -41 | 12,006 | 1.2% | 31.59B | 6 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,357 | +50 | 300,778 | 0.3% | 6.74B | 2 |
| 86 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,345 | -128 | 9,253 | 1.2% | 9.15B | 1 |
| 87 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,297 | +25 | 30,258 | 1.0% | 11.17B | 5 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,296 | +50 | 184,153 | 0.5% | 6.74B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,294 | +49 | 144,945 | 0.5% | 13.02B | 1 |
| 90 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,222 | +30 | 57,107 | 0.8% | 1.35B | 3 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,215 | +42 | 19,759 | 1.0% | 4.30B | 2 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,184 | +8 | 7,428 | 1.1% | 9.82B | 1 |
| 93 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,145 | +23 | 95,568 | 0.6% | 1.35B | 8 |
| 94 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,135 | +18 | 32,327 | 0.9% | 56.7M | 1 |
| 95 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,077 | +1 | 7,270 | 1.0% | 4.30B | 3 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,072 | +10 | 7,902 | 1.0% | 28.84B | 3 |
| 97 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,062 | -22 | 19,384 | 0.9% | 12.25B | 3 |
| 98 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,028 | +13 | 227,708 | 0.3% | 35.13B | 4 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,009 | -6 | 800,203 | 0.1% | — | 3 |
| 100 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 983 | -90 | 2,823 | 1.0% | 31.59B | 6 |
| 101 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 972 | +2 | 8,333 | 0.9% | 27.43B | 3 |
| 102 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 929 | +19 | 38,616 | 0.7% | 70.55B | 3 |
| 103 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 918 | +5 | 37,437 | 0.7% | 27.23B | 3 |
| 104 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 872 | -127 | 81,189 | 0.5% | 8.03B | 3 |
| 105 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 852 | +54 | 52,367 | 0.6% | 7.24B | 5 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 828 | +2 | 18,524 | 0.7% | 1.20B | 2 |
| 107 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 782 | +2 | 14,045 | 0.7% | 353.4M | 2 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 763 | +25 | 19,988 | 0.6% | 3.20B | 2 |
| 109 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 755 | +50 | 51,233 | 0.5% | 7.24B | 1 |
| 110 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 730 | -37 | 70,236 | 0.4% | 8.03B | 3 |
| 111 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 653 | +39 | 43,950 | 0.5% | 12.19B | 2 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 629 | +2 | 217,797 | 0.2% | 12.19B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 629 | -9 | 232,586 | 0.2% | — | 2 |
| 114 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 609 | +173 | 15,885 | 0.5% | 1.54B | 4 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 604 | +27 | 2,913 | 0.6% | 30.68B | 1 |
| 116 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 549 | +5 | 2,943 | 0.5% | 560.9M | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 516 | -21 | 1,330 | 0.5% | 31.58B | 2 |
| 118 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 512 | -41 | 12,424 | 0.5% | 70.55B | 2 |
| 119 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 494 | -32 | 3,650 | 0.5% | 8.03B | 3 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 484 | -8 | 32,409 | 0.4% | 40.43B | 2 |
| 121 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 472 | +1 | 39,060 | 0.3% | 7.48B | 2 |
| 122 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 455 | +25 | 13,749 | 0.4% | 4.33B | 3 |
| 123 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 454 | +36 | 27,213 | 0.4% | 9.24B | 2 |
| 124 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 446 | +2 | 321,881 | 0.1% | 7.24B | 2 |
| 125 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 439 | +1 | 76,009 | 0.2% | 7.04B | 4 |
| 126 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 409 | -2 | 44,380 | 0.3% | 7.70B | 5 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 406 | +9 | 7,274 | 0.4% | 31.59B | 6 |
| 128 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 370 | +30 | 21,680 | 0.3% | 2.61B | 2 |
| 129 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 351 | +25 | 11,684 | 0.3% | 27.23B | 2 |
| 130 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 344 | -50 | 106,855 | 0.2% | — | 3 |
| 131 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 321 | -111 | 1,184 | 0.3% | 27.23B | 3 |
| 132 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 302 | -5 | 2,413 | 0.3% | 4.02B | 2 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 298 | +3 | 1,086 | 0.3% | — | 1 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 275 | -20 | 41,561 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 263 | -5 | 16,389 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 249 | +26 | 21,378 | 0.2% | 9.24B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 227 | +6 | 19,397 | 0.2% | 68.98B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 205 | 0 | 5,296 | 0.2% | 353.4M | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 195 | -6 | 38,594 | 0.1% | 70.55B | 3 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 194 | +9 | 5,137 | 0.2% | 11.51B | 5 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 178 | +5 | 2,314 | 0.2% | — | 1 |
| 142 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 177 | -7 | 4,867 | 0.2% | 437.8M | 1 |
| 143 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 165 | +35 | 2,062 | 0.2% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 146 | -1 | 7,136 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 143 | +2 | 4,818 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 127 | -13 | 28,218 | 0.1% | 46.70B | 6 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 113 | +7 | 984 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 100 | -3 | 1,231 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 73 | 0 | 185 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 46 | +1 | 346 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | +3 | 254 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | +2 | 142 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 19 | 0 | 213 | 0.0% | 15.17B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -1 | 350 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 107 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | 0 | 156 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,364,552 | 298,086,130 | 30 | 2.8% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,021,164 | 5,149,417 | 7 | 19.5% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 663,990 | 1,426,368 | 11 | 43.5% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 466,438 | 2,298,508 | 11 | 19.4% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 227,275 | 6,300,019 | 12 | 3.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,344 | 1,353,329 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 18,647 | 428,754 | 6 | 3.5% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,147 | 538,031 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,848 | 189,407 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 9,647 | 354,983 | 14 | 2.1% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,998 | 191,795 | 3 | 2.7% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,572 | 852,205 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,840 | 367,007 | 10 | 1.3% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,711 | 150,571 | 2 | 1.9% |
| 15 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,399 | 693,154 | 2 | 0.6% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,996 | 132,944 | 1 | 1.7% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,985 | 486,370 | 3 | 0.7% |
| 18 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,285 | 23,433 | 4 | 2.7% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,865 | 656,254 | 2 | 0.4% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,367 | 152,675 | 2 | 0.9% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,225 | 102,583 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,209 | 1,159,041 | 4 | 0.2% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,184 | 7,428 | 1 | 1.1% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 439 | 76,009 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 165 | 2,062 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,444,590 | 57,226,327 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 506,970 | 4,152,102 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 335,470 | 533,764 | 9 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 221,889 | 416,709 | 13 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 175,383 | 4,141,399 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 31,195 | 676,056 | 28 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,117 | 108,355 | 42 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,434 | 48,070 | 43 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,216 | 66,114 | 45 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,029 | 111,080 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,100 | 668,882 | 50 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,996 | 132,944 | 52 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,953 | 371,273 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,757 | 91,238 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,140 | 65,815 | 58 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,587 | 99,301 | 75 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,508 | 355,476 | 78 |
| 18 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,489 | 176,378 | 79 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,395 | 157,272 | 82 |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,380 | 12,006 | 84 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,222 | 57,107 | 90 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,184 | 7,428 | 92 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,009 | 800,203 | 99 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 439 | 76,009 | 125 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 165 | 2,062 | 143 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 43.5% | 663,990 | 1,426,368 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 19.5% | 1,021,164 | 5,149,417 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 19.4% | 466,438 | 2,298,508 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.6% | 227,275 | 6,300,019 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.5% | 18,647 | 428,754 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,848 | 189,407 | 9 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,364,552 | 298,086,130 | 1 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 7,998 | 191,795 | 11 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,344 | 1,353,329 | 6 |
| 10 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.7% | 3,285 | 23,433 | 18 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.1% | 9,647 | 354,983 | 10 |
| 12 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,147 | 538,031 | 8 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.9% | 4,711 | 150,571 | 14 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.7% | 3,996 | 132,944 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,840 | 367,007 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.1% | 1,184 | 7,428 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,225 | 102,583 | 21 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,367 | 152,675 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,572 | 852,205 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.7% | 3,985 | 486,370 | 17 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,399 | 693,154 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 2,865 | 656,254 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 439 | 76,009 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,209 | 1,159,041 | 22 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 165 | 2,062 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
