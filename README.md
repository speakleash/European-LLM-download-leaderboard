# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-28
- **Generated at:** 2026-10-28T12:25:58Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,890,095 | -7,456 | 59,324,166 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,832,566 | +855 | 66,353,031 | 2.8% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 541,739 | +35,365 | 46,221,652 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 474,601 | +25,637 | 4,154,272 | 11.2% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 405,152 | -8,739 | 4,603,467 | 8.6% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 307,699 | +6,775 | 32,634,892 | 0.9% | 46.70B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 291,738 | -2,639 | 16,617,585 | 1.7% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 238,665 | -31,373 | 735,778 | 28.6% | 8.90B | 1 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 216,858 | +598 | 5,792,647 | 3.7% | 4.25B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 215,711 | -6,910 | 4,939,405 | 4.3% | 24.01B | 2 |
| 11 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 200,465 | +8,917 | 2,403,702 | 8.0% | 8.92B | 6 |
| 12 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 193,089 | +1,126 | 939,111 | 18.6% | 1.66B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 174,279 | -7,644 | 3,000,286 | 5.6% | 24.01B | 1 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 147,161 | -30,549 | 5,583,533 | 2.6% | 24.01B | 1 |
| 15 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 111,978 | +11,688 | 178,598 | 40.2% | 12.77B | 5 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 92,091 | +2,768 | 7,666,637 | 1.2% | 23.57B | 2 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,896 | +3,017 | 730,972 | 8.4% | 119.40B | 3 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,427 | +385 | 792,797 | 7.8% | 23.57B | 2 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 67,078 | +4 | 11,272,076 | 0.6% | 140.63B | 2 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 53,086 | -1,701 | 8,562,773 | 0.6% | 8.02B | 1 |
| 21 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 41,171 | +1,160 | 718,821 | 5.0% | 7.77B | 8 |
| 22 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,051 | +340 | 360,220 | 7.4% | 24.01B | 2 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 30,997 | -7,041 | 1,113,950 | 2.6% | 127.70B | 2 |
| 24 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,613 | -12,695 | 601,140 | 4.4% | 22.64B | 1 |
| 25 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,165 | +587 | 239,456 | 8.0% | — | 1 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,484 | +12 | 44,052 | 17.0% | 12.25B | 3 |
| 27 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,758 | +67 | 4,165,325 | 0.5% | 11.34B | 8 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 18,358 | -495 | 548,638 | 2.8% | 70.60B | 2 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,781 | -19 | 646,052 | 2.0% | 23.57B | 2 |
| 30 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,843 | +141 | 791,129 | 1.6% | 11.25B | 10 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,382 | +43 | 157,370 | 5.2% | 9.15B | 1 |
| 32 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,449 | -626 | 5,045,091 | 0.2% | 122.61B | 1 |
| 33 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,727 | +52 | 20,092 | 9.8% | 27.43B | 3 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,190 | +44 | 518,742 | 1.8% | 7.24B | 8 |
| 35 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,877 | -111 | 491,833 | 1.8% | 9.15B | 1 |
| 36 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,877 | +215 | 4,936,054 | 0.2% | 122.61B | 1 |
| 37 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,850 | -212 | 83,258 | 5.9% | — | 5 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,544 | +197 | 5,385,749 | 0.2% | 22.25B | 1 |
| 39 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,344 | -19,974 | 76,179 | 4.7% | — | 1 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,059 | +861 | 33,196 | 6.1% | 72.01B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,961 | -56 | 20,499 | 5.8% | 572.6M | 5 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,820 | -687 | 139,098 | 2.9% | 7.48B | 5 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,721 | +33 | 115,638 | 3.1% | 8.42B | 7 |
| 44 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,208 | +751 | 150,000 | 2.5% | 2.25B | 7 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,956 | +133 | 355,047 | 1.3% | 125.03B | 1 |
| 46 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,485 | -8 | 81,576 | 3.0% | 7.04B | 4 |
| 47 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,969 | +183 | 12,954 | 4.4% | 1.51B | 6 |
| 48 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,862 | -66 | 138,400 | 2.0% | 7.40B | 3 |
| 49 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,433 | +20 | 152,531 | 1.8% | 7.24B | 4 |
| 50 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,432 | -8 | 168,602 | 1.7% | 11.17B | 16 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,372 | +28 | 376,150 | 0.9% | 7.24B | 8 |
| 52 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,299 | -25 | 5,163,259 | 0.1% | 22.25B | 1 |
| 53 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,292 | +432 | 19,056 | 3.6% | 3.83B | 5 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,068 | +4 | 908,657 | 0.4% | 23.57B | 2 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,927 | +23 | 39,155 | 2.8% | 2.61B | 3 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,916 | +58 | 61,539 | 2.4% | 1.60B | 5 |
| 57 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,772 | +33 | 156,617 | 1.5% | 23.57B | 2 |
| 58 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,766 | -44 | 52,205 | 2.5% | 8.03B | 7 |
| 59 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,750 | +164 | 256,314 | 1.1% | 4.76B | 5 |
| 60 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,280 | +133 | 35,811 | 2.4% | 56.7M | 1 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,128 | +16 | 94,689 | 1.6% | 2.89B | 1 |
| 62 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,839 | -52 | 42,511 | 2.0% | 13.29B | 3 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,677 | +21 | 34,298 | 2.0% | 14.03B | 1 |
| 64 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,665 | +8 | 25,882 | 2.1% | 22.64B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,460 | +15 | 179,012 | 0.9% | 12.25B | 6 |
| 66 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,295 | +175 | 5,302,764 | 0.0% | 7.25B | 1 |
| 67 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,179 | +52 | 22,046 | 1.8% | 4.30B | 2 |
| 68 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,122 | +95 | 51,493 | 1.4% | 7.77B | 1 |
| 69 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,105 | -150 | 415,540 | 0.4% | 1.20B | 1 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,015 | +35 | 50,974 | 1.3% | 9.24B | 4 |
| 71 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,969 | +100 | 229,778 | 0.6% | 35.13B | 4 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,952 | +32 | 101,409 | 1.0% | 30.68B | 1 |
| 73 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,939 | -148 | 400,384 | 0.4% | 3.21B | 1 |
| 74 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,925 | +40 | 357,572 | 0.4% | — | 3 |
| 75 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,908 | -92 | 19,383 | 1.6% | 12.19B | 2 |
| 76 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,903 | +35 | 79,899 | 1.1% | 7.45B | 1 |
| 77 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,893 | -155 | 418,855 | 0.4% | 353.4M | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,847 | +28 | 107,512 | 0.9% | 7.45B | 1 |
| 79 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,751 | +28 | 9,086 | 1.6% | 4.30B | 3 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,741 | +28 | 34,226 | 1.3% | 22.64B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,724 | +26 | 159,171 | 0.7% | 1.10B | 1 |
| 82 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,716 | +30 | 302,655 | 0.4% | 6.74B | 2 |
| 83 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,666 | +34 | 185,972 | 0.6% | 6.74B | 1 |
| 84 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,648 | +28 | 146,750 | 0.7% | 13.02B | 1 |
| 85 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,629 | -118 | 670,915 | 0.2% | 7.45B | 2 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,550 | +5 | 54,074 | 1.0% | 7.24B | 5 |
| 87 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,507 | +52 | 40,191 | 1.1% | 70.55B | 3 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,486 | +11 | 9,075 | 1.4% | 9.82B | 1 |
| 89 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,473 | +13 | 52,859 | 1.0% | 7.24B | 1 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,424 | -17 | 174,621 | 0.5% | 11.51B | 7 |
| 91 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,341 | +15 | 31,424 | 1.0% | 33.12B | 1 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,339 | -22 | 23,659 | 1.1% | 11.17B | 5 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,240 | +54 | 801,568 | 0.1% | — | 3 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,190 | -101 | 19,878 | 1.0% | 1.20B | 2 |
| 95 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,119 | -47 | 10,494 | 1.0% | 9.15B | 1 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,115 | -24 | 31,538 | 0.8% | 11.17B | 5 |
| 97 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,085 | +8 | 56,183 | 0.7% | 7.55B | 1 |
| 98 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,059 | -31 | 9,061 | 1.0% | 28.84B | 3 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,040 | +13 | 58,240 | 0.7% | 1.35B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 990 | +17 | 15,178 | 0.9% | 353.4M | 2 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 893 | +16 | 453,234 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 815 | -9 | 218,632 | 0.3% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 801 | +14 | 44,789 | 0.6% | 12.19B | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 781 | -33 | 112,066 | 0.4% | 7.29B | 2 |
| 105 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 758 | +7 | 16,712 | 0.6% | 1.54B | 4 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 663 | -7 | 81,932 | 0.4% | 8.03B | 3 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 646 | +8 | 14,445 | 0.6% | 4.33B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 612 | +15 | 96,241 | 0.3% | 1.35B | 8 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 533 | -13 | 4,253 | 0.5% | 8.03B | 3 |
| 110 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 522 | +177 | 1,710 | 0.5% | 27.23B | 3 |
| 111 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 512 | +30 | 3,458 | 0.5% | 30.68B | 1 |
| 112 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 499 | +4 | 21,913 | 0.4% | 9.24B | 2 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 471 | +52 | 233,090 | 0.1% | — | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 422 | -11 | 20,435 | 0.4% | 3.20B | 2 |
| 115 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 416 | +4 | 1,523 | 0.4% | — | 1 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 374 | +4 | 32,831 | 0.3% | 40.43B | 2 |
| 117 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 355 | +17 | 27,589 | 0.3% | 9.24B | 2 |
| 118 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 325 | -1 | 2,762 | 0.3% | 4.02B | 2 |
| 119 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 322 | +10 | 37,795 | 0.2% | 27.23B | 3 |
| 120 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 321 | +7 | 5,478 | 0.3% | 11.51B | 5 |
| 121 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 318 | +4 | 22,048 | 0.3% | 2.61B | 2 |
| 122 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 315 | -6 | 84,538 | 0.2% | 9.15B | 1 |
| 123 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 302 | +4 | 12,027 | 0.3% | 27.23B | 2 |
| 124 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 301 | -5 | 322,217 | 0.1% | 7.24B | 2 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 298 | +11 | 107,182 | 0.1% | — | 3 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 293 | +9 | 39,370 | 0.2% | 7.48B | 2 |
| 127 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 277 | +6 | 5,148 | 0.3% | 437.8M | 1 |
| 128 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 251 | -6 | 12,696 | 0.2% | 70.55B | 2 |
| 129 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 227 | +5 | 19,646 | 0.2% | 68.98B | 2 |
| 130 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 219 | +4 | 44,617 | 0.2% | 7.70B | 5 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 218 | -5 | 41,858 | 0.2% | 11.17B | 1 |
| 132 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 212 | -5 | 5,041 | 0.2% | 70.55B | 3 |
| 133 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 195 | -5 | 2,530 | 0.2% | — | 1 |
| 134 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 185 | -5 | 16,587 | 0.2% | 7.29B | 2 |
| 135 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | -14 | 7,461 | 0.2% | 31.59B | 6 |
| 136 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 182 | +2 | 70,436 | 0.1% | 8.03B | 3 |
| 137 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 162 | +5 | 3,124 | 0.2% | 560.9M | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 153 | +4 | 5,464 | 0.1% | 353.4M | 2 |
| 139 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 153 | -1 | 28,386 | 0.1% | 46.70B | 6 |
| 140 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 142 | -3 | 12,151 | 0.1% | 31.59B | 6 |
| 141 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 6,171 | 0.1% | 12.25B | 3 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 134 | +10 | 1,133 | 0.1% | — | 1 |
| 143 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 105 | -68 | 1,503 | 0.1% | 31.58B | 2 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 103 | -1 | 7,246 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 99 | -1 | 38,707 | 0.1% | 70.55B | 3 |
| 146 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 82 | -2 | 432 | 0.1% | 321.0M | 1 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 70 | 0 | 1,302 | 0.1% | 560.9M | 1 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | 0 | 397 | 0.0% | 437.8M | 1 |
| 149 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | -5 | 2,854 | 0.0% | 31.59B | 6 |
| 150 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 40 | -1 | 254 | 0.0% | 15.17B | 3 |
| 151 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 34 | -2 | 192 | 0.0% | 8.16B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 34 | +1 | 220 | 0.0% | 437.8M | 1 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 131 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 274 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | +2 | 157 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,787,979 | 305,509,800 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 686,456 | 5,973,588 | 7 | 11.3% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 285,088 | 2,625,735 | 11 | 10.5% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 116,017 | 306,224 | 6 | 28.6% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 69,126 | 6,377,903 | 12 | 1.1% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 50,768 | 1,406,379 | 5 | 3.4% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,261 | 397,840 | 10 | 6.1% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,575 | 560,678 | 13 | 3.3% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,237 | 1,443,231 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,345 | 444,079 | 6 | 2.3% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,549 | 367,676 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,344 | 76,179 | 1 | 4.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,233 | 199,625 | 3 | 2.4% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,485 | 81,576 | 1 | 3.0% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,379 | 858,326 | 3 | 0.6% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,038 | 491,893 | 3 | 0.9% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,862 | 138,400 | 1 | 2.0% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,673 | 698,367 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,641 | 660,227 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,538 | 105,313 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,236 | 1,161,486 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,652 | 154,481 | 2 | 0.6% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,486 | 9,075 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 475 | 23,969 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,890,095 | 59,324,166 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 405,152 | 4,603,467 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 193,089 | 939,111 | 12 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 111,978 | 178,598 | 15 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 41,171 | 718,821 | 21 |
| 6 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,484 | 44,052 | 26 |
| 7 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,758 | 4,165,325 | 27 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,727 | 20,092 | 33 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,344 | 76,179 | 39 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,721 | 115,638 | 43 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,485 | 81,576 | 46 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,862 | 138,400 | 48 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,433 | 152,531 | 49 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,372 | 376,150 | 51 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,766 | 52,205 | 58 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,280 | 35,811 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,952 | 101,409 | 72 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,925 | 357,572 | 74 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,903 | 79,899 | 76 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,724 | 159,171 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,486 | 9,075 | 88 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,240 | 801,568 | 93 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,040 | 58,240 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 185 | 7,461 | 135 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 28.6% | 116,017 | 306,224 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 11.3% | 686,456 | 5,973,588 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 10.5% | 285,088 | 2,625,735 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,261 | 397,840 | 7 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | 4.7% | 8,344 | 76,179 | 12 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.4% | 50,768 | 1,406,379 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,575 | 560,678 | 8 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,485 | 81,576 | 14 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,549 | 367,676 | 11 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,233 | 199,625 | 13 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.3% | 12,345 | 444,079 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,787,979 | 305,509,800 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.0% | 4,862 | 138,400 | 17 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,486 | 9,075 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,538 | 105,313 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 69,126 | 6,377,903 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,237 | 1,443,231 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,038 | 491,893 | 16 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.6% | 1,652 | 154,481 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,673 | 698,367 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,379 | 858,326 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,641 | 660,227 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 475 | 23,969 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,236 | 1,161,486 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
