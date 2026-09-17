# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-17
- **Generated at:** 2026-09-17T11:19:04Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,591,576 | +1,114 | 56,461,089 | 4.6% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,745,229 | +29,327 | 64,023,321 | 2.7% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 621,152 | -2,911 | 3,545,214 | 17.0% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 570,777 | +3,281 | 45,503,502 | 1.3% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 529,216 | -8,389 | 16,205,871 | 3.2% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 492,692 | -2,073 | 3,987,564 | 12.1% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 449,392 | +6,550 | 4,594,297 | 9.6% | 24.01B | 2 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 352,491 | -935 | 415,500 | 68.4% | 353.4M | 1 |
| 9 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 350,086 | -934 | 411,985 | 68.4% | 1.20B | 1 |
| 10 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 339,763 | -928 | 397,018 | 68.4% | 3.21B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 336,991 | -14,850 | 5,484,392 | 6.0% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 299,864 | -5,975 | 32,220,592 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 252,483 | -510 | 2,681,795 | 9.1% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 235,006 | -2,526 | 4,135,256 | 5.5% | 11.34B | 8 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 217,196 | +12,252 | 413,203 | 42.3% | 22.64B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 198,349 | -6,941 | 2,087,093 | 9.1% | 8.92B | 6 |
| 17 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190,480 | -3,684 | 8,450,084 | 2.2% | 8.02B | 1 |
| 18 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 136,603 | -768 | 5,284,082 | 2.5% | 24.01B | 1 |
| 19 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 116,354 | -9,074 | 1,032,849 | 10.3% | 127.70B | 2 |
| 20 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 102,883 | +29,865 | 115,680 | 47.7% | 8.90B | 1 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,956 | -106 | 521,788 | 15.6% | 70.60B | 2 |
| 22 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,329 | -733 | 693,813 | 9.4% | 23.57B | 2 |
| 23 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,177 | +1,069 | 623,642 | 10.0% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,217 | +98 | 7,553,948 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,983 | -192 | 639,408 | 7.8% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 39,658 | +799 | 11,188,693 | 0.4% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 33,394 | +523 | 668,469 | 4.3% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 26,278 | -2,949 | 135,328 | 11.2% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,046 | +563 | 476,101 | 3.7% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,180 | +7,262 | 5,157,341 | 0.4% | 22.25B | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,570 | +87 | 23,968 | 14.2% | 72.01B | 1 |
| 32 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,374 | -276 | 347,186 | 3.7% | 125.03B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,192 | +340 | 323,591 | 3.8% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,848 | +48 | 771,252 | 1.8% | 11.25B | 10 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,136 | +36 | 5,299,939 | 0.3% | 7.25B | 1 |
| 36 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,005 | -336 | 696,153 | 1.8% | 1.66B | 1 |
| 37 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,223 | +209 | 67,070 | 7.9% | — | 5 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,441 | +334 | 206,044 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,513 | +6 | 503,119 | 1.6% | 7.24B | 8 |
| 40 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,940 | +40 | 4,921,563 | 0.1% | 122.61B | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,651 | +99 | 106,401 | 3.2% | 8.42B | 5 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,962 | +14 | 128,338 | 2.6% | 7.48B | 5 |
| 43 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,386 | +3,145 | 110,766 | 2.6% | 7.29B | 2 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,092 | +30 | 162,227 | 1.9% | 11.17B | 16 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,683 | +22 | 63,963 | 2.9% | 11.77B | 4 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,545 | +51 | 45,501 | 3.1% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,366 | +9 | 28,604 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,250 | -38 | 141,756 | 1.8% | 2.25B | 7 |
| 49 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,180 | -29 | 90,259 | 2.2% | 2.89B | 1 |
| 50 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,137 | +27 | 667,341 | 0.5% | 7.45B | 2 |
| 51 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,849 | -67 | 902,398 | 0.4% | 23.57B | 2 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,648 | +39 | 54,202 | 2.4% | 7.55B | 1 |
| 53 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,602 | -81 | 131,459 | 1.6% | 7.40B | 3 |
| 54 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,509 | -3 | 250,814 | 1.0% | 4.76B | 5 |
| 55 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,425 | +4 | 5,375,157 | 0.1% | 22.25B | 1 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,377 | -133 | 56,217 | 2.2% | 1.60B | 5 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,341 | -1 | 369,794 | 0.7% | 7.24B | 8 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,309 | -126 | 30,921 | 2.5% | 14.03B | 1 |
| 59 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,459 | -491 | 11,264 | 2.2% | 572.6M | 5 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,449 | -28 | 38,819 | 1.8% | 321.0M | 2 |
| 61 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,416 | -39 | 5,030,818 | 0.0% | 122.61B | 1 |
| 62 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,225 | -23 | 146,352 | 0.9% | 7.24B | 4 |
| 63 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,101 | +75 | 64,182 | 1.3% | 14.08B | 1 |
| 64 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,087 | -58 | 33,729 | 1.6% | 2.61B | 3 |
| 65 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,066 | +17 | 14,128 | 1.8% | 3.83B | 5 |
| 66 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,847 | -499 | 19,539 | 1.5% | 4.30B | 2 |
| 67 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,840 | +12 | 9,076 | 1.7% | 9.15B | 1 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,669 | +366 | 48,323 | 1.1% | 9.24B | 4 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,624 | -26 | 31,841 | 1.2% | 22.64B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,548 | -534 | 16,561 | 1.3% | 12.19B | 2 |
| 71 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,529 | -15 | 22,346 | 1.2% | 22.64B | 1 |
| 72 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,525 | -42 | 6,807 | 1.4% | 1.51B | 6 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,487 | -13 | 77,229 | 0.8% | 7.45B | 1 |
| 74 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,429 | -2 | 11,995 | 1.3% | 31.59B | 6 |
| 75 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,417 | -78 | 19,110 | 1.2% | 12.25B | 3 |
| 76 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,416 | +2 | 175,890 | 0.5% | 12.25B | 6 |
| 77 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,409 | +13 | 21,717 | 1.2% | 11.17B | 5 |
| 78 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,399 | +15 | 172,647 | 0.5% | 11.51B | 7 |
| 79 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,297 | +10 | 29,913 | 1.0% | 11.17B | 5 |
| 80 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,291 | -286 | 7,566 | 1.2% | 28.84B | 3 |
| 81 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,276 | -116 | 7,007 | 1.2% | 4.30B | 3 |
| 82 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,225 | -1 | 98,732 | 0.6% | 30.68B | 1 |
| 83 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,211 | 0 | 2,804 | 1.2% | 31.59B | 6 |
| 84 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,194 | -12 | 104,882 | 0.6% | 7.45B | 1 |
| 85 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,180 | +5 | 32,046 | 0.9% | 56.7M | 1 |
| 86 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,141 | -4 | 354,955 | 0.3% | — | 3 |
| 87 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,098 | -3 | 95,268 | 0.6% | 1.35B | 8 |
| 88 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,046 | -2 | 80,983 | 0.6% | 8.03B | 3 |
| 89 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,037 | -6 | 300,322 | 0.3% | 6.74B | 2 |
| 90 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,029 | +152 | 150,113 | 0.4% | 23.57B | 2 |
| 91 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,029 | -10 | 156,753 | 0.4% | 1.10B | 1 |
| 92 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,005 | +7 | 38,380 | 0.7% | 70.55B | 3 |
| 93 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 993 | -13 | 56,653 | 0.6% | 1.35B | 3 |
| 94 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 971 | -8 | 217,606 | 0.3% | 12.19B | 3 |
| 95 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 965 | -6 | 144,504 | 0.4% | 13.02B | 1 |
| 96 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 961 | +9 | 799,814 | 0.1% | — | 3 |
| 97 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 959 | +15 | 7,089 | 0.9% | 9.82B | 1 |
| 98 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 955 | -27 | 12,359 | 0.9% | 70.55B | 2 |
| 99 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 955 | -5 | 183,703 | 0.3% | 6.74B | 1 |
| 100 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 927 | -4 | 83,901 | 0.5% | 2.22B | 1 |
| 101 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 908 | +13 | 227,382 | 0.3% | 35.13B | 4 |
| 102 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 904 | -19 | 48,275 | 0.6% | 7.77B | 1 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 889 | -404 | 43,774 | 0.6% | 12.19B | 2 |
| 104 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 856 | -104 | 37,345 | 0.6% | 27.23B | 3 |
| 105 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 829 | -106 | 7,962 | 0.8% | 27.43B | 3 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 784 | 0 | 1,089 | 0.8% | 27.23B | 3 |
| 107 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 752 | -5 | 18,168 | 0.6% | 1.20B | 2 |
| 108 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 713 | -34 | 70,103 | 0.4% | 8.03B | 3 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 693 | +114 | 19,828 | 0.6% | 3.20B | 2 |
| 110 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 678 | +2 | 13,790 | 0.6% | 353.4M | 2 |
| 111 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 646 | -3 | 13,585 | 0.6% | 4.33B | 3 |
| 112 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 638 | -15 | 81,928 | 0.4% | 9.15B | 1 |
| 113 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 589 | -19 | 450,951 | 0.1% | 40.43B | 1 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 580 | 0 | 2,781 | 0.6% | 30.68B | 1 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 550 | +4 | 3,470 | 0.5% | 8.03B | 3 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 516 | -2 | 32,263 | 0.4% | 40.43B | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 512 | 0 | 1,273 | 0.5% | 31.58B | 2 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 484 | +12 | 321,732 | 0.1% | 7.24B | 2 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 464 | +1 | 2,777 | 0.5% | 560.9M | 2 |
| 120 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 453 | +17 | 7,085 | 0.4% | 31.59B | 6 |
| 121 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 450 | +21 | 44,303 | 0.3% | 7.70B | 5 |
| 122 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 448 | +42 | 15,603 | 0.4% | 1.54B | 4 |
| 123 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 448 | -10 | 51,909 | 0.3% | 7.24B | 5 |
| 124 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 421 | -2 | 232,304 | 0.1% | — | 2 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 402 | +13 | 38,912 | 0.3% | 7.48B | 2 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 400 | -13 | 106,770 | 0.2% | — | 3 |
| 127 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 379 | -9 | 50,808 | 0.3% | 7.24B | 1 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 370 | -14 | 75,836 | 0.2% | 7.04B | 4 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 364 | +3 | 21,617 | 0.3% | 2.61B | 2 |
| 130 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 355 | 0 | 2,373 | 0.3% | 4.02B | 2 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 346 | -3 | 27,010 | 0.3% | 9.24B | 2 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 255 | -11 | 41,481 | 0.2% | 11.17B | 1 |
| 133 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 251 | -17 | 4,856 | 0.2% | 437.8M | 1 |
| 134 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 248 | -3 | 11,542 | 0.2% | 27.23B | 2 |
| 135 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 227 | +10 | 21,298 | 0.2% | 9.24B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 198 | +8 | 19,335 | 0.2% | 68.98B | 2 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 195 | -3 | 5,256 | 0.2% | 353.4M | 2 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 194 | -19 | 16,302 | 0.2% | 7.29B | 2 |
| 139 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190 | -4 | 925 | 0.2% | — | 1 |
| 140 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 179 | +44 | 1,984 | 0.2% | — | 1 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 156 | +3 | 5,068 | 0.1% | 11.51B | 5 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 156 | +2 | 38,526 | 0.1% | 70.55B | 3 |
| 143 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 142 | +3 | 2,247 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 138 | -4 | 7,100 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 131 | +3 | 4,788 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 116 | +2 | 28,183 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 112 | -1 | 1,225 | 0.1% | 560.9M | 1 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 83 | 0 | 177 | 0.1% | 437.8M | 1 |
| 149 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70 | +2 | 920 | 0.1% | — | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | 0 | 250 | 0.0% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 42 | -2 | 328 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | 0 | 136 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 348 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 16 | -1 | 204 | 0.0% | 15.17B | 3 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 16 | -2 | 151 | 0.0% | 8.16B | 3 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,448,854 | 295,850,706 | 30 | 2.9% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,048,820 | 1,420,993 | 11 | 69.0% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 716,151 | 4,681,199 | 7 | 15.0% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 297,826 | 2,107,996 | 11 | 13.5% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 282,823 | 6,278,049 | 12 | 4.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,653 | 1,341,714 | 5 | 2.8% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,781 | 424,990 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 14,786 | 535,128 | 13 | 2.3% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,133 | 186,151 | 6 | 3.2% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,600 | 351,584 | 14 | 1.9% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,503 | 189,616 | 3 | 2.6% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,818 | 849,452 | 3 | 0.7% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,810 | 365,471 | 10 | 1.5% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,825 | 691,526 | 2 | 0.5% |
| 15 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,605 | 23,157 | 4 | 2.9% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,602 | 131,459 | 1 | 1.6% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 3,028 | 148,083 | 2 | 1.2% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,949 | 484,960 | 3 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,178 | 655,277 | 2 | 0.3% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,091 | 151,921 | 2 | 0.8% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,980 | 1,158,223 | 4 | 0.2% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,837 | 101,868 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 959 | 7,089 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 370 | 75,836 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 179 | 1,984 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,591,576 | 56,461,089 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 492,692 | 3,987,564 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 352,491 | 415,500 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 235,006 | 4,135,256 | 14 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 217,196 | 413,203 | 15 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 33,394 | 668,469 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,651 | 106,401 | 41 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,386 | 110,766 | 43 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,683 | 63,963 | 45 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,545 | 45,501 | 46 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,180 | 90,259 | 49 |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,137 | 667,341 | 50 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,602 | 131,459 | 53 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,341 | 369,794 | 57 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,101 | 64,182 | 63 |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,429 | 11,995 | 74 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 1,417 | 19,110 | 75 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,225 | 98,732 | 82 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,141 | 354,955 | 86 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,098 | 95,268 | 87 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,029 | 156,753 | 91 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 961 | 799,814 | 96 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 959 | 7,089 | 97 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 370 | 75,836 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 179 | 1,984 | 140 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.0% | 1,048,820 | 1,420,993 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 15.0% | 716,151 | 4,681,199 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 13.5% | 297,826 | 2,107,996 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.4% | 282,823 | 6,278,049 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,781 | 424,990 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,133 | 186,151 | 9 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.9% | 3,605 | 23,157 | 15 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.9% | 8,448,854 | 295,850,706 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.8% | 39,653 | 1,341,714 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.6% | 7,503 | 189,616 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.3% | 14,786 | 535,128 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,600 | 351,584 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,602 | 131,459 | 16 |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.5% | 6,810 | 365,471 | 13 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.2% | 3,028 | 148,083 | 17 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,837 | 101,868 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 0.9% | 959 | 7,089 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,091 | 151,921 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,818 | 849,452 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,949 | 484,960 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,825 | 691,526 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,178 | 655,277 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 370 | 75,836 | 24 |
| 24 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 179 | 1,984 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,980 | 1,158,223 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
