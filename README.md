# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-28
- **Generated at:** 2026-09-28T13:23:04Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,391,591 | +2,825 | 57,366,732 | 4.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,689,068 | -56,934 | 64,474,143 | 2.6% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 589,576 | +60 | 45,670,224 | 1.3% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 577,659 | -18,173 | 3,671,941 | 15.3% | 13.95B | 6 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 511,155 | +1,798 | 4,713,180 | 10.6% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 504,937 | -1,813 | 4,185,695 | 11.8% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 467,461 | -8,278 | 16,317,998 | 2.8% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 455,779 | +35,147 | 470,690 | 79.9% | 8.90B | 1 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 361,119 | +14,136 | 559,480 | 54.8% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 308,389 | +856 | 2,818,434 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 282,013 | +2,163 | 5,568,698 | 5.0% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 266,118 | -4,533 | 32,319,020 | 0.8% | 46.70B | 2 |
| 13 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 221,070 | +8,363 | 2,194,274 | 9.6% | 8.92B | 6 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,974 | +1,559 | 5,403,099 | 3.7% | 24.01B | 1 |
| 15 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 177,051 | -16,366 | 416,783 | 34.3% | 353.4M | 1 |
| 16 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 176,394 | -16,336 | 413,263 | 34.4% | 1.20B | 1 |
| 17 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 172,606 | -15,960 | 398,276 | 34.6% | 3.21B | 1 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 159,481 | -8,608 | 4,144,014 | 3.8% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,246 | -1,593 | 8,506,819 | 1.8% | 8.02B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 124,414 | +6,886 | 1,076,277 | 10.6% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 95,608 | -52 | 529,640 | 15.2% | 70.60B | 2 |
| 22 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,762 | -390 | 721,311 | 8.9% | 23.57B | 2 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,880 | +104 | 745,590 | 6.8% | 1.66B | 1 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,022 | -441 | 7,572,998 | 0.7% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 51,616 | +1,037 | 658,073 | 6.8% | 119.40B | 3 |
| 26 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 50,077 | +30,734 | 51,974 | 33.0% | — | 1 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,147 | -8,250 | 630,819 | 6.7% | 23.57B | 2 |
| 28 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 44,435 | +466 | 11,203,741 | 0.4% | 140.63B | 2 |
| 29 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 30,752 | +276 | 676,721 | 4.0% | 7.77B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,665 | -103 | 143,759 | 11.3% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,528 | +81 | 5,158,841 | 0.4% | 22.25B | 1 |
| 32 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,762 | -624 | 480,489 | 3.2% | 9.15B | 1 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,726 | +6 | 25,047 | 14.2% | 72.01B | 1 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,140 | -49 | 776,832 | 1.8% | 11.25B | 10 |
| 35 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,130 | +447 | 212,098 | 4.8% | — | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,026 | -40 | 71,969 | 8.2% | — | 5 |
| 37 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,460 | +24 | 5,300,430 | 0.2% | 7.25B | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,713 | +299 | 507,211 | 1.9% | 7.24B | 8 |
| 39 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,598 | -1,847 | 326,014 | 2.7% | 24.01B | 2 |
| 40 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,279 | -82 | 348,952 | 2.5% | 125.03B | 1 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 8,182 | +80 | 131,487 | 3.5% | 7.48B | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,396 | +74 | 108,797 | 3.5% | 8.42B | 7 |
| 43 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,263 | +144 | 4,924,921 | 0.1% | 122.61B | 1 |
| 44 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,703 | +370 | 30,065 | 4.4% | 33.12B | 1 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,481 | +69 | 48,323 | 3.7% | 8.03B | 7 |
| 46 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,363 | +89 | 163,994 | 2.0% | 11.17B | 16 |
| 47 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,079 | +64 | 111,261 | 2.4% | 7.29B | 2 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,474 | -340 | 66,418 | 2.7% | 12.77B | 5 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,468 | +48 | 143,659 | 1.8% | 2.25B | 7 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,325 | -29 | 904,462 | 0.4% | 23.57B | 2 |
| 51 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,308 | +137 | 5,377,055 | 0.1% | 22.25B | 1 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,229 | +85 | 55,079 | 2.7% | 7.55B | 1 |
| 53 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,192 | +93 | 133,343 | 1.8% | 7.40B | 3 |
| 54 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,183 | +83 | 669,153 | 0.5% | 7.45B | 2 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,132 | +61 | 252,455 | 1.2% | 4.76B | 5 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,124 | +125 | 371,624 | 0.9% | 7.24B | 8 |
| 57 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,769 | +61 | 91,472 | 2.0% | 2.89B | 1 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,647 | +29 | 31,607 | 2.8% | 14.03B | 1 |
| 59 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,463 | +30 | 152,796 | 1.4% | 23.57B | 2 |
| 60 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,329 | +101 | 66,009 | 2.0% | 14.08B | 1 |
| 61 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,192 | +112 | 147,967 | 1.3% | 7.24B | 4 |
| 62 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,047 | +59 | 13,245 | 2.7% | 572.6M | 5 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,006 | +66 | 35,121 | 2.2% | 2.61B | 3 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,679 | -77 | 57,469 | 1.7% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,666 | -19 | 84,205 | 1.4% | 9.15B | 1 |
| 66 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,572 | +6 | 5,031,881 | 0.1% | 122.61B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,210 | -2 | 39,523 | 1.6% | 321.0M | 2 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,131 | -1 | 7,956 | 2.0% | 1.51B | 6 |
| 69 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,126 | +65 | 48,917 | 1.4% | 9.24B | 4 |
| 70 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,057 | +55 | 32,441 | 1.6% | 22.64B | 1 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,918 | +50 | 77,941 | 1.1% | 7.45B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,872 | +65 | 23,140 | 1.5% | 22.64B | 1 |
| 73 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,853 | +4 | 14,717 | 1.6% | 3.83B | 5 |
| 74 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,774 | +38 | 452,309 | 0.3% | 40.43B | 1 |
| 75 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,756 | +96 | 84,941 | 0.9% | 2.22B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,711 | +40 | 105,615 | 0.8% | 7.45B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,678 | +57 | 99,414 | 0.8% | 30.68B | 1 |
| 78 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,631 | +90 | 17,334 | 1.4% | 12.19B | 2 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,613 | +61 | 355,603 | 0.4% | — | 3 |
| 80 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,603 | -2 | 49,335 | 1.1% | 7.77B | 1 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,596 | +57 | 176,503 | 0.6% | 12.25B | 6 |
| 82 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,539 | +41 | 22,289 | 1.3% | 11.17B | 5 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,490 | +55 | 157,398 | 0.6% | 1.10B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,434 | +32 | 300,892 | 0.4% | 6.74B | 2 |
| 85 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,395 | +56 | 145,057 | 0.6% | 13.02B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,392 | +58 | 184,261 | 0.5% | 6.74B | 1 |
| 87 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,381 | -7 | 173,143 | 0.5% | 11.51B | 7 |
| 88 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,380 | 0 | 12,006 | 1.2% | 31.59B | 6 |
| 89 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,346 | +15 | 30,361 | 1.0% | 11.17B | 5 |
| 90 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,277 | -12 | 9,296 | 1.2% | 9.15B | 1 |
| 91 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,252 | +29 | 7,527 | 1.2% | 9.82B | 1 |
| 92 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,246 | +5 | 57,178 | 0.8% | 1.35B | 3 |
| 93 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,222 | +20 | 19,832 | 1.0% | 4.30B | 2 |
| 94 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,205 | +68 | 32,438 | 0.9% | 56.7M | 1 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,169 | -2 | 19,543 | 1.0% | 12.25B | 3 |
| 96 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,103 | +9 | 95,610 | 0.6% | 1.35B | 8 |
| 97 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,063 | +13 | 7,324 | 1.0% | 4.30B | 3 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,050 | +19 | 800,305 | 0.1% | — | 3 |
| 99 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,031 | -7 | 227,771 | 0.3% | 35.13B | 4 |
| 100 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,000 | -16 | 7,961 | 0.9% | 28.84B | 3 |
| 101 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 980 | 0 | 2,823 | 1.0% | 31.59B | 6 |
| 102 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 970 | +1 | 8,357 | 0.9% | 27.43B | 3 |
| 103 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 959 | +60 | 52,478 | 0.6% | 7.24B | 5 |
| 104 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 908 | +11 | 37,471 | 0.7% | 27.23B | 3 |
| 105 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 864 | +65 | 51,346 | 0.6% | 7.24B | 1 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 860 | +30 | 18,568 | 0.7% | 1.20B | 2 |
| 107 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 845 | -9 | 38,651 | 0.6% | 70.55B | 3 |
| 108 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 835 | +7 | 81,238 | 0.5% | 8.03B | 3 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 795 | +11 | 14,074 | 0.7% | 353.4M | 2 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 758 | -7 | 20,007 | 0.6% | 3.20B | 2 |
| 111 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 669 | +11 | 43,978 | 0.5% | 12.19B | 2 |
| 112 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 645 | -56 | 70,246 | 0.4% | 8.03B | 3 |
| 113 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 639 | +19 | 15,926 | 0.6% | 1.54B | 4 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 619 | +13 | 2,940 | 0.6% | 30.68B | 1 |
| 115 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 594 | -17 | 217,805 | 0.2% | 12.19B | 3 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 552 | -29 | 232,614 | 0.2% | — | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 550 | +3 | 2,961 | 0.5% | 560.9M | 2 |
| 118 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 525 | -10 | 3,702 | 0.5% | 8.03B | 3 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 510 | +24 | 32,453 | 0.4% | 40.43B | 2 |
| 120 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 486 | -11 | 12,437 | 0.4% | 70.55B | 2 |
| 121 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 465 | -14 | 39,070 | 0.3% | 7.48B | 2 |
| 122 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 461 | +16 | 27,231 | 0.4% | 9.24B | 2 |
| 123 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 458 | -22 | 1,330 | 0.5% | 31.58B | 2 |
| 124 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 455 | -5 | 321,910 | 0.1% | 7.24B | 2 |
| 125 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 447 | +8 | 13,781 | 0.4% | 4.33B | 3 |
| 126 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 439 | -3 | 76,032 | 0.2% | 7.04B | 4 |
| 127 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 404 | +1 | 44,396 | 0.3% | 7.70B | 5 |
| 128 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 402 | -4 | 7,284 | 0.4% | 31.59B | 6 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 401 | +10 | 21,720 | 0.3% | 2.61B | 2 |
| 130 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 381 | 0 | 11,720 | 0.3% | 27.23B | 2 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 337 | -1 | 41,627 | 0.2% | 11.17B | 1 |
| 132 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 315 | -2 | 1,187 | 0.3% | 27.23B | 3 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 308 | -8 | 106,878 | 0.1% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 306 | -4 | 2,429 | 0.3% | 4.02B | 2 |
| 135 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 292 | -7 | 1,097 | 0.3% | — | 1 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 265 | +5 | 16,394 | 0.2% | 7.29B | 2 |
| 137 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 260 | -5 | 21,398 | 0.2% | 9.24B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 239 | +4 | 19,414 | 0.2% | 68.98B | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 201 | +5 | 38,604 | 0.1% | 70.55B | 3 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 196 | +7 | 5,307 | 0.2% | 353.4M | 2 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 189 | +1 | 5,145 | 0.2% | 11.51B | 5 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 181 | +2 | 2,326 | 0.2% | — | 1 |
| 143 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 168 | -6 | 4,870 | 0.2% | 437.8M | 1 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 144 | -2 | 4,824 | 0.1% | 70.55B | 3 |
| 145 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | -3 | 7,139 | 0.1% | 1.20B | 2 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | +4 | 28,228 | 0.1% | 46.70B | 6 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 121 | +8 | 997 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 101 | +1 | 1,232 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 68 | -4 | 186 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 45 | -3 | 348 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 38 | -2 | 256 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | 0 | 142 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +2 | 353 | 0.0% | 437.8M | 1 |
| 154 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | +2 | 111 | 0.0% | 7.24B | 1 |
| 155 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 18 | 0 | 213 | 0.0% | 15.17B | 3 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | 0 | 156 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 9 | -2 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,152,951 | 298,487,196 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,081,081 | 5,246,990 | 7 | 20.2% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 532,339 | 1,426,957 | 11 | 34.9% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 491,615 | 2,327,945 | 11 | 20.2% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 212,482 | 6,306,027 | 12 | 3.3% |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 50,077 | 51,974 | 1 | 33.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,107 | 1,354,477 | 5 | 2.7% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 20,936 | 431,496 | 6 | 3.9% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,380 | 538,772 | 13 | 2.1% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 10,082 | 355,811 | 14 | 2.2% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,220 | 189,926 | 6 | 3.2% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,265 | 192,263 | 3 | 2.8% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,812 | 852,709 | 3 | 0.8% |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,974 | 367,446 | 10 | 1.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,085 | 150,950 | 2 | 2.0% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,579 | 693,534 | 2 | 0.6% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,277 | 486,716 | 3 | 0.7% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,192 | 133,343 | 1 | 1.8% |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,220 | 23,443 | 4 | 2.6% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,047 | 656,495 | 2 | 0.4% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,349 | 152,788 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,330 | 102,723 | 4 | 1.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,149 | 1,159,211 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,252 | 7,527 | 1 | 1.2% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 439 | 76,032 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,391,591 | 57,366,732 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 504,937 | 4,185,695 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 361,119 | 559,480 | 9 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 177,051 | 416,783 | 15 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 159,481 | 4,144,014 | 18 |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 50,077 | 51,974 | 26 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 30,752 | 676,721 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,396 | 108,797 | 42 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Viking 33B | 5,703 | 30,065 | 44 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,079 | 111,261 | 47 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,474 | 66,418 | 48 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,192 | 133,343 | 53 |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,183 | 669,153 | 54 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,124 | 371,624 | 56 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,769 | 91,472 | 57 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,329 | 66,009 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,678 | 99,414 | 77 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,613 | 355,603 | 79 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,596 | 176,503 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,490 | 157,398 | 83 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,380 | 12,006 | 88 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,252 | 7,527 | 91 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,246 | 57,178 | 92 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,050 | 800,305 | 98 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 439 | 76,032 | 126 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 34.9% | 532,339 | 1,426,957 | 3 |
| 2 | [openeurollm](https://huggingface.co/openeurollm) | 33.0% | 50,077 | 51,974 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 20.2% | 491,615 | 2,327,945 | 4 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 20.2% | 1,081,081 | 5,246,990 | 2 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.9% | 20,936 | 431,496 | 8 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 3.3% | 212,482 | 6,306,027 | 5 |
| 7 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,220 | 189,926 | 11 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,265 | 192,263 | 12 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,152,951 | 298,487,196 | 1 |
| 10 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,107 | 1,354,477 | 7 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.6% | 3,220 | 23,443 | 19 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.2% | 10,082 | 355,811 | 10 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,380 | 538,772 | 9 |
| 14 | [Almawave](https://huggingface.co/Almawave) | 2.0% | 5,085 | 150,950 | 15 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.8% | 4,192 | 133,343 | 18 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,974 | 367,446 | 14 |
| 17 | [domyn](https://huggingface.co/domyn) | 1.2% | 1,252 | 7,527 | 24 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,330 | 102,723 | 22 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,349 | 152,788 | 21 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,812 | 852,709 | 13 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.7% | 4,277 | 486,716 | 17 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,579 | 693,534 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,047 | 656,495 | 20 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 439 | 76,032 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,149 | 1,159,211 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
