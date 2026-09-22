# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-22
- **Generated at:** 2026-09-22T11:15:47Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,529,471 | +1,840 | 56,902,530 | 4.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,769,441 | +665 | 64,238,579 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 637,407 | +11,553 | 3,601,397 | 17.2% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 606,896 | +777 | 45,603,131 | 1.3% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 486,456 | +4,155 | 4,067,212 | 11.7% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 485,595 | -4,104 | 16,250,641 | 3.0% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 475,406 | +9,260 | 4,638,773 | 10.0% | 24.01B | 2 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303,169 | +1,739 | 5,521,893 | 5.4% | 4.25B | 7 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 300,782 | +92 | 415,974 | 58.3% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 299,465 | +104 | 412,470 | 58.4% | 1.20B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 296,053 | +1,224 | 32,271,013 | 0.9% | 46.70B | 2 |
| 12 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 291,527 | +100 | 397,480 | 58.6% | 3.21B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 289,153 | +11,785 | 2,755,360 | 10.1% | 24.01B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 283,813 | +13,543 | 480,929 | 48.9% | 22.64B | 1 |
| 15 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 266,769 | +33,722 | 281,063 | 70.0% | 8.90B | 1 |
| 16 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 195,552 | +7,126 | 5,366,183 | 3.6% | 24.01B | 1 |
| 17 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 195,458 | -7,450 | 4,138,592 | 4.6% | 11.34B | 8 |
| 18 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 174,895 | +7,532 | 2,117,267 | 7.9% | 8.92B | 6 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,374 | -4,076 | 8,480,916 | 1.8% | 8.02B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,903 | +306 | 525,359 | 15.5% | 70.60B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 89,467 | +448 | 1,034,997 | 7.9% | 127.70B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,078 | -15 | 628,071 | 10.3% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,977 | -73 | 705,894 | 9.1% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,706 | +172 | 7,562,440 | 0.9% | 23.57B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 58,330 | +45,501 | 743,706 | 6.9% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 54,962 | -222 | 645,514 | 7.4% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 42,396 | +1,131 | 11,195,127 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,947 | +842 | 672,617 | 4.3% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,522 | +561 | 138,956 | 10.3% | 9.15B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 22,090 | +147 | 478,613 | 3.8% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,495 | +44 | 5,157,843 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,435 | +37 | 24,490 | 14.0% | 72.01B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,220 | +230 | 324,259 | 3.8% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,910 | +73 | 773,376 | 1.8% | 11.25B | 10 |
| 35 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,320 | -97 | 347,827 | 3.2% | 125.03B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,531 | +401 | 69,135 | 8.0% | — | 5 |
| 37 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,247 | +42 | 5,300,121 | 0.2% | 7.25B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,355 | +45 | 206,962 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,318 | +300 | 504,930 | 1.7% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,594 | +462 | 130,428 | 3.3% | 7.48B | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,859 | +153 | 107,309 | 3.3% | 8.42B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,325 | +84 | 4,922,689 | 0.1% | 122.61B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,109 | +20 | 162,919 | 1.9% | 11.17B | 16 |
| 44 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,055 | -24 | 110,880 | 2.4% | 7.29B | 2 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,016 | -172 | 65,239 | 3.0% | 11.77B | 4 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,844 | +321 | 46,465 | 3.3% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,411 | +29 | 28,706 | 3.4% | 33.12B | 1 |
| 48 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,198 | +217 | 903,123 | 0.4% | 23.57B | 2 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,108 | +188 | 668,305 | 0.5% | 7.45B | 2 |
| 50 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,034 | -131 | 142,563 | 1.7% | 2.25B | 7 |
| 51 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,846 | +163 | 5,375,925 | 0.1% | 22.25B | 1 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,798 | +135 | 370,677 | 0.8% | 7.24B | 8 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,706 | -8 | 251,552 | 1.1% | 4.76B | 5 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,700 | +104 | 132,194 | 1.6% | 7.40B | 3 |
| 55 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,547 | +13 | 54,290 | 2.3% | 7.55B | 1 |
| 56 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,473 | -42 | 90,756 | 1.8% | 2.89B | 1 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,133 | +19 | 31,011 | 2.4% | 14.03B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,806 | +39 | 56,740 | 1.8% | 1.60B | 5 |
| 59 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,767 | +36 | 65,071 | 1.7% | 14.08B | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,651 | +103 | 147,064 | 1.1% | 7.24B | 4 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,571 | +115 | 34,525 | 1.9% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,438 | +24 | 5,031,328 | 0.0% | 122.61B | 1 |
| 63 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,065 | +77 | 151,304 | 0.8% | 23.57B | 2 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,056 | -14 | 39,069 | 1.5% | 321.0M | 2 |
| 65 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,002 | +99 | 14,381 | 1.8% | 3.83B | 5 |
| 66 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,813 | +45 | 48,578 | 1.2% | 9.24B | 4 |
| 67 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,784 | +50 | 32,107 | 1.4% | 22.64B | 1 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,731 | +244 | 7,278 | 1.6% | 1.51B | 6 |
| 69 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,676 | +41 | 22,635 | 1.4% | 22.64B | 1 |
| 70 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,670 | +66 | 77,562 | 0.9% | 7.45B | 1 |
| 71 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,532 | -4 | 9,183 | 1.4% | 9.15B | 1 |
| 72 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,529 | -27 | 11,430 | 1.4% | 572.6M | 5 |
| 73 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,485 | +43 | 22,026 | 1.2% | 11.17B | 5 |
| 74 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,433 | +6 | 12,006 | 1.3% | 31.59B | 6 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,400 | +60 | 105,218 | 0.7% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,397 | +65 | 99,049 | 0.7% | 30.68B | 1 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,376 | +31 | 176,134 | 0.5% | 12.25B | 6 |
| 78 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,360 | +35 | 172,885 | 0.5% | 11.51B | 7 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,314 | +49 | 355,237 | 0.3% | — | 3 |
| 80 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,282 | +19 | 30,102 | 1.0% | 11.17B | 5 |
| 81 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,261 | +5 | 19,601 | 1.1% | 4.30B | 2 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,240 | +74 | 157,052 | 0.5% | 1.10B | 1 |
| 83 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,240 | +87 | 84,393 | 0.7% | 2.22B | 1 |
| 84 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,213 | +33 | 19,293 | 1.0% | 12.25B | 3 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,178 | +46 | 300,563 | 0.3% | 6.74B | 2 |
| 86 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,163 | -4 | 7,820 | 1.1% | 28.84B | 3 |
| 87 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,154 | 0 | 2,810 | 1.1% | 31.59B | 6 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,117 | +49 | 144,738 | 0.5% | 13.02B | 1 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,114 | +50 | 183,944 | 0.4% | 6.74B | 1 |
| 90 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,098 | +25 | 16,735 | 0.9% | 12.19B | 2 |
| 91 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,073 | +13 | 95,401 | 0.5% | 1.35B | 8 |
| 92 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,032 | -7 | 32,170 | 0.8% | 56.7M | 1 |
| 93 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,020 | +5 | 81,077 | 0.6% | 8.03B | 3 |
| 94 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,020 | +9 | 7,146 | 1.0% | 4.30B | 3 |
| 95 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,015 | +30 | 7,204 | 0.9% | 9.82B | 1 |
| 96 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 992 | +15 | 38,470 | 0.7% | 70.55B | 3 |
| 97 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 989 | -19 | 8,264 | 0.9% | 27.43B | 3 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 985 | -27 | 800,058 | 0.1% | — | 3 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 980 | -4 | 56,795 | 0.6% | 1.35B | 3 |
| 100 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 961 | +24 | 227,562 | 0.3% | 35.13B | 4 |
| 101 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 889 | +4 | 37,401 | 0.6% | 27.23B | 3 |
| 102 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 807 | +30 | 48,373 | 0.5% | 7.77B | 1 |
| 103 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 787 | +2 | 1,176 | 0.8% | 27.23B | 3 |
| 104 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 749 | +2 | 19,892 | 0.6% | 3.20B | 2 |
| 105 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 706 | -7 | 70,152 | 0.4% | 8.03B | 3 |
| 106 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 703 | -108 | 12,396 | 0.6% | 70.55B | 2 |
| 107 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 700 | -7 | 217,714 | 0.2% | 12.19B | 3 |
| 108 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 676 | +6 | 13,897 | 0.6% | 353.4M | 2 |
| 109 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 670 | +52 | 52,153 | 0.4% | 7.24B | 5 |
| 110 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 657 | +8 | 82,005 | 0.4% | 9.15B | 1 |
| 111 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 634 | -164 | 18,282 | 0.5% | 1.20B | 2 |
| 112 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 622 | +1 | 13,639 | 0.5% | 4.33B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 597 | +2 | 232,503 | 0.2% | — | 2 |
| 114 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 590 | +20 | 451,033 | 0.1% | 40.43B | 1 |
| 115 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 580 | +41 | 51,034 | 0.4% | 7.24B | 1 |
| 116 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 561 | +7 | 2,816 | 0.5% | 30.68B | 1 |
| 117 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 557 | -7 | 43,814 | 0.4% | 12.19B | 2 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 526 | -15 | 321,846 | 0.1% | 7.24B | 2 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 514 | -12 | 32,353 | 0.4% | 40.43B | 2 |
| 120 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 512 | +2 | 1,275 | 0.5% | 31.58B | 2 |
| 121 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 479 | -8 | 3,536 | 0.5% | 8.03B | 3 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 476 | +18 | 39,017 | 0.3% | 7.48B | 2 |
| 123 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 454 | -8 | 2,805 | 0.4% | 560.9M | 2 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 446 | -6 | 27,146 | 0.4% | 9.24B | 2 |
| 125 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 412 | -25 | 44,336 | 0.3% | 7.70B | 5 |
| 126 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 407 | 0 | 7,190 | 0.4% | 31.59B | 6 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 401 | 0 | 106,818 | 0.2% | — | 3 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 382 | +7 | 75,910 | 0.2% | 7.04B | 4 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 374 | +3 | 21,641 | 0.3% | 2.61B | 2 |
| 130 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 369 | +1 | 15,642 | 0.3% | 1.54B | 4 |
| 131 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 341 | -13 | 2,401 | 0.3% | 4.02B | 2 |
| 132 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 324 | +1 | 11,631 | 0.3% | 27.23B | 2 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 294 | +8 | 1,056 | 0.3% | — | 1 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 266 | +10 | 41,515 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 237 | +6 | 16,354 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 236 | +1 | 21,327 | 0.2% | 9.24B | 2 |
| 137 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 225 | -8 | 4,861 | 0.2% | 437.8M | 1 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 206 | -3 | 19,366 | 0.2% | 68.98B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 202 | +2 | 5,279 | 0.2% | 353.4M | 2 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 170 | +1 | 5,101 | 0.2% | 11.51B | 5 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 170 | +6 | 2,286 | 0.2% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 161 | -1 | 38,545 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 143 | +4 | 7,120 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 130 | +1 | 4,801 | 0.1% | 70.55B | 3 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 130 | +7 | 28,205 | 0.1% | 46.70B | 6 |
| 146 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 119 | -14 | 1,988 | 0.1% | — | 1 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 106 | -1 | 1,229 | 0.1% | 560.9M | 1 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 103 | +3 | 963 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 82 | 0 | 179 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 43 | +4 | 334 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 41 | 0 | 251 | 0.0% | 437.8M | 1 |
| 152 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 33 | -22 | 6,035 | 0.0% | 12.25B | 3 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 139 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | +1 | 350 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | 0 | 207 | 0.0% | 15.17B | 3 |
| 157 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 12 | 0 | 153 | 0.0% | 8.16B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,415,080 | 297,105,299 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 897,580 | 1,423,152 | 11 | 58.9% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 872,825 | 4,931,213 | 7 | 17.3% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 408,500 | 2,231,907 | 11 | 17.5% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 245,464 | 6,290,166 | 12 | 3.8% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,892 | 1,346,939 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,888 | 426,504 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,062 | 536,566 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,623 | 187,928 | 6 | 3.3% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,683 | 353,336 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,747 | 190,662 | 3 | 2.7% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,178 | 851,085 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,951 | 366,243 | 10 | 1.3% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,324 | 692,523 | 2 | 0.5% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,007 | 149,464 | 2 | 1.6% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,700 | 132,194 | 1 | 1.6% |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,506 | 23,281 | 4 | 2.8% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,471 | 485,734 | 3 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,492 | 655,800 | 2 | 0.3% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,189 | 1,158,745 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,053 | 152,196 | 2 | 0.8% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,983 | 102,225 | 4 | 1.0% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,015 | 7,204 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 382 | 75,910 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 119 | 1,988 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,529,471 | 56,902,530 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 486,456 | 4,067,212 | 5 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 300,782 | 415,974 | 9 |
| 4 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 283,813 | 480,929 | 14 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 195,458 | 4,138,592 | 17 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,947 | 672,617 | 28 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,859 | 107,309 | 41 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,055 | 110,880 | 44 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,016 | 65,239 | 45 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,844 | 46,465 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,108 | 668,305 | 49 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,798 | 370,677 | 52 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,700 | 132,194 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,473 | 90,756 | 56 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,767 | 65,071 | 59 |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,433 | 12,006 | 74 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,397 | 99,049 | 76 |
| 18 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,376 | 176,134 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,314 | 355,237 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,240 | 157,052 | 82 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,073 | 95,401 | 91 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,015 | 7,204 | 95 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 985 | 800,058 | 98 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 382 | 75,910 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 119 | 1,988 | 146 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 58.9% | 897,580 | 1,423,152 | 2 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 17.5% | 408,500 | 2,231,907 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 17.3% | 872,825 | 4,931,213 | 3 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.8% | 245,464 | 6,290,166 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,888 | 426,504 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.3% | 9,623 | 187,928 | 9 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,506 | 23,281 | 17 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,415,080 | 297,105,299 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 38,892 | 1,346,939 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 7,747 | 190,662 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,062 | 536,566 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,683 | 353,336 | 10 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.6% | 4,007 | 149,464 | 15 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,700 | 132,194 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,951 | 366,243 | 13 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.0% | 1,983 | 102,225 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 0.9% | 1,015 | 7,204 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,053 | 152,196 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,178 | 851,085 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.6% | 3,471 | 485,734 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,324 | 692,523 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,492 | 655,800 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 382 | 75,910 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,189 | 1,158,745 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 119 | 1,988 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
