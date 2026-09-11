# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-11
- **Generated at:** 2026-09-11T10:56:42Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,529,275 | -9,740 | 55,959,463 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,487,624 | +13,553 | 63,578,386 | 2.3% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 610,333 | +25,927 | 3,475,241 | 17.1% | 13.95B | 6 |
| 4 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 524,426 | +27,889 | 16,087,024 | 3.2% | 12.25B | 3 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 512,045 | -14,175 | 3,886,673 | 12.8% | 8.05B | 2 |
| 6 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 452,502 | -25,018 | 5,435,306 | 8.2% | 4.25B | 7 |
| 7 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 447,837 | +33,077 | 45,312,218 | 1.0% | 7.24B | 2 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,449 | +76 | 414,605 | 68.7% | 353.4M | 1 |
| 9 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,066 | +231 | 411,110 | 68.7% | 1.20B | 1 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 345,649 | +41,544 | 4,462,383 | 7.6% | 24.01B | 2 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,770 | +89 | 396,198 | 68.7% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 298,357 | -1,882 | 32,157,251 | 0.9% | 46.70B | 2 |
| 13 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 253,439 | +184 | 4,102,555 | 6.0% | 11.34B | 8 |
| 14 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,328 | +3,681 | 2,625,390 | 9.2% | 24.01B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 212,649 | -13,018 | 2,042,979 | 9.9% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 204,973 | -854 | 8,401,581 | 2.4% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 145,420 | +6,159 | 1,028,883 | 12.9% | 127.70B | 2 |
| 18 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 132,700 | +14,299 | 327,620 | 31.0% | 22.64B | 1 |
| 19 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130,714 | +2,529 | 5,253,725 | 2.4% | 24.01B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 99,027 | +2,960 | 514,359 | 16.1% | 70.60B | 2 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,770 | -165 | 678,981 | 9.9% | 23.57B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,200 | +887 | 619,268 | 9.6% | 23.57B | 2 |
| 23 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,360 | +445 | 7,539,079 | 0.9% | 23.57B | 2 |
| 24 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,519 | -483 | 627,929 | 7.9% | 119.40B | 3 |
| 25 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 39,464 | +450 | 11,180,556 | 0.3% | 140.63B | 2 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 34,906 | +587 | 130,412 | 15.1% | 9.15B | 1 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 30,000 | +782 | 661,244 | 3.9% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,666 | +192 | 472,330 | 3.4% | 9.15B | 1 |
| 29 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,985 | -183 | 344,780 | 4.0% | 125.03B | 1 |
| 30 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,496 | +52 | 321,279 | 3.9% | 24.01B | 2 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,882 | +167 | 768,318 | 1.8% | 11.25B | 10 |
| 32 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,613 | -392 | 694,179 | 1.8% | 1.66B | 1 |
| 33 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 14,365 | 0 | 25,561 | 11.4% | 8.90B | 1 |
| 34 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,857 | -18 | 5,299,360 | 0.3% | 7.25B | 1 |
| 35 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 13,450 | 0 | 18,831 | 11.3% | 72.01B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,324 | +125 | 63,943 | 7.5% | — | 5 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 9,895 | -460 | 202,356 | 3.3% | — | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,432 | +118 | 500,823 | 1.6% | 7.24B | 8 |
| 39 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 9,061 | +52 | 105,040 | 4.4% | 8.42B | 5 |
| 40 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,958 | -111 | 4,920,031 | 0.2% | 122.61B | 1 |
| 41 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,137 | +20 | 30,805 | 3.9% | 14.03B | 1 |
| 42 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,116 | -783 | 5,141,310 | 0.1% | 22.25B | 1 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,931 | -375 | 141,007 | 2.0% | 2.25B | 7 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,847 | +111 | 161,295 | 1.9% | 11.17B | 16 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,624 | -77 | 45,011 | 3.2% | 8.03B | 7 |
| 46 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,460 | +26 | 28,503 | 3.5% | 33.12B | 1 |
| 47 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,428 | +32 | 63,132 | 2.7% | 11.77B | 4 |
| 48 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,188 | -77 | 666,497 | 0.5% | 7.45B | 2 |
| 49 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,158 | +233 | 89,616 | 2.2% | 2.89B | 1 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,678 | -239 | 5,374,110 | 0.1% | 22.25B | 1 |
| 51 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,662 | +17 | 901,495 | 0.4% | 23.57B | 2 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,614 | +67 | 130,296 | 1.6% | 7.40B | 3 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,500 | -52 | 55,614 | 2.2% | 1.60B | 5 |
| 54 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,427 | +41 | 53,898 | 2.2% | 7.55B | 1 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,401 | +157 | 250,286 | 1.0% | 4.76B | 5 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,181 | +22 | 368,848 | 0.7% | 7.24B | 8 |
| 57 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,101 | -12 | 10,981 | 2.8% | 572.6M | 5 |
| 58 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,728 | -2,201 | 5,029,987 | 0.1% | 122.61B | 1 |
| 59 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,438 | +24 | 21,991 | 2.0% | 22.64B | 1 |
| 60 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 2,351 | -3 | 124,232 | 1.0% | 7.48B | 5 |
| 61 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,345 | +176 | 38,468 | 1.7% | 321.0M | 2 |
| 62 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,263 | -77 | 145,510 | 0.9% | 7.24B | 4 |
| 63 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,209 | +31 | 107,222 | 1.1% | 7.29B | 2 |
| 64 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,123 | -1,190 | 13,669 | 1.9% | 3.83B | 5 |
| 65 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,051 | -232 | 19,117 | 1.7% | 4.30B | 2 |
| 66 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,900 | +51 | 33,047 | 1.4% | 2.61B | 3 |
| 67 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,862 | -3 | 6,812 | 1.7% | 4.30B | 3 |
| 68 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,813 | -31 | 8,789 | 1.7% | 9.15B | 1 |
| 69 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,809 | -35 | 6,611 | 1.7% | 1.51B | 6 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,744 | +18 | 16,116 | 1.5% | 12.19B | 2 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,700 | +15 | 76,862 | 1.0% | 7.45B | 1 |
| 72 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,696 | +89 | 63,239 | 1.0% | 14.08B | 1 |
| 73 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,600 | -108 | 18,785 | 1.3% | 12.25B | 3 |
| 74 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,597 | +490 | 31,470 | 1.2% | 22.64B | 1 |
| 75 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,468 | +7 | 172,439 | 0.5% | 11.51B | 7 |
| 76 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,414 | +23 | 7,276 | 1.3% | 28.84B | 3 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,389 | +10 | 175,539 | 0.5% | 12.25B | 6 |
| 78 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,271 | +69 | 21,341 | 1.0% | 11.17B | 5 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,251 | -1 | 98,397 | 0.6% | 30.68B | 1 |
| 80 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,234 | +99 | 29,662 | 1.0% | 11.17B | 5 |
| 81 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,221 | +5 | 47,517 | 0.8% | 9.24B | 4 |
| 82 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,205 | +15 | 95,143 | 0.6% | 1.35B | 8 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,185 | +7 | 104,534 | 0.6% | 7.45B | 1 |
| 84 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,118 | +3 | 43,541 | 0.8% | 12.19B | 2 |
| 85 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,111 | +11 | 354,598 | 0.2% | — | 3 |
| 86 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,096 | +122 | 31,853 | 0.8% | 56.7M | 1 |
| 87 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,094 | -6 | 48,144 | 0.7% | 7.77B | 1 |
| 88 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,061 | -1 | 7,790 | 1.0% | 27.43B | 3 |
| 89 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,054 | -54 | 81,883 | 0.6% | 9.15B | 1 |
| 90 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,039 | +6 | 300,003 | 0.3% | 6.74B | 2 |
| 91 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,037 | 0 | 156,444 | 0.4% | 1.10B | 1 |
| 92 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,014 | +4 | 37,265 | 0.7% | 27.23B | 3 |
| 93 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,013 | +8 | 80,872 | 0.6% | 8.03B | 3 |
| 94 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 988 | +13 | 2,729 | 1.0% | 30.68B | 1 |
| 95 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 975 | +27 | 799,614 | 0.1% | — | 3 |
| 96 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 963 | +7 | 144,192 | 0.4% | 13.02B | 1 |
| 97 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 962 | -22 | 217,467 | 0.3% | 12.19B | 3 |
| 98 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 961 | +6 | 183,397 | 0.3% | 6.74B | 1 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 954 | +42 | 56,495 | 0.6% | 1.35B | 3 |
| 100 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 942 | -4 | 12,228 | 0.8% | 70.55B | 2 |
| 101 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 939 | -6 | 38,209 | 0.7% | 70.55B | 3 |
| 102 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 850 | -87 | 83,288 | 0.5% | 2.22B | 1 |
| 103 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 766 | +27 | 227,141 | 0.2% | 35.13B | 4 |
| 104 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 759 | +2 | 1,061 | 0.8% | 27.23B | 3 |
| 105 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 751 | +3 | 70,039 | 0.4% | 8.03B | 3 |
| 106 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 655 | -34 | 6,551 | 0.6% | 9.82B | 1 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 630 | -5 | 13,494 | 0.6% | 4.33B | 3 |
| 108 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 613 | +27 | 450,831 | 0.1% | 40.43B | 1 |
| 109 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 599 | -7 | 321,648 | 0.1% | 7.24B | 2 |
| 110 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 585 | +13 | 149,581 | 0.2% | 23.57B | 2 |
| 111 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 570 | -3 | 3,356 | 0.6% | 8.03B | 3 |
| 112 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 552 | +25 | 17,923 | 0.5% | 1.20B | 2 |
| 113 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 508 | +293 | 11,052 | 0.5% | 31.59B | 6 |
| 114 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 505 | +19 | 13,557 | 0.4% | 353.4M | 2 |
| 115 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 501 | +5 | 32,165 | 0.4% | 40.43B | 2 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 473 | 0 | 232,269 | 0.1% | — | 2 |
| 117 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 460 | -44 | 51,617 | 0.3% | 7.24B | 5 |
| 118 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 445 | -27 | 7,018 | 0.4% | 31.59B | 6 |
| 119 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 433 | -26 | 1,981 | 0.4% | 31.59B | 6 |
| 120 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 413 | -16 | 44,198 | 0.3% | 7.70B | 5 |
| 121 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 407 | +8 | 19,499 | 0.3% | 3.20B | 2 |
| 122 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 407 | +9 | 106,704 | 0.2% | — | 3 |
| 123 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 404 | -42 | 50,544 | 0.3% | 7.24B | 1 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 392 | +1 | 38,789 | 0.3% | 7.48B | 2 |
| 125 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 389 | -25 | 2,619 | 0.4% | 560.9M | 2 |
| 126 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 362 | -8 | 2,315 | 0.4% | 4.02B | 2 |
| 127 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 345 | +9 | 15,487 | 0.3% | 1.54B | 4 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 334 | -1 | 75,728 | 0.2% | 7.04B | 4 |
| 129 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 333 | +6 | 4,845 | 0.3% | 437.8M | 1 |
| 130 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 322 | 0 | 1,048 | 0.3% | 31.58B | 2 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 282 | 0 | 26,885 | 0.2% | 9.24B | 2 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 278 | +9 | 41,436 | 0.2% | 11.17B | 1 |
| 133 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 224 | -10 | 21,232 | 0.2% | 9.24B | 2 |
| 134 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 191 | 0 | 870 | 0.2% | — | 1 |
| 135 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 190 | 0 | 1,937 | 0.2% | — | 1 |
| 136 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 183 | +2 | 5,208 | 0.2% | 353.4M | 2 |
| 137 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 175 | +3 | 21,389 | 0.1% | 2.61B | 2 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 164 | +9 | 16,237 | 0.1% | 7.29B | 2 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 161 | +8 | 5,040 | 0.2% | 11.51B | 5 |
| 140 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 153 | +2 | 11,432 | 0.1% | 27.23B | 2 |
| 141 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 152 | +4 | 19,271 | 0.1% | 68.98B | 2 |
| 142 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 140 | +7 | 1,219 | 0.1% | 560.9M | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 129 | +10 | 7,075 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 120 | -8 | 38,477 | 0.1% | 70.55B | 3 |
| 145 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 111 | +4 | 2,201 | 0.1% | — | 1 |
| 146 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 94 | +3 | 170 | 0.1% | 437.8M | 1 |
| 147 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 87 | -5 | 28,141 | 0.1% | 46.70B | 6 |
| 148 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 75 | 0 | 6,030 | 0.1% | 12.25B | 3 |
| 149 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 71 | +4 | 4,720 | 0.1% | 70.55B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63 | -2 | 898 | 0.1% | — | 1 |
| 151 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 62 | 0 | 314 | 0.1% | 321.0M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 51 | +1 | 243 | 0.1% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | +1 | 345 | 0.0% | 437.8M | 1 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | +2 | 129 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | 0 | 145 | 0.0% | 8.16B | 3 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 9 | -1 | 100 | 0.0% | 7.24B | 1 |
| 157 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 9 | 0 | 196 | 0.0% | 15.17B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,036,043 | 294,013,287 | 30 | 2.7% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,051,170 | 1,417,183 | 11 | 69.3% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 645,920 | 4,476,685 | 7 | 14.1% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 297,264 | 6,233,041 | 12 | 4.7% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 220,693 | 2,006,278 | 11 | 10.5% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 37,139 | 1,333,391 | 5 | 2.6% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 19,353 | 423,567 | 6 | 3.7% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,187 | 529,198 | 13 | 1.9% |
| 9 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 9,866 | 188,027 | 3 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,713 | 349,280 | 14 | 1.9% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,174 | 183,961 | 6 | 2.9% |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,467 | 364,127 | 10 | 1.6% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,073 | 847,893 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,780 | 690,496 | 2 | 0.5% |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,614 | 130,296 | 1 | 1.6% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,961 | 484,033 | 3 | 0.5% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,546 | 146,527 | 2 | 1.0% |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,261 | 101,467 | 4 | 1.1% |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,159 | 151,638 | 2 | 0.9% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,150 | 654,601 | 2 | 0.3% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,007 | 1,157,858 | 4 | 0.2% |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 1,708 | 21,099 | 4 | 1.4% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 655 | 6,551 | 1 | 0.6% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 334 | 75,728 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 190 | 1,937 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,529,275 | 55,959,463 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 512,045 | 3,886,673 | 5 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,449 | 414,605 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 253,439 | 4,102,555 | 13 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 132,700 | 327,620 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 30,000 | 661,244 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 9,061 | 105,040 | 39 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Viking 13B | 5,137 | 30,805 | 41 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,428 | 63,132 | 47 |
| 10 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,188 | 666,497 | 48 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,158 | 89,616 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,614 | 130,296 | 52 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,181 | 368,848 | 56 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 2,209 | 107,222 | 63 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 4B (2512) | 1,862 | 6,812 | 67 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 1,696 | 63,239 | 72 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,251 | 98,397 | 79 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,205 | 95,143 | 82 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,111 | 354,598 | 85 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,037 | 156,444 | 91 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 975 | 799,614 | 95 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 655 | 6,551 | 106 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 508 | 11,052 | 113 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 334 | 75,728 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 190 | 1,937 | 135 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.3% | 1,051,170 | 1,417,183 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 14.1% | 645,920 | 4,476,685 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 10.5% | 220,693 | 2,006,278 | 5 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.7% | 297,264 | 6,233,041 | 4 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.7% | 19,353 | 423,567 | 7 |
| 6 | [ilsp](https://huggingface.co/ilsp) | 3.4% | 9,866 | 188,027 | 9 |
| 7 | [cjvt](https://huggingface.co/cjvt) | 2.9% | 8,174 | 183,961 | 11 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,036,043 | 294,013,287 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 37,139 | 1,333,391 | 6 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,713 | 349,280 | 10 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1.9% | 12,187 | 529,198 | 8 |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.6% | 7,467 | 364,127 | 12 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,614 | 130,296 | 15 |
| 14 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1.4% | 1,708 | 21,099 | 22 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,261 | 101,467 | 18 |
| 16 | [Almawave](https://huggingface.co/Almawave) | 1.0% | 2,546 | 146,527 | 17 |
| 17 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,159 | 151,638 | 19 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 7,073 | 847,893 | 13 |
| 19 | [domyn](https://huggingface.co/domyn) | 0.6% | 655 | 6,551 | 23 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,961 | 484,033 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,780 | 690,496 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,150 | 654,601 | 20 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 334 | 75,728 | 24 |
| 24 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 190 | 1,937 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,007 | 1,157,858 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
