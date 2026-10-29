# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-29
- **Generated at:** 2026-10-29T12:36:28Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,839,989 | -50,106 | 59,379,252 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,814,710 | -17,856 | 66,391,331 | 2.7% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 547,193 | +5,454 | 46,237,736 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 490,681 | +16,080 | 4,180,231 | 11.5% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 405,190 | +38 | 4,619,580 | 8.6% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 310,568 | +2,869 | 32,647,113 | 0.9% | 46.70B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 268,630 | -23,108 | 16,620,659 | 1.6% | 12.25B | 3 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 215,085 | -1,773 | 5,799,795 | 3.6% | 4.25B | 7 |
| 9 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 208,327 | +7,862 | 2,420,185 | 8.3% | 8.92B | 6 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 207,748 | -7,963 | 4,949,378 | 4.1% | 24.01B | 2 |
| 11 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 206,132 | -32,533 | 736,696 | 24.6% | 8.90B | 1 |
| 12 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 193,233 | +144 | 939,505 | 18.6% | 1.66B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 167,005 | -7,274 | 3,001,231 | 5.4% | 24.01B | 1 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 132,630 | -14,531 | 5,587,098 | 2.3% | 24.01B | 1 |
| 15 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 121,308 | +9,330 | 188,098 | 42.1% | 12.77B | 5 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 93,486 | +1,395 | 7,671,560 | 1.2% | 23.57B | 2 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,026 | +130 | 733,734 | 8.4% | 119.40B | 3 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,344 | -83 | 795,259 | 7.7% | 23.57B | 2 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,357 | -721 | 11,272,978 | 0.6% | 140.63B | 2 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,706 | -3,380 | 8,563,852 | 0.6% | 8.02B | 1 |
| 21 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 42,045 | +874 | 720,978 | 5.1% | 7.77B | 8 |
| 22 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,393 | +342 | 360,751 | 7.5% | 24.01B | 2 |
| 23 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,346 | +181 | 239,950 | 8.0% | — | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 27,316 | -3,681 | 1,114,512 | 2.2% | 127.70B | 2 |
| 25 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,538 | +54 | 44,142 | 17.0% | 12.25B | 3 |
| 26 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,295 | -463 | 4,165,951 | 0.5% | 11.34B | 8 |
| 27 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,821 | -537 | 548,820 | 2.7% | 70.60B | 2 |
| 28 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 16,931 | -13,682 | 601,281 | 2.4% | 22.64B | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,981 | +200 | 646,487 | 2.0% | 23.57B | 2 |
| 30 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,815 | -28 | 791,597 | 1.5% | 11.25B | 10 |
| 31 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,619 | +170 | 5,045,715 | 0.2% | 122.61B | 1 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,137 | -1,245 | 157,615 | 4.7% | 9.15B | 1 |
| 33 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,794 | +67 | 20,176 | 9.8% | 27.43B | 3 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,072 | -118 | 519,048 | 1.8% | 7.24B | 8 |
| 35 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,963 | +86 | 4,936,515 | 0.2% | 122.61B | 1 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,711 | -166 | 492,234 | 1.8% | 9.15B | 1 |
| 37 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,376 | -474 | 83,494 | 5.7% | — | 5 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,669 | +610 | 33,881 | 6.5% | 72.01B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,447 | -97 | 5,386,078 | 0.2% | 22.25B | 1 |
| 40 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,355 | +11 | 76,202 | 4.7% | — | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,845 | +124 | 115,848 | 3.2% | 8.42B | 7 |
| 42 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,692 | -269 | 20,582 | 5.5% | 572.6M | 5 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,312 | +104 | 150,416 | 2.5% | 2.25B | 7 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,054 | +98 | 355,346 | 1.3% | 125.03B | 1 |
| 45 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,029 | -791 | 139,230 | 2.5% | 7.48B | 5 |
| 46 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,499 | +14 | 81,604 | 3.0% | 7.04B | 4 |
| 47 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,339 | +370 | 13,366 | 4.7% | 1.51B | 6 |
| 48 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,808 | -54 | 138,520 | 2.0% | 7.40B | 3 |
| 49 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,480 | +188 | 19,306 | 3.8% | 3.83B | 5 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,424 | -9 | 152,679 | 1.8% | 7.24B | 4 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,415 | +43 | 376,334 | 0.9% | 7.24B | 8 |
| 52 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,365 | -67 | 168,723 | 1.6% | 11.17B | 16 |
| 53 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,310 | +11 | 5,163,460 | 0.1% | 22.25B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,188 | +120 | 908,873 | 0.4% | 23.57B | 2 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,934 | +7 | 39,269 | 2.8% | 2.61B | 3 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,912 | -4 | 61,624 | 2.4% | 1.60B | 5 |
| 57 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,826 | +54 | 156,703 | 1.5% | 23.57B | 2 |
| 58 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,780 | +30 | 256,495 | 1.1% | 4.76B | 5 |
| 59 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,487 | +207 | 36,098 | 2.6% | 56.7M | 1 |
| 60 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,250 | -516 | 52,269 | 2.1% | 8.03B | 7 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,117 | -11 | 94,785 | 1.6% | 2.89B | 1 |
| 62 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,834 | -5 | 42,648 | 2.0% | 13.29B | 3 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,690 | +25 | 25,969 | 2.1% | 22.64B | 1 |
| 64 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,683 | +6 | 34,322 | 2.0% | 14.03B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,463 | +3 | 179,067 | 0.9% | 12.25B | 6 |
| 66 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,432 | +137 | 5,302,969 | 0.0% | 7.25B | 1 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,243 | +121 | 51,705 | 1.5% | 7.77B | 1 |
| 68 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,096 | -83 | 22,076 | 1.7% | 4.30B | 2 |
| 69 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,094 | -11 | 415,561 | 0.4% | 1.20B | 1 |
| 70 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,036 | +67 | 229,886 | 0.6% | 35.13B | 4 |
| 71 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,028 | +13 | 51,040 | 1.3% | 9.24B | 4 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,970 | +18 | 101,484 | 1.0% | 30.68B | 1 |
| 73 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,940 | +15 | 357,644 | 0.4% | — | 3 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,916 | +13 | 79,970 | 1.1% | 7.45B | 1 |
| 75 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,877 | -16 | 418,874 | 0.4% | 353.4M | 1 |
| 76 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,872 | -67 | 400,402 | 0.4% | 3.21B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,860 | +13 | 107,580 | 0.9% | 7.45B | 1 |
| 78 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,779 | +28 | 9,140 | 1.6% | 4.30B | 3 |
| 79 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,772 | -136 | 19,462 | 1.5% | 12.19B | 2 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,757 | +16 | 34,291 | 1.3% | 22.64B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,739 | +15 | 159,234 | 0.7% | 1.10B | 1 |
| 82 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,723 | +7 | 302,717 | 0.4% | 6.74B | 2 |
| 83 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,680 | +14 | 186,036 | 0.6% | 6.74B | 1 |
| 84 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,656 | +8 | 146,809 | 0.7% | 13.02B | 1 |
| 85 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,548 | -2 | 54,123 | 1.0% | 7.24B | 5 |
| 86 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,540 | +33 | 40,282 | 1.1% | 70.55B | 3 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,476 | +3 | 52,911 | 1.0% | 7.24B | 1 |
| 88 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,460 | -169 | 670,945 | 0.2% | 7.45B | 2 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,426 | -60 | 9,099 | 1.3% | 9.82B | 1 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,388 | -36 | 174,648 | 0.5% | 11.51B | 7 |
| 91 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,335 | -6 | 31,446 | 1.0% | 33.12B | 1 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,323 | -16 | 23,687 | 1.1% | 11.17B | 5 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,295 | +55 | 801,642 | 0.1% | — | 3 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,198 | +8 | 19,903 | 1.0% | 1.20B | 2 |
| 95 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,130 | +11 | 10,515 | 1.0% | 9.15B | 1 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,107 | -8 | 31,561 | 0.8% | 11.17B | 5 |
| 97 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,074 | -11 | 56,204 | 0.7% | 7.55B | 1 |
| 98 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,073 | +14 | 9,100 | 1.0% | 28.84B | 3 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,041 | +1 | 58,279 | 0.7% | 1.35B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 993 | +3 | 15,203 | 0.9% | 353.4M | 2 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 909 | +16 | 453,271 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 850 | +35 | 218,681 | 0.3% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 812 | +11 | 44,808 | 0.6% | 12.19B | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 762 | -19 | 112,070 | 0.4% | 7.29B | 2 |
| 105 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 697 | +51 | 14,501 | 0.6% | 4.33B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 680 | +17 | 81,965 | 0.4% | 8.03B | 3 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 639 | -119 | 16,744 | 0.5% | 1.54B | 4 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 625 | +13 | 96,263 | 0.3% | 1.35B | 8 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 561 | +139 | 20,586 | 0.5% | 3.20B | 2 |
| 110 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 552 | +81 | 233,175 | 0.2% | — | 2 |
| 111 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 519 | +7 | 3,475 | 0.5% | 30.68B | 1 |
| 112 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 507 | +8 | 21,934 | 0.4% | 9.24B | 2 |
| 113 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 497 | -25 | 1,730 | 0.5% | 27.23B | 3 |
| 114 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 493 | -40 | 4,262 | 0.5% | 8.03B | 3 |
| 115 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 424 | +8 | 1,540 | 0.4% | — | 1 |
| 116 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 407 | +52 | 27,641 | 0.3% | 9.24B | 2 |
| 117 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 375 | +1 | 32,841 | 0.3% | 40.43B | 2 |
| 118 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 370 | +45 | 2,811 | 0.4% | 4.02B | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 331 | +13 | 22,064 | 0.3% | 2.61B | 2 |
| 120 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 330 | +9 | 5,501 | 0.3% | 11.51B | 5 |
| 121 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 318 | +16 | 12,046 | 0.3% | 27.23B | 2 |
| 122 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 317 | +2 | 84,546 | 0.2% | 9.15B | 1 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 307 | +9 | 107,196 | 0.1% | — | 3 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 306 | -16 | 37,795 | 0.2% | 27.23B | 3 |
| 125 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 300 | -1 | 322,223 | 0.1% | 7.24B | 2 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 293 | 0 | 39,376 | 0.2% | 7.48B | 2 |
| 127 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 272 | -5 | 5,149 | 0.3% | 437.8M | 1 |
| 128 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 236 | +9 | 19,659 | 0.2% | 68.98B | 2 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 223 | -28 | 12,700 | 0.2% | 70.55B | 2 |
| 130 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 222 | +3 | 44,629 | 0.2% | 7.70B | 5 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 219 | +1 | 41,865 | 0.2% | 11.17B | 1 |
| 132 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 211 | -1 | 5,043 | 0.2% | 70.55B | 3 |
| 133 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 195 | 0 | 2,535 | 0.2% | — | 1 |
| 134 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 186 | +1 | 16,591 | 0.2% | 7.29B | 2 |
| 135 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 183 | -2 | 7,461 | 0.2% | 31.59B | 6 |
| 136 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 177 | -5 | 70,441 | 0.1% | 8.03B | 3 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 177 | +24 | 5,493 | 0.2% | 353.4M | 2 |
| 138 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 156 | +3 | 28,392 | 0.1% | 46.70B | 6 |
| 139 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 155 | -7 | 3,125 | 0.2% | 560.9M | 2 |
| 140 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 142 | 0 | 12,151 | 0.1% | 31.59B | 6 |
| 141 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 6,171 | 0.1% | 12.25B | 3 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 133 | -1 | 1,139 | 0.1% | — | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 103 | 0 | 7,249 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 98 | -1 | 38,708 | 0.1% | 70.55B | 3 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 81 | -1 | 432 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 69 | -1 | 1,303 | 0.1% | 560.9M | 1 |
| 147 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 43 | -1 | 397 | 0.0% | 437.8M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,854 | 0.0% | 31.59B | 6 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 39 | -1 | 254 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 34 | 0 | 193 | 0.0% | 8.16B | 3 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | -1 | 220 | 0.0% | 437.8M | 1 |
| 152 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 131 | 0.0% | 7.24B | 1 |
| 153 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 275 | 0.0% | 437.8M | 1 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 158 | 0.0% | 437.8M | 1 |
| 155 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 6 | -99 | 1,503 | 0.0% | 31.58B | 2 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,691,947 | 305,714,974 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 654,323 | 5,992,231 | 7 | 10.7% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 270,381 | 2,627,710 | 11 | 9.9% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 125,339 | 315,993 | 6 | 30.1% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 67,635 | 6,379,930 | 12 | 1.0% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 51,884 | 1,409,211 | 5 | 3.4% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,274 | 398,066 | 10 | 6.1% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,605 | 561,150 | 13 | 3.3% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,396 | 1,443,828 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 11,918 | 444,409 | 6 | 2.2% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,560 | 368,075 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,355 | 76,202 | 1 | 4.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,360 | 199,853 | 3 | 2.5% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,499 | 81,604 | 1 | 3.0% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,236 | 858,495 | 3 | 0.5% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,075 | 492,079 | 3 | 0.9% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,808 | 138,520 | 1 | 2.0% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,715 | 698,557 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,663 | 660,361 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,562 | 105,406 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,390 | 1,161,672 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,666 | 154,542 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,426 | 9,099 | 1 | 1.3% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 374 | 23,969 | 4 | 0.3% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,839,989 | 59,379,252 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 405,190 | 4,619,580 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 193,233 | 939,505 | 12 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 121,308 | 188,098 | 15 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 42,045 | 720,978 | 21 |
| 6 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,538 | 44,142 | 25 |
| 7 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,295 | 4,165,951 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,794 | 20,176 | 33 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,355 | 76,202 | 40 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,845 | 115,848 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,499 | 81,604 | 46 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,808 | 138,520 | 48 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,424 | 152,679 | 50 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,415 | 376,334 | 51 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,487 | 36,098 | 59 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,250 | 52,269 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,970 | 101,484 | 72 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,940 | 357,644 | 73 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,916 | 79,970 | 74 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,739 | 159,234 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,426 | 9,099 | 89 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,295 | 801,642 | 93 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,041 | 58,279 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 183 | 7,461 | 135 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 30.1% | 125,339 | 315,993 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 10.7% | 654,323 | 5,992,231 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 9.9% | 270,381 | 2,627,710 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,274 | 398,066 | 7 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | 4.7% | 8,355 | 76,202 | 12 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.4% | 51,884 | 1,409,211 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,605 | 561,150 | 8 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,499 | 81,604 | 14 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,560 | 368,075 | 11 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,360 | 199,853 | 13 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.2% | 11,918 | 444,409 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,691,947 | 305,714,974 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.0% | 4,808 | 138,520 | 17 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,426 | 9,099 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,562 | 105,406 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.0% | 67,635 | 6,379,930 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,396 | 1,443,828 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,075 | 492,079 | 16 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,666 | 154,542 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,715 | 698,557 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,236 | 858,495 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,663 | 660,361 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.3% | 374 | 23,969 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,390 | 1,161,672 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
