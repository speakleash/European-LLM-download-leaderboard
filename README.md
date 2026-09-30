# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-30
- **Generated at:** 2026-09-30T12:12:53Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,408,466 | +25,444 | 57,548,137 | 4.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,658,803 | +10,875 | 64,581,968 | 2.6% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 584,253 | +1,290 | 45,691,323 | 1.3% | 7.24B | 2 |
| 4 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 530,948 | +11,592 | 4,743,246 | 11.0% | 24.01B | 2 |
| 5 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 521,411 | +33,495 | 536,514 | 81.9% | 8.90B | 1 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 520,300 | -29,541 | 3,690,242 | 13.7% | 13.95B | 6 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 500,785 | -1,527 | 4,216,597 | 11.6% | 8.05B | 2 |
| 8 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 473,854 | +6,763 | 16,358,439 | 2.9% | 12.25B | 3 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 387,938 | +13,757 | 586,512 | 56.5% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 311,724 | +1,374 | 2,835,437 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 283,855 | -1,353 | 5,590,281 | 5.0% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 267,720 | +249 | 32,337,791 | 0.8% | 46.70B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 252,349 | +5,721 | 5,455,112 | 4.5% | 24.01B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 227,804 | +709 | 2,212,355 | 9.9% | 8.92B | 6 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,833 | -25 | 8,514,499 | 1.8% | 8.02B | 1 |
| 16 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 142,189 | -8,277 | 4,145,701 | 3.3% | 11.34B | 8 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 134,664 | +2,612 | 1,087,246 | 11.3% | 127.70B | 2 |
| 18 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 95,549 | -176 | 531,092 | 15.1% | 70.60B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,529 | +166 | 726,278 | 8.8% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 65,950 | +12 | 67,847 | 39.3% | — | 1 |
| 21 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 60,367 | -88,083 | 417,010 | 11.7% | 353.4M | 1 |
| 22 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 60,254 | -87,838 | 413,479 | 11.7% | 1.20B | 1 |
| 23 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 59,150 | +1,960 | 7,578,285 | 0.8% | 23.57B | 2 |
| 24 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 58,510 | -87,227 | 398,540 | 11.7% | 3.21B | 1 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,848 | -261 | 746,290 | 6.8% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 53,529 | +106 | 664,024 | 7.0% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 46,290 | +916 | 11,206,904 | 0.4% | 140.63B | 2 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,615 | -6,615 | 631,529 | 4.7% | 23.57B | 2 |
| 29 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 31,330 | -693 | 679,030 | 4.0% | 7.77B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 28,195 | +909 | 145,543 | 11.5% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,522 | +36 | 5,159,164 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,871 | +59 | 25,212 | 14.3% | 72.01B | 1 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,018 | -1,098 | 481,597 | 2.9% | 9.15B | 1 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,650 | -91 | 777,832 | 1.8% | 11.25B | 10 |
| 35 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,148 | +41 | 212,624 | 4.8% | — | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,069 | -186 | 73,247 | 8.1% | — | 5 |
| 37 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 12,140 | +146 | 508,011 | 2.0% | 7.24B | 8 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,548 | -635 | 349,358 | 2.3% | 125.03B | 1 |
| 39 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,809 | +793 | 133,274 | 4.2% | 7.48B | 5 |
| 40 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,515 | -911 | 326,375 | 2.0% | 24.01B | 2 |
| 41 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,785 | +295 | 4,925,582 | 0.2% | 122.61B | 1 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,491 | -538 | 109,016 | 3.1% | 8.42B | 7 |
| 43 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,002 | +510 | 49,026 | 4.0% | 8.03B | 7 |
| 44 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,715 | +22 | 30,113 | 4.4% | 33.12B | 1 |
| 45 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,276 | -69 | 164,372 | 2.0% | 11.17B | 16 |
| 46 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,014 | -39 | 111,311 | 2.4% | 7.29B | 2 |
| 47 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,856 | +405 | 5,377,683 | 0.1% | 22.25B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,693 | +192 | 144,116 | 1.9% | 2.25B | 7 |
| 49 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,654 | +53 | 66,804 | 2.8% | 12.77B | 5 |
| 50 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,430 | +102 | 133,725 | 1.9% | 7.40B | 3 |
| 51 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,305 | +23 | 669,535 | 0.6% | 7.45B | 2 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,239 | +15 | 55,135 | 2.7% | 7.55B | 1 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,212 | -89 | 904,696 | 0.4% | 23.57B | 2 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,178 | +22 | 371,930 | 0.9% | 7.24B | 8 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,156 | +74 | 252,720 | 1.2% | 4.76B | 5 |
| 56 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,856 | +53 | 91,682 | 2.0% | 2.89B | 1 |
| 57 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,779 | +446 | 14,087 | 3.3% | 572.6M | 5 |
| 58 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,695 | +279 | 5,033,106 | 0.1% | 122.61B | 1 |
| 59 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,632 | -8 | 31,641 | 2.8% | 14.03B | 1 |
| 60 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,527 | +26 | 152,882 | 1.4% | 23.57B | 2 |
| 61 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,513 | +89 | 66,196 | 2.1% | 14.08B | 1 |
| 62 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,346 | +95 | 148,270 | 1.3% | 7.24B | 4 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,175 | +63 | 35,352 | 2.3% | 2.61B | 3 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,829 | +21 | 57,717 | 1.8% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,494 | -23 | 84,229 | 1.4% | 9.15B | 1 |
| 66 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,395 | +73 | 39,827 | 1.7% | 321.0M | 2 |
| 67 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,207 | +38 | 49,020 | 1.5% | 9.24B | 4 |
| 68 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,128 | +42 | 32,543 | 1.6% | 22.64B | 1 |
| 69 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,017 | -49 | 8,031 | 1.9% | 1.51B | 6 |
| 70 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,003 | +42 | 78,061 | 1.1% | 7.45B | 1 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,981 | +209 | 17,691 | 1.7% | 12.19B | 2 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,964 | +29 | 23,289 | 1.6% | 22.64B | 1 |
| 73 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,905 | +60 | 85,126 | 1.0% | 2.22B | 1 |
| 74 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,878 | +28 | 14,830 | 1.6% | 3.83B | 5 |
| 75 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,857 | -11,629 | 5,300,542 | 0.0% | 7.25B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,807 | +43 | 105,727 | 0.9% | 7.45B | 1 |
| 77 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,791 | +7 | 452,366 | 0.3% | 40.43B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,734 | +39 | 99,523 | 0.9% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,687 | +47 | 355,713 | 0.4% | — | 3 |
| 80 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,661 | +49 | 176,611 | 0.6% | 12.25B | 6 |
| 81 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,626 | +23 | 49,470 | 1.1% | 7.77B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,565 | +43 | 157,502 | 0.6% | 1.10B | 1 |
| 83 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,531 | +49 | 301,002 | 0.4% | 6.74B | 2 |
| 84 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,485 | -40 | 22,367 | 1.2% | 11.17B | 5 |
| 85 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,470 | +44 | 145,160 | 0.6% | 13.02B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,464 | +42 | 184,362 | 0.5% | 6.74B | 1 |
| 87 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,429 | +36 | 173,285 | 0.5% | 11.51B | 7 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,391 | +78 | 7,674 | 1.3% | 9.82B | 1 |
| 89 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,381 | -2 | 12,009 | 1.2% | 31.59B | 6 |
| 90 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,350 | +73 | 32,627 | 1.0% | 56.7M | 1 |
| 91 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,331 | -44 | 30,460 | 1.0% | 11.17B | 5 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,325 | +77 | 19,981 | 1.1% | 4.30B | 2 |
| 93 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,287 | -28 | 9,387 | 1.2% | 9.15B | 1 |
| 94 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,268 | +22 | 57,245 | 0.8% | 1.35B | 3 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,129 | -25 | 19,604 | 0.9% | 12.25B | 3 |
| 96 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,065 | +17 | 227,854 | 0.3% | 35.13B | 4 |
| 97 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,059 | -36 | 95,646 | 0.5% | 1.35B | 8 |
| 98 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,035 | +13 | 8,028 | 1.0% | 28.84B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,034 | +8 | 800,351 | 0.1% | — | 3 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,025 | +17 | 7,362 | 1.0% | 4.30B | 3 |
| 101 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,024 | +43 | 52,581 | 0.7% | 7.24B | 5 |
| 102 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 989 | +4 | 18,707 | 0.8% | 1.20B | 2 |
| 103 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 970 | -2 | 8,383 | 0.9% | 27.43B | 3 |
| 104 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 932 | +43 | 51,439 | 0.6% | 7.24B | 1 |
| 105 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 919 | +12 | 37,490 | 0.7% | 27.23B | 3 |
| 106 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 897 | +32 | 38,749 | 0.6% | 70.55B | 3 |
| 107 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 873 | -18 | 14,212 | 0.8% | 353.4M | 2 |
| 108 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 869 | -112 | 2,828 | 0.8% | 31.59B | 6 |
| 109 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 799 | -36 | 81,289 | 0.4% | 8.03B | 3 |
| 110 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 777 | +119 | 16,107 | 0.7% | 1.54B | 4 |
| 111 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 769 | +7 | 20,025 | 0.6% | 3.20B | 2 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 669 | -2 | 43,997 | 0.5% | 12.19B | 2 |
| 113 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 629 | +6 | 70,264 | 0.4% | 8.03B | 3 |
| 114 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 623 | +97 | 1,497 | 0.6% | 31.58B | 2 |
| 115 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 584 | +9 | 217,832 | 0.2% | 12.19B | 3 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 534 | -8 | 232,623 | 0.2% | — | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 532 | +4 | 2,971 | 0.5% | 560.9M | 2 |
| 118 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 521 | +28 | 3,770 | 0.5% | 8.03B | 3 |
| 119 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 499 | +13 | 12,478 | 0.4% | 70.55B | 2 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 484 | -2 | 32,470 | 0.4% | 40.43B | 2 |
| 121 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 477 | -2 | 76,107 | 0.3% | 7.04B | 4 |
| 122 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 452 | -82 | 2,958 | 0.4% | 30.68B | 1 |
| 123 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 449 | -11 | 13,804 | 0.4% | 4.33B | 3 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 446 | -8 | 27,234 | 0.4% | 9.24B | 2 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 446 | 0 | 39,083 | 0.3% | 7.48B | 2 |
| 126 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 408 | -8 | 321,923 | 0.1% | 7.24B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 406 | -8 | 7,302 | 0.4% | 31.59B | 6 |
| 128 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 403 | -5 | 21,734 | 0.3% | 2.61B | 2 |
| 129 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 374 | -7 | 11,728 | 0.3% | 27.23B | 2 |
| 130 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 371 | -16 | 44,407 | 0.3% | 7.70B | 5 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 345 | +3 | 41,646 | 0.2% | 11.17B | 1 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 304 | +6 | 1,118 | 0.3% | — | 1 |
| 133 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 287 | -5 | 2,441 | 0.3% | 4.02B | 2 |
| 134 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 281 | -12 | 106,890 | 0.1% | — | 3 |
| 135 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 264 | -1 | 21,428 | 0.2% | 9.24B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 253 | -20 | 16,405 | 0.2% | 7.29B | 2 |
| 137 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 243 | +37 | 1,233 | 0.2% | 27.23B | 3 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 240 | 0 | 19,423 | 0.2% | 68.98B | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 202 | 0 | 38,610 | 0.1% | 70.55B | 3 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 199 | +5 | 5,171 | 0.2% | 11.51B | 5 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 198 | 0 | 5,317 | 0.2% | 353.4M | 2 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 194 | +5 | 2,343 | 0.2% | — | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 146 | +1 | 7,147 | 0.1% | 1.20B | 2 |
| 144 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 146 | +2 | 4,877 | 0.1% | 437.8M | 1 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | +1 | 28,238 | 0.1% | 46.70B | 6 |
| 146 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | -6 | 4,832 | 0.1% | 70.55B | 3 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 125 | +3 | 1,006 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 97 | +1 | 1,234 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 54 | -13 | 187 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 48 | +1 | 351 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 37 | 0 | 257 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | +1 | 143 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 20 | +1 | 215 | 0.0% | 15.17B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 354 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 18 | +1 | 159 | 0.0% | 8.16B | 3 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | -2 | 111 | 0.0% | 7.24B | 1 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 9 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,152,701 | 299,057,855 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,143,290 | 5,346,363 | 7 | 21.0% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 517,389 | 2,359,709 | 11 | 21.0% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 196,838 | 6,312,556 | 12 | 3.1% |
| 5 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 185,929 | 1,428,506 | 11 | 12.2% |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 65,950 | 67,847 | 1 | 39.3% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,924 | 1,357,452 | 5 | 2.7% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 21,550 | 432,518 | 6 | 4.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,767 | 539,556 | 13 | 2.2% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 10,372 | 356,555 | 14 | 2.3% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,569 | 190,679 | 6 | 3.3% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 8,115 | 853,323 | 3 | 0.9% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,308 | 192,506 | 3 | 2.5% |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,956 | 367,804 | 10 | 1.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,418 | 151,322 | 2 | 2.2% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,586 | 693,853 | 2 | 0.6% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,499 | 487,024 | 3 | 0.8% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,430 | 133,725 | 1 | 1.9% |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,279 | 23,636 | 4 | 2.7% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,218 | 656,715 | 2 | 0.4% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,327 | 152,891 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,224 | 102,855 | 4 | 1.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,089 | 1,159,287 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,391 | 7,674 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 477 | 76,107 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,408,466 | 57,548,137 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 521,411 | 536,514 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 387,938 | 586,512 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 142,189 | 4,145,701 | 16 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 65,950 | 67,847 | 20 |
| 6 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 60,367 | 417,010 | 21 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 31,330 | 679,030 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,491 | 109,016 | 42 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,002 | 49,026 | 43 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,014 | 111,311 | 46 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,654 | 66,804 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,430 | 133,725 | 50 |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,305 | 669,535 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,178 | 371,930 | 54 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,856 | 91,682 | 56 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,513 | 66,196 | 61 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,734 | 99,523 | 78 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,687 | 355,713 | 79 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,661 | 176,611 | 80 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,565 | 157,502 | 82 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,391 | 7,674 | 88 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,381 | 12,009 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,268 | 57,245 | 94 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,034 | 800,351 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 477 | 76,107 | 121 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.3% | 65,950 | 67,847 | 6 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 21.0% | 517,389 | 2,359,709 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.0% | 1,143,290 | 5,346,363 | 2 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | 12.2% | 185,929 | 1,428,506 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 4.0% | 21,550 | 432,518 | 8 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.3% | 9,569 | 190,679 | 11 |
| 7 | [speakleash](https://huggingface.co/speakleash) | 3.1% | 196,838 | 6,312,556 | 4 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,924 | 1,357,452 | 7 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,152,701 | 299,057,855 | 1 |
| 10 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.7% | 3,279 | 23,636 | 19 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,308 | 192,506 | 13 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.3% | 10,372 | 356,555 | 10 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 2.2% | 5,418 | 151,322 | 15 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 13,767 | 539,556 | 9 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,430 | 133,725 | 18 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,391 | 7,674 | 24 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,956 | 367,804 | 14 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,224 | 102,855 | 22 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,327 | 152,891 | 21 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.9% | 8,115 | 853,323 | 12 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,499 | 487,024 | 17 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,586 | 693,853 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,218 | 656,715 | 20 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 477 | 76,107 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,089 | 1,159,287 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
