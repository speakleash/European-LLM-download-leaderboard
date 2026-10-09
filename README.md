# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-09
- **Generated at:** 2026-10-09T12:53:09Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,346,706 | -28,748 | 58,224,702 | 4.0% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,592,653 | +27,108 | 65,130,858 | 2.4% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 698,641 | -399 | 724,159 | 84.8% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 635,202 | +49,892 | 45,900,965 | 1.4% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 485,996 | -6,168 | 4,355,020 | 10.9% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 447,613 | -21,934 | 16,490,090 | 2.7% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 413,924 | -17,501 | 4,830,168 | 8.4% | 24.01B | 2 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 355,837 | -26,187 | 3,791,442 | 9.1% | 13.95B | 6 |
| 9 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 290,699 | -7,885 | 2,904,274 | 9.7% | 24.01B | 1 |
| 10 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 283,094 | -13,281 | 595,828 | 40.7% | 22.64B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 273,310 | -2,884 | 32,420,233 | 0.8% | 46.70B | 2 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 258,111 | -1,849 | 5,505,115 | 4.6% | 24.01B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 238,761 | -10,735 | 5,661,484 | 4.1% | 4.25B | 7 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 230,576 | -1,970 | 924,518 | 22.5% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 228,541 | -986 | 2,265,153 | 9.7% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 139,091 | -3,321 | 8,536,322 | 1.6% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 81,694 | -503 | 708,429 | 10.1% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 80,327 | -6,300 | 1,101,791 | 6.7% | 127.70B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,894 | -855 | 749,181 | 8.6% | 23.57B | 2 |
| 20 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 67,787 | -1,054 | 7,603,448 | 0.9% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,323 | +1 | 68,260 | 39.4% | — | 1 |
| 22 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 58,971 | -10,322 | 4,151,401 | 1.4% | 11.34B | 8 |
| 23 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 54,877 | +520 | 11,233,600 | 0.5% | 140.63B | 2 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 29,224 | -659 | 688,701 | 3.7% | 7.77B | 8 |
| 25 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 28,433 | -3,078 | 537,802 | 4.5% | 70.60B | 2 |
| 26 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,789 | +99 | 5,160,944 | 0.4% | 22.25B | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 18,670 | +1,579 | 37,416 | 13.6% | 12.25B | 3 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,533 | -1,744 | 148,123 | 7.5% | 9.15B | 1 |
| 29 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,496 | -1,050 | 219,783 | 5.8% | — | 1 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,723 | -1,803 | 633,741 | 2.1% | 23.57B | 2 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,171 | -294 | 781,832 | 1.6% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,896 | -155 | 77,247 | 7.8% | — | 5 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,459 | -364 | 485,256 | 2.3% | 9.15B | 1 |
| 34 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 11,998 | +221 | 136,172 | 5.1% | 7.48B | 5 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,611 | -227 | 332,521 | 2.7% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,098 | -133 | 511,511 | 1.8% | 7.24B | 8 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,901 | +158 | 4,928,811 | 0.2% | 122.61B | 1 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,182 | -1,590 | 26,815 | 6.5% | 72.01B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,853 | +66 | 5,380,855 | 0.1% | 22.25B | 1 |
| 40 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,620 | -179 | 350,896 | 1.5% | 125.03B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,146 | +18 | 17,099 | 5.2% | 572.6M | 5 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,108 | +68 | 146,638 | 2.5% | 2.25B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,572 | -50 | 110,353 | 2.6% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,250 | +25 | 135,385 | 2.2% | 7.40B | 3 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,101 | -128 | 49,794 | 3.4% | 8.03B | 7 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,966 | -1 | 154,526 | 2.0% | 23.57B | 2 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,886 | -86 | 165,986 | 1.8% | 11.17B | 16 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,814 | +13 | 67,931 | 2.9% | 12.77B | 5 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,654 | -10 | 373,371 | 1.0% | 7.24B | 8 |
| 50 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,610 | -170 | 111,645 | 2.2% | 7.29B | 2 |
| 51 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,416 | +33 | 12,157 | 3.9% | 27.43B | 3 |
| 52 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,163 | +60 | 149,616 | 1.7% | 7.24B | 4 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,158 | +31 | 905,564 | 0.4% | 23.57B | 2 |
| 54 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,148 | -42 | 415,013 | 0.8% | 1.20B | 1 |
| 55 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,123 | +7 | 5,034,045 | 0.1% | 122.61B | 1 |
| 56 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,975 | -47 | 418,507 | 0.8% | 353.4M | 1 |
| 57 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,945 | -35 | 400,059 | 0.8% | 3.21B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,927 | -95 | 67,018 | 2.4% | 14.08B | 1 |
| 59 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,753 | -577 | 253,862 | 1.1% | 4.76B | 5 |
| 60 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,746 | -185 | 670,130 | 0.5% | 7.45B | 2 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,386 | -31 | 36,318 | 2.5% | 2.61B | 3 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,354 | -103 | 92,616 | 1.7% | 2.89B | 1 |
| 63 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,197 | +23 | 58,707 | 2.0% | 1.60B | 5 |
| 64 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,662 | +52 | 85,950 | 1.4% | 2.22B | 1 |
| 65 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,607 | +139 | 9,187 | 2.4% | 1.51B | 6 |
| 66 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,512 | +14 | 84,394 | 1.4% | 9.15B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,301 | -4 | 40,589 | 1.6% | 13.29B | 3 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,204 | +13 | 49,667 | 1.5% | 9.24B | 4 |
| 69 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,178 | -12 | 24,091 | 1.8% | 22.64B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,128 | +11 | 18,218 | 1.8% | 12.19B | 2 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,120 | -20 | 33,053 | 1.6% | 22.64B | 1 |
| 72 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,865 | +63 | 49,983 | 1.2% | 7.77B | 1 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,863 | -5 | 78,650 | 1.0% | 7.45B | 1 |
| 74 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,818 | -6 | 30,295 | 1.4% | 33.12B | 1 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,811 | +5 | 452,609 | 0.3% | 40.43B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,811 | -14 | 106,277 | 0.9% | 7.45B | 1 |
| 77 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,810 | -12 | 15,437 | 1.6% | 3.83B | 5 |
| 78 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,803 | +38 | 33,524 | 1.4% | 56.7M | 1 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,785 | -24 | 100,121 | 0.9% | 30.68B | 1 |
| 80 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,728 | -498 | 55,568 | 1.1% | 7.55B | 1 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,714 | -19 | 356,257 | 0.4% | — | 3 |
| 82 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,692 | -5 | 5,300,998 | 0.0% | 7.25B | 1 |
| 83 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,637 | +5 | 22,901 | 1.3% | 11.17B | 5 |
| 84 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,625 | -14 | 177,107 | 0.6% | 12.25B | 6 |
| 85 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,617 | 0 | 158,009 | 0.6% | 1.10B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,545 | -17 | 301,496 | 0.4% | 6.74B | 2 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,503 | -1 | 184,852 | 0.5% | 6.74B | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,496 | -16 | 145,638 | 0.6% | 13.02B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,433 | +32 | 53,050 | 0.9% | 7.24B | 5 |
| 90 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,381 | -130 | 7,938 | 1.3% | 9.82B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,359 | +128 | 173,741 | 0.5% | 11.51B | 7 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,340 | -4 | 20,444 | 1.1% | 4.30B | 2 |
| 93 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,339 | +31 | 51,883 | 0.9% | 7.24B | 1 |
| 94 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,311 | -11 | 30,862 | 1.0% | 11.17B | 5 |
| 95 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,289 | -2 | 12,023 | 1.2% | 31.59B | 6 |
| 96 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,170 | +10 | 228,276 | 0.4% | 35.13B | 4 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,148 | +2 | 57,580 | 0.7% | 1.35B | 3 |
| 98 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,140 | +76 | 19,041 | 1.0% | 1.20B | 2 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,097 | -4 | 800,674 | 0.1% | — | 3 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,081 | -3 | 7,876 | 1.0% | 4.30B | 3 |
| 101 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,010 | -555 | 31,797 | 0.8% | 14.03B | 1 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 965 | -10 | 14,493 | 0.8% | 353.4M | 2 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 933 | -13 | 39,114 | 0.7% | 70.55B | 3 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 904 | -21 | 8,152 | 0.8% | 28.84B | 3 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 864 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 106 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 839 | -28 | 9,605 | 0.8% | 9.15B | 1 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 795 | -3 | 16,273 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 745 | +5 | 20,227 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 679 | -15 | 95,779 | 0.3% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 630 | -9 | 81,484 | 0.3% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 607 | +2 | 76,320 | 0.3% | 7.04B | 4 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 594 | -3 | 44,123 | 0.4% | 12.19B | 2 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 525 | +3 | 3,880 | 0.5% | 8.03B | 3 |
| 114 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 514 | +26 | 27,387 | 0.4% | 9.24B | 2 |
| 115 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 500 | +3 | 232,765 | 0.2% | — | 2 |
| 116 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 485 | -7 | 217,933 | 0.2% | 12.19B | 3 |
| 117 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 457 | +3 | 21,841 | 0.4% | 2.61B | 2 |
| 118 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 451 | -30 | 1,499 | 0.4% | 31.58B | 2 |
| 119 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 446 | -5 | 13,933 | 0.4% | 4.33B | 3 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 444 | +1 | 32,596 | 0.3% | 40.43B | 2 |
| 121 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 436 | -22 | 3,032 | 0.4% | 560.9M | 2 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 418 | -1 | 322,057 | 0.1% | 7.24B | 2 |
| 123 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 395 | +25 | 7,389 | 0.4% | 31.59B | 6 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 393 | -21 | 39,174 | 0.3% | 7.48B | 2 |
| 125 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 387 | +10 | 3,104 | 0.4% | 30.68B | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 376 | 0 | 11,802 | 0.3% | 27.23B | 2 |
| 127 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 357 | +2 | 1,228 | 0.4% | — | 1 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 348 | -21 | 37,609 | 0.3% | 27.23B | 3 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 316 | -63 | 12,537 | 0.3% | 70.55B | 2 |
| 130 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 311 | -6 | 21,541 | 0.3% | 9.24B | 2 |
| 131 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 307 | +5 | 107,000 | 0.1% | — | 3 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 295 | +13 | 70,322 | 0.2% | 8.03B | 3 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 295 | -10 | 44,479 | 0.2% | 7.70B | 5 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 285 | +12 | 41,704 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 239 | -12 | 16,467 | 0.2% | 7.29B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 236 | -15 | 19,503 | 0.2% | 68.98B | 2 |
| 137 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 233 | +5 | 5,263 | 0.2% | 11.51B | 5 |
| 138 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 231 | 0 | 2,546 | 0.2% | 4.02B | 2 |
| 139 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 208 | -4 | 2,407 | 0.2% | — | 1 |
| 140 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 195 | +18 | 5,031 | 0.2% | 437.8M | 1 |
| 141 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 186 | -17 | 1,244 | 0.2% | 27.23B | 3 |
| 142 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 179 | +8 | 4,895 | 0.2% | 70.55B | 3 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 169 | -4 | 38,640 | 0.1% | 70.55B | 3 |
| 144 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 145 | -28 | 5,364 | 0.1% | 353.4M | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | +3 | 28,275 | 0.1% | 46.70B | 6 |
| 146 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 128 | -2 | 1,027 | 0.1% | — | 1 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 119 | -8 | 7,185 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 89 | +2 | 403 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 35 | -4 | 1,249 | 0.0% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 34 | -7 | 201 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | 0 | 227 | 0.0% | 15.17B | 3 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | 0 | 171 | 0.0% | 8.16B | 3 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | 0 | 148 | 0.0% | 437.8M | 1 |
| 155 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | +3 | 363 | 0.0% | 437.8M | 1 |
| 156 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 261 | 0.0% | 437.8M | 1 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 118 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,676,844 | 301,319,658 | 30 | 2.5% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,231,815 | 5,685,519 | 7 | 21.3% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 575,401 | 2,563,376 | 11 | 21.6% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 112,899 | 6,333,942 | 12 | 1.8% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,323 | 68,260 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,452 | 1,370,527 | 5 | 2.7% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 23,136 | 387,115 | 10 | 4.7% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 19,260 | 1,435,662 | 11 | 1.3% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,820 | 545,643 | 13 | 2.6% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 11,760 | 434,844 | 6 | 2.2% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,297 | 360,122 | 14 | 2.5% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,092 | 192,951 | 6 | 3.1% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,420 | 855,057 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,589 | 152,968 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,260 | 194,006 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,250 | 135,385 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,072 | 695,428 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,616 | 488,499 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,259 | 657,753 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,999 | 23,739 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,229 | 103,623 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,140 | 1,159,942 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,827 | 153,359 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,381 | 7,938 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 607 | 76,320 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,346,706 | 58,224,702 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 698,641 | 724,159 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 283,094 | 595,828 | 10 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,323 | 68,260 | 21 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 58,971 | 4,151,401 | 22 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 29,224 | 688,701 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 18,670 | 37,416 | 27 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,572 | 110,353 | 43 |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,250 | 135,385 | 44 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,101 | 49,794 | 45 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,814 | 67,931 | 48 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,654 | 373,371 | 49 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,610 | 111,645 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,163 | 149,616 | 52 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 4,148 | 415,013 | 54 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,927 | 67,018 | 58 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,746 | 670,130 | 60 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,785 | 100,121 | 79 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,714 | 356,257 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,617 | 158,009 | 85 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,381 | 7,938 | 90 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,289 | 12,023 | 95 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,148 | 57,580 | 97 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,097 | 800,674 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 607 | 76,320 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,323 | 68,260 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 21.6% | 575,401 | 2,563,376 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.3% | 1,231,815 | 5,685,519 | 2 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4.7% | 23,136 | 387,115 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.1% | 9,092 | 192,951 | 12 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,452 | 1,370,527 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.6% | 16,820 | 545,643 | 9 |
| 8 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,589 | 152,968 | 14 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.5% | 7,676,844 | 301,319,658 | 1 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,297 | 360,122 | 11 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 2,999 | 23,739 | 20 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,250 | 135,385 | 16 |
| 13 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.2% | 11,760 | 434,844 | 10 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,260 | 194,006 | 15 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.8% | 112,899 | 6,333,942 | 4 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,381 | 7,938 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.3% | 19,260 | 1,435,662 | 8 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,229 | 103,623 | 21 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,616 | 488,499 | 18 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,420 | 855,057 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,827 | 153,359 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,072 | 695,428 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,259 | 657,753 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 607 | 76,320 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,140 | 1,159,942 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
