# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-11
- **Generated at:** 2026-10-11T12:25:12Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,319,744 | -11,285 | 58,356,155 | 4.0% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,650,386 | +25,412 | 65,277,476 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 698,867 | +1,022 | 726,014 | 84.6% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 522,249 | -76,442 | 45,924,437 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 485,147 | +929 | 4,388,200 | 10.8% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 391,275 | -16,454 | 16,503,111 | 2.4% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 349,754 | -29,449 | 4,843,880 | 7.1% | 24.01B | 2 |
| 8 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 318,657 | +15,137 | 2,953,439 | 10.4% | 24.01B | 1 |
| 9 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 317,081 | -4,791 | 3,807,092 | 8.1% | 13.95B | 6 |
| 10 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 256,908 | -12,546 | 32,432,828 | 0.8% | 46.70B | 2 |
| 11 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 255,508 | -14,115 | 596,831 | 36.7% | 22.64B | 1 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 254,806 | -1,986 | 5,513,329 | 4.5% | 24.01B | 1 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 230,974 | +94 | 925,622 | 22.5% | 1.66B | 1 |
| 14 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,035 | -3,710 | 5,675,748 | 4.0% | 4.25B | 7 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 224,031 | -4,984 | 2,275,926 | 9.4% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130,642 | -5,556 | 8,540,111 | 1.5% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 80,484 | -1,177 | 710,678 | 9.9% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,195 | -467 | 1,103,016 | 6.0% | 127.70B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,820 | -861 | 753,213 | 8.4% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 67,012 | +674 | 68,950 | 39.7% | — | 1 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,927 | +30 | 7,608,349 | 0.9% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,537 | -284 | 11,240,539 | 0.5% | 140.63B | 2 |
| 23 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 41,174 | -9,000 | 4,153,021 | 1.0% | 11.34B | 8 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 26,972 | -1,275 | 689,700 | 3.4% | 7.77B | 8 |
| 25 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 23,229 | -980 | 539,218 | 3.6% | 70.60B | 2 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 20,335 | +794 | 39,273 | 14.6% | 12.25B | 3 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,886 | +70 | 5,161,318 | 0.4% | 22.25B | 1 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,548 | -404 | 148,796 | 7.1% | 9.15B | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,485 | -709 | 637,763 | 2.4% | 23.57B | 2 |
| 30 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,133 | -595 | 220,730 | 5.3% | — | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,835 | -74 | 782,770 | 1.6% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,340 | -407 | 77,856 | 7.5% | — | 5 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,252 | -134 | 486,143 | 2.3% | 9.15B | 1 |
| 34 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 12,447 | +194 | 136,752 | 5.3% | 7.48B | 5 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,828 | +160 | 333,351 | 2.7% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,111 | +87 | 512,386 | 1.8% | 7.24B | 8 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,055 | -12 | 4,929,307 | 0.2% | 122.61B | 1 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,050 | +98 | 5,381,260 | 0.1% | 22.25B | 1 |
| 39 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,210 | +38 | 17,223 | 5.3% | 572.6M | 5 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,193 | -500 | 26,903 | 4.9% | 72.01B | 1 |
| 41 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,973 | -314 | 351,209 | 1.3% | 125.03B | 1 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,630 | -150 | 146,863 | 2.3% | 2.25B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,408 | -11 | 110,773 | 2.6% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,329 | +63 | 135,770 | 2.3% | 7.40B | 3 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,999 | +68 | 68,278 | 3.0% | 12.77B | 5 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,989 | +8 | 154,582 | 2.0% | 23.57B | 2 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,831 | +26 | 166,349 | 1.8% | 11.17B | 16 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,831 | +8 | 49,938 | 3.2% | 8.03B | 7 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,751 | +101 | 373,726 | 1.0% | 7.24B | 8 |
| 50 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,404 | +16 | 12,200 | 3.9% | 27.43B | 3 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,359 | +90 | 149,968 | 1.7% | 7.24B | 4 |
| 52 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,311 | -100 | 111,737 | 2.0% | 7.29B | 2 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,181 | +4 | 5,034,264 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,116 | -41 | 905,700 | 0.4% | 23.57B | 2 |
| 55 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,720 | -119 | 67,200 | 2.2% | 14.08B | 1 |
| 56 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,656 | -25 | 670,296 | 0.5% | 7.45B | 2 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,606 | -17 | 254,031 | 1.0% | 4.76B | 5 |
| 58 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,481 | -425 | 418,539 | 0.7% | 353.4M | 1 |
| 59 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,456 | -456 | 415,044 | 0.7% | 1.20B | 1 |
| 60 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,456 | -406 | 400,095 | 0.7% | 3.21B | 1 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,302 | -45 | 36,537 | 2.4% | 2.61B | 3 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,130 | +3 | 92,868 | 1.6% | 2.89B | 1 |
| 63 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,113 | -155 | 58,976 | 2.0% | 1.60B | 5 |
| 64 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,769 | +13 | 86,135 | 1.5% | 2.22B | 1 |
| 65 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,640 | +21 | 9,267 | 2.4% | 1.51B | 6 |
| 66 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,535 | +168 | 24,580 | 2.0% | 22.64B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,534 | +23 | 84,425 | 1.4% | 9.15B | 1 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,245 | +24 | 49,813 | 1.5% | 9.24B | 4 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,219 | +300 | 50,384 | 1.5% | 7.77B | 1 |
| 70 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,203 | +23 | 40,756 | 1.6% | 13.29B | 3 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,123 | -11 | 18,285 | 1.8% | 12.19B | 2 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,989 | +174 | 30,501 | 1.5% | 33.12B | 1 |
| 73 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,896 | +62 | 33,809 | 1.4% | 56.7M | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,876 | +20 | 78,796 | 1.0% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,832 | +26 | 106,420 | 0.9% | 7.45B | 1 |
| 76 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,808 | -2 | 15,534 | 1.6% | 3.83B | 5 |
| 77 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,807 | -1 | 452,675 | 0.3% | 40.43B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,798 | +13 | 100,246 | 0.9% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,740 | +19 | 356,397 | 0.4% | — | 3 |
| 80 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,672 | +15 | 5,301,066 | 0.0% | 7.25B | 1 |
| 81 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,652 | +8 | 33,174 | 1.2% | 22.64B | 1 |
| 82 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,644 | +24 | 177,238 | 0.6% | 12.25B | 6 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,640 | +21 | 158,138 | 0.6% | 1.10B | 1 |
| 84 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,631 | -39 | 55,674 | 1.0% | 7.55B | 1 |
| 85 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,629 | +48 | 23,063 | 1.3% | 11.17B | 5 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,564 | +16 | 301,618 | 0.4% | 6.74B | 2 |
| 87 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,535 | +47 | 53,176 | 1.0% | 7.24B | 5 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,518 | +8 | 184,967 | 0.5% | 6.74B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,506 | +5 | 145,753 | 0.6% | 13.02B | 1 |
| 90 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,456 | -27 | 20,687 | 1.2% | 4.30B | 2 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,441 | +47 | 52,008 | 0.9% | 7.24B | 1 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,362 | -14 | 8,010 | 1.3% | 9.82B | 1 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,343 | +1 | 173,828 | 0.5% | 11.51B | 7 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,275 | +19 | 19,230 | 1.1% | 1.20B | 2 |
| 95 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,270 | +25 | 30,981 | 1.0% | 11.17B | 5 |
| 96 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,247 | +124 | 8,115 | 1.2% | 4.30B | 3 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,216 | +31 | 228,384 | 0.4% | 35.13B | 4 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,145 | +299 | 9,949 | 1.0% | 9.15B | 1 |
| 99 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,133 | +129 | 31,950 | 0.9% | 14.03B | 1 |
| 100 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,129 | -2 | 57,664 | 0.7% | 1.35B | 3 |
| 101 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,098 | +12 | 800,746 | 0.1% | — | 3 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,039 | +62 | 14,616 | 0.9% | 353.4M | 2 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 970 | +31 | 39,199 | 0.7% | 70.55B | 3 |
| 104 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 933 | -47 | 12,033 | 0.8% | 31.59B | 6 |
| 105 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 889 | -7 | 8,204 | 0.8% | 28.84B | 3 |
| 106 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 870 | 0 | 2,834 | 0.8% | 31.59B | 6 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 800 | -1 | 16,312 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 761 | +29 | 20,267 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 659 | +12 | 95,821 | 0.3% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 648 | +18 | 81,537 | 0.4% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 629 | +9 | 76,367 | 0.4% | 7.04B | 4 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 599 | +1 | 44,145 | 0.4% | 12.19B | 2 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 581 | +46 | 3,947 | 0.6% | 8.03B | 3 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 516 | +15 | 232,791 | 0.2% | — | 2 |
| 115 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 509 | -1 | 27,396 | 0.4% | 9.24B | 2 |
| 116 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 480 | -21 | 217,988 | 0.2% | 12.19B | 3 |
| 117 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | 0 | 21,850 | 0.4% | 2.61B | 2 |
| 118 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 452 | +8 | 13,959 | 0.4% | 4.33B | 3 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 432 | -5 | 32,620 | 0.3% | 40.43B | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 427 | -1 | 322,089 | 0.1% | 7.24B | 2 |
| 121 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 426 | +8 | 3,057 | 0.4% | 560.9M | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 403 | +4 | 39,197 | 0.3% | 7.48B | 2 |
| 123 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 397 | +13 | 3,139 | 0.4% | 30.68B | 1 |
| 124 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 396 | +1 | 7,390 | 0.4% | 31.59B | 6 |
| 125 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 376 | +4 | 11,810 | 0.3% | 27.23B | 2 |
| 126 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 375 | +10 | 1,262 | 0.4% | — | 1 |
| 127 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 338 | +19 | 21,572 | 0.3% | 9.24B | 2 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 320 | -30 | 37,623 | 0.2% | 27.23B | 3 |
| 129 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 313 | +5 | 107,024 | 0.2% | — | 3 |
| 130 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 298 | -13 | 12,554 | 0.3% | 70.55B | 2 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 293 | +16 | 41,730 | 0.2% | 11.17B | 1 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 291 | +7 | 70,333 | 0.2% | 8.03B | 3 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 283 | -11 | 44,498 | 0.2% | 7.70B | 5 |
| 134 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 252 | +14 | 5,295 | 0.2% | 11.51B | 5 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 243 | +2 | 16,483 | 0.2% | 7.29B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 236 | -1 | 19,520 | 0.2% | 68.98B | 2 |
| 137 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 230 | -3 | 2,551 | 0.2% | 4.02B | 2 |
| 138 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | -42 | 1,499 | 0.2% | 31.58B | 2 |
| 139 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 227 | +10 | 1,290 | 0.2% | 27.23B | 3 |
| 140 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 219 | +17 | 4,957 | 0.2% | 70.55B | 3 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 214 | +1 | 5,061 | 0.2% | 437.8M | 1 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 212 | 0 | 2,423 | 0.2% | — | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | -1 | 38,649 | 0.1% | 70.55B | 3 |
| 144 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 146 | +6 | 28,291 | 0.1% | 46.70B | 6 |
| 145 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 144 | -4 | 5,380 | 0.1% | 353.4M | 2 |
| 146 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | -1 | 6,167 | 0.1% | 12.25B | 3 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130 | -1 | 1,030 | 0.1% | — | 1 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 120 | +3 | 7,199 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 85 | -1 | 403 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | +2 | 1,255 | 0.0% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | -1 | 205 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | 0 | 227 | 0.0% | 15.17B | 3 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | 0 | 171 | 0.0% | 8.16B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | +3 | 370 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +1 | 150 | 0.0% | 437.8M | 1 |
| 156 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 263 | 0.0% | 437.8M | 1 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -1 | 118 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,414,611 | 301,789,295 | 30 | 2.5% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,224,094 | 5,722,359 | 7 | 21.0% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 545,795 | 2,569,210 | 11 | 20.4% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 94,904 | 6,339,182 | 12 | 1.5% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 67,012 | 68,950 | 1 | 39.7% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 37,060 | 1,372,242 | 5 | 2.5% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 25,060 | 389,524 | 10 | 5.1% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,803 | 1,436,608 | 11 | 1.2% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,639 | 546,316 | 13 | 2.6% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 11,770 | 435,646 | 6 | 2.2% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,480 | 361,058 | 14 | 2.5% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,352 | 193,583 | 6 | 3.2% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,364 | 855,512 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,489 | 153,335 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,094 | 194,468 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,329 | 135,770 | 1 | 2.3% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,178 | 695,815 | 2 | 0.7% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,664 | 488,858 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,304 | 658,015 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,427 | 23,756 | 4 | 2.0% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,252 | 103,783 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,163 | 1,160,081 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,788 | 153,485 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,362 | 8,010 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 629 | 76,367 | 1 | 0.4% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,319,744 | 58,356,155 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 698,867 | 726,014 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 255,508 | 596,831 | 11 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 67,012 | 68,950 | 20 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 41,174 | 4,153,021 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 26,972 | 689,700 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 20,335 | 39,273 | 26 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,408 | 110,773 | 43 |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,329 | 135,770 | 44 |
| 10 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,999 | 68,278 | 45 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,831 | 49,938 | 48 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,751 | 373,726 | 49 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,404 | 12,200 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,359 | 149,968 | 51 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,720 | 67,200 | 55 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,656 | 670,296 | 56 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 3,481 | 418,539 | 58 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,798 | 100,246 | 78 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,740 | 356,397 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,640 | 158,138 | 83 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,362 | 8,010 | 92 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,129 | 57,664 | 100 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,098 | 800,746 | 101 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 933 | 12,033 | 104 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 629 | 76,367 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.7% | 67,012 | 68,950 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.0% | 1,224,094 | 5,722,359 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 20.4% | 545,795 | 2,569,210 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5.1% | 25,060 | 389,524 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,352 | 193,583 | 12 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.6% | 16,639 | 546,316 | 9 |
| 7 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,489 | 153,335 | 14 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.5% | 37,060 | 1,372,242 | 6 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,480 | 361,058 | 11 |
| 10 | [mistralai](https://huggingface.co/mistralai) | 2.5% | 7,414,611 | 301,789,295 | 1 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.3% | 5,329 | 135,770 | 16 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.2% | 11,770 | 435,646 | 10 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,094 | 194,468 | 15 |
| 14 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.0% | 2,427 | 23,756 | 20 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.5% | 94,904 | 6,339,182 | 4 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,362 | 8,010 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 17,803 | 1,436,608 | 8 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,252 | 103,783 | 21 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,664 | 488,858 | 18 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,364 | 855,512 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,788 | 153,485 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.7% | 5,178 | 695,815 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,304 | 658,015 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.4% | 629 | 76,367 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,163 | 1,160,081 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
