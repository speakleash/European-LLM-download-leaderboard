# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-19
- **Generated at:** 2026-10-19T12:39:15Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,098,954 | -42,359 | 58,834,754 | 3.6% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,710,510 | +26,482 | 65,866,704 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 523,963 | -32,104 | 733,213 | 62.9% | 8.90B | 1 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 476,284 | -1,980 | 4,510,735 | 10.3% | 8.05B | 2 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 452,553 | -4,882 | 46,012,455 | 1.0% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 368,852 | +14,947 | 3,940,729 | 9.1% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 328,436 | +9,474 | 16,560,606 | 2.0% | 12.25B | 3 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 281,335 | -3,908 | 4,903,915 | 5.6% | 24.01B | 2 |
| 9 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 262,267 | +3,031 | 32,510,004 | 0.8% | 46.70B | 2 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 261,069 | -12,493 | 2,987,452 | 8.5% | 24.01B | 1 |
| 11 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,451 | -62 | 928,623 | 22.5% | 1.66B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 223,217 | -571 | 2,326,293 | 9.2% | 8.92B | 6 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 222,694 | -2,285 | 5,729,138 | 3.8% | 4.25B | 7 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 208,652 | -12,046 | 5,558,129 | 3.7% | 24.01B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 147,321 | -13,133 | 599,184 | 21.1% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 77,820 | -2,424 | 8,550,866 | 0.9% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,123 | +156 | 1,109,092 | 6.2% | 127.70B | 2 |
| 18 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,780 | +218 | 7,634,244 | 1.0% | 23.57B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,502 | -489 | 717,564 | 9.1% | 119.40B | 3 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 73,478 | +403 | 75,464 | 41.9% | — | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,250 | -117 | 771,945 | 8.2% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,396 | +84 | 11,254,873 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,177 | -9 | 119,253 | 24.7% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 35,551 | +347 | 706,216 | 4.4% | 7.77B | 8 |
| 25 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,651 | -16 | 237,298 | 9.1% | — | 1 |
| 26 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 30,441 | +4,827 | 354,311 | 6.7% | 24.01B | 2 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,312 | +30 | 43,541 | 16.9% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,817 | +21 | 545,565 | 3.4% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,964 | +410 | 4,158,294 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,936 | -585 | 155,504 | 7.0% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,501 | +901 | 641,580 | 2.0% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,967 | +21 | 786,480 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,905 | -16 | 81,216 | 7.1% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,663 | +78 | 515,776 | 1.9% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,369 | -18 | 19,582 | 9.5% | 27.43B | 3 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,147 | -159 | 488,798 | 1.9% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,030 | +120 | 4,932,215 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,270 | -46 | 137,926 | 3.9% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,532 | +91 | 5,383,096 | 0.1% | 22.25B | 1 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,713 | +103 | 113,429 | 3.1% | 8.42B | 7 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,661 | +13 | 18,031 | 5.6% | 572.6M | 5 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,028 | -33 | 148,094 | 2.4% | 2.25B | 7 |
| 43 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,458 | +9 | 81,343 | 3.0% | 7.04B | 4 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,392 | -41 | 51,322 | 3.6% | 8.03B | 7 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,281 | +76 | 352,845 | 1.2% | 125.03B | 1 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,281 | +82 | 137,190 | 2.2% | 7.40B | 3 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,922 | -5 | 167,516 | 1.8% | 11.17B | 16 |
| 48 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,772 | +18 | 5,162,366 | 0.1% | 22.25B | 1 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,690 | +14 | 374,949 | 1.0% | 7.24B | 8 |
| 50 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,680 | +147 | 155,476 | 1.8% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,471 | +17 | 151,229 | 1.8% | 7.24B | 4 |
| 52 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,315 | +697 | 28,477 | 3.4% | 72.01B | 1 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,059 | +38 | 5,035,165 | 0.1% | 122.61B | 1 |
| 54 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,931 | -137 | 255,000 | 1.1% | 4.76B | 5 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,815 | +12 | 906,541 | 0.4% | 23.57B | 2 |
| 56 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,727 | -176 | 38,013 | 2.7% | 2.61B | 3 |
| 57 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,721 | +19 | 60,129 | 2.3% | 1.60B | 5 |
| 58 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,269 | +82 | 10,227 | 3.0% | 1.51B | 6 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,202 | +12 | 93,747 | 1.7% | 2.89B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,029 | +74 | 415,335 | 0.6% | 1.20B | 1 |
| 61 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,880 | +2 | 400,212 | 0.6% | 3.21B | 1 |
| 62 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,875 | -121 | 670,612 | 0.4% | 7.45B | 2 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,851 | -8 | 418,672 | 0.5% | 353.4M | 1 |
| 64 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,721 | +34 | 25,217 | 2.2% | 22.64B | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,642 | -10 | 41,606 | 1.9% | 13.29B | 3 |
| 66 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,621 | +27 | 50,932 | 1.7% | 7.77B | 1 |
| 67 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,557 | +36 | 34,675 | 1.9% | 56.7M | 1 |
| 68 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,496 | +5 | 178,525 | 0.9% | 12.25B | 6 |
| 69 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,494 | -42 | 84,473 | 1.4% | 9.15B | 1 |
| 70 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,381 | +16 | 33,336 | 1.8% | 14.03B | 1 |
| 71 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,268 | +16 | 30,918 | 1.7% | 33.12B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,128 | +40 | 18,726 | 1.8% | 12.19B | 2 |
| 73 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,947 | +26 | 452,932 | 0.4% | 40.43B | 1 |
| 74 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,889 | +8 | 16,105 | 1.6% | 3.83B | 5 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,888 | +18 | 100,780 | 0.9% | 30.68B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,874 | +5 | 106,915 | 0.9% | 7.45B | 1 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,868 | -12 | 79,291 | 1.0% | 7.45B | 1 |
| 78 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,863 | +9 | 50,327 | 1.2% | 9.24B | 4 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,820 | +10 | 356,935 | 0.4% | — | 3 |
| 80 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,764 | +13 | 21,333 | 1.5% | 4.30B | 2 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,662 | -8 | 158,588 | 0.6% | 1.10B | 1 |
| 82 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,660 | +17 | 33,658 | 1.2% | 22.64B | 1 |
| 83 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,636 | +9 | 55,884 | 1.0% | 7.55B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,631 | +14 | 302,095 | 0.4% | 6.74B | 2 |
| 85 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,616 | +84 | 5,301,627 | 0.0% | 7.25B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,586 | +19 | 185,426 | 0.6% | 6.74B | 1 |
| 87 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,575 | +4 | 53,620 | 1.0% | 7.24B | 5 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,571 | +20 | 146,209 | 0.6% | 13.02B | 1 |
| 89 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,561 | -19 | 23,399 | 1.3% | 11.17B | 5 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,517 | +50 | 174,272 | 0.6% | 11.51B | 7 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,491 | +3 | 52,428 | 1.0% | 7.24B | 1 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,437 | +8 | 8,590 | 1.3% | 9.82B | 1 |
| 93 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,360 | -36 | 8,468 | 1.3% | 4.30B | 3 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,353 | -9 | 19,585 | 1.1% | 1.20B | 2 |
| 95 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,343 | +20 | 228,834 | 0.4% | 35.13B | 4 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,257 | -16 | 31,270 | 1.0% | 11.17B | 5 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,169 | -13 | 57,912 | 0.7% | 1.35B | 3 |
| 98 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,144 | +7 | 39,575 | 0.8% | 70.55B | 3 |
| 99 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,142 | -6 | 10,283 | 1.0% | 9.15B | 1 |
| 100 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,083 | +19 | 111,897 | 0.5% | 7.29B | 2 |
| 101 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,042 | +22 | 801,049 | 0.1% | — | 3 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,011 | +5 | 14,870 | 0.9% | 353.4M | 2 |
| 103 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 833 | -3 | 16,466 | 0.7% | 1.54B | 4 |
| 104 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 691 | +56 | 218,375 | 0.2% | 12.19B | 3 |
| 105 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 685 | -13 | 81,729 | 0.4% | 8.03B | 3 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 667 | -36 | 96,012 | 0.3% | 1.35B | 8 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 648 | +167 | 14,252 | 0.6% | 4.33B | 3 |
| 108 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 621 | +19 | 8,328 | 0.6% | 28.84B | 3 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 580 | -21 | 4,109 | 0.6% | 8.03B | 3 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 562 | +107 | 44,371 | 0.4% | 12.19B | 2 |
| 111 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 479 | -3 | 20,327 | 0.4% | 3.20B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 475 | -1 | 27,490 | 0.4% | 9.24B | 2 |
| 113 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 449 | +16 | 3,247 | 0.4% | 30.68B | 1 |
| 114 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 446 | +18 | 21,762 | 0.4% | 9.24B | 2 |
| 115 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 414 | +18 | 32,752 | 0.3% | 40.43B | 2 |
| 116 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 396 | +31 | 11,943 | 0.4% | 27.23B | 2 |
| 117 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 376 | -9 | 39,311 | 0.3% | 7.48B | 2 |
| 118 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 352 | -8 | 232,850 | 0.1% | — | 2 |
| 119 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 351 | -13 | 322,174 | 0.1% | 7.24B | 2 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 346 | +14 | 21,970 | 0.3% | 2.61B | 2 |
| 121 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 332 | -4 | 37,695 | 0.2% | 27.23B | 3 |
| 122 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 315 | -2 | 1,483 | 0.3% | 27.23B | 3 |
| 123 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 315 | +7 | 1,352 | 0.3% | — | 1 |
| 124 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 306 | +7 | 41,801 | 0.2% | 11.17B | 1 |
| 125 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 289 | +1 | 3,086 | 0.3% | 560.9M | 2 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 288 | -9 | 107,090 | 0.1% | — | 3 |
| 127 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 268 | 0 | 5,349 | 0.3% | 11.51B | 5 |
| 128 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 256 | 0 | 7,422 | 0.2% | 31.59B | 6 |
| 129 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 250 | +1 | 5,110 | 0.2% | 437.8M | 1 |
| 130 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 249 | -9 | 12,638 | 0.2% | 70.55B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 239 | -5 | 44,557 | 0.2% | 7.70B | 5 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 231 | -26 | 70,376 | 0.1% | 8.03B | 3 |
| 133 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 228 | +20 | 2,625 | 0.2% | 4.02B | 2 |
| 134 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 221 | -6 | 19,577 | 0.2% | 68.98B | 2 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 213 | -4 | 2,483 | 0.2% | — | 1 |
| 137 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 204 | 0 | 5,002 | 0.2% | 70.55B | 3 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 198 | -2 | 16,528 | 0.2% | 7.29B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 157 | +1 | 5,428 | 0.1% | 353.4M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 155 | +2 | 28,347 | 0.1% | 46.70B | 6 |
| 141 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | -1 | 38,681 | 0.1% | 70.55B | 3 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 117 | -2 | 7,229 | 0.1% | 1.20B | 2 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 102 | +2 | 1,060 | 0.1% | — | 1 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 80 | -1 | 410 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | +3 | 1,272 | 0.0% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 148 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 34 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 149 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | +3 | 380 | 0.0% | 437.8M | 1 |
| 150 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | -1 | 237 | 0.0% | 15.17B | 3 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | 0 | 210 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 24 | -2 | 177 | 0.0% | 8.16B | 3 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 124 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 266 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | +1 | 152 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | -3,221 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | -2,619 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,954,459 | 303,577,613 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,038,198 | 5,862,353 | 7 | 17.4% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 450,463 | 2,603,534 | 11 | 16.7% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 73,478 | 75,464 | 1 | 41.9% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 73,347 | 6,357,212 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 57,999 | 245,551 | 6 | 16.8% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 46,561 | 1,390,926 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,858 | 395,854 | 10 | 6.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,727 | 556,557 | 13 | 3.2% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,362 | 1,439,751 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,164 | 439,869 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,659 | 364,257 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,328 | 197,297 | 3 | 2.5% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,617 | 856,818 | 3 | 0.7% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,458 | 81,343 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,281 | 137,190 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,041 | 697,123 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,819 | 490,223 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,451 | 659,030 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,392 | 104,441 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,903 | 1,160,566 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,836 | 153,924 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,437 | 8,590 | 1 | 1.3% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 561 | 23,793 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,098,954 | 58,834,754 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 523,963 | 733,213 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,451 | 928,623 | 11 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 73,478 | 75,464 | 20 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,177 | 119,253 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 35,551 | 706,216 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,312 | 43,541 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,964 | 4,158,294 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,369 | 19,582 | 35 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,713 | 113,429 | 40 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,458 | 81,343 | 43 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,392 | 51,322 | 44 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,281 | 137,190 | 46 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,690 | 374,949 | 49 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,471 | 151,229 | 51 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,029 | 415,335 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,875 | 670,612 | 62 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,888 | 100,780 | 75 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,820 | 356,935 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,662 | 158,588 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,437 | 8,590 | 92 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,169 | 57,912 | 97 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,042 | 801,049 | 101 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 256 | 7,422 | 128 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 41.9% | 73,478 | 75,464 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 17.4% | 1,038,198 | 5,862,353 | 2 |
| 3 | [cjvt](https://huggingface.co/cjvt) | 16.8% | 57,999 | 245,551 | 6 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 16.7% | 450,463 | 2,603,534 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,858 | 395,854 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 20,727 | 556,557 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 46,561 | 1,390,926 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,458 | 81,343 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,164 | 439,869 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,659 | 364,257 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,328 | 197,297 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 6,954,459 | 303,577,613 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,281 | 137,190 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,437 | 8,590 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,392 | 104,441 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 73,347 | 6,357,212 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,362 | 1,439,751 | 10 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,819 | 490,223 | 18 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,836 | 153,924 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,617 | 856,818 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,041 | 697,123 | 17 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,451 | 659,030 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 561 | 23,793 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,903 | 1,160,566 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
