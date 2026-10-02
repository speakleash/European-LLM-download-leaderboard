# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-02
- **Generated at:** 2026-10-02T12:11:14Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,397,021 | -9,395 | 57,714,422 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,698,146 | +27,922 | 64,696,893 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 585,851 | +31,095 | 603,147 | 83.3% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 565,969 | -14,783 | 45,716,045 | 1.2% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 543,566 | +2,633 | 4,774,888 | 11.2% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 497,286 | -1,444 | 4,248,892 | 11.4% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 495,099 | +15,859 | 16,414,610 | 3.0% | 12.25B | 3 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 482,027 | -16,229 | 3,709,751 | 12.7% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 382,940 | -11,667 | 593,470 | 55.2% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 316,355 | +4,137 | 2,851,196 | 10.7% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 270,538 | +548 | 32,358,920 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 269,020 | -5,048 | 5,611,345 | 4.7% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 254,948 | +988 | 5,467,706 | 4.6% | 24.01B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,743 | +1,528 | 2,223,817 | 9.9% | 8.92B | 6 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 151,373 | -162 | 8,522,226 | 1.8% | 8.02B | 1 |
| 16 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 127,050 | -7,312 | 1,088,542 | 10.7% | 127.70B | 2 |
| 17 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 123,944 | -9,486 | 4,147,297 | 2.9% | 11.34B | 8 |
| 18 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 92,696 | -1,742 | 532,566 | 14.7% | 70.60B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,534 | -14 | 731,310 | 8.7% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,265 | -1 | 68,173 | 39.4% | — | 1 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 61,479 | +827 | 7,583,214 | 0.8% | 23.57B | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,591 | +2 | 747,073 | 6.8% | 1.66B | 1 |
| 23 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,523 | +2,310 | 670,574 | 7.3% | 119.40B | 3 |
| 24 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,499 | +4,965 | 11,216,171 | 0.4% | 140.63B | 2 |
| 25 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,519 | +61 | 632,257 | 4.7% | 23.57B | 2 |
| 26 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 30,268 | -485 | 680,990 | 3.9% | 7.77B | 8 |
| 27 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,407 | -346 | 146,098 | 11.1% | 9.15B | 1 |
| 28 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,353 | -32 | 5,159,403 | 0.4% | 22.25B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,841 | -293 | 482,297 | 2.7% | 9.15B | 1 |
| 30 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,342 | +179 | 213,523 | 4.9% | — | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,250 | -164 | 778,715 | 1.7% | 11.25B | 10 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 14,996 | -2,934 | 25,292 | 12.0% | 72.01B | 1 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,813 | -214 | 74,343 | 7.9% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,013 | -1,208 | 508,809 | 1.8% | 7.24B | 8 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 10,633 | +435 | 134,221 | 4.5% | 7.48B | 5 |
| 36 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,724 | +12 | 326,843 | 2.0% | 24.01B | 2 |
| 37 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,682 | -696 | 349,664 | 1.9% | 125.03B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,333 | +267 | 4,926,402 | 0.2% | 122.61B | 1 |
| 39 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,212 | +51 | 49,319 | 4.2% | 8.03B | 7 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,028 | -403 | 109,322 | 2.9% | 8.42B | 7 |
| 41 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,729 | -1 | 30,156 | 4.4% | 33.12B | 1 |
| 42 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,346 | +246 | 5,378,375 | 0.1% | 22.25B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,119 | -74 | 164,718 | 1.9% | 11.17B | 16 |
| 44 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,908 | -59 | 111,343 | 2.3% | 7.29B | 2 |
| 45 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,877 | +11 | 154,259 | 1.9% | 23.57B | 2 |
| 46 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,696 | -15 | 144,437 | 1.9% | 2.25B | 7 |
| 47 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,663 | +33 | 66,999 | 2.8% | 12.77B | 5 |
| 48 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,621 | +28 | 134,086 | 2.0% | 7.40B | 3 |
| 49 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,382 | +13 | 55,306 | 2.8% | 7.55B | 1 |
| 50 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,266 | +305 | 14,666 | 3.7% | 572.6M | 5 |
| 51 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,260 | +115 | 252,970 | 1.2% | 4.76B | 5 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,256 | +17 | 372,226 | 0.9% | 7.24B | 8 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,222 | -22 | 904,908 | 0.4% | 23.57B | 2 |
| 54 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,218 | -34 | 669,669 | 0.5% | 7.45B | 2 |
| 55 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,955 | +44 | 91,887 | 2.1% | 2.89B | 1 |
| 56 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,789 | +41 | 5,033,310 | 0.1% | 122.61B | 1 |
| 57 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,706 | +98 | 66,392 | 2.2% | 14.08B | 1 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,633 | -6 | 31,677 | 2.8% | 14.03B | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,527 | +90 | 148,560 | 1.4% | 7.24B | 4 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,324 | +117 | 413,781 | 0.6% | 1.20B | 1 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,256 | +16 | 35,546 | 2.4% | 2.61B | 3 |
| 62 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,186 | +113 | 417,300 | 0.6% | 353.4M | 1 |
| 63 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,148 | +117 | 398,846 | 0.6% | 3.21B | 1 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,914 | +46 | 57,903 | 1.8% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,515 | +22 | 84,280 | 1.4% | 9.15B | 1 |
| 66 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,447 | +18 | 39,954 | 1.7% | 321.0M | 2 |
| 67 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,232 | +19 | 49,185 | 1.5% | 9.24B | 4 |
| 68 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,155 | -55 | 17,943 | 1.8% | 12.19B | 2 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,154 | +2 | 32,657 | 1.6% | 22.64B | 1 |
| 70 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,098 | +98 | 85,319 | 1.1% | 2.22B | 1 |
| 71 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,033 | +38 | 23,492 | 1.6% | 22.64B | 1 |
| 72 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,020 | -14 | 78,192 | 1.1% | 7.45B | 1 |
| 73 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,951 | -8 | 8,242 | 1.8% | 1.51B | 6 |
| 74 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,923 | +27 | 5,300,656 | 0.0% | 7.25B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,840 | +5 | 105,849 | 0.9% | 7.45B | 1 |
| 76 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,827 | -12 | 14,933 | 1.6% | 3.83B | 5 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,800 | +3 | 99,676 | 0.9% | 30.68B | 1 |
| 78 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,796 | +2 | 452,415 | 0.3% | 40.43B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,706 | +5 | 355,831 | 0.4% | — | 3 |
| 80 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,661 | +22 | 49,565 | 1.1% | 7.77B | 1 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,639 | -26 | 176,715 | 0.6% | 12.25B | 6 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,590 | +2 | 157,612 | 0.6% | 1.10B | 1 |
| 83 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,552 | +3 | 301,116 | 0.4% | 6.74B | 2 |
| 84 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,544 | +24 | 22,495 | 1.3% | 11.17B | 5 |
| 85 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,529 | +134 | 32,826 | 1.2% | 56.7M | 1 |
| 86 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,490 | 0 | 145,265 | 0.6% | 13.02B | 1 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,485 | +2 | 184,466 | 0.5% | 6.74B | 1 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,435 | +32 | 7,737 | 1.3% | 9.82B | 1 |
| 89 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,404 | +256 | 8,859 | 1.3% | 27.43B | 3 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,399 | -12 | 173,357 | 0.5% | 11.51B | 7 |
| 91 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,375 | +33 | 30,571 | 1.1% | 11.17B | 5 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,318 | +32 | 20,045 | 1.1% | 4.30B | 2 |
| 93 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,305 | -58 | 12,013 | 1.2% | 31.59B | 6 |
| 94 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,287 | +7 | 57,294 | 0.8% | 1.35B | 3 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,181 | +17 | 19,699 | 1.0% | 12.25B | 3 |
| 96 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,112 | +44 | 52,678 | 0.7% | 7.24B | 5 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,099 | +4 | 227,932 | 0.3% | 35.13B | 4 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,093 | 0 | 9,427 | 1.0% | 9.15B | 1 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,062 | +18 | 800,424 | 0.1% | — | 3 |
| 100 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,022 | +44 | 51,534 | 0.7% | 7.24B | 1 |
| 101 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,014 | -12 | 8,045 | 0.9% | 28.84B | 3 |
| 102 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,002 | +2 | 18,746 | 0.8% | 1.20B | 2 |
| 103 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 986 | -72 | 95,669 | 0.5% | 1.35B | 8 |
| 104 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 982 | -81 | 7,426 | 0.9% | 4.30B | 3 |
| 105 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 903 | +24 | 14,270 | 0.8% | 353.4M | 2 |
| 106 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 889 | -23 | 38,817 | 0.6% | 70.55B | 3 |
| 107 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 869 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 108 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 807 | +9 | 16,150 | 0.7% | 1.54B | 4 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 778 | +5 | 20,048 | 0.6% | 3.20B | 2 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 656 | +4 | 44,022 | 0.5% | 12.19B | 2 |
| 111 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 647 | -296 | 37,526 | 0.5% | 27.23B | 3 |
| 112 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 616 | -159 | 81,331 | 0.3% | 8.03B | 3 |
| 113 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 582 | +1 | 217,852 | 0.2% | 12.19B | 3 |
| 114 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 571 | 0 | 1,497 | 0.6% | 31.58B | 2 |
| 115 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 531 | -64 | 70,280 | 0.3% | 8.03B | 3 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 530 | -1 | 3,797 | 0.5% | 8.03B | 3 |
| 117 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 526 | -12 | 232,640 | 0.2% | — | 2 |
| 118 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 524 | -6 | 2,985 | 0.5% | 560.9M | 2 |
| 119 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 493 | -2 | 12,489 | 0.4% | 70.55B | 2 |
| 120 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 490 | +4 | 76,134 | 0.3% | 7.04B | 4 |
| 121 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 489 | +2 | 32,504 | 0.4% | 40.43B | 2 |
| 122 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 449 | +1 | 27,259 | 0.4% | 9.24B | 2 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 438 | -5 | 39,088 | 0.3% | 7.48B | 2 |
| 124 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 434 | -16 | 13,826 | 0.4% | 4.33B | 3 |
| 125 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 414 | -4 | 321,944 | 0.1% | 7.24B | 2 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 410 | +3 | 21,751 | 0.3% | 2.61B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 403 | -4 | 7,334 | 0.4% | 31.59B | 6 |
| 128 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 385 | -36 | 2,991 | 0.4% | 30.68B | 1 |
| 129 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 369 | -7 | 11,745 | 0.3% | 27.23B | 2 |
| 130 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 357 | -3 | 44,424 | 0.2% | 7.70B | 5 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 333 | -12 | 41,654 | 0.2% | 11.17B | 1 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303 | -7 | 1,135 | 0.3% | — | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 278 | -1 | 106,911 | 0.1% | — | 3 |
| 134 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 270 | +1 | 21,455 | 0.2% | 9.24B | 2 |
| 135 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 265 | -24 | 2,459 | 0.3% | 4.02B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 258 | +2 | 16,415 | 0.2% | 7.29B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 251 | 0 | 19,446 | 0.2% | 68.98B | 2 |
| 138 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 228 | -5 | 1,234 | 0.2% | 27.23B | 3 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 216 | +15 | 5,196 | 0.2% | 11.51B | 5 |
| 140 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 202 | -5 | 38,619 | 0.1% | 70.55B | 3 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 199 | +1 | 2,356 | 0.2% | — | 1 |
| 142 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 198 | -1 | 5,324 | 0.2% | 353.4M | 2 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 143 | -3 | 7,152 | 0.1% | 1.20B | 2 |
| 144 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | 0 | 28,246 | 0.1% | 46.70B | 6 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | +2 | 4,839 | 0.1% | 70.55B | 3 |
| 146 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 130 | -8 | 4,882 | 0.1% | 437.8M | 1 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 129 | +2 | 1,011 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 92 | -1 | 1,239 | 0.1% | 560.9M | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 86 | +37 | 393 | 0.1% | 321.0M | 1 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | +1 | 190 | 0.1% | 437.8M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 34 | 0 | 258 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +2 | 145 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 28 | 0 | 223 | 0.0% | 15.17B | 3 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 23 | -1 | 165 | 0.0% | 8.16B | 3 |
| 155 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +1 | 355 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | +1 | 112 | 0.0% | 7.24B | 1 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,155,903 | 299,594,196 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,198,873 | 5,447,738 | 7 | 21.6% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 510,371 | 2,370,219 | 11 | 20.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 178,000 | 6,317,906 | 12 | 2.8% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,265 | 68,173 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,910 | 1,359,911 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 21,944 | 433,207 | 6 | 4.1% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,582 | 1,429,923 | 11 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 14,227 | 540,560 | 13 | 2.2% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 10,780 | 357,292 | 14 | 2.4% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,355 | 191,142 | 6 | 3.2% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 8,078 | 853,710 | 3 | 0.8% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,823 | 192,834 | 3 | 2.3% |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,841 | 368,145 | 10 | 1.2% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,804 | 151,711 | 2 | 2.3% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,670 | 694,170 | 2 | 0.6% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,621 | 134,086 | 1 | 2.0% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,565 | 487,343 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,258 | 656,947 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,148 | 23,672 | 4 | 2.5% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,273 | 152,963 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,236 | 103,055 | 4 | 1.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,117 | 1,159,421 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,435 | 7,737 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 490 | 76,134 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,397,021 | 57,714,422 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 585,851 | 603,147 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 382,940 | 593,470 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 123,944 | 4,147,297 | 17 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,265 | 68,173 | 20 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 30,268 | 680,990 | 26 |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,212 | 49,319 | 39 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,028 | 109,322 | 40 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,908 | 111,343 | 44 |
| 10 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,663 | 66,999 | 47 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,621 | 134,086 | 48 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,256 | 372,226 | 52 |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,218 | 669,669 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,955 | 91,887 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,706 | 66,392 | 57 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,324 | 413,781 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,800 | 99,676 | 77 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,706 | 355,831 | 79 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,639 | 176,715 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,590 | 157,612 | 82 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,435 | 7,737 | 88 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,305 | 12,013 | 93 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,287 | 57,294 | 94 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,062 | 800,424 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 490 | 76,134 | 120 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,265 | 68,173 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.6% | 1,198,873 | 5,447,738 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 20.7% | 510,371 | 2,370,219 | 3 |
| 4 | [LumiOpen](https://huggingface.co/LumiOpen) | 4.1% | 21,944 | 433,207 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,355 | 191,142 | 11 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 2.8% | 178,000 | 6,317,906 | 4 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,155,903 | 299,594,196 | 1 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 38,910 | 1,359,911 | 6 |
| 9 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.5% | 3,148 | 23,672 | 20 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 10,780 | 357,292 | 10 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.3% | 6,823 | 192,834 | 13 |
| 12 | [Almawave](https://huggingface.co/Almawave) | 2.3% | 5,804 | 151,711 | 15 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 14,227 | 540,560 | 9 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.0% | 4,621 | 134,086 | 17 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,435 | 7,737 | 24 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 5,841 | 368,145 | 14 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,236 | 103,055 | 22 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,582 | 1,429,923 | 8 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,273 | 152,963 | 21 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 8,078 | 853,710 | 12 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,565 | 487,343 | 18 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,670 | 694,170 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,258 | 656,947 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 490 | 76,134 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,117 | 1,159,421 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
