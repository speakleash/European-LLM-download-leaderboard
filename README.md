# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-20
- **Generated at:** 2026-10-20T11:11:35Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,075,970 | -22,984 | 58,885,306 | 3.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,736,575 | +26,065 | 65,925,508 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 492,587 | -31,376 | 733,541 | 59.1% | 8.90B | 1 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 474,895 | -1,389 | 4,523,836 | 10.3% | 8.05B | 2 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 434,266 | -18,287 | 46,023,368 | 0.9% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 382,415 | +13,563 | 3,961,860 | 9.4% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 327,009 | -1,427 | 16,566,899 | 2.0% | 12.25B | 3 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 282,058 | +723 | 4,908,280 | 5.6% | 24.01B | 2 |
| 9 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 265,082 | +2,815 | 32,522,412 | 0.8% | 46.70B | 2 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,230 | -7,839 | 2,988,759 | 8.2% | 24.01B | 1 |
| 11 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,368 | -83 | 928,935 | 22.5% | 1.66B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 227,616 | +4,399 | 2,334,242 | 9.4% | 8.92B | 6 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,456 | +2,762 | 5,737,146 | 3.9% | 4.25B | 7 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 207,288 | -1,364 | 5,561,991 | 3.7% | 24.01B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 134,780 | -12,541 | 599,392 | 19.3% | 22.64B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,962 | +2,182 | 7,637,635 | 1.0% | 23.57B | 2 |
| 17 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,743 | -1,077 | 8,552,156 | 0.9% | 8.02B | 1 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,223 | +100 | 1,109,622 | 6.2% | 127.70B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,249 | -253 | 718,390 | 9.1% | 119.40B | 3 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 73,569 | +91 | 75,555 | 41.9% | — | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,106 | -144 | 774,132 | 8.1% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,363 | +967 | 11,256,850 | 0.6% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,229 | +52 | 119,398 | 24.7% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 36,859 | +1,308 | 708,091 | 4.6% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 30,819 | +378 | 354,773 | 6.8% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,814 | +163 | 237,548 | 9.1% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,369 | +57 | 43,612 | 17.0% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,890 | +73 | 546,223 | 3.4% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 21,084 | +120 | 4,158,921 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,677 | -259 | 155,804 | 6.9% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,411 | -90 | 642,061 | 1.9% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,077 | +110 | 786,958 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,908 | +3 | 81,445 | 7.1% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,644 | -19 | 516,129 | 1.9% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,393 | +24 | 19,641 | 9.5% | 27.43B | 3 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,038 | -109 | 489,176 | 1.9% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,290 | +260 | 4,932,606 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 8,203 | -1,067 | 138,039 | 3.4% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,660 | +128 | 5,383,347 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,936 | +275 | 18,332 | 5.9% | 572.6M | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,771 | +58 | 113,825 | 3.2% | 8.42B | 7 |
| 42 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,245 | +2,186 | 5,037,451 | 0.1% | 122.61B | 1 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,757 | -271 | 148,161 | 2.3% | 2.25B | 7 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,483 | +25 | 81,376 | 3.0% | 7.04B | 4 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,418 | +137 | 353,057 | 1.2% | 125.03B | 1 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,368 | -24 | 51,385 | 3.5% | 8.03B | 7 |
| 47 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,254 | -27 | 137,320 | 2.2% | 7.40B | 3 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,893 | -29 | 167,648 | 1.8% | 11.17B | 16 |
| 49 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,781 | +9 | 5,162,493 | 0.1% | 22.25B | 1 |
| 50 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,623 | -67 | 375,054 | 1.0% | 7.24B | 8 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,472 | +1 | 151,369 | 1.8% | 7.24B | 4 |
| 52 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,429 | -251 | 155,626 | 1.7% | 23.57B | 2 |
| 53 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,199 | -116 | 28,626 | 3.3% | 72.01B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,908 | +93 | 906,738 | 0.4% | 23.57B | 2 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,771 | +44 | 38,137 | 2.7% | 2.61B | 3 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,759 | +38 | 60,336 | 2.3% | 1.60B | 5 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,661 | -270 | 255,102 | 1.0% | 4.76B | 5 |
| 58 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,398 | +129 | 10,384 | 3.1% | 1.51B | 6 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,199 | -3 | 93,840 | 1.7% | 2.89B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,008 | -21 | 415,352 | 0.6% | 1.20B | 1 |
| 61 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,857 | -23 | 400,227 | 0.6% | 3.21B | 1 |
| 62 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,829 | -22 | 418,688 | 0.5% | 353.4M | 1 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,736 | +15 | 25,294 | 2.2% | 22.64B | 1 |
| 64 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,693 | +72 | 51,012 | 1.8% | 7.77B | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,674 | +32 | 41,691 | 1.9% | 13.29B | 3 |
| 66 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,651 | -224 | 670,644 | 0.3% | 7.45B | 2 |
| 67 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,624 | +67 | 34,787 | 1.9% | 56.7M | 1 |
| 68 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,505 | +9 | 178,578 | 0.9% | 12.25B | 6 |
| 69 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,502 | +8 | 84,489 | 1.4% | 9.15B | 1 |
| 70 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,370 | -11 | 33,353 | 1.8% | 14.03B | 1 |
| 71 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,276 | +8 | 30,943 | 1.7% | 33.12B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,089 | -39 | 18,776 | 1.8% | 12.19B | 2 |
| 73 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,034 | +145 | 16,272 | 1.7% | 3.83B | 5 |
| 74 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,967 | +20 | 452,960 | 0.4% | 40.43B | 1 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,893 | +5 | 100,856 | 0.9% | 30.68B | 1 |
| 76 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,873 | +5 | 79,353 | 1.0% | 7.45B | 1 |
| 77 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,859 | -4 | 50,379 | 1.2% | 9.24B | 4 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,828 | -46 | 106,976 | 0.9% | 7.45B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,826 | +6 | 356,999 | 0.4% | — | 3 |
| 80 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,771 | +7 | 21,356 | 1.5% | 4.30B | 2 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,672 | +10 | 158,645 | 0.6% | 1.10B | 1 |
| 82 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,667 | +7 | 33,715 | 1.2% | 22.64B | 1 |
| 83 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,656 | +40 | 5,301,715 | 0.0% | 7.25B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,643 | +12 | 302,151 | 0.4% | 6.74B | 2 |
| 85 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,642 | +6 | 55,905 | 1.1% | 7.55B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,593 | +7 | 185,481 | 0.6% | 6.74B | 1 |
| 87 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,579 | +8 | 146,263 | 0.6% | 13.02B | 1 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,573 | -2 | 53,668 | 1.0% | 7.24B | 5 |
| 89 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,493 | +2 | 52,477 | 1.0% | 7.24B | 1 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,478 | -39 | 174,307 | 0.5% | 11.51B | 7 |
| 91 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,478 | +41 | 8,636 | 1.4% | 9.82B | 1 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,476 | -85 | 23,428 | 1.2% | 11.17B | 5 |
| 93 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,415 | +72 | 228,929 | 0.4% | 35.13B | 4 |
| 94 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,391 | +31 | 8,508 | 1.3% | 4.30B | 3 |
| 95 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,374 | +21 | 19,615 | 1.1% | 1.20B | 2 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,245 | -12 | 31,301 | 0.9% | 11.17B | 5 |
| 97 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,206 | +62 | 39,651 | 0.9% | 70.55B | 3 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,189 | +20 | 57,968 | 0.8% | 1.35B | 3 |
| 99 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,150 | +8 | 10,300 | 1.0% | 9.15B | 1 |
| 100 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,072 | -11 | 111,916 | 0.5% | 7.29B | 2 |
| 101 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,057 | +15 | 801,085 | 0.1% | — | 3 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,019 | +8 | 14,887 | 0.9% | 353.4M | 2 |
| 103 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 853 | +20 | 16,490 | 0.7% | 1.54B | 4 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 782 | +161 | 8,596 | 0.7% | 28.84B | 3 |
| 105 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 747 | +56 | 218,439 | 0.2% | 12.19B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 691 | +6 | 81,749 | 0.4% | 8.03B | 3 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 670 | +3 | 96,031 | 0.3% | 1.35B | 8 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 656 | +8 | 14,282 | 0.6% | 4.33B | 3 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 587 | +7 | 4,117 | 0.6% | 8.03B | 3 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 575 | +13 | 44,387 | 0.4% | 12.19B | 2 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 469 | +23 | 21,790 | 0.4% | 9.24B | 2 |
| 112 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 463 | +14 | 3,266 | 0.4% | 30.68B | 1 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 444 | -35 | 20,332 | 0.4% | 3.20B | 2 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 407 | -7 | 32,754 | 0.3% | 40.43B | 2 |
| 115 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 364 | -111 | 27,498 | 0.3% | 9.24B | 2 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 356 | +4 | 232,855 | 0.1% | — | 2 |
| 117 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 350 | -1 | 322,179 | 0.1% | 7.24B | 2 |
| 118 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 340 | -6 | 21,974 | 0.3% | 2.61B | 2 |
| 119 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 338 | -58 | 11,963 | 0.3% | 27.23B | 2 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 326 | -50 | 39,314 | 0.2% | 7.48B | 2 |
| 121 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 318 | +3 | 1,361 | 0.3% | — | 1 |
| 122 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 315 | 0 | 1,486 | 0.3% | 27.23B | 3 |
| 123 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 310 | +4 | 41,805 | 0.2% | 11.17B | 1 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 308 | -24 | 37,698 | 0.2% | 27.23B | 3 |
| 125 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 290 | +1 | 3,087 | 0.3% | 560.9M | 2 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 289 | +1 | 107,097 | 0.1% | — | 3 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 264 | +8 | 7,430 | 0.2% | 31.59B | 6 |
| 128 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 257 | -11 | 5,354 | 0.2% | 11.51B | 5 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 253 | +4 | 12,646 | 0.2% | 70.55B | 2 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 252 | +2 | 5,112 | 0.2% | 437.8M | 1 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 244 | +5 | 44,570 | 0.2% | 7.70B | 5 |
| 132 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 237 | +9 | 2,637 | 0.2% | 4.02B | 2 |
| 133 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 233 | +2 | 70,381 | 0.1% | 8.03B | 3 |
| 134 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 223 | +2 | 19,582 | 0.2% | 68.98B | 2 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 211 | -2 | 2,489 | 0.2% | — | 1 |
| 137 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 210 | +6 | 5,010 | 0.2% | 70.55B | 3 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 188 | -10 | 16,535 | 0.2% | 7.29B | 2 |
| 139 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 159 | +4 | 28,355 | 0.1% | 46.70B | 6 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 155 | -2 | 5,430 | 0.1% | 353.4M | 2 |
| 141 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | 0 | 38,684 | 0.1% | 70.55B | 3 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 117 | 0 | 7,231 | 0.1% | 1.20B | 2 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105 | +3 | 1,063 | 0.1% | — | 1 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 81 | +1 | 411 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 45 | +1 | 1,273 | 0.0% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 35 | +4 | 242 | 0.0% | 15.17B | 3 |
| 149 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 34 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 150 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | +1 | 381 | 0.0% | 437.8M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | 0 | 210 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 29 | +5 | 182 | 0.0% | 8.16B | 3 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 124 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 266 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | -1 | 152 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,957,559 | 303,778,292 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,005,939 | 5,877,214 | 7 | 16.8% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 437,714 | 2,605,279 | 11 | 16.2% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 73,569 | 75,555 | 1 | 41.9% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 72,087 | 6,359,328 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,008 | 245,783 | 6 | 16.8% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 47,683 | 1,392,978 | 5 | 3.2% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,978 | 396,058 | 10 | 6.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,784 | 557,153 | 13 | 3.2% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,429 | 1,440,068 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,277 | 440,166 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,670 | 364,604 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,341 | 197,709 | 3 | 2.5% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,352 | 856,973 | 3 | 0.7% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,483 | 81,376 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,254 | 137,320 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,973 | 697,233 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,844 | 490,389 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,469 | 659,150 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,420 | 104,546 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,925 | 1,160,619 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,859 | 153,999 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,478 | 8,636 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 569 | 23,801 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,075,970 | 58,885,306 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 492,587 | 733,541 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,368 | 928,935 | 11 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 73,569 | 75,555 | 20 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,229 | 119,398 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 36,859 | 708,091 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,369 | 43,612 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 21,084 | 4,158,921 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,393 | 19,641 | 35 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,771 | 113,825 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,483 | 81,376 | 44 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,368 | 51,385 | 46 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,254 | 137,320 | 47 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,623 | 375,054 | 50 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,472 | 151,369 | 51 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,008 | 415,352 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,651 | 670,644 | 66 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,893 | 100,856 | 75 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,826 | 356,999 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,672 | 158,645 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,478 | 8,636 | 91 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,189 | 57,968 | 98 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,057 | 801,085 | 101 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 264 | 7,430 | 127 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 41.9% | 73,569 | 75,555 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 16.8% | 1,005,939 | 5,877,214 | 2 |
| 3 | [cjvt](https://huggingface.co/cjvt) | 16.8% | 58,008 | 245,783 | 6 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 16.2% | 437,714 | 2,605,279 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,978 | 396,058 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.2% | 47,683 | 1,392,978 | 7 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 20,784 | 557,153 | 9 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,483 | 81,376 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,277 | 440,166 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,670 | 364,604 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,341 | 197,709 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 6,957,559 | 303,778,292 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,254 | 137,320 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,478 | 8,636 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,420 | 104,546 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,429 | 1,440,068 | 10 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 72,087 | 6,359,328 | 5 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,844 | 490,389 | 18 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,859 | 153,999 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,352 | 856,973 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,973 | 697,233 | 17 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 569 | 23,801 | 24 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,469 | 659,150 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,925 | 1,160,619 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
