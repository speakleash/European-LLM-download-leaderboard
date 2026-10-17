# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-17
- **Generated at:** 2026-10-17T10:23:28Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,193,507 | -22,586 | 58,735,748 | 3.7% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,663,750 | +25,700 | 65,743,777 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 589,026 | -32,626 | 732,307 | 70.8% | 8.90B | 1 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 480,865 | +185 | 4,482,896 | 10.5% | 8.05B | 2 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 463,404 | -15,943 | 45,993,811 | 1.0% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 341,497 | +13,455 | 3,895,348 | 8.5% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 323,480 | -1,730 | 16,537,976 | 1.9% | 12.25B | 3 |
| 8 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 291,025 | -13,665 | 2,986,004 | 9.4% | 24.01B | 1 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 290,857 | -3,057 | 4,896,176 | 5.8% | 24.01B | 2 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,773 | -362 | 5,548,520 | 4.6% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 255,941 | +4,761 | 32,485,964 | 0.8% | 46.70B | 2 |
| 12 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,402 | +342 | 927,930 | 22.5% | 1.66B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,715 | -1,647 | 5,717,506 | 3.9% | 4.25B | 7 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 221,289 | -1,751 | 2,314,217 | 9.2% | 8.92B | 6 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 173,940 | -13,426 | 598,740 | 24.9% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 86,706 | -12,090 | 8,549,339 | 1.0% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,626 | -679 | 716,255 | 9.3% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,870 | +581 | 1,108,032 | 6.2% | 127.70B | 2 |
| 19 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,323 | +3,528 | 7,628,992 | 0.9% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 72,237 | +1,088 | 74,221 | 41.5% | — | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,507 | +532 | 767,466 | 8.2% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,622 | +617 | 11,252,593 | 0.6% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,766 | +212 | 118,922 | 25.0% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 34,254 | +6,551 | 703,907 | 4.3% | 7.77B | 8 |
| 25 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,607 | +21 | 236,978 | 9.1% | — | 1 |
| 26 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 25,409 | +330 | 349,114 | 5.7% | 24.01B | 2 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,223 | +39 | 43,384 | 16.9% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,752 | +453 | 544,131 | 3.4% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 21,095 | -224 | 4,157,081 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,089 | -538 | 155,215 | 7.5% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,356 | -1,224 | 639,877 | 1.9% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,914 | +196 | 785,535 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,179 | -125 | 80,824 | 7.3% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,546 | +177 | 514,942 | 1.9% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,453 | +6,781 | 19,544 | 9.6% | 27.43B | 3 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,371 | -448 | 488,136 | 1.9% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,803 | +372 | 4,931,556 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,130 | +15 | 137,595 | 3.8% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,393 | +107 | 5,382,691 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,588 | +132 | 17,893 | 5.6% | 572.6M | 5 |
| 41 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,056 | +295 | 147,870 | 2.4% | 2.25B | 7 |
| 42 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,462 | -10 | 51,135 | 3.6% | 8.03B | 7 |
| 43 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,436 | +38 | 81,286 | 3.0% | 7.04B | 4 |
| 44 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,322 | +21 | 111,872 | 2.5% | 8.42B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,235 | +68 | 136,822 | 2.2% | 7.40B | 3 |
| 46 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,134 | +131 | 352,470 | 1.1% | 125.03B | 1 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,903 | +63 | 167,216 | 1.8% | 11.17B | 16 |
| 48 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,736 | +119 | 5,162,167 | 0.1% | 22.25B | 1 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,672 | -11 | 374,647 | 1.0% | 7.24B | 8 |
| 50 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,585 | -149 | 154,969 | 1.8% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,404 | +39 | 150,879 | 1.8% | 7.24B | 4 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,025 | +38 | 254,873 | 1.1% | 4.76B | 5 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,980 | +12 | 5,034,889 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,868 | +43 | 906,339 | 0.4% | 23.57B | 2 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,782 | +296 | 37,577 | 2.7% | 2.61B | 3 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,648 | +378 | 59,918 | 2.3% | 1.60B | 5 |
| 57 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,623 | 0 | 27,683 | 2.8% | 72.01B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,258 | -140 | 67,681 | 1.9% | 14.08B | 1 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,175 | +36 | 93,519 | 1.6% | 2.89B | 1 |
| 60 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,142 | +203 | 10,001 | 2.9% | 1.51B | 6 |
| 61 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,064 | -78 | 400,176 | 0.6% | 3.21B | 1 |
| 62 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,047 | -77 | 415,127 | 0.6% | 1.20B | 1 |
| 63 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,047 | -172 | 670,536 | 0.4% | 7.45B | 2 |
| 64 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,030 | -74 | 418,627 | 0.6% | 353.4M | 1 |
| 65 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,667 | +28 | 25,057 | 2.1% | 22.64B | 1 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,625 | +19 | 86,608 | 1.4% | 2.22B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,571 | +55 | 41,426 | 1.8% | 13.29B | 3 |
| 68 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,545 | +56 | 50,832 | 1.7% | 7.77B | 1 |
| 69 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,534 | -3 | 84,469 | 1.4% | 9.15B | 1 |
| 70 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,505 | +60 | 34,564 | 1.9% | 56.7M | 1 |
| 71 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,466 | +46 | 178,400 | 0.9% | 12.25B | 6 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,242 | 0 | 30,862 | 1.7% | 33.12B | 1 |
| 73 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,070 | +49 | 18,655 | 1.7% | 12.19B | 2 |
| 74 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,903 | +239 | 32,832 | 1.4% | 14.03B | 1 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,895 | +36 | 452,859 | 0.3% | 40.43B | 1 |
| 76 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,872 | +11 | 79,155 | 1.0% | 7.45B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,863 | +19 | 100,639 | 0.9% | 30.68B | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,851 | +13 | 106,778 | 0.9% | 7.45B | 1 |
| 79 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,828 | +31 | 50,192 | 1.2% | 9.24B | 4 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,802 | +50 | 15,952 | 1.6% | 3.83B | 5 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,789 | +23 | 356,793 | 0.4% | — | 3 |
| 82 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,718 | +356 | 21,264 | 1.4% | 4.30B | 2 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,657 | +10 | 158,459 | 0.6% | 1.10B | 1 |
| 84 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,640 | +16 | 33,525 | 1.2% | 22.64B | 1 |
| 85 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,617 | +26 | 55,828 | 1.0% | 7.55B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,599 | +18 | 301,963 | 0.4% | 6.74B | 2 |
| 87 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,560 | +5 | 23,309 | 1.3% | 11.17B | 5 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,555 | +14 | 185,300 | 0.5% | 6.74B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,545 | +12 | 53,497 | 1.0% | 7.24B | 5 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,536 | +16 | 146,081 | 0.6% | 13.02B | 1 |
| 91 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,531 | -22 | 5,301,491 | 0.0% | 7.25B | 1 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,506 | +37 | 174,175 | 0.5% | 11.51B | 7 |
| 93 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,464 | +18 | 52,309 | 1.0% | 7.24B | 1 |
| 94 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,409 | -8 | 8,531 | 1.3% | 9.82B | 1 |
| 95 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,394 | +10 | 8,421 | 1.3% | 4.30B | 3 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,351 | -1 | 19,545 | 1.1% | 1.20B | 2 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,312 | +18 | 228,748 | 0.4% | 35.13B | 4 |
| 98 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,247 | +10 | 31,193 | 1.0% | 11.17B | 5 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,164 | +31 | 57,831 | 0.7% | 1.35B | 3 |
| 100 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,134 | +50 | 39,537 | 0.8% | 70.55B | 3 |
| 101 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,121 | +29 | 10,221 | 1.0% | 9.15B | 1 |
| 102 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,112 | +2 | 800,956 | 0.1% | — | 3 |
| 103 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,061 | -15 | 111,851 | 0.5% | 7.29B | 2 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,034 | +7 | 14,835 | 0.9% | 353.4M | 2 |
| 105 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 813 | +6 | 16,426 | 0.7% | 1.54B | 4 |
| 106 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 686 | -24 | 8,280 | 0.6% | 28.84B | 3 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 681 | +5 | 81,677 | 0.4% | 8.03B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 661 | -3 | 95,949 | 0.3% | 1.35B | 8 |
| 109 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 639 | +33 | 218,264 | 0.2% | 12.19B | 3 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 603 | +6 | 4,083 | 0.6% | 8.03B | 3 |
| 111 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 501 | -26 | 232,832 | 0.2% | — | 2 |
| 112 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 477 | +32 | 14,070 | 0.4% | 4.33B | 3 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 474 | +9 | 20,305 | 0.4% | 3.20B | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 462 | +41 | 44,242 | 0.3% | 12.19B | 2 |
| 115 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | +6 | 27,470 | 0.4% | 9.24B | 2 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 436 | +29 | 32,714 | 0.3% | 40.43B | 2 |
| 117 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 418 | +7 | 3,203 | 0.4% | 30.68B | 1 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 396 | -16 | 322,159 | 0.1% | 7.24B | 2 |
| 119 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 380 | +51 | 21,682 | 0.3% | 9.24B | 2 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 378 | +20 | 39,294 | 0.3% | 7.48B | 2 |
| 121 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 372 | -21 | 1,336 | 0.4% | — | 1 |
| 122 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 361 | +6 | 11,906 | 0.3% | 27.23B | 2 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 358 | +2 | 1,477 | 0.4% | 27.23B | 3 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 338 | +2 | 37,687 | 0.2% | 27.23B | 3 |
| 125 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 322 | -39 | 7,422 | 0.3% | 31.59B | 6 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 317 | +4 | 21,935 | 0.3% | 2.61B | 2 |
| 127 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 297 | -2 | 41,779 | 0.2% | 11.17B | 1 |
| 128 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 294 | -6 | 107,073 | 0.1% | — | 3 |
| 129 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 286 | -12 | 3,080 | 0.3% | 560.9M | 2 |
| 130 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 267 | -2 | 5,339 | 0.3% | 11.51B | 5 |
| 131 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 264 | -5 | 12,635 | 0.2% | 70.55B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 260 | -3 | 70,372 | 0.2% | 8.03B | 3 |
| 133 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 249 | +5 | 5,107 | 0.2% | 437.8M | 1 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 248 | +5 | 44,556 | 0.2% | 7.70B | 5 |
| 135 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 219 | +1 | 19,559 | 0.2% | 68.98B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 213 | 0 | 2,466 | 0.2% | — | 1 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 202 | -10 | 16,518 | 0.2% | 7.29B | 2 |
| 139 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 202 | -1 | 4,997 | 0.2% | 70.55B | 3 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 187 | -18 | 2,582 | 0.2% | 4.02B | 2 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 159 | +4 | 5,419 | 0.2% | 353.4M | 2 |
| 142 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 150 | -1 | 28,339 | 0.1% | 46.70B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 147 | +8 | 38,678 | 0.1% | 70.55B | 3 |
| 144 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 145 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 122 | +4 | 7,224 | 0.1% | 1.20B | 2 |
| 146 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 102 | -33 | 1,056 | 0.1% | — | 1 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 81 | +1 | 410 | 0.1% | 321.0M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 49 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 149 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 42 | +3 | 1,269 | 0.0% | 560.9M | 1 |
| 150 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 39 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 151 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 32 | +3 | 236 | 0.0% | 15.17B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 207 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | +2 | 376 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | +2 | 177 | 0.0% | 8.16B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 124 | 0.0% | 7.24B | 1 |
| 156 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | +1 | 265 | 0.0% | 437.8M | 1 |
| 157 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | -2 | 151 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,069,340 | 303,176,503 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,106,798 | 5,830,863 | 7 | 18.7% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 478,366 | 2,600,314 | 11 | 17.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 73,138 | 6,352,955 | 12 | 1.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 72,237 | 74,221 | 1 | 41.5% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,577 | 245,009 | 6 | 17.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 45,186 | 1,388,182 | 5 | 3.0% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,841 | 395,476 | 10 | 6.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,285 | 555,681 | 13 | 3.1% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,645 | 1,439,030 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,670 | 438,942 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,455 | 363,373 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,770 | 856,469 | 3 | 0.7% |
| 14 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 5,948 | 195,722 | 3 | 2.0% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,883 | 154,289 | 2 | 2.3% |
| 16 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,436 | 81,286 | 1 | 3.0% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,235 | 136,822 | 1 | 2.2% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,068 | 696,806 | 2 | 0.6% |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,748 | 489,840 | 3 | 0.8% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,388 | 658,756 | 2 | 0.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,339 | 104,255 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,126 | 1,160,420 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,825 | 153,780 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,409 | 8,531 | 1 | 1.3% |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 638 | 23,793 | 4 | 0.5% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,193,507 | 58,735,748 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 589,026 | 732,307 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,402 | 927,930 | 12 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 72,237 | 74,221 | 20 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,766 | 118,922 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 34,254 | 703,907 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,223 | 43,384 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 21,095 | 4,157,081 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,453 | 19,544 | 35 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,462 | 51,135 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,436 | 81,286 | 43 |
| 12 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,322 | 111,872 | 44 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,235 | 136,822 | 45 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,672 | 374,647 | 49 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,404 | 150,879 | 51 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,258 | 67,681 | 58 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 3B Preview | 3,064 | 400,176 | 61 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,047 | 670,536 | 63 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,863 | 100,639 | 77 |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,789 | 356,793 | 81 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,657 | 158,459 | 83 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,409 | 8,531 | 94 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,164 | 57,831 | 99 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,112 | 800,956 | 102 |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 322 | 7,422 | 125 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 41.5% | 72,237 | 74,221 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 18.7% | 1,106,798 | 5,830,863 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 17.7% | 478,366 | 2,600,314 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 17.0% | 58,577 | 245,009 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,841 | 395,476 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.1% | 20,285 | 555,681 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.0% | 45,186 | 1,388,182 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,436 | 81,286 | 16 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,670 | 438,942 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,455 | 363,373 | 12 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 7,069,340 | 303,176,503 | 1 |
| 12 | [Almawave](https://huggingface.co/Almawave) | 2.3% | 5,883 | 154,289 | 15 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,235 | 136,822 | 17 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.0% | 5,948 | 195,722 | 14 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,409 | 8,531 | 24 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,645 | 1,439,030 | 10 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,339 | 104,255 | 21 |
| 18 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 73,138 | 6,352,955 | 4 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,748 | 489,840 | 19 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,825 | 153,780 | 23 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,770 | 856,469 | 13 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,068 | 696,806 | 18 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 638 | 23,793 | 25 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,388 | 658,756 | 20 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,126 | 1,160,420 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
