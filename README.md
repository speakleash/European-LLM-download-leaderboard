# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-23
- **Generated at:** 2026-09-23T11:08:18Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,509,349 | -20,122 | 56,989,891 | 4.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,781,761 | +12,320 | 64,275,360 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 651,971 | +14,564 | 3,623,950 | 17.5% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 609,088 | +2,192 | 45,620,011 | 1.3% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 489,217 | +2,761 | 4,083,027 | 11.7% | 8.05B | 2 |
| 6 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 485,691 | +10,285 | 4,655,090 | 10.2% | 24.01B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 481,923 | -3,672 | 16,260,290 | 2.9% | 12.25B | 3 |
| 8 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 301,084 | +11,931 | 2,774,115 | 10.5% | 24.01B | 1 |
| 9 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 299,594 | +32,825 | 313,983 | 72.4% | 8.90B | 1 |
| 10 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 296,570 | +12,757 | 494,388 | 49.9% | 22.64B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 295,371 | -7,798 | 5,530,172 | 5.2% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 290,454 | -5,599 | 32,281,616 | 0.9% | 46.70B | 2 |
| 13 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 285,782 | -15,000 | 416,031 | 55.4% | 353.4M | 1 |
| 14 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 284,571 | -14,894 | 412,532 | 55.5% | 1.20B | 1 |
| 15 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 277,023 | -14,504 | 397,535 | 55.7% | 3.21B | 1 |
| 16 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 197,795 | +2,243 | 5,374,065 | 3.6% | 24.01B | 1 |
| 17 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 189,705 | +14,810 | 2,136,100 | 8.5% | 8.92B | 6 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 187,018 | -8,440 | 4,139,509 | 4.4% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,771 | +397 | 8,485,070 | 1.8% | 8.02B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 97,121 | +218 | 526,196 | 15.5% | 70.60B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 92,149 | +2,682 | 1,038,147 | 8.1% | 127.70B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,307 | +229 | 628,549 | 10.3% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,036 | +1,059 | 709,694 | 9.1% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,587 | +881 | 7,564,551 | 0.9% | 23.57B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,902 | -428 | 744,148 | 6.9% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 54,321 | -641 | 647,067 | 7.3% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,473 | +1,077 | 11,196,914 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,972 | +25 | 674,162 | 4.3% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,998 | +476 | 139,663 | 10.4% | 9.15B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 22,150 | +60 | 479,035 | 3.8% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,416 | -79 | 5,157,946 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,512 | +77 | 24,583 | 14.1% | 72.01B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,165 | -55 | 324,371 | 3.8% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,936 | +26 | 773,914 | 1.8% | 11.25B | 10 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,724 | +193 | 69,744 | 8.1% | — | 5 |
| 36 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,315 | +68 | 5,300,200 | 0.2% | 7.25B | 1 |
| 37 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,829 | -1,491 | 348,053 | 2.9% | 125.03B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,474 | +119 | 207,417 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,636 | +318 | 505,304 | 1.8% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,604 | +10 | 130,529 | 3.3% | 7.48B | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,228 | +369 | 107,818 | 3.5% | 8.42B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,566 | +241 | 4,923,125 | 0.1% | 122.61B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,201 | +92 | 163,094 | 2.0% | 11.17B | 16 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,074 | +230 | 46,956 | 3.5% | 8.03B | 7 |
| 45 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,021 | -34 | 110,895 | 2.4% | 7.29B | 2 |
| 46 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,007 | -9 | 65,392 | 3.0% | 12.77B | 4 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,424 | +13 | 28,726 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,133 | +99 | 142,866 | 1.7% | 2.25B | 7 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,123 | -75 | 903,207 | 0.4% | 23.57B | 2 |
| 50 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,041 | -67 | 668,440 | 0.5% | 7.45B | 2 |
| 51 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,034 | +188 | 5,376,157 | 0.1% | 22.25B | 1 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,866 | +160 | 251,751 | 1.1% | 4.76B | 5 |
| 53 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,836 | +38 | 370,816 | 0.8% | 7.24B | 8 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,693 | -7 | 132,398 | 1.6% | 7.40B | 3 |
| 55 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,627 | +80 | 54,395 | 2.3% | 7.55B | 1 |
| 56 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,604 | +131 | 90,938 | 1.9% | 2.89B | 1 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,138 | +5 | 31,034 | 2.4% | 14.03B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,896 | +90 | 56,916 | 1.8% | 1.60B | 5 |
| 59 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,851 | +84 | 65,345 | 1.7% | 14.08B | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,746 | +95 | 147,208 | 1.1% | 7.24B | 4 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,627 | +56 | 34,631 | 2.0% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,477 | +39 | 5,031,418 | 0.0% | 122.61B | 1 |
| 63 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,276 | +1,619 | 83,643 | 1.2% | 9.15B | 1 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,142 | +86 | 39,198 | 1.5% | 321.0M | 2 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,075 | +10 | 151,355 | 0.8% | 23.57B | 2 |
| 66 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,004 | +2 | 14,479 | 1.8% | 3.83B | 5 |
| 67 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,866 | +53 | 48,634 | 1.3% | 9.24B | 4 |
| 68 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,834 | +50 | 32,160 | 1.4% | 22.64B | 1 |
| 69 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,751 | +20 | 7,337 | 1.6% | 1.51B | 6 |
| 70 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,713 | +43 | 77,632 | 1.0% | 7.45B | 1 |
| 71 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,697 | +21 | 22,690 | 1.4% | 22.64B | 1 |
| 72 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,580 | +51 | 11,525 | 1.4% | 572.6M | 5 |
| 73 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,511 | -21 | 9,197 | 1.4% | 9.15B | 1 |
| 74 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,498 | +13 | 22,049 | 1.2% | 11.17B | 5 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,476 | +76 | 105,318 | 0.7% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,438 | +41 | 99,117 | 0.7% | 30.68B | 1 |
| 77 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,432 | -1 | 12,006 | 1.3% | 31.59B | 6 |
| 78 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,384 | +8 | 176,200 | 0.5% | 12.25B | 6 |
| 79 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,381 | +21 | 172,934 | 0.5% | 11.51B | 7 |
| 80 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,369 | +55 | 355,298 | 0.3% | — | 3 |
| 81 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,307 | +67 | 84,487 | 0.7% | 2.22B | 1 |
| 82 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,305 | +23 | 30,137 | 1.0% | 11.17B | 5 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,296 | +56 | 157,110 | 0.5% | 1.10B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,233 | +55 | 300,621 | 0.3% | 6.74B | 2 |
| 85 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,230 | +17 | 19,317 | 1.0% | 12.25B | 3 |
| 86 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,223 | -38 | 19,613 | 1.0% | 4.30B | 2 |
| 87 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,172 | +9 | 7,854 | 1.1% | 28.84B | 3 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,169 | +52 | 144,791 | 0.5% | 13.02B | 1 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,166 | +52 | 183,997 | 0.4% | 6.74B | 1 |
| 90 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,151 | +53 | 16,797 | 1.0% | 12.19B | 2 |
| 91 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,133 | -21 | 2,810 | 1.1% | 31.59B | 6 |
| 92 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,120 | +313 | 48,711 | 0.8% | 7.77B | 1 |
| 93 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,107 | +75 | 32,259 | 0.8% | 56.7M | 1 |
| 94 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,081 | +8 | 95,420 | 0.6% | 1.35B | 8 |
| 95 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,075 | +60 | 7,279 | 1.0% | 9.82B | 1 |
| 96 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,070 | +50 | 7,216 | 1.0% | 4.30B | 3 |
| 97 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,052 | +462 | 451,508 | 0.2% | 40.43B | 1 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,012 | +27 | 800,105 | 0.1% | — | 3 |
| 99 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,010 | +18 | 38,503 | 0.7% | 70.55B | 3 |
| 100 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,001 | +12 | 8,294 | 0.9% | 27.43B | 3 |
| 101 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 997 | +17 | 56,818 | 0.6% | 1.35B | 3 |
| 102 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 987 | -33 | 81,099 | 0.5% | 8.03B | 3 |
| 103 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 979 | +18 | 227,607 | 0.3% | 35.13B | 4 |
| 104 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 896 | +7 | 37,408 | 0.7% | 27.23B | 3 |
| 105 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 759 | +10 | 19,903 | 0.6% | 3.20B | 2 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 748 | -39 | 1,179 | 0.7% | 27.23B | 3 |
| 107 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 718 | +48 | 52,204 | 0.5% | 7.24B | 5 |
| 108 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 702 | -4 | 70,157 | 0.4% | 8.03B | 3 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 682 | +6 | 13,912 | 0.6% | 353.4M | 2 |
| 110 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 647 | -53 | 217,750 | 0.2% | 12.19B | 3 |
| 111 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 645 | +11 | 18,301 | 0.5% | 1.20B | 2 |
| 112 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 628 | +48 | 51,083 | 0.4% | 7.24B | 1 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 586 | -11 | 232,517 | 0.2% | — | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 581 | +24 | 43,849 | 0.4% | 12.19B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 572 | +11 | 2,842 | 0.6% | 30.68B | 1 |
| 116 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 551 | -152 | 12,403 | 0.5% | 70.55B | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 525 | +13 | 1,290 | 0.5% | 31.58B | 2 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 514 | 0 | 32,364 | 0.4% | 40.43B | 2 |
| 119 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 507 | -19 | 321,852 | 0.1% | 7.24B | 2 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 493 | +17 | 39,047 | 0.4% | 7.48B | 2 |
| 121 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 468 | -11 | 3,547 | 0.5% | 8.03B | 3 |
| 122 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 454 | 0 | 2,819 | 0.4% | 560.9M | 2 |
| 123 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 435 | -11 | 27,161 | 0.3% | 9.24B | 2 |
| 124 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 422 | -200 | 13,676 | 0.4% | 4.33B | 3 |
| 125 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 416 | +4 | 44,349 | 0.3% | 7.70B | 5 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 406 | +5 | 106,827 | 0.2% | — | 3 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 403 | -4 | 7,210 | 0.4% | 31.59B | 6 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 383 | +1 | 75,918 | 0.2% | 7.04B | 4 |
| 129 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 374 | +5 | 15,647 | 0.3% | 1.54B | 4 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 368 | -6 | 21,643 | 0.3% | 2.61B | 2 |
| 131 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 329 | -12 | 2,401 | 0.3% | 4.02B | 2 |
| 132 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 328 | +4 | 11,636 | 0.3% | 27.23B | 2 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 297 | +3 | 1,063 | 0.3% | — | 1 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 262 | -4 | 41,517 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 237 | 0 | 16,354 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 225 | -11 | 21,339 | 0.2% | 9.24B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 209 | +3 | 19,370 | 0.2% | 68.98B | 2 |
| 138 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 209 | -16 | 4,861 | 0.2% | 437.8M | 1 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 202 | 0 | 5,283 | 0.2% | 353.4M | 2 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 173 | +3 | 5,104 | 0.2% | 11.51B | 5 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 172 | +2 | 2,290 | 0.2% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 166 | +5 | 38,550 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 144 | +1 | 7,123 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 131 | +1 | 4,802 | 0.1% | 70.55B | 3 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 131 | +1 | 28,206 | 0.1% | 46.70B | 6 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 103 | -3 | 1,229 | 0.1% | 560.9M | 1 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 102 | -1 | 964 | 0.1% | — | 1 |
| 148 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 98 | -21 | 1,988 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 71 | -11 | 183 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 45 | +2 | 336 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | -2 | 251 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 140 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | -1 | 350 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 17 | +4 | 211 | 0.0% | 15.17B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 107 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 14 | +2 | 155 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11 | -22 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,450,959 | 297,378,255 | 30 | 2.8% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 908,779 | 4,981,130 | 7 | 17.9% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 853,330 | 1,423,609 | 11 | 56.0% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 423,211 | 2,249,262 | 11 | 18.0% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 237,776 | 6,292,758 | 12 | 3.7% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,791 | 1,349,611 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 18,252 | 427,221 | 6 | 3.5% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,811 | 536,861 | 13 | 2.0% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,650 | 188,163 | 6 | 3.3% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,960 | 353,782 | 14 | 2.0% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,137 | 191,214 | 3 | 2.8% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,230 | 851,390 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,844 | 366,433 | 10 | 1.3% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,343 | 692,668 | 2 | 0.5% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,158 | 149,832 | 2 | 1.7% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,693 | 132,398 | 1 | 1.6% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,631 | 485,898 | 3 | 0.6% |
| 18 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,493 | 23,316 | 4 | 2.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,602 | 655,919 | 2 | 0.3% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,213 | 1,158,819 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,078 | 152,238 | 2 | 0.8% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,041 | 102,325 | 4 | 1.0% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,075 | 7,279 | 1 | 1.0% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 383 | 75,918 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 98 | 1,988 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,509,349 | 56,989,891 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 489,217 | 4,083,027 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 296,570 | 494,388 | 10 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 285,782 | 416,031 | 13 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 187,018 | 4,139,509 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,972 | 674,162 | 28 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,228 | 107,818 | 41 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,074 | 46,956 | 44 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,021 | 110,895 | 45 |
| 10 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,007 | 65,392 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,041 | 668,440 | 50 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,836 | 370,816 | 53 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,693 | 132,398 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,604 | 90,938 | 56 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,851 | 65,345 | 59 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,438 | 99,117 | 76 |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,432 | 12,006 | 77 |
| 18 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,384 | 176,200 | 78 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,369 | 355,298 | 80 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,296 | 157,110 | 83 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,081 | 95,420 | 94 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,075 | 7,279 | 95 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,012 | 800,105 | 98 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 383 | 75,918 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 98 | 1,988 | 148 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 56.0% | 853,330 | 1,423,609 | 3 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 18.0% | 423,211 | 2,249,262 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 17.9% | 908,779 | 4,981,130 | 2 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.7% | 237,776 | 6,292,758 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.5% | 18,252 | 427,221 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.3% | 9,650 | 188,163 | 9 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,450,959 | 297,378,255 | 1 |
| 8 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,493 | 23,316 | 18 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,137 | 191,214 | 11 |
| 10 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,791 | 1,349,611 | 6 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,811 | 536,861 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.0% | 8,960 | 353,782 | 10 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.7% | 4,158 | 149,832 | 15 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,693 | 132,398 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,844 | 366,433 | 13 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.0% | 2,041 | 102,325 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 1.0% | 1,075 | 7,279 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,078 | 152,238 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,230 | 851,390 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.6% | 3,631 | 485,898 | 17 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,343 | 692,668 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,602 | 655,919 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 383 | 75,918 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,213 | 1,158,819 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 98 | 1,988 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
