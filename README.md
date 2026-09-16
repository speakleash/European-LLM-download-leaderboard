# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-16
- **Generated at:** 2026-09-16T11:11:13Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,590,462 | +54,020 | 56,381,821 | 4.6% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,715,902 | +56,111 | 63,956,983 | 2.7% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 624,063 | +417 | 3,535,307 | 17.2% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 567,496 | +33,049 | 45,488,434 | 1.2% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 537,605 | +10,212 | 16,195,630 | 3.3% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 494,765 | +494,765 | 3,971,068 | 12.2% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 442,842 | +12,426 | 4,583,080 | 9.5% | 24.01B | 2 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,426 | -276 | 415,449 | 68.6% | 353.4M | 1 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 351,841 | -22,988 | 5,474,742 | 6.3% | 4.25B | 7 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,020 | -282 | 411,934 | 68.6% | 1.20B | 1 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,691 | -280 | 396,967 | 68.6% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 305,839 | +135 | 32,212,125 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 252,993 | -3,829 | 2,673,815 | 9.1% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 237,532 | +237,532 | 4,134,404 | 5.6% | 11.34B | 8 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,290 | +1,867 | 2,079,599 | 9.4% | 8.92B | 6 |
| 16 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 204,944 | +16,924 | 400,520 | 40.9% | 22.64B | 1 |
| 17 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 194,164 | -8,259 | 8,442,937 | 2.3% | 8.02B | 1 |
| 18 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 137,371 | +4,052 | 5,279,765 | 2.6% | 24.01B | 1 |
| 19 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 125,428 | -886 | 1,032,446 | 11.1% | 127.70B | 2 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 97,062 | +97,062 | 521,164 | 15.6% | 70.60B | 2 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,062 | -154 | 691,589 | 9.5% | 23.57B | 2 |
| 22 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 73,018 | +36,498 | 85,071 | 39.5% | 8.90B | 1 |
| 23 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,108 | +358 | 622,179 | 9.8% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,119 | +4,296 | 7,552,094 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,175 | -589 | 637,544 | 7.9% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,859 | +651 | 11,186,872 | 0.3% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,871 | +1,701 | 667,060 | 4.3% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 29,227 | -1,034 | 134,637 | 12.5% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,483 | +223 | 475,249 | 3.6% | 9.15B | 1 |
| 30 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,483 | -485 | 23,833 | 14.1% | 72.01B | 1 |
| 31 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,650 | -349 | 346,937 | 3.7% | 125.03B | 1 |
| 32 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,852 | -212 | 323,086 | 3.7% | 24.01B | 2 |
| 33 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,800 | +57 | 770,848 | 1.8% | 11.25B | 10 |
| 34 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,341 | +195 | 695,841 | 1.8% | 1.66B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,100 | +18 | 5,299,828 | 0.3% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,014 | +255 | 66,399 | 7.8% | — | 5 |
| 37 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,918 | +7,956 | 5,149,825 | 0.2% | 22.25B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,107 | +431 | 205,317 | 3.6% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,507 | +9,507 | 502,774 | 1.6% | 7.24B | 8 |
| 40 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,900 | -277 | 4,921,256 | 0.1% | 122.61B | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,552 | +356 | 106,204 | 3.2% | 8.42B | 5 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,948 | +5,948 | 128,228 | 2.6% | 7.48B | 5 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,062 | +92 | 162,112 | 1.9% | 11.17B | 16 |
| 44 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,661 | +87 | 63,822 | 2.8% | 11.77B | 4 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,494 | -9 | 45,440 | 3.1% | 8.03B | 7 |
| 46 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,357 | +9 | 28,591 | 3.4% | 33.12B | 1 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,288 | +150 | 141,679 | 1.8% | 2.25B | 7 |
| 48 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,209 | +39 | 90,171 | 2.2% | 2.89B | 1 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,110 | +13 | 667,189 | 0.5% | 7.45B | 2 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,916 | -13 | 902,317 | 0.4% | 23.57B | 2 |
| 51 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,683 | +240 | 131,319 | 1.6% | 7.40B | 3 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,609 | +39 | 54,159 | 2.3% | 7.55B | 1 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,512 | +3,512 | 250,771 | 1.0% | 4.76B | 5 |
| 54 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,510 | -40 | 56,186 | 2.2% | 1.60B | 5 |
| 55 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,435 | -18 | 30,863 | 2.6% | 14.03B | 1 |
| 56 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,421 | +1 | 5,374,817 | 0.1% | 22.25B | 1 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,342 | +90 | 369,645 | 0.7% | 7.24B | 8 |
| 58 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,950 | +2,950 | 11,235 | 2.7% | 572.6M | 5 |
| 59 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,477 | +1 | 38,774 | 1.8% | 321.0M | 2 |
| 60 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,455 | +7 | 5,030,719 | 0.0% | 122.61B | 1 |
| 61 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,346 | +72 | 19,533 | 2.0% | 4.30B | 2 |
| 62 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,248 | +27 | 146,220 | 0.9% | 7.24B | 4 |
| 63 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,241 | +22 | 107,541 | 1.1% | 7.29B | 2 |
| 64 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,145 | +51 | 33,673 | 1.6% | 2.61B | 3 |
| 65 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,082 | +37 | 16,525 | 1.8% | 12.19B | 2 |
| 66 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,049 | -23 | 14,078 | 1.8% | 3.83B | 5 |
| 67 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,026 | +137 | 64,017 | 1.2% | 14.08B | 1 |
| 68 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,828 | +68 | 9,038 | 1.7% | 9.15B | 1 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,650 | +12 | 31,799 | 1.3% | 22.64B | 1 |
| 70 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,577 | +62 | 7,501 | 1.5% | 28.84B | 3 |
| 71 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,567 | +562 | 6,780 | 1.5% | 1.51B | 6 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,544 | +7 | 22,291 | 1.3% | 22.64B | 1 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,500 | -63 | 77,175 | 0.8% | 7.45B | 1 |
| 74 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,495 | +82 | 19,087 | 1.3% | 12.25B | 3 |
| 75 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,431 | 0 | 11,995 | 1.3% | 31.59B | 6 |
| 76 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,414 | +40 | 175,842 | 0.5% | 12.25B | 6 |
| 77 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,396 | +58 | 21,681 | 1.1% | 11.17B | 5 |
| 78 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,392 | -148 | 6,994 | 1.3% | 4.30B | 3 |
| 79 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,384 | +395 | 172,614 | 0.5% | 11.51B | 7 |
| 80 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,303 | -15 | 47,900 | 0.9% | 9.24B | 4 |
| 81 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,293 | +4 | 43,759 | 0.9% | 12.19B | 2 |
| 82 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,287 | +48 | 29,884 | 1.0% | 11.17B | 5 |
| 83 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,226 | 0 | 98,681 | 0.6% | 30.68B | 1 |
| 84 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,211 | -13 | 2,804 | 1.2% | 31.59B | 6 |
| 85 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,206 | +21 | 104,836 | 0.6% | 7.45B | 1 |
| 86 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,175 | +48 | 31,989 | 0.9% | 56.7M | 1 |
| 87 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,145 | +22 | 354,907 | 0.3% | — | 3 |
| 88 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,101 | +14 | 95,247 | 0.6% | 1.35B | 8 |
| 89 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,048 | -7 | 80,969 | 0.6% | 8.03B | 3 |
| 90 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,043 | +14 | 300,277 | 0.3% | 6.74B | 2 |
| 91 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,039 | +10 | 156,712 | 0.4% | 1.10B | 1 |
| 92 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,006 | -2 | 56,640 | 0.6% | 1.35B | 3 |
| 93 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 998 | +30 | 38,365 | 0.7% | 70.55B | 3 |
| 94 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 982 | -10 | 12,356 | 0.9% | 70.55B | 2 |
| 95 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 979 | -9 | 217,600 | 0.3% | 12.19B | 3 |
| 96 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 971 | +13 | 144,463 | 0.4% | 13.02B | 1 |
| 97 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 960 | +4 | 37,343 | 0.7% | 27.23B | 3 |
| 98 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 960 | +14 | 183,660 | 0.3% | 6.74B | 1 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 952 | -27 | 799,786 | 0.1% | — | 3 |
| 100 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 944 | +31 | 7,071 | 0.9% | 9.82B | 1 |
| 101 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 935 | -1 | 7,906 | 0.9% | 27.43B | 3 |
| 102 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 931 | +8 | 83,816 | 0.5% | 2.22B | 1 |
| 103 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 923 | +14 | 48,251 | 0.6% | 7.77B | 1 |
| 104 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 895 | +21 | 227,354 | 0.3% | 35.13B | 4 |
| 105 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 877 | +150 | 149,942 | 0.4% | 23.57B | 2 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 784 | +2 | 1,088 | 0.8% | 27.23B | 3 |
| 107 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 757 | +30 | 18,164 | 0.6% | 1.20B | 2 |
| 108 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 747 | +15 | 70,094 | 0.4% | 8.03B | 3 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 676 | +29 | 13,777 | 0.6% | 353.4M | 2 |
| 110 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 653 | -33 | 81,913 | 0.4% | 9.15B | 1 |
| 111 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 649 | -1 | 13,585 | 0.6% | 4.33B | 3 |
| 112 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 608 | -33 | 450,944 | 0.1% | 40.43B | 1 |
| 113 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 580 | -13 | 2,777 | 0.6% | 30.68B | 1 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 579 | +63 | 19,704 | 0.5% | 3.20B | 2 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 546 | -20 | 3,434 | 0.5% | 8.03B | 3 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 518 | +18 | 32,258 | 0.4% | 40.43B | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 512 | -9 | 1,273 | 0.5% | 31.58B | 2 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 472 | -91 | 321,716 | 0.1% | 7.24B | 2 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 463 | +79 | 2,772 | 0.5% | 560.9M | 2 |
| 120 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 458 | +12 | 51,862 | 0.3% | 7.24B | 5 |
| 121 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 436 | +23 | 7,063 | 0.4% | 31.59B | 6 |
| 122 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 429 | -6 | 44,278 | 0.3% | 7.70B | 5 |
| 123 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 423 | +11 | 232,304 | 0.1% | — | 2 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 413 | +4 | 106,765 | 0.2% | — | 3 |
| 125 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 406 | +7 | 15,553 | 0.4% | 1.54B | 4 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 389 | +14 | 38,882 | 0.3% | 7.48B | 2 |
| 127 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 388 | +10 | 50,764 | 0.3% | 7.24B | 1 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 384 | -13 | 75,825 | 0.2% | 7.04B | 4 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 361 | 0 | 21,611 | 0.3% | 2.61B | 2 |
| 130 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 355 | -3 | 2,371 | 0.3% | 4.02B | 2 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | -10 | 27,006 | 0.3% | 9.24B | 2 |
| 132 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 268 | -17 | 4,856 | 0.3% | 437.8M | 1 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 266 | -12 | 41,477 | 0.2% | 11.17B | 1 |
| 134 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 251 | +2 | 11,542 | 0.2% | 27.23B | 2 |
| 135 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 217 | -40 | 21,287 | 0.2% | 9.24B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 213 | -3 | 16,299 | 0.2% | 7.29B | 2 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 198 | +17 | 5,255 | 0.2% | 353.4M | 2 |
| 138 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 194 | +4 | 921 | 0.2% | — | 1 |
| 139 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 190 | +16 | 19,326 | 0.2% | 68.98B | 2 |
| 140 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 154 | +2 | 38,523 | 0.1% | 70.55B | 3 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 153 | +1 | 5,064 | 0.1% | 11.51B | 5 |
| 142 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | -1 | 7,099 | 0.1% | 1.20B | 2 |
| 143 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 139 | +8 | 2,242 | 0.1% | — | 1 |
| 144 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 135 | -21 | 1,938 | 0.1% | — | 1 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 128 | +1 | 4,785 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 114 | +4 | 28,179 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 113 | +3 | 1,225 | 0.1% | 560.9M | 1 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 83 | -12 | 177 | 0.1% | 437.8M | 1 |
| 149 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68 | +5 | 914 | 0.1% | — | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | -11 | 250 | 0.0% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 44 | +1 | 327 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | 0 | 136 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +1 | 348 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 18 | 0 | 151 | 0.0% | 8.16B | 3 |
| 156 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 17 | 0 | 204 | 0.0% | 15.17B | 3 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | +1 | 106 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,452,984 | 295,593,923 | 30 | 2.9% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,051,654 | 1,420,704 | 11 | 69.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 688,894 | 4,633,229 | 7 | 14.6% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 288,061 | 2,092,520 | 11 | 13.1% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 285,357 | 6,276,043 | 12 | 4.5% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,208 | 1,340,192 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,788 | 424,772 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | UA | 13,493 | 531,695 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,693 | 185,410 | 6 | 3.0% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,688 | 351,266 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,370 | 189,364 | 3 | 2.5% |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,052 | 365,329 | 10 | 1.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,816 | 849,200 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,814 | 691,361 | 2 | 0.5% |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,683 | 131,319 | 1 | 1.6% |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,590 | 23,135 | 4 | 2.9% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,970 | 484,835 | 3 | 0.5% |
| 18 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,957 | 147,833 | 2 | 1.2% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,188 | 655,184 | 2 | 0.3% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,107 | 151,887 | 2 | 0.8% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,978 | 1,158,181 | 4 | 0.2% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,841 | 101,813 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 944 | 7,071 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 384 | 75,825 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 135 | 1,938 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,590,462 | 56,381,821 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 494,765 | 3,971,068 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,426 | 415,449 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 237,532 | 4,134,404 | 14 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 204,944 | 400,520 | 16 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,871 | 667,060 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,552 | 106,204 | 41 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,661 | 63,822 | 44 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,494 | 45,440 | 45 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,209 | 90,171 | 48 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,110 | 667,189 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,683 | 131,319 | 51 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,342 | 369,645 | 57 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | MamayLM Gemma 3 4B v1.0 | 2,346 | 19,533 | 61 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,026 | 64,017 | 67 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 1,495 | 19,087 | 74 |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,431 | 11,995 | 75 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,226 | 98,681 | 83 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,145 | 354,907 | 87 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,101 | 95,247 | 88 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,039 | 156,712 | 91 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 952 | 799,786 | 99 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 944 | 7,071 | 100 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 384 | 75,825 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 135 | 1,938 | 144 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.2% | 1,051,654 | 1,420,704 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 14.6% | 688,894 | 4,633,229 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 13.1% | 288,061 | 2,092,520 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.5% | 285,357 | 6,276,043 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,788 | 424,772 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.0% | 8,693 | 185,410 | 9 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.9% | 3,590 | 23,135 | 16 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.9% | 8,452,984 | 295,593,923 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,208 | 1,340,192 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,370 | 189,364 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,493 | 531,695 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,688 | 351,266 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,683 | 131,319 | 15 |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.5% | 7,052 | 365,329 | 12 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.2% | 2,957 | 147,833 | 18 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,841 | 101,813 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 0.9% | 944 | 7,071 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,107 | 151,887 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,816 | 849,200 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,970 | 484,835 | 17 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,814 | 691,361 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,188 | 655,184 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 384 | 75,825 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,978 | 1,158,181 | 21 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 135 | 1,938 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
