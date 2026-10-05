# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-05
- **Generated at:** 2026-10-05T14:06:08Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,388,120 | +11,056 | 57,948,558 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,660,754 | -54,503 | 64,869,740 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 681,716 | +30,998 | 702,557 | 84.9% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 561,925 | -2,438 | 45,756,999 | 1.2% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 526,900 | -14,900 | 4,791,359 | 10.8% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 493,084 | -1,259 | 4,295,464 | 11.2% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 481,423 | -12,548 | 16,454,820 | 2.9% | 12.25B | 3 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 430,473 | -19,430 | 3,741,605 | 11.2% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 341,281 | -13,961 | 594,233 | 49.2% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 316,487 | -6,927 | 2,874,399 | 10.6% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 264,826 | -1,222 | 32,380,145 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 258,430 | +936 | 5,633,326 | 4.5% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 256,615 | +665 | 5,483,373 | 4.6% | 24.01B | 1 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,366 | +14,558 | 922,022 | 22.6% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,504 | +360 | 2,241,714 | 9.6% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 148,125 | -654 | 8,530,142 | 1.7% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 102,770 | -7,799 | 1,090,351 | 8.6% | 127.70B | 2 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 96,698 | -8,938 | 4,149,144 | 2.3% | 11.34B | 8 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,857 | +602 | 740,249 | 8.8% | 23.57B | 2 |
| 20 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,948 | +7,765 | 689,726 | 8.7% | 119.40B | 3 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,261 | +13 | 68,189 | 39.4% | — | 1 |
| 22 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,554 | +1,263 | 7,591,446 | 0.8% | 23.57B | 2 |
| 23 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 61,185 | -6,173 | 534,655 | 9.6% | 70.60B | 2 |
| 24 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,479 | -60 | 11,219,658 | 0.4% | 140.63B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,340 | +545 | 682,712 | 3.6% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,404 | -1,833 | 146,908 | 9.9% | 9.15B | 1 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,162 | +40 | 5,159,828 | 0.4% | 22.25B | 1 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,303 | -44 | 632,931 | 2.5% | 23.57B | 2 |
| 29 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,707 | +1,071 | 216,799 | 5.6% | — | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,734 | +296 | 483,876 | 2.7% | 9.15B | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,753 | -244 | 780,114 | 1.7% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,524 | +51 | 75,266 | 7.7% | — | 5 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 12,730 | -1,372 | 26,344 | 10.1% | 72.01B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,967 | -90 | 509,866 | 1.8% | 7.24B | 8 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 10,819 | +19 | 134,683 | 4.6% | 7.48B | 5 |
| 36 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,448 | +301 | 327,994 | 2.2% | 24.01B | 2 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,225 | +57 | 4,927,431 | 0.2% | 122.61B | 1 |
| 38 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 7,832 | +2,494 | 26,421 | 6.2% | 12.25B | 3 |
| 39 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,408 | -263 | 350,095 | 1.6% | 125.03B | 1 |
| 40 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,115 | +385 | 5,379,623 | 0.1% | 22.25B | 1 |
| 41 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,752 | -299 | 49,450 | 3.8% | 8.03B | 7 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,672 | -270 | 109,774 | 2.7% | 8.42B | 7 |
| 43 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,546 | -5 | 30,191 | 4.3% | 33.12B | 1 |
| 44 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,521 | +882 | 16,171 | 4.8% | 572.6M | 5 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,258 | +244 | 145,400 | 2.1% | 2.25B | 7 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,955 | +22 | 134,746 | 2.1% | 7.40B | 3 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,910 | +21 | 154,366 | 1.9% | 23.57B | 2 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,858 | -104 | 165,177 | 1.8% | 11.17B | 16 |
| 49 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,778 | -43 | 111,414 | 2.3% | 7.29B | 2 |
| 50 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,594 | -33 | 67,237 | 2.7% | 12.77B | 5 |
| 51 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,492 | +371 | 11,979 | 4.0% | 27.43B | 3 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,433 | +38 | 372,676 | 0.9% | 7.24B | 8 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,277 | +39 | 253,319 | 1.2% | 4.76B | 5 |
| 54 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,104 | +11 | 669,873 | 0.5% | 7.45B | 2 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,077 | +17 | 905,148 | 0.4% | 23.57B | 2 |
| 56 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,991 | +101 | 66,685 | 2.4% | 14.08B | 1 |
| 57 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,935 | +68 | 5,033,622 | 0.1% | 122.61B | 1 |
| 58 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,891 | +40 | 92,189 | 2.0% | 2.89B | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,801 | +80 | 149,010 | 1.5% | 7.24B | 4 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,393 | +10 | 35,897 | 2.5% | 2.61B | 3 |
| 61 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,251 | -9 | 413,866 | 0.6% | 1.20B | 1 |
| 62 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,104 | -9 | 417,379 | 0.6% | 353.4M | 1 |
| 63 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,062 | -12 | 398,919 | 0.6% | 3.21B | 1 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,951 | -5 | 58,154 | 1.9% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,505 | +6 | 84,307 | 1.4% | 9.15B | 1 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,366 | +80 | 85,604 | 1.3% | 2.22B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,355 | -20 | 40,116 | 1.7% | 13.29B | 3 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,233 | +69 | 49,406 | 1.5% | 9.24B | 4 |
| 69 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,183 | +14 | 18,043 | 1.8% | 12.19B | 2 |
| 70 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,144 | -9 | 32,819 | 1.6% | 22.64B | 1 |
| 71 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,140 | +123 | 8,531 | 2.0% | 1.51B | 6 |
| 72 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,105 | -426 | 55,360 | 1.4% | 7.55B | 1 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,031 | -6 | 23,671 | 1.6% | 22.64B | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,850 | -26 | 78,362 | 1.0% | 7.45B | 1 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,809 | +6 | 452,476 | 0.3% | 40.43B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,801 | -3 | 106,018 | 0.9% | 7.45B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,791 | -4 | 99,839 | 0.9% | 30.68B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,723 | -1 | 356,009 | 0.4% | — | 3 |
| 79 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,714 | -18 | 49,708 | 1.1% | 7.77B | 1 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,698 | -12 | 15,033 | 1.5% | 3.83B | 5 |
| 81 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,693 | +88 | 33,034 | 1.3% | 56.7M | 1 |
| 82 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,628 | +2 | 176,872 | 0.6% | 12.25B | 6 |
| 83 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,615 | +12 | 5,300,780 | 0.0% | 7.25B | 1 |
| 84 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,601 | +4 | 157,770 | 0.6% | 1.10B | 1 |
| 85 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,601 | -88 | 31,736 | 1.2% | 14.03B | 1 |
| 86 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,580 | -35 | 22,699 | 1.3% | 11.17B | 5 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,556 | -1 | 301,273 | 0.4% | 6.74B | 2 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,496 | -1 | 145,415 | 0.6% | 13.02B | 1 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,493 | +57 | 7,829 | 1.4% | 9.82B | 1 |
| 90 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,492 | -1 | 184,618 | 0.5% | 6.74B | 1 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,459 | +240 | 20,336 | 1.2% | 4.30B | 2 |
| 92 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,321 | -31 | 30,699 | 1.0% | 11.17B | 5 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,318 | +11 | 173,461 | 0.5% | 11.51B | 7 |
| 94 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,285 | 0 | 12,013 | 1.1% | 31.59B | 6 |
| 95 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,249 | +42 | 52,829 | 0.8% | 7.24B | 5 |
| 96 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,169 | -2 | 57,444 | 0.7% | 1.35B | 3 |
| 97 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,162 | +48 | 51,679 | 0.8% | 7.24B | 1 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,103 | -14 | 800,523 | 0.1% | — | 3 |
| 99 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,064 | -22 | 228,039 | 0.3% | 35.13B | 4 |
| 100 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,042 | +2 | 9,463 | 1.0% | 9.15B | 1 |
| 101 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,034 | -32 | 7,707 | 1.0% | 4.30B | 3 |
| 102 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,009 | +6 | 18,806 | 0.8% | 1.20B | 2 |
| 103 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 977 | -10 | 8,066 | 0.9% | 28.84B | 3 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 894 | +12 | 14,322 | 0.8% | 353.4M | 2 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 869 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 106 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 842 | -51 | 38,896 | 0.6% | 70.55B | 3 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 809 | +17 | 16,193 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 777 | +80 | 20,172 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 761 | +17 | 95,723 | 0.4% | 1.35B | 8 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 664 | -5 | 44,075 | 0.5% | 12.19B | 2 |
| 111 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 620 | -4 | 81,385 | 0.3% | 8.03B | 3 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 569 | +8 | 217,883 | 0.2% | 12.19B | 3 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 534 | -2 | 3,826 | 0.5% | 8.03B | 3 |
| 114 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 505 | -1 | 76,172 | 0.3% | 7.04B | 4 |
| 115 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 497 | -16 | 2,997 | 0.5% | 560.9M | 2 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 484 | +4 | 232,660 | 0.1% | — | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 481 | 0 | 1,497 | 0.5% | 31.58B | 2 |
| 118 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 472 | +10 | 21,818 | 0.4% | 2.61B | 2 |
| 119 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 471 | +16 | 13,902 | 0.4% | 4.33B | 3 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 462 | -6 | 32,528 | 0.3% | 40.43B | 2 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 447 | +5 | 27,289 | 0.4% | 9.24B | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 436 | +34 | 39,144 | 0.3% | 7.48B | 2 |
| 123 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 414 | -4 | 12,527 | 0.4% | 70.55B | 2 |
| 124 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 412 | -6 | 321,977 | 0.1% | 7.24B | 2 |
| 125 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 385 | -6 | 3,031 | 0.4% | 30.68B | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 369 | -6 | 11,780 | 0.3% | 27.23B | 2 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 363 | +14 | 37,557 | 0.3% | 27.23B | 3 |
| 128 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 363 | 0 | 7,339 | 0.3% | 31.59B | 6 |
| 129 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 329 | -12 | 44,447 | 0.2% | 7.70B | 5 |
| 130 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 321 | +8 | 1,162 | 0.3% | — | 1 |
| 131 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 317 | +42 | 21,509 | 0.3% | 9.24B | 2 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 312 | -3 | 41,663 | 0.2% | 11.17B | 1 |
| 133 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 306 | -16 | 70,291 | 0.2% | 8.03B | 3 |
| 134 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 291 | -8 | 106,941 | 0.1% | — | 3 |
| 135 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 269 | +11 | 2,505 | 0.3% | 4.02B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 257 | -7 | 19,472 | 0.2% | 68.98B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 252 | +5 | 16,430 | 0.2% | 7.29B | 2 |
| 138 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 223 | -7 | 1,241 | 0.2% | 27.23B | 3 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 211 | +1 | 5,226 | 0.2% | 11.51B | 5 |
| 140 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 211 | +2 | 2,380 | 0.2% | — | 1 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 193 | -7 | 5,348 | 0.2% | 353.4M | 2 |
| 142 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 193 | +13 | 4,962 | 0.2% | 437.8M | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 186 | -2 | 38,626 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | -4 | 7,166 | 0.1% | 1.20B | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | -1 | 28,255 | 0.1% | 46.70B | 6 |
| 146 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 138 | 0 | 4,847 | 0.1% | 70.55B | 3 |
| 147 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | +9 | 6,167 | 0.1% | 12.25B | 3 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 126 | +1 | 1,015 | 0.1% | — | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 83 | +1 | 395 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 76 | -3 | 1,242 | 0.1% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | +4 | 195 | 0.1% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 29 | +1 | 224 | 0.0% | 15.17B | 3 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | -1 | 145 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 25 | +2 | 168 | 0.0% | 8.16B | 3 |
| 155 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | -4 | 258 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 115 | 0.0% | 7.24B | 1 |
| 157 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -1 | 356 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,976,359 | 300,286,871 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,258,074 | 5,598,755 | 7 | 22.1% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 641,818 | 2,552,375 | 11 | 24.2% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 150,065 | 6,324,205 | 12 | 2.3% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,261 | 68,189 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 37,583 | 1,362,824 | 5 | 2.6% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 17,450 | 544,524 | 13 | 2.7% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 16,910 | 433,672 | 6 | 3.2% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,406 | 1,430,736 | 11 | 1.1% |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 12,349 | 375,539 | 10 | 2.6% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,280 | 358,490 | 14 | 2.5% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,999 | 191,806 | 6 | 3.1% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,755 | 854,253 | 3 | 0.8% |
| 14 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,437 | 193,365 | 3 | 2.2% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,357 | 152,289 | 2 | 2.5% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,955 | 134,746 | 1 | 2.1% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,845 | 694,653 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,589 | 487,803 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,279 | 657,282 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,998 | 23,677 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,230 | 103,262 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,135 | 1,159,596 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,930 | 153,167 | 2 | 0.8% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,493 | 7,829 | 1 | 1.4% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 505 | 76,172 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,388,120 | 57,948,558 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 681,716 | 702,557 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 341,281 | 594,233 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 96,698 | 4,149,144 | 18 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,261 | 68,189 | 21 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,340 | 682,712 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 7,832 | 26,421 | 38 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,752 | 49,450 | 41 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,672 | 109,774 | 42 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,955 | 134,746 | 46 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,778 | 111,414 | 49 |
| 12 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,594 | 67,237 | 50 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,433 | 372,676 | 52 |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,104 | 669,873 | 54 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,991 | 66,685 | 56 |
| 16 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,891 | 92,189 | 58 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,251 | 413,866 | 61 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,791 | 99,839 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,723 | 356,009 | 78 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,601 | 157,770 | 84 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,493 | 7,829 | 89 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,285 | 12,013 | 94 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,169 | 57,444 | 96 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,103 | 800,523 | 98 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 505 | 76,172 | 114 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,261 | 68,189 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 24.2% | 641,818 | 2,552,375 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 22.1% | 1,258,074 | 5,598,755 | 2 |
| 4 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.2% | 16,910 | 433,672 | 8 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.1% | 8,999 | 191,806 | 12 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.7% | 17,450 | 544,524 | 7 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 7,976,359 | 300,286,871 | 1 |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.6% | 12,349 | 375,539 | 10 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 37,583 | 1,362,824 | 6 |
| 10 | [Almawave](https://huggingface.co/Almawave) | 2.5% | 6,357 | 152,289 | 15 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,280 | 358,490 | 11 |
| 12 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 2,998 | 23,677 | 20 |
| 13 | [speakleash](https://huggingface.co/speakleash) | 2.3% | 150,065 | 6,324,205 | 4 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.2% | 6,437 | 193,365 | 14 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,955 | 134,746 | 16 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,493 | 7,829 | 24 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,230 | 103,262 | 21 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,406 | 1,430,736 | 9 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,755 | 854,253 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,589 | 487,803 | 18 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 1,930 | 153,167 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,845 | 694,653 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,279 | 657,282 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 505 | 76,172 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,135 | 1,159,596 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
