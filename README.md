# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-25
- **Generated at:** 2026-09-25T11:30:44Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,468,748 | -33,548 | 57,149,554 | 4.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,784,153 | -4,194 | 64,344,071 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 636,285 | -10,170 | 3,645,070 | 17.0% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 599,819 | -11,673 | 45,643,534 | 1.3% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 501,332 | +5,086 | 4,683,861 | 10.5% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 482,672 | -5,663 | 4,110,093 | 11.5% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 480,176 | -3,589 | 16,283,712 | 2.9% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 356,296 | +23,767 | 371,019 | 75.6% | 8.90B | 1 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 320,719 | +10,162 | 518,870 | 51.8% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 304,840 | -328 | 2,792,007 | 10.5% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 283,697 | -5,129 | 5,543,053 | 5.0% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 279,426 | -4,308 | 32,299,886 | 0.9% | 46.70B | 2 |
| 13 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 250,380 | -29,437 | 416,181 | 48.5% | 353.4M | 1 |
| 14 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 249,160 | -29,459 | 412,666 | 48.6% | 1.20B | 1 |
| 15 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 242,260 | -28,937 | 397,669 | 48.7% | 3.21B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,178 | +3,254 | 2,160,532 | 8.9% | 8.92B | 6 |
| 17 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 198,640 | -1,015 | 5,386,919 | 3.6% | 24.01B | 1 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 180,549 | -4,612 | 4,140,628 | 4.3% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,182 | -1 | 8,494,397 | 1.8% | 8.02B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,536 | +5,106 | 1,052,598 | 9.1% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 97,226 | -52 | 527,523 | 15.5% | 70.60B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,054 | -2,349 | 630,230 | 10.1% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,792 | -911 | 714,356 | 8.9% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,180 | +270 | 7,567,909 | 0.9% | 23.57B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,644 | +124 | 744,711 | 6.8% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 52,464 | +52 | 650,284 | 7.0% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 42,735 | +39 | 11,199,602 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 31,728 | -639 | 675,487 | 4.1% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,639 | +1,986 | 142,552 | 11.4% | 9.15B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,049 | -995 | 479,572 | 3.6% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,305 | +75 | 5,158,276 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,739 | -63 | 24,962 | 14.2% | 72.01B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,050 | +15 | 325,517 | 4.0% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,052 | +138 | 775,239 | 1.8% | 11.25B | 10 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,119 | +116 | 70,861 | 8.3% | — | 5 |
| 36 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,369 | +12 | 5,300,289 | 0.2% | 7.25B | 1 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,192 | +686 | 209,441 | 4.3% | — | 1 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,097 | -294 | 348,395 | 2.7% | 125.03B | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,862 | +23 | 505,995 | 1.8% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,971 | +232 | 131,076 | 3.4% | 7.48B | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,125 | +27 | 108,251 | 3.4% | 8.42B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,918 | +103 | 4,923,893 | 0.1% | 122.61B | 1 |
| 43 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,323 | +158 | 66,018 | 3.2% | 12.77B | 4 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,239 | +42 | 163,463 | 2.0% | 11.17B | 16 |
| 45 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,065 | -35 | 111,064 | 2.4% | 7.29B | 2 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,060 | -245 | 47,492 | 3.4% | 8.03B | 7 |
| 47 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,452 | -460 | 904,179 | 0.4% | 23.57B | 2 |
| 48 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,451 | +6 | 28,769 | 3.5% | 33.12B | 1 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,373 | -10 | 143,272 | 1.8% | 2.25B | 7 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,178 | +9 | 5,376,460 | 0.1% | 22.25B | 1 |
| 51 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,110 | -31 | 668,735 | 0.5% | 7.45B | 2 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,886 | -42 | 371,118 | 0.8% | 7.24B | 8 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,854 | +28 | 251,948 | 1.1% | 4.76B | 5 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,837 | +32 | 132,768 | 1.6% | 7.40B | 3 |
| 55 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,708 | +34 | 91,140 | 1.9% | 2.89B | 1 |
| 56 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,633 | -13 | 54,449 | 2.4% | 7.55B | 1 |
| 57 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,148 | +27 | 65,712 | 1.9% | 14.08B | 1 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,143 | -19 | 31,077 | 2.4% | 14.03B | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,883 | +32 | 147,496 | 1.2% | 7.24B | 4 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,786 | +63 | 34,853 | 2.1% | 2.61B | 3 |
| 61 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,752 | -116 | 57,035 | 1.8% | 1.60B | 5 |
| 62 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,676 | +408 | 84,097 | 1.5% | 9.15B | 1 |
| 63 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,534 | +9 | 5,031,588 | 0.0% | 122.61B | 1 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,188 | -27 | 39,323 | 1.6% | 321.0M | 2 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,123 | +13 | 151,418 | 0.8% | 23.57B | 2 |
| 66 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,080 | +332 | 12,177 | 1.9% | 572.6M | 5 |
| 67 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,966 | +37 | 48,742 | 1.3% | 9.24B | 4 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,939 | +93 | 7,611 | 1.8% | 1.51B | 6 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,906 | +17 | 32,268 | 1.4% | 22.64B | 1 |
| 70 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,872 | +50 | 14,609 | 1.6% | 3.83B | 5 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,801 | +58 | 77,762 | 1.0% | 7.45B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,717 | +18 | 22,855 | 1.4% | 22.64B | 1 |
| 73 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,573 | +30 | 105,439 | 0.8% | 7.45B | 1 |
| 74 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,537 | +199 | 452,012 | 0.3% | 40.43B | 1 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,528 | +30 | 99,231 | 0.8% | 30.68B | 1 |
| 76 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,473 | -15 | 9,240 | 1.3% | 9.15B | 1 |
| 77 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,470 | +66 | 84,655 | 0.8% | 2.22B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,460 | +25 | 355,419 | 0.3% | — | 3 |
| 79 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,450 | 0 | 22,126 | 1.2% | 11.17B | 5 |
| 80 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,449 | +122 | 49,099 | 1.0% | 7.77B | 1 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,444 | -1 | 176,305 | 0.5% | 12.25B | 6 |
| 82 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,421 | 0 | 12,006 | 1.3% | 31.59B | 6 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,392 | +38 | 157,212 | 0.5% | 1.10B | 1 |
| 84 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,390 | -13 | 173,033 | 0.5% | 11.51B | 7 |
| 85 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,345 | +115 | 17,017 | 1.1% | 12.19B | 2 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,307 | +16 | 300,723 | 0.3% | 6.74B | 2 |
| 87 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,272 | -27 | 30,213 | 1.0% | 11.17B | 5 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,246 | +19 | 184,101 | 0.4% | 6.74B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,245 | +19 | 144,892 | 0.5% | 13.02B | 1 |
| 90 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,192 | +136 | 57,064 | 0.8% | 1.35B | 3 |
| 91 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,176 | +5 | 7,391 | 1.1% | 9.82B | 1 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,173 | -37 | 19,716 | 1.0% | 4.30B | 2 |
| 93 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,122 | +18 | 95,487 | 0.6% | 1.35B | 8 |
| 94 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,117 | -4 | 32,302 | 0.8% | 56.7M | 1 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,084 | -117 | 19,368 | 0.9% | 12.25B | 3 |
| 96 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,076 | -19 | 7,257 | 1.0% | 4.30B | 3 |
| 97 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,073 | -60 | 2,823 | 1.0% | 31.59B | 6 |
| 98 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,062 | -40 | 7,884 | 1.0% | 28.84B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,015 | -42 | 800,179 | 0.1% | — | 3 |
| 100 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,015 | -3 | 227,680 | 0.3% | 35.13B | 4 |
| 101 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 999 | -9 | 81,154 | 0.6% | 8.03B | 3 |
| 102 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 970 | -33 | 8,316 | 0.9% | 27.43B | 3 |
| 103 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 913 | +4 | 37,430 | 0.7% | 27.23B | 3 |
| 104 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 910 | -51 | 38,549 | 0.7% | 70.55B | 3 |
| 105 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 826 | +4 | 18,501 | 0.7% | 1.20B | 2 |
| 106 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 798 | +18 | 52,311 | 0.5% | 7.24B | 5 |
| 107 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 780 | -4 | 14,035 | 0.7% | 353.4M | 2 |
| 108 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 767 | +68 | 70,230 | 0.5% | 8.03B | 3 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 738 | -44 | 19,930 | 0.6% | 3.20B | 2 |
| 110 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 705 | +18 | 51,183 | 0.5% | 7.24B | 1 |
| 111 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 638 | +16 | 232,574 | 0.2% | — | 2 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 627 | -21 | 217,768 | 0.2% | 12.19B | 3 |
| 113 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 614 | +25 | 43,890 | 0.4% | 12.19B | 2 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 577 | -10 | 2,880 | 0.6% | 30.68B | 1 |
| 115 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 553 | +2 | 12,420 | 0.5% | 70.55B | 2 |
| 116 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 544 | +12 | 2,934 | 0.5% | 560.9M | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 537 | -20 | 1,330 | 0.5% | 31.58B | 2 |
| 118 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 526 | +32 | 3,647 | 0.5% | 8.03B | 3 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 492 | -20 | 32,397 | 0.4% | 40.43B | 2 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 471 | -23 | 39,055 | 0.3% | 7.48B | 2 |
| 121 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 444 | -39 | 321,873 | 0.1% | 7.24B | 2 |
| 122 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 438 | -12 | 76,002 | 0.2% | 7.04B | 4 |
| 123 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 436 | +37 | 15,711 | 0.4% | 1.54B | 4 |
| 124 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 432 | -196 | 1,180 | 0.4% | 27.23B | 3 |
| 125 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 430 | +2 | 13,720 | 0.4% | 4.33B | 3 |
| 126 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 418 | -28 | 27,174 | 0.3% | 9.24B | 2 |
| 127 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 411 | -9 | 44,374 | 0.3% | 7.70B | 5 |
| 128 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 397 | 0 | 7,259 | 0.4% | 31.59B | 6 |
| 129 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 394 | -16 | 106,849 | 0.2% | — | 3 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 340 | -9 | 21,648 | 0.3% | 2.61B | 2 |
| 131 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 326 | -13 | 11,654 | 0.3% | 27.23B | 2 |
| 132 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 307 | -5 | 2,412 | 0.3% | 4.02B | 2 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 295 | +12 | 41,555 | 0.2% | 11.17B | 1 |
| 134 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 295 | -10 | 1,080 | 0.3% | — | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 268 | +14 | 16,389 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 223 | -4 | 21,346 | 0.2% | 9.24B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 221 | -1 | 19,390 | 0.2% | 68.98B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 205 | +3 | 5,293 | 0.2% | 353.4M | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 201 | +5 | 38,587 | 0.1% | 70.55B | 3 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 185 | +9 | 5,126 | 0.2% | 11.51B | 5 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 184 | -6 | 4,866 | 0.2% | 437.8M | 1 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 173 | -2 | 2,305 | 0.2% | — | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 147 | -2 | 7,133 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | +7 | 4,812 | 0.1% | 70.55B | 3 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | +6 | 28,216 | 0.1% | 46.70B | 6 |
| 146 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 130 | -2 | 2,024 | 0.1% | — | 1 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 106 | +1 | 972 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 103 | +1 | 1,231 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 73 | +2 | 185 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 45 | +4 | 344 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 36 | 0 | 251 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 140 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 19 | +2 | 213 | 0.0% | 15.17B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 350 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 107 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | +1 | 156 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,403,783 | 297,834,503 | 30 | 2.8% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 959,824 | 5,067,994 | 7 | 18.6% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 748,107 | 1,424,601 | 11 | 49.1% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 450,974 | 2,280,764 | 11 | 18.9% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 231,871 | 6,297,437 | 12 | 3.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,579 | 1,352,267 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 18,212 | 428,016 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,861 | 537,586 | 13 | 2.0% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,808 | 189,011 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 9,400 | 354,614 | 14 | 2.1% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,007 | 191,680 | 3 | 2.7% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,484 | 851,936 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,943 | 366,877 | 10 | 1.3% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,618 | 150,367 | 2 | 1.8% |
| 15 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,330 | 692,991 | 2 | 0.5% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,883 | 486,205 | 3 | 0.7% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,837 | 132,768 | 1 | 1.6% |
| 18 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,428 | 23,418 | 4 | 2.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,767 | 656,142 | 2 | 0.4% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,314 | 152,551 | 2 | 0.9% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,268 | 1,158,992 | 4 | 0.2% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,139 | 102,480 | 4 | 1.1% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,176 | 7,391 | 1 | 1.1% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 438 | 76,002 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 130 | 2,024 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,468,748 | 57,149,554 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 482,672 | 4,110,093 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 320,719 | 518,870 | 9 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 250,380 | 416,181 | 13 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 180,549 | 4,140,628 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 31,728 | 675,487 | 28 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,125 | 108,251 | 41 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,323 | 66,018 | 43 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,065 | 111,064 | 45 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,060 | 47,492 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,110 | 668,735 | 51 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,886 | 371,118 | 52 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,837 | 132,768 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,708 | 91,140 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,148 | 65,712 | 57 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,528 | 99,231 | 75 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,460 | 355,419 | 78 |
| 18 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,444 | 176,305 | 81 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,421 | 12,006 | 82 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,392 | 157,212 | 83 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,192 | 57,064 | 90 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,176 | 7,391 | 91 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,015 | 800,179 | 99 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 438 | 76,002 | 122 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 130 | 2,024 | 146 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 49.1% | 748,107 | 1,424,601 | 3 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 18.9% | 450,974 | 2,280,764 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 18.6% | 959,824 | 5,067,994 | 2 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.6% | 231,871 | 6,297,437 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 18,212 | 428,016 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,808 | 189,011 | 9 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,403,783 | 297,834,503 | 1 |
| 8 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,428 | 23,418 | 18 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 8,007 | 191,680 | 11 |
| 10 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,579 | 1,352,267 | 6 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.1% | 9,400 | 354,614 | 10 |
| 12 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,861 | 537,586 | 8 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.8% | 4,618 | 150,367 | 14 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,837 | 132,768 | 17 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,943 | 366,877 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.1% | 1,176 | 7,391 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,139 | 102,480 | 22 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,314 | 152,551 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,484 | 851,936 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.7% | 3,883 | 486,205 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,330 | 692,991 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 2,767 | 656,142 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 438 | 76,002 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,268 | 1,158,992 | 21 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 130 | 2,024 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
