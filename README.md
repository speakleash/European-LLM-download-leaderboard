# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-21
- **Generated at:** 2026-09-21T12:25:35Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,527,631 | -19,052 | 56,817,604 | 4.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,768,776 | -4,704 | 64,192,688 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 625,854 | -885 | 3,580,348 | 17.0% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 606,119 | +14,455 | 45,590,091 | 1.3% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 489,699 | -14,332 | 16,241,037 | 3.0% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 482,301 | -1,705 | 4,051,319 | 11.6% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 466,146 | +1,345 | 4,626,842 | 9.9% | 24.01B | 2 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 301,430 | -8,226 | 5,512,447 | 5.4% | 4.25B | 7 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 300,690 | -5,630 | 415,868 | 58.3% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 299,361 | -5,632 | 412,353 | 58.4% | 1.20B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 294,829 | +645 | 32,258,121 | 0.9% | 46.70B | 2 |
| 12 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 291,427 | -5,189 | 397,377 | 58.6% | 3.21B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 277,368 | +2,358 | 2,737,125 | 9.8% | 24.01B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 270,270 | +12,873 | 466,810 | 47.7% | 22.64B | 1 |
| 15 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 233,047 | +31,984 | 247,032 | 67.2% | 8.90B | 1 |
| 16 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 202,908 | -7,274 | 4,137,879 | 4.8% | 11.34B | 8 |
| 17 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 188,426 | +1,650 | 5,355,802 | 3.5% | 24.01B | 1 |
| 18 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 167,363 | -13,703 | 2,107,018 | 7.6% | 8.92B | 6 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 156,450 | -8,836 | 8,475,668 | 1.8% | 8.02B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,597 | -93 | 524,471 | 15.5% | 70.60B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 89,019 | -588 | 1,034,435 | 7.8% | 127.70B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,093 | +115 | 627,698 | 10.3% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,050 | -193 | 703,395 | 9.1% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,534 | -515 | 7,560,772 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 55,184 | -436 | 644,254 | 7.4% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 41,265 | +159 | 11,193,599 | 0.4% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,105 | +354 | 671,387 | 4.2% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 23,961 | +324 | 138,193 | 10.1% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,943 | +251 | 478,203 | 3.8% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,451 | -198 | 5,157,730 | 0.4% | 22.25B | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,398 | +206 | 24,437 | 14.0% | 72.01B | 1 |
| 32 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,990 | -130 | 323,963 | 3.8% | 24.01B | 2 |
| 33 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,837 | -12 | 772,925 | 1.8% | 11.25B | 10 |
| 34 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,417 | -201 | 347,668 | 3.2% | 125.03B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,205 | +25 | 5,300,064 | 0.2% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,130 | +47 | 68,605 | 7.8% | — | 5 |
| 37 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,829 | -31 | 697,588 | 1.6% | 1.66B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,310 | -49 | 206,751 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,018 | +257 | 504,516 | 1.7% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,132 | +975 | 129,888 | 3.1% | 7.48B | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,706 | +241 | 107,067 | 3.2% | 8.42B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,241 | -20 | 4,922,332 | 0.1% | 122.61B | 1 |
| 43 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,188 | +21 | 65,095 | 3.1% | 11.77B | 4 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,089 | +21 | 162,766 | 1.9% | 11.17B | 16 |
| 45 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,079 | -22 | 110,848 | 2.4% | 7.29B | 2 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,523 | -30 | 46,067 | 3.1% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,382 | -1 | 28,667 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,165 | -147 | 142,414 | 1.7% | 2.25B | 7 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,981 | +56 | 902,839 | 0.4% | 23.57B | 2 |
| 50 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,920 | +157 | 668,031 | 0.5% | 7.45B | 2 |
| 51 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,714 | +325 | 251,498 | 1.1% | 4.76B | 5 |
| 52 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,683 | +86 | 5,375,708 | 0.1% | 22.25B | 1 |
| 53 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,663 | +83 | 370,442 | 0.8% | 7.24B | 8 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,596 | +105 | 132,077 | 1.5% | 7.40B | 3 |
| 55 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,534 | -74 | 54,263 | 2.3% | 7.55B | 1 |
| 56 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,515 | -402 | 90,651 | 1.8% | 2.89B | 1 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,114 | +7 | 30,983 | 2.4% | 14.03B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,767 | +2 | 56,578 | 1.8% | 1.60B | 5 |
| 59 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,731 | +148 | 64,835 | 1.7% | 14.08B | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,548 | +77 | 146,913 | 1.0% | 7.24B | 4 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,456 | +7 | 34,380 | 1.8% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,414 | +39 | 5,031,216 | 0.0% | 122.61B | 1 |
| 63 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,070 | +10 | 39,027 | 1.5% | 321.0M | 2 |
| 64 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,988 | +353 | 151,210 | 0.8% | 23.57B | 2 |
| 65 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,903 | -25 | 14,242 | 1.7% | 3.83B | 5 |
| 66 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,768 | +41 | 48,526 | 1.2% | 9.24B | 4 |
| 67 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,734 | +24 | 32,054 | 1.3% | 22.64B | 1 |
| 68 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,635 | +40 | 22,565 | 1.3% | 22.64B | 1 |
| 69 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,604 | +36 | 77,485 | 0.9% | 7.45B | 1 |
| 70 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,556 | -24 | 11,398 | 1.4% | 572.6M | 5 |
| 71 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,536 | -5 | 9,151 | 1.4% | 9.15B | 1 |
| 72 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,487 | -20 | 6,988 | 1.4% | 1.51B | 6 |
| 73 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,442 | +3 | 21,957 | 1.2% | 11.17B | 5 |
| 74 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,427 | 0 | 12,000 | 1.3% | 31.59B | 6 |
| 75 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,345 | +13 | 176,077 | 0.5% | 12.25B | 6 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,340 | +81 | 105,151 | 0.7% | 7.45B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,332 | +41 | 98,970 | 0.7% | 30.68B | 1 |
| 78 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,325 | -27 | 172,829 | 0.5% | 11.51B | 7 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,265 | +42 | 355,179 | 0.3% | — | 3 |
| 80 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,263 | -19 | 30,056 | 1.0% | 11.17B | 5 |
| 81 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,256 | -6 | 19,589 | 1.1% | 4.30B | 2 |
| 82 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,180 | -3 | 19,243 | 1.0% | 12.25B | 3 |
| 83 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,167 | +66 | 7,814 | 1.1% | 28.84B | 3 |
| 84 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,166 | +38 | 156,977 | 0.5% | 1.10B | 1 |
| 85 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,154 | 0 | 2,810 | 1.1% | 31.59B | 6 |
| 86 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,153 | +96 | 84,297 | 0.6% | 2.22B | 1 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,132 | +30 | 300,511 | 0.3% | 6.74B | 2 |
| 88 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,073 | +37 | 16,693 | 0.9% | 12.19B | 2 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,068 | +33 | 144,687 | 0.4% | 13.02B | 1 |
| 90 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,064 | +37 | 183,892 | 0.4% | 6.74B | 1 |
| 91 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,060 | -46 | 95,361 | 0.5% | 1.35B | 8 |
| 92 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,039 | +25 | 32,163 | 0.8% | 56.7M | 1 |
| 93 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,015 | -3 | 81,058 | 0.6% | 8.03B | 3 |
| 94 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,012 | -29 | 800,028 | 0.1% | — | 3 |
| 95 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,011 | -14 | 7,117 | 0.9% | 4.30B | 3 |
| 96 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,008 | -10 | 8,248 | 0.9% | 27.43B | 3 |
| 97 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 985 | -12 | 7,159 | 0.9% | 9.82B | 1 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 984 | -24 | 56,780 | 0.6% | 1.35B | 3 |
| 99 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 977 | -15 | 38,445 | 0.7% | 70.55B | 3 |
| 100 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 937 | -9 | 227,514 | 0.3% | 35.13B | 4 |
| 101 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 885 | +20 | 37,392 | 0.6% | 27.23B | 3 |
| 102 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 811 | -16 | 12,393 | 0.7% | 70.55B | 2 |
| 103 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 798 | +7 | 18,250 | 0.7% | 1.20B | 2 |
| 104 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 785 | -77 | 1,171 | 0.8% | 27.23B | 3 |
| 105 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 777 | -39 | 48,320 | 0.5% | 7.77B | 1 |
| 106 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 747 | +39 | 19,888 | 0.6% | 3.20B | 2 |
| 107 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 713 | -1 | 70,148 | 0.4% | 8.03B | 3 |
| 108 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 707 | -230 | 217,692 | 0.2% | 12.19B | 3 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 670 | +5 | 13,873 | 0.6% | 353.4M | 2 |
| 110 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 649 | -7 | 81,987 | 0.4% | 9.15B | 1 |
| 111 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 621 | +5 | 13,626 | 0.5% | 4.33B | 3 |
| 112 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 618 | +40 | 52,100 | 0.4% | 7.24B | 5 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 595 | -3 | 232,499 | 0.2% | — | 2 |
| 114 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 570 | -20 | 450,994 | 0.1% | 40.43B | 1 |
| 115 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 564 | -4 | 43,812 | 0.4% | 12.19B | 2 |
| 116 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 554 | -3 | 2,803 | 0.5% | 30.68B | 1 |
| 117 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 541 | -13 | 321,829 | 0.1% | 7.24B | 2 |
| 118 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 539 | +39 | 50,987 | 0.4% | 7.24B | 1 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 526 | -8 | 32,347 | 0.4% | 40.43B | 2 |
| 120 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 510 | 0 | 1,273 | 0.5% | 31.58B | 2 |
| 121 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 487 | -14 | 3,530 | 0.5% | 8.03B | 3 |
| 122 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 462 | -6 | 2,797 | 0.4% | 560.9M | 2 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 458 | +44 | 38,988 | 0.3% | 7.48B | 2 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 452 | +38 | 27,134 | 0.4% | 9.24B | 2 |
| 125 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 437 | -9 | 44,327 | 0.3% | 7.70B | 5 |
| 126 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 407 | 0 | 7,190 | 0.4% | 31.59B | 6 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 401 | 0 | 106,808 | 0.2% | — | 3 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 375 | -17 | 75,893 | 0.2% | 7.04B | 4 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 371 | +9 | 21,636 | 0.3% | 2.61B | 2 |
| 130 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 368 | +2 | 15,637 | 0.3% | 1.54B | 4 |
| 131 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 354 | -15 | 2,400 | 0.3% | 4.02B | 2 |
| 132 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 323 | +44 | 11,627 | 0.3% | 27.23B | 2 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 286 | +4 | 1,043 | 0.3% | — | 1 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 256 | -3 | 41,496 | 0.2% | 11.17B | 1 |
| 135 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 235 | -1 | 21,321 | 0.2% | 9.24B | 2 |
| 136 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 233 | -8 | 4,860 | 0.2% | 437.8M | 1 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 231 | +15 | 16,347 | 0.2% | 7.29B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 209 | 0 | 19,361 | 0.2% | 68.98B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 200 | 0 | 5,275 | 0.2% | 353.4M | 2 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 169 | -3 | 5,097 | 0.2% | 11.51B | 5 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 164 | +5 | 2,278 | 0.2% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 162 | +2 | 38,545 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 139 | -3 | 7,114 | 0.1% | 1.20B | 2 |
| 144 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 133 | -12 | 1,986 | 0.1% | — | 1 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 129 | +2 | 4,800 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 123 | +3 | 28,197 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 107 | -2 | 1,228 | 0.1% | 560.9M | 1 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 100 | -4 | 958 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 82 | -2 | 179 | 0.1% | 437.8M | 1 |
| 150 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 55 | -25 | 6,035 | 0.1% | 12.25B | 3 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 41 | -1 | 251 | 0.0% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 39 | -3 | 330 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | +1 | 139 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | -1 | 349 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | -3 | 207 | 0.0% | 15.17B | 3 |
| 157 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 12 | -3 | 153 | 0.0% | 8.16B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,367,122 | 296,842,280 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 897,448 | 1,422,688 | 11 | 58.9% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 834,289 | 4,879,887 | 7 | 16.8% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 348,487 | 2,169,960 | 11 | 15.4% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 251,920 | 6,287,485 | 12 | 3.9% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,143 | 1,345,462 | 5 | 2.6% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,467 | 425,939 | 6 | 3.3% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,087 | 536,387 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,741 | 187,709 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,558 | 352,968 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,601 | 190,382 | 3 | 2.6% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,864 | 850,667 | 3 | 0.7% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,016 | 366,085 | 10 | 1.3% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,204 | 692,271 | 2 | 0.5% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 3,884 | 149,132 | 2 | 1.6% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,596 | 132,077 | 1 | 1.5% |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,498 | 23,273 | 4 | 2.8% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,298 | 485,556 | 3 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,397 | 655,690 | 2 | 0.3% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,217 | 1,158,696 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,044 | 152,141 | 2 | 0.8% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,911 | 102,133 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 985 | 7,159 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 375 | 75,893 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 133 | 1,986 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,527,631 | 56,817,604 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 482,301 | 4,051,319 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 300,690 | 415,868 | 9 |
| 4 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 270,270 | 466,810 | 14 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 202,908 | 4,137,879 | 16 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,105 | 671,387 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,706 | 107,067 | 41 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,188 | 65,095 | 43 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,079 | 110,848 | 45 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,523 | 46,067 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,920 | 668,031 | 50 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,663 | 370,442 | 53 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,596 | 132,077 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,515 | 90,651 | 56 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,731 | 64,835 | 59 |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,427 | 12,000 | 74 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,345 | 176,077 | 75 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,332 | 98,970 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,265 | 355,179 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,166 | 156,977 | 84 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,060 | 95,361 | 91 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,012 | 800,028 | 94 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 985 | 7,159 | 97 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 375 | 75,893 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 133 | 1,986 | 144 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 58.9% | 897,448 | 1,422,688 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 16.8% | 834,289 | 4,879,887 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 15.4% | 348,487 | 2,169,960 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.9% | 251,920 | 6,287,485 | 5 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,741 | 187,709 | 9 |
| 6 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.3% | 17,467 | 425,939 | 7 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,498 | 23,273 | 17 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,367,122 | 296,842,280 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,143 | 1,345,462 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.6% | 7,601 | 190,382 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,087 | 536,387 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,558 | 352,968 | 10 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.6% | 3,884 | 149,132 | 15 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,596 | 132,077 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 6,016 | 366,085 | 13 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,911 | 102,133 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 0.9% | 985 | 7,159 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,044 | 152,141 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,864 | 850,667 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.6% | 3,298 | 485,556 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,204 | 692,271 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,397 | 655,690 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 375 | 75,893 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,217 | 1,158,696 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 133 | 1,986 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
