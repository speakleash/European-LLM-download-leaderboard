# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-19
- **Generated at:** 2026-09-19T10:36:02Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,570,218 | +189 | 56,659,657 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,782,269 | +9,006 | 64,126,658 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 625,211 | +2,976 | 3,564,404 | 17.1% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 590,137 | +1,039 | 45,547,730 | 1.3% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 512,007 | -7,531 | 16,225,015 | 3.1% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 489,715 | -1,899 | 4,021,616 | 11.9% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 464,058 | +6,806 | 4,617,529 | 9.8% | 24.01B | 2 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 352,280 | -248 | 415,802 | 68.3% | 353.4M | 1 |
| 9 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 349,887 | -242 | 412,289 | 68.3% | 1.20B | 1 |
| 10 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 339,565 | -247 | 397,314 | 68.3% | 3.21B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 323,037 | -8,271 | 5,500,354 | 5.8% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 295,650 | -2,547 | 32,239,714 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 270,920 | +10,256 | 2,716,018 | 9.6% | 24.01B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 244,408 | +13,648 | 440,765 | 45.2% | 22.64B | 1 |
| 15 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 217,917 | -8,822 | 4,136,932 | 5.1% | 11.34B | 8 |
| 16 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 185,194 | +48,360 | 5,343,324 | 3.4% | 24.01B | 1 |
| 17 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 183,781 | -6,466 | 2,097,316 | 8.4% | 8.92B | 6 |
| 18 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 174,565 | -12,371 | 8,470,209 | 2.0% | 8.02B | 1 |
| 19 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 169,489 | +33,347 | 182,799 | 59.9% | 8.90B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,769 | -13 | 523,155 | 15.5% | 70.60B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 90,255 | -10,648 | 1,033,557 | 8.0% | 127.70B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,988 | +988 | 626,864 | 10.3% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,817 | -144 | 698,835 | 9.2% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 67,983 | -264 | 7,557,523 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,121 | -1,581 | 642,123 | 7.6% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 40,814 | +676 | 11,191,616 | 0.4% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 33,133 | -363 | 670,452 | 4.3% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 23,401 | -1,212 | 137,022 | 9.9% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,444 | +31 | 477,224 | 3.7% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,736 | -329 | 5,157,522 | 0.4% | 22.25B | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,126 | -53 | 24,101 | 13.8% | 72.01B | 1 |
| 32 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,152 | -8 | 323,804 | 3.8% | 24.01B | 2 |
| 33 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,874 | +15 | 772,125 | 1.8% | 11.25B | 10 |
| 34 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,329 | -459 | 347,508 | 3.4% | 125.03B | 1 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,404 | -30 | 68,158 | 8.0% | — | 5 |
| 36 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,238 | -189 | 696,955 | 1.7% | 1.66B | 1 |
| 37 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,209 | -446 | 5,299,992 | 0.2% | 7.25B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,417 | -140 | 206,538 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,596 | +86 | 503,792 | 1.6% | 7.24B | 8 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,576 | -112 | 106,646 | 3.2% | 8.42B | 5 |
| 41 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,503 | -158 | 4,922,001 | 0.1% | 122.61B | 1 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,971 | -39 | 128,509 | 2.6% | 7.48B | 5 |
| 43 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,199 | -141 | 110,802 | 2.5% | 7.29B | 2 |
| 44 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,198 | +493 | 64,848 | 3.2% | 11.77B | 4 |
| 45 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,076 | +25 | 162,487 | 1.9% | 11.17B | 16 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,789 | +118 | 45,813 | 3.3% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,372 | +4 | 28,634 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,187 | -53 | 141,950 | 1.7% | 2.25B | 7 |
| 49 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,963 | -2 | 90,452 | 2.1% | 2.89B | 1 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,919 | +53 | 902,647 | 0.4% | 23.57B | 2 |
| 51 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,766 | -443 | 667,668 | 0.5% | 7.45B | 2 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,631 | -14 | 54,227 | 2.4% | 7.55B | 1 |
| 53 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,528 | +73 | 370,145 | 0.8% | 7.24B | 8 |
| 54 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,504 | +33 | 5,375,457 | 0.1% | 22.25B | 1 |
| 55 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,456 | -10 | 131,804 | 1.5% | 7.40B | 3 |
| 56 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,339 | -131 | 250,889 | 1.0% | 4.76B | 5 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,097 | +3 | 30,942 | 2.4% | 14.03B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,046 | -89 | 56,332 | 1.9% | 1.60B | 5 |
| 59 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,466 | +132 | 64,567 | 1.5% | 14.08B | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,383 | +94 | 146,635 | 1.0% | 7.24B | 4 |
| 61 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,352 | +46 | 5,031,024 | 0.0% | 122.61B | 1 |
| 62 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,169 | +65 | 33,904 | 1.6% | 2.61B | 3 |
| 63 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,161 | -182 | 38,897 | 1.6% | 321.0M | 2 |
| 64 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,998 | +2 | 14,186 | 1.7% | 3.83B | 5 |
| 65 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,691 | +23 | 48,419 | 1.1% | 9.24B | 4 |
| 66 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,686 | -759 | 11,335 | 1.5% | 572.6M | 5 |
| 67 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,662 | +40 | 31,953 | 1.3% | 22.64B | 1 |
| 68 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,586 | -170 | 9,119 | 1.5% | 9.15B | 1 |
| 69 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,575 | +227 | 150,689 | 0.6% | 23.57B | 2 |
| 70 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,559 | +30 | 22,450 | 1.3% | 22.64B | 1 |
| 71 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,521 | -20 | 6,904 | 1.4% | 1.51B | 6 |
| 72 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,515 | +19 | 77,359 | 0.9% | 7.45B | 1 |
| 73 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,440 | +20 | 175,989 | 0.5% | 12.25B | 6 |
| 74 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,428 | -4 | 12,000 | 1.3% | 31.59B | 6 |
| 75 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,382 | -251 | 19,561 | 1.2% | 4.30B | 2 |
| 76 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,378 | -51 | 21,790 | 1.1% | 11.17B | 5 |
| 77 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,343 | -22 | 172,740 | 0.5% | 11.51B | 7 |
| 78 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,274 | -39 | 29,972 | 1.0% | 11.17B | 5 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,259 | +35 | 98,838 | 0.6% | 30.68B | 1 |
| 80 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,214 | +35 | 104,993 | 0.6% | 7.45B | 1 |
| 81 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,210 | -162 | 19,171 | 1.0% | 12.25B | 3 |
| 82 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,172 | -3 | 2,810 | 1.1% | 31.59B | 6 |
| 83 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,166 | +25 | 355,059 | 0.3% | — | 3 |
| 84 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,153 | -38 | 32,104 | 0.9% | 56.7M | 1 |
| 85 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,152 | -71 | 7,698 | 1.1% | 28.84B | 3 |
| 86 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,132 | +4 | 16,596 | 1.0% | 12.19B | 2 |
| 87 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,089 | -16 | 95,298 | 0.6% | 1.35B | 8 |
| 88 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,070 | +35 | 156,870 | 0.4% | 1.10B | 1 |
| 89 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,054 | +20 | 300,415 | 0.3% | 6.74B | 2 |
| 90 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,049 | +2 | 81,018 | 0.6% | 8.03B | 3 |
| 91 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,031 | +92 | 799,974 | 0.1% | — | 3 |
| 92 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,006 | +13 | 84,096 | 0.5% | 2.22B | 1 |
| 93 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,004 | -5 | 38,417 | 0.7% | 70.55B | 3 |
| 94 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,003 | +44 | 8,176 | 0.9% | 27.43B | 3 |
| 95 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 992 | +12 | 7,142 | 0.9% | 9.82B | 1 |
| 96 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 991 | -142 | 7,038 | 0.9% | 4.30B | 3 |
| 97 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 989 | +27 | 144,596 | 0.4% | 13.02B | 1 |
| 98 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 981 | +27 | 183,798 | 0.3% | 6.74B | 1 |
| 99 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 980 | -1 | 217,662 | 0.3% | 12.19B | 3 |
| 100 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 971 | -23 | 56,693 | 0.6% | 1.35B | 3 |
| 101 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 944 | +22 | 227,471 | 0.3% | 35.13B | 4 |
| 102 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 859 | -1 | 37,355 | 0.6% | 27.23B | 3 |
| 103 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 858 | +43 | 1,163 | 0.8% | 27.23B | 3 |
| 104 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 831 | -10 | 12,380 | 0.7% | 70.55B | 2 |
| 105 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 830 | -17 | 48,298 | 0.6% | 7.77B | 1 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 782 | +18 | 18,214 | 0.7% | 1.20B | 2 |
| 107 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 704 | +9 | 19,843 | 0.6% | 3.20B | 2 |
| 108 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 700 | -11 | 70,117 | 0.4% | 8.03B | 3 |
| 109 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 694 | +15 | 43,800 | 0.5% | 12.19B | 2 |
| 110 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 661 | +31 | 13,843 | 0.6% | 353.4M | 2 |
| 111 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 640 | -1 | 13,603 | 0.6% | 4.33B | 3 |
| 112 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 618 | +2 | 81,937 | 0.3% | 9.15B | 1 |
| 113 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 583 | -10 | 450,973 | 0.1% | 40.43B | 1 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 581 | +133 | 232,480 | 0.2% | — | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 574 | -6 | 2,791 | 0.6% | 30.68B | 1 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 557 | +34 | 32,331 | 0.4% | 40.43B | 2 |
| 117 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 553 | +44 | 321,817 | 0.1% | 7.24B | 2 |
| 118 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 526 | +41 | 52,002 | 0.3% | 7.24B | 5 |
| 119 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 510 | 0 | 1,273 | 0.5% | 31.58B | 2 |
| 120 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 498 | +21 | 7,190 | 0.5% | 31.59B | 6 |
| 121 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 475 | -73 | 3,488 | 0.5% | 8.03B | 3 |
| 122 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 473 | -5 | 2,795 | 0.5% | 560.9M | 2 |
| 123 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 454 | +45 | 50,896 | 0.3% | 7.24B | 1 |
| 124 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 447 | -3 | 44,313 | 0.3% | 7.70B | 5 |
| 125 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 437 | -21 | 15,619 | 0.4% | 1.54B | 4 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 407 | +3 | 38,924 | 0.3% | 7.48B | 2 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 388 | +3 | 106,786 | 0.2% | — | 3 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 386 | +8 | 75,865 | 0.2% | 7.04B | 4 |
| 129 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 371 | -2 | 2,396 | 0.4% | 4.02B | 2 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 362 | +1 | 21,622 | 0.3% | 2.61B | 2 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 342 | -1 | 27,012 | 0.3% | 9.24B | 2 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 284 | +18 | 1,033 | 0.3% | — | 1 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 250 | -2 | 41,484 | 0.2% | 11.17B | 1 |
| 134 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 245 | -4 | 4,859 | 0.2% | 437.8M | 1 |
| 135 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 244 | 0 | 11,546 | 0.2% | 27.23B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 227 | +1 | 21,305 | 0.2% | 9.24B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 210 | +2 | 16,320 | 0.2% | 7.29B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 198 | +2 | 5,267 | 0.2% | 353.4M | 2 |
| 139 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 194 | -7 | 19,341 | 0.2% | 68.98B | 2 |
| 140 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | +9 | 38,541 | 0.1% | 70.55B | 3 |
| 141 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 163 | -16 | 1,986 | 0.2% | — | 1 |
| 142 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 158 | 0 | 5,079 | 0.2% | 11.51B | 5 |
| 143 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 148 | +1 | 2,258 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 140 | +2 | 7,108 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | -1 | 4,795 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 119 | -2 | 28,189 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 110 | -3 | 1,228 | 0.1% | 560.9M | 1 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105 | +2 | 958 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 82 | 0 | 177 | 0.1% | 437.8M | 1 |
| 150 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 151 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 42 | 0 | 329 | 0.0% | 321.0M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 42 | 0 | 250 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 25 | 0 | 138 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 349 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 14 | 0 | 204 | 0.0% | 15.17B | 3 |
| 157 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | 0 | 151 | 0.0% | 8.16B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,477,097 | 296,439,239 | 30 | 2.9% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,047,918 | 1,422,185 | 11 | 68.8% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 778,304 | 4,784,096 | 7 | 15.9% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 321,650 | 2,140,125 | 11 | 14.4% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 265,222 | 6,282,131 | 12 | 4.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,290 | 1,344,004 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,837 | 425,504 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,567 | 535,703 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,747 | 187,247 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,708 | 352,291 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,430 | 189,883 | 3 | 2.6% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,495 | 850,020 | 3 | 0.7% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,145 | 365,743 | 10 | 1.3% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,081 | 691,962 | 2 | 0.5% |
| 15 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,608 | 23,273 | 4 | 2.9% |
| 16 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 3,472 | 148,663 | 2 | 1.4% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,456 | 131,804 | 1 | 1.5% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,040 | 485,264 | 3 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,220 | 655,474 | 2 | 0.3% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,194 | 1,158,581 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,060 | 151,991 | 2 | 0.8% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,860 | 101,984 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 992 | 7,142 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 386 | 75,865 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 163 | 1,986 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,570,218 | 56,659,657 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 489,715 | 4,021,616 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 352,280 | 415,802 | 8 |
| 4 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 244,408 | 440,765 | 14 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 217,917 | 4,136,932 | 15 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 33,133 | 670,452 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,576 | 106,646 | 40 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,199 | 110,802 | 43 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,198 | 64,848 | 44 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,789 | 45,813 | 46 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,963 | 90,452 | 49 |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,766 | 667,668 | 51 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,528 | 370,145 | 53 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,456 | 131,804 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,466 | 64,567 | 59 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,440 | 175,989 | 73 |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,428 | 12,000 | 74 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,259 | 98,838 | 79 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,166 | 355,059 | 83 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,089 | 95,298 | 87 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,070 | 156,870 | 88 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,031 | 799,974 | 91 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 992 | 7,142 | 95 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 386 | 75,865 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 163 | 1,986 | 141 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 68.8% | 1,047,918 | 1,422,185 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 15.9% | 778,304 | 4,784,096 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 14.4% | 321,650 | 2,140,125 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.2% | 265,222 | 6,282,131 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,837 | 425,504 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,747 | 187,247 | 9 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.9% | 3,608 | 23,273 | 15 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.9% | 8,477,097 | 296,439,239 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,290 | 1,344,004 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.6% | 7,430 | 189,883 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,567 | 535,703 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,708 | 352,291 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,456 | 131,804 | 17 |
| 14 | [Almawave](https://huggingface.co/Almawave) | 1.4% | 3,472 | 148,663 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 6,145 | 365,743 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 0.9% | 992 | 7,142 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,860 | 101,984 | 22 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,060 | 151,991 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,495 | 850,020 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 3,040 | 485,264 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,081 | 691,962 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,220 | 655,474 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 386 | 75,865 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,194 | 1,158,581 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 163 | 1,986 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
