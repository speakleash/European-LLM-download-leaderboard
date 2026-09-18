# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-18
- **Generated at:** 2026-09-18T10:53:00Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,570,029 | -21,547 | 56,552,629 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,773,263 | +28,034 | 64,082,933 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 622,235 | +1,083 | 3,554,758 | 17.0% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 589,098 | +18,321 | 45,533,277 | 1.3% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 519,538 | -9,678 | 16,215,498 | 3.2% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 491,614 | -1,078 | 4,004,845 | 12.0% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 457,252 | +7,860 | 4,606,360 | 9.7% | 24.01B | 2 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 352,528 | +37 | 415,601 | 68.4% | 353.4M | 1 |
| 9 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 350,129 | +43 | 412,086 | 68.4% | 1.20B | 1 |
| 10 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 339,812 | +49 | 397,116 | 68.4% | 3.21B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 331,308 | -5,683 | 5,492,574 | 5.9% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 298,197 | -1,667 | 32,230,819 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 260,664 | +8,181 | 2,697,735 | 9.3% | 24.01B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 230,760 | +13,564 | 426,904 | 43.8% | 22.64B | 1 |
| 15 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 226,739 | -8,267 | 4,136,017 | 5.4% | 11.34B | 8 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190,247 | -8,102 | 2,093,187 | 8.7% | 8.92B | 6 |
| 17 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 186,936 | -3,544 | 8,463,895 | 2.2% | 8.02B | 1 |
| 18 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 136,834 | +231 | 5,289,735 | 2.5% | 24.01B | 1 |
| 19 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 136,142 | +33,259 | 149,394 | 54.6% | 8.90B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 100,903 | -15,451 | 1,033,197 | 8.9% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,782 | -174 | 522,478 | 15.5% | 70.60B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,000 | +1,823 | 625,670 | 10.2% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,961 | -368 | 696,323 | 9.3% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,247 | +30 | 7,555,915 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,702 | -281 | 640,815 | 7.8% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 40,138 | +480 | 11,190,217 | 0.4% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 33,496 | +102 | 669,814 | 4.4% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,613 | -1,665 | 136,274 | 10.4% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,413 | +367 | 476,843 | 3.7% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,065 | -115 | 5,157,440 | 0.4% | 22.25B | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,179 | -391 | 24,060 | 13.8% | 72.01B | 1 |
| 32 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,160 | -32 | 323,704 | 3.8% | 24.01B | 2 |
| 33 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,859 | +11 | 771,661 | 1.8% | 11.25B | 10 |
| 34 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,788 | -586 | 347,354 | 3.5% | 125.03B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,655 | -481 | 5,299,962 | 0.3% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,434 | +211 | 67,730 | 8.0% | — | 5 |
| 37 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,427 | -578 | 696,540 | 1.7% | 1.66B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,557 | +116 | 206,377 | 3.8% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,510 | -3 | 503,439 | 1.6% | 7.24B | 8 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,688 | +37 | 106,557 | 3.2% | 8.42B | 5 |
| 41 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,661 | -279 | 4,921,784 | 0.1% | 122.61B | 1 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,010 | +48 | 128,468 | 2.6% | 7.48B | 5 |
| 43 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,340 | -46 | 110,789 | 2.5% | 7.29B | 2 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,051 | -41 | 162,316 | 1.9% | 11.17B | 16 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,705 | +22 | 64,094 | 2.9% | 11.77B | 4 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,671 | +126 | 45,664 | 3.2% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,368 | +2 | 28,620 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,240 | -10 | 141,818 | 1.8% | 2.25B | 7 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,209 | +72 | 667,518 | 0.5% | 7.45B | 2 |
| 50 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,965 | -215 | 90,353 | 2.1% | 2.89B | 1 |
| 51 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,866 | +17 | 902,513 | 0.4% | 23.57B | 2 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,645 | -3 | 54,211 | 2.4% | 7.55B | 1 |
| 53 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,471 | +46 | 5,375,316 | 0.1% | 22.25B | 1 |
| 54 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,470 | -39 | 250,850 | 1.0% | 4.76B | 5 |
| 55 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,466 | -136 | 131,599 | 1.5% | 7.40B | 3 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,455 | +114 | 369,994 | 0.7% | 7.24B | 8 |
| 57 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,135 | -242 | 56,275 | 2.0% | 1.60B | 5 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,094 | -215 | 30,928 | 2.4% | 14.03B | 1 |
| 59 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,445 | -14 | 11,313 | 2.2% | 572.6M | 5 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,343 | -106 | 38,859 | 1.7% | 321.0M | 2 |
| 61 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,334 | +233 | 64,435 | 1.4% | 14.08B | 1 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,306 | -110 | 5,030,923 | 0.0% | 122.61B | 1 |
| 63 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,289 | +64 | 146,489 | 0.9% | 7.24B | 4 |
| 64 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,104 | +17 | 33,811 | 1.6% | 2.61B | 3 |
| 65 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,996 | -70 | 14,159 | 1.7% | 3.83B | 5 |
| 66 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,756 | -84 | 9,104 | 1.6% | 9.15B | 1 |
| 67 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,668 | -1 | 48,373 | 1.1% | 9.24B | 4 |
| 68 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,633 | -214 | 19,547 | 1.4% | 4.30B | 2 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,622 | -2 | 31,895 | 1.2% | 22.64B | 1 |
| 70 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,541 | +16 | 6,867 | 1.4% | 1.51B | 6 |
| 71 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,529 | 0 | 22,400 | 1.2% | 22.64B | 1 |
| 72 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,496 | +9 | 77,293 | 0.8% | 7.45B | 1 |
| 73 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,432 | +3 | 12,000 | 1.3% | 31.59B | 6 |
| 74 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,429 | +20 | 21,753 | 1.2% | 11.17B | 5 |
| 75 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,420 | +4 | 175,942 | 0.5% | 12.25B | 6 |
| 76 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,372 | -45 | 19,162 | 1.2% | 12.25B | 3 |
| 77 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,365 | -34 | 172,669 | 0.5% | 11.51B | 7 |
| 78 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,348 | +319 | 150,447 | 0.5% | 23.57B | 2 |
| 79 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,313 | +16 | 29,946 | 1.0% | 11.17B | 5 |
| 80 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,224 | -1 | 98,784 | 0.6% | 30.68B | 1 |
| 81 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,223 | -68 | 7,658 | 1.1% | 28.84B | 3 |
| 82 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,191 | +11 | 32,063 | 0.9% | 56.7M | 1 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,179 | -15 | 104,936 | 0.6% | 7.45B | 1 |
| 84 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,175 | -36 | 2,810 | 1.1% | 31.59B | 6 |
| 85 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,141 | 0 | 355,011 | 0.3% | — | 3 |
| 86 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,133 | -143 | 7,029 | 1.1% | 4.30B | 3 |
| 87 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,128 | -420 | 16,591 | 1.0% | 12.19B | 2 |
| 88 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,105 | +7 | 95,290 | 0.6% | 1.35B | 8 |
| 89 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,047 | +1 | 81,003 | 0.6% | 8.03B | 3 |
| 90 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,035 | +6 | 156,810 | 0.4% | 1.10B | 1 |
| 91 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,034 | -3 | 300,371 | 0.3% | 6.74B | 2 |
| 92 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,009 | +4 | 38,405 | 0.7% | 70.55B | 3 |
| 93 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 994 | +1 | 56,668 | 0.6% | 1.35B | 3 |
| 94 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 993 | +66 | 83,997 | 0.5% | 2.22B | 1 |
| 95 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 981 | +10 | 217,634 | 0.3% | 12.19B | 3 |
| 96 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 980 | +21 | 7,125 | 0.9% | 9.82B | 1 |
| 97 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 962 | -3 | 144,551 | 0.4% | 13.02B | 1 |
| 98 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 959 | +130 | 8,115 | 0.9% | 27.43B | 3 |
| 99 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 954 | -1 | 183,752 | 0.3% | 6.74B | 1 |
| 100 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 939 | -22 | 799,844 | 0.1% | — | 3 |
| 101 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 922 | +14 | 227,435 | 0.3% | 35.13B | 4 |
| 102 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 860 | +4 | 37,350 | 0.6% | 27.23B | 3 |
| 103 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 847 | -57 | 48,288 | 0.6% | 7.77B | 1 |
| 104 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 841 | -114 | 12,373 | 0.7% | 70.55B | 2 |
| 105 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 815 | +31 | 1,120 | 0.8% | 27.23B | 3 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 764 | +12 | 18,190 | 0.6% | 1.20B | 2 |
| 107 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 711 | -2 | 70,113 | 0.4% | 8.03B | 3 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 695 | +2 | 19,832 | 0.6% | 3.20B | 2 |
| 109 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 679 | -210 | 43,783 | 0.5% | 12.19B | 2 |
| 110 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 641 | -5 | 13,594 | 0.6% | 4.33B | 3 |
| 111 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 630 | -48 | 13,803 | 0.6% | 353.4M | 2 |
| 112 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 616 | -22 | 81,935 | 0.3% | 9.15B | 1 |
| 113 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 593 | +4 | 450,966 | 0.1% | 40.43B | 1 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 580 | 0 | 2,786 | 0.6% | 30.68B | 1 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 548 | -2 | 3,482 | 0.5% | 8.03B | 3 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 523 | +7 | 32,280 | 0.4% | 40.43B | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 510 | -2 | 1,273 | 0.5% | 31.58B | 2 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 509 | +25 | 321,765 | 0.1% | 7.24B | 2 |
| 119 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 485 | +37 | 51,957 | 0.3% | 7.24B | 5 |
| 120 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 478 | +14 | 2,795 | 0.5% | 560.9M | 2 |
| 121 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 477 | +24 | 7,129 | 0.4% | 31.59B | 6 |
| 122 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 458 | +10 | 15,613 | 0.4% | 1.54B | 4 |
| 123 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 450 | 0 | 44,309 | 0.3% | 7.70B | 5 |
| 124 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 448 | +27 | 232,334 | 0.1% | — | 2 |
| 125 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 409 | +30 | 50,849 | 0.3% | 7.24B | 1 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 404 | +2 | 38,920 | 0.3% | 7.48B | 2 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 385 | -15 | 106,779 | 0.2% | — | 3 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 378 | +8 | 75,852 | 0.2% | 7.04B | 4 |
| 129 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 373 | +18 | 2,395 | 0.4% | 4.02B | 2 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 361 | -3 | 21,618 | 0.3% | 2.61B | 2 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 343 | -3 | 27,011 | 0.3% | 9.24B | 2 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 266 | +76 | 1,011 | 0.3% | — | 1 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 252 | -3 | 41,482 | 0.2% | 11.17B | 1 |
| 134 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 249 | -2 | 4,858 | 0.2% | 437.8M | 1 |
| 135 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 244 | -4 | 11,545 | 0.2% | 27.23B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 226 | -1 | 21,302 | 0.2% | 9.24B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 208 | +14 | 16,318 | 0.2% | 7.29B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 201 | +3 | 19,340 | 0.2% | 68.98B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 196 | +1 | 5,262 | 0.2% | 353.4M | 2 |
| 140 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 179 | 0 | 1,984 | 0.2% | — | 1 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 158 | +2 | 5,072 | 0.2% | 11.51B | 5 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 154 | -2 | 38,531 | 0.1% | 70.55B | 3 |
| 143 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 147 | +5 | 2,254 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 138 | 0 | 7,103 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | +6 | 4,795 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 121 | +5 | 28,189 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 113 | +1 | 1,227 | 0.1% | 560.9M | 1 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 103 | +33 | 955 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 82 | -1 | 177 | 0.1% | 437.8M | 1 |
| 150 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 151 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 42 | 0 | 329 | 0.0% | 321.0M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 42 | -4 | 250 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 25 | +1 | 138 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | +1 | 349 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 14 | -2 | 204 | 0.0% | 15.17B | 3 |
| 157 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | -3 | 151 | 0.0% | 8.16B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,447,675 | 296,134,676 | 30 | 2.9% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,048,820 | 1,421,415 | 11 | 68.9% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 747,699 | 4,733,116 | 7 | 15.5% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 309,544 | 2,124,337 | 11 | 13.9% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 274,291 | 6,279,948 | 12 | 4.3% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,699 | 1,343,166 | 5 | 2.8% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,709 | 425,263 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,966 | 535,505 | 13 | 2.2% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,201 | 186,382 | 6 | 3.2% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,544 | 351,951 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,542 | 189,786 | 3 | 2.6% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,884 | 849,747 | 3 | 0.7% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,517 | 365,651 | 10 | 1.4% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,964 | 691,759 | 2 | 0.5% |
| 15 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,594 | 23,212 | 4 | 2.9% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,466 | 131,599 | 1 | 1.5% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 3,327 | 148,432 | 2 | 1.3% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,951 | 485,113 | 3 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,175 | 655,382 | 2 | 0.3% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,099 | 151,958 | 2 | 0.8% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,973 | 1,158,297 | 4 | 0.2% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,831 | 101,925 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 980 | 7,125 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 378 | 75,852 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 179 | 1,984 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,570,029 | 56,552,629 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 491,614 | 4,004,845 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 352,528 | 415,601 | 8 |
| 4 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 230,760 | 426,904 | 14 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 226,739 | 4,136,017 | 15 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 33,496 | 669,814 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,688 | 106,557 | 40 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,340 | 110,789 | 43 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,705 | 64,094 | 45 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,671 | 45,664 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,209 | 667,518 | 49 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,965 | 90,353 | 50 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,466 | 131,599 | 55 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,455 | 369,994 | 56 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,334 | 64,435 | 61 |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,432 | 12,000 | 73 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,420 | 175,942 | 75 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,224 | 98,784 | 80 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,141 | 355,011 | 85 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,105 | 95,290 | 88 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,035 | 156,810 | 90 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 980 | 7,125 | 96 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 939 | 799,844 | 100 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 378 | 75,852 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 179 | 1,984 | 140 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 68.9% | 1,048,820 | 1,421,415 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 15.5% | 747,699 | 4,733,116 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 13.9% | 309,544 | 2,124,337 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.3% | 274,291 | 6,279,948 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,709 | 425,263 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,201 | 186,382 | 9 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.9% | 3,594 | 23,212 | 15 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.9% | 8,447,675 | 296,134,676 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.8% | 39,699 | 1,343,166 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.6% | 7,542 | 189,786 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 13,966 | 535,505 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,544 | 351,951 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,466 | 131,599 | 16 |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.4% | 6,517 | 365,651 | 13 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.3% | 3,327 | 148,432 | 17 |
| 16 | [domyn](https://huggingface.co/domyn) | 0.9% | 980 | 7,125 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,831 | 101,925 | 22 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,099 | 151,958 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,884 | 849,747 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,951 | 485,113 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,964 | 691,759 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,175 | 655,382 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 378 | 75,852 | 24 |
| 24 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 179 | 1,984 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,973 | 1,158,297 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
