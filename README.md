# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-11
- **Generated at:** 2026-11-11T13:51:06Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,968,570 | +12,314 | 60,456,105 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,390,685 | -39,230 | 66,805,810 | 2.1% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 661,982 | +14,499 | 4,485,737 | 14.4% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 546,360 | +8,787 | 46,497,074 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 354,459 | +6,877 | 32,796,950 | 1.1% | 46.70B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 269,182 | -13,966 | 4,691,773 | 5.6% | 8.05B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 255,900 | +2,498 | 2,542,139 | 9.7% | 8.92B | 6 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 211,104 | -15,978 | 312,661 | 51.2% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 206,090 | +3,091 | 5,893,922 | 3.4% | 3.85B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 160,268 | -3,225 | 5,017,211 | 3.1% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 158,813 | +222 | 16,668,444 | 0.9% | 12.25B | 3 |
| 12 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,809 | -1,001 | 7,720,249 | 1.4% | 23.57B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,660 | +155 | 5,624,254 | 1.8% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 76,972 | +11,725 | 4,231,415 | 1.8% | 11.34B | 8 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,495 | +2,849 | 8,606,435 | 0.7% | 8.02B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,880 | -1,979 | 807,115 | 5.5% | 23.57B | 2 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 47,046 | +755 | 11,289,694 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,279 | -640 | 737,270 | 5.4% | 7.77B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,516 | +1,838 | 746,689 | 4.1% | 119.40B | 3 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,130 | +325 | 367,310 | 7.1% | 24.01B | 2 |
| 21 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 30,333 | -6,181 | 3,010,299 | 1.0% | 24.01B | 1 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 23,998 | -109 | 245,974 | 6.9% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,394 | -64 | 945,614 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,907 | +119 | 1,121,092 | 1.4% | 127.70B | 2 |
| 25 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,472 | +25 | 800,078 | 1.8% | 11.25B | 10 |
| 26 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,578 | +209 | 4,944,437 | 0.3% | 122.61B | 1 |
| 27 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,743 | -11 | 5,047,209 | 0.2% | 122.61B | 1 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,665 | +89 | 650,851 | 1.7% | 23.57B | 2 |
| 29 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 12,646 | -622 | 740,395 | 1.5% | 8.90B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,156 | +376 | 498,211 | 1.9% | 9.15B | 1 |
| 31 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,009 | -81 | 524,128 | 1.8% | 7.24B | 8 |
| 32 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 10,414 | -694 | 551,072 | 1.6% | 70.60B | 2 |
| 33 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,310 | -73 | 22,612 | 8.4% | 27.43B | 3 |
| 34 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,072 | +125 | 5,390,719 | 0.2% | 22.25B | 1 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,573 | -203 | 87,078 | 4.6% | — | 5 |
| 36 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,493 | -2,476 | 160,247 | 3.3% | 9.15B | 1 |
| 37 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,366 | +2 | 119,590 | 3.8% | 8.42B | 7 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,230 | -10 | 35,309 | 6.1% | 72.01B | 1 |
| 39 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,351 | +645 | 16,731 | 6.3% | 1.51B | 6 |
| 40 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,977 | -91 | 604,326 | 1.0% | 22.64B | 1 |
| 41 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,732 | +76 | 358,285 | 1.5% | 125.03B | 1 |
| 42 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 6,228 | +124 | 260,644 | 1.7% | 4.76B | 5 |
| 43 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,186 | +994 | 23,624 | 5.0% | 572.6M | 5 |
| 44 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,990 | +96 | 21,612 | 4.9% | 3.83B | 5 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,894 | +95 | 153,043 | 2.3% | 2.25B | 7 |
| 46 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,624 | +8 | 82,025 | 3.1% | 7.04B | 4 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,538 | +265 | 55,956 | 3.6% | 8.03B | 7 |
| 48 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,335 | +270 | 64,544 | 3.2% | 1.60B | 5 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,701 | +9 | 910,568 | 0.5% | 23.57B | 2 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,493 | +6 | 154,743 | 1.8% | 7.24B | 4 |
| 51 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,418 | -35 | 140,518 | 1.8% | 7.40B | 3 |
| 52 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,401 | -14 | 38,505 | 3.2% | 56.7M | 1 |
| 53 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,188 | -17 | 40,965 | 3.0% | 2.61B | 3 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,179 | -44 | 378,237 | 0.9% | 7.24B | 8 |
| 55 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,051 | -41 | 141,100 | 1.7% | 7.48B | 5 |
| 56 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,951 | -29 | 5,165,525 | 0.1% | 22.25B | 1 |
| 57 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,783 | +35 | 28,511 | 2.9% | 22.64B | 1 |
| 58 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,586 | -97 | 44,655 | 2.5% | 13.29B | 3 |
| 59 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,321 | -34 | 169,916 | 1.2% | 11.17B | 16 |
| 60 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,244 | -14 | 96,339 | 1.7% | 2.89B | 1 |
| 61 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,973 | -44 | 13,016 | 2.6% | 9.15B | 1 |
| 62 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,929 | +379 | 53,452 | 1.9% | 7.77B | 1 |
| 63 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,736 | -16 | 5,303,898 | 0.1% | 7.25B | 1 |
| 64 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,550 | -47 | 157,231 | 1.0% | 23.57B | 2 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,502 | -72 | 179,929 | 0.9% | 12.25B | 6 |
| 66 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,393 | -2 | 230,880 | 0.7% | 35.13B | 4 |
| 67 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,323 | +279 | 23,120 | 1.9% | 4.30B | 2 |
| 68 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,312 | -3,030 | 44,790 | 1.6% | 12.25B | 3 |
| 69 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,292 | +53 | 20,712 | 1.9% | 12.19B | 2 |
| 70 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,234 | -267 | 34,645 | 1.7% | 14.03B | 1 |
| 71 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,170 | 0 | 86,609 | 1.2% | 9.15B | 1 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,099 | +3 | 102,489 | 1.0% | 30.68B | 1 |
| 73 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,057 | +12 | 358,585 | 0.4% | — | 3 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,035 | +12 | 80,946 | 1.1% | 7.45B | 1 |
| 75 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,021 | -5 | 51,962 | 1.3% | 9.24B | 4 |
| 76 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,978 | +14 | 160,218 | 0.8% | 1.10B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,939 | +6 | 108,481 | 0.9% | 7.45B | 1 |
| 78 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,871 | +17 | 35,163 | 1.4% | 22.64B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,870 | +18 | 303,605 | 0.5% | 6.74B | 2 |
| 80 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,860 | +14 | 186,945 | 0.6% | 6.74B | 1 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,794 | +12 | 147,663 | 0.7% | 13.02B | 1 |
| 82 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,742 | -15 | 41,027 | 1.2% | 70.55B | 3 |
| 83 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,706 | +20 | 9,756 | 1.6% | 9.82B | 1 |
| 84 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,644 | +380 | 454,379 | 0.3% | 40.43B | 1 |
| 85 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,565 | +6 | 54,842 | 1.0% | 7.24B | 5 |
| 86 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,517 | +22 | 802,347 | 0.2% | — | 3 |
| 87 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,506 | -25 | 20,818 | 1.2% | 1.20B | 2 |
| 88 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,499 | +5 | 53,605 | 1.0% | 7.24B | 1 |
| 89 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,420 | -23 | 9,698 | 1.3% | 4.30B | 3 |
| 90 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,316 | -65 | 16,051 | 1.1% | 353.4M | 2 |
| 91 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,315 | +7 | 9,543 | 1.2% | 28.84B | 3 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,262 | +9 | 175,165 | 0.5% | 11.51B | 7 |
| 93 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,223 | -40 | 31,839 | 0.9% | 33.12B | 1 |
| 94 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,217 | +175 | 416,286 | 0.2% | 1.20B | 1 |
| 95 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,114 | -78 | 219,194 | 0.3% | 12.19B | 3 |
| 96 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,106 | -1 | 56,842 | 0.7% | 7.55B | 1 |
| 97 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,100 | +169 | 419,668 | 0.2% | 353.4M | 1 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,035 | +17 | 58,752 | 0.7% | 1.35B | 3 |
| 99 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,033 | +29 | 45,193 | 0.7% | 12.19B | 2 |
| 100 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 946 | +164 | 401,066 | 0.2% | 3.21B | 1 |
| 101 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 920 | -43 | 671,351 | 0.1% | 7.45B | 2 |
| 102 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 911 | -2 | 24,060 | 0.7% | 11.17B | 5 |
| 103 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 832 | +6 | 233,645 | 0.2% | — | 2 |
| 104 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 801 | -11 | 31,842 | 0.6% | 11.17B | 5 |
| 105 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 800 | +17 | 14,784 | 0.7% | 4.33B | 3 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 755 | -17 | 96,653 | 0.4% | 1.35B | 8 |
| 107 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 742 | -6 | 112,510 | 0.3% | 7.29B | 2 |
| 108 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 692 | -80 | 2,102 | 0.7% | 27.23B | 3 |
| 109 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 687 | -10 | 82,284 | 0.4% | 8.03B | 3 |
| 110 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 686 | -14 | 17,053 | 0.6% | 1.54B | 4 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 606 | +2 | 22,198 | 0.5% | 9.24B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 600 | +3 | 28,021 | 0.5% | 9.24B | 2 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 594 | +14 | 20,875 | 0.5% | 3.20B | 2 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 555 | +10 | 3,730 | 0.5% | 30.68B | 1 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 466 | -7 | 4,465 | 0.4% | 8.03B | 3 |
| 116 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 428 | 0 | 12,461 | 0.4% | 31.59B | 6 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 426 | -5 | 1,713 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 422 | +2 | 12,248 | 0.4% | 27.23B | 2 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 360 | +10 | 3,425 | 0.3% | 560.9M | 2 |
| 120 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 358 | +23 | 5,668 | 0.3% | 11.51B | 5 |
| 121 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 342 | -8 | 22,207 | 0.3% | 2.61B | 2 |
| 122 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 297 | -10 | 2,862 | 0.3% | 4.02B | 2 |
| 123 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 280 | +4 | 37,915 | 0.2% | 27.23B | 3 |
| 124 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 279 | +9 | 32,927 | 0.2% | 40.43B | 2 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 276 | -6 | 107,316 | 0.1% | — | 3 |
| 126 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 261 | +5 | 70,606 | 0.2% | 8.03B | 3 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 237 | -1 | 39,462 | 0.2% | 7.48B | 2 |
| 128 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 207 | +2 | 16,696 | 0.2% | 7.29B | 2 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 204 | +3 | 41,962 | 0.1% | 11.17B | 1 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 198 | -8 | 322,316 | 0.0% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 194 | -4 | 19,726 | 0.2% | 68.98B | 2 |
| 132 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 186 | +8 | 12,748 | 0.2% | 70.55B | 2 |
| 133 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | 0 | 3,002 | 0.2% | 31.59B | 6 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 167 | -14 | 44,694 | 0.1% | 7.70B | 5 |
| 135 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 160 | +1 | 28,463 | 0.1% | 46.70B | 6 |
| 136 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 156 | -4 | 1,199 | 0.2% | — | 1 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 144 | -6 | 2,581 | 0.1% | — | 1 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 140 | +8 | 5,536 | 0.1% | 353.4M | 2 |
| 139 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 124 | 0 | 7,490 | 0.1% | 31.59B | 6 |
| 140 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 103 | -18 | 5,087 | 0.1% | 70.55B | 3 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 100 | -14 | 5,195 | 0.1% | 437.8M | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 83 | 0 | 38,734 | 0.1% | 70.55B | 3 |
| 143 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 64 | -4 | 1,323 | 0.1% | 560.9M | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 59 | +1 | 7,269 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 50 | +11 | 456 | 0.0% | 321.0M | 1 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | +6 | 415 | 0.0% | 437.8M | 1 |
| 147 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 43 | +6 | 217 | 0.0% | 8.16B | 3 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 43 | +4 | 248 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 40 | +3 | 270 | 0.0% | 15.17B | 3 |
| 150 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | +2 | 151 | 0.0% | 7.24B | 1 |
| 151 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | +1 | 180 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | +1 | 290 | 0.0% | 437.8M | 1 |
| 153 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 154 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 155 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 156 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 0 | 0 | 0 | 0.0% | — | 0 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,267,786 | 308,475,242 | 30 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 319,999 | 6,080,516 | 7 | 5.2% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 215,377 | 442,568 | 6 | 39.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 126,924 | 6,470,522 | 12 | 1.9% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 85,147 | 2,661,217 | 11 | 3.1% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 56,025 | 1,431,071 | 5 | 3.7% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 22,106 | 569,038 | 13 | 3.3% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,008 | 1,452,594 | 11 | 1.0% |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,236 | 451,189 | 6 | 2.6% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,797 | 373,626 | 14 | 2.5% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,770 | 203,746 | 3 | 2.9% |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,497 | 400,691 | 10 | 1.5% |
| 13 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,632 | 494,826 | 3 | 0.9% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,624 | 82,025 | 1 | 3.1% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,894 | 860,778 | 3 | 0.5% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,418 | 140,518 | 1 | 1.8% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,377 | 700,553 | 2 | 0.5% |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,927 | 662,190 | 2 | 0.5% |
| 19 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,819 | 1,163,034 | 4 | 0.2% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,737 | 106,706 | 4 | 1.3% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,790 | 155,405 | 2 | 0.7% |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,706 | 9,756 | 1 | 1.6% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 745 | 24,462 | 4 | 0.6% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,968,570 | 60,456,105 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 269,182 | 4,691,773 | 6 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 211,104 | 312,661 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 76,972 | 4,231,415 | 14 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,279 | 737,270 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 23,998 | 245,974 | 22 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,310 | 22,612 | 33 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,366 | 119,590 | 37 |
| 9 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,624 | 82,025 | 46 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,538 | 55,956 | 47 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,493 | 154,743 | 50 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,418 | 140,518 | 51 |
| 13 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,401 | 38,505 | 52 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,179 | 378,237 | 54 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 2,502 | 179,929 | 65 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,099 | 102,489 | 72 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,057 | 358,585 | 73 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,035 | 80,946 | 74 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,978 | 160,218 | 76 |
| 20 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,706 | 9,756 | 83 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,517 | 802,347 | 86 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,035 | 58,752 | 98 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 428 | 12,461 | 116 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 156 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 39.7% | 215,377 | 442,568 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 5.2% | 319,999 | 6,080,516 | 2 |
| 3 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.7% | 56,025 | 1,431,071 | 6 |
| 4 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 22,106 | 569,038 | 7 |
| 5 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,624 | 82,025 | 14 |
| 6 | [utter-project](https://huggingface.co/utter-project) | 3.1% | 85,147 | 2,661,217 | 5 |
| 7 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,770 | 203,746 | 11 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,236 | 451,189 | 9 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,797 | 373,626 | 10 |
| 10 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,267,786 | 308,475,242 | 1 |
| 11 | [speakleash](https://huggingface.co/speakleash) | 1.9% | 126,924 | 6,470,522 | 4 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.8% | 4,418 | 140,518 | 16 |
| 13 | [domyn](https://huggingface.co/domyn) | 1.6% | 1,706 | 9,756 | 22 |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.5% | 7,497 | 400,691 | 12 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,737 | 106,706 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,008 | 1,452,594 | 8 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,632 | 494,826 | 13 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,790 | 155,405 | 21 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 745 | 24,462 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,377 | 700,553 | 17 |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,927 | 662,190 | 18 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,894 | 860,778 | 15 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,819 | 1,163,034 | 19 |
| 24 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 24 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
