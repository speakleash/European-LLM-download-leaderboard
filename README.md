# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-03
- **Generated at:** 2026-11-03T13:53:43Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,829,024 | +2,842 | 59,768,582 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,690,368 | -19,175 | 66,554,403 | 2.5% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 570,733 | +7,872 | 46,326,857 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 565,322 | +11,459 | 4,305,893 | 12.8% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 390,552 | -14,351 | 4,683,972 | 8.2% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 330,021 | +7,182 | 32,709,461 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 219,149 | -3,074 | 2,460,198 | 8.6% | 8.92B | 6 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,277 | +483 | 5,834,100 | 3.4% | 3.85B | 7 |
| 9 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 185,061 | -4,509 | 16,638,983 | 1.1% | 12.25B | 3 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 183,551 | +2,017 | 4,974,460 | 3.6% | 24.01B | 2 |
| 11 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 172,495 | +9,266 | 239,724 | 50.8% | 12.77B | 5 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 131,254 | -6,975 | 3,004,594 | 4.2% | 24.01B | 1 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 118,879 | -1,106 | 5,601,659 | 2.1% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 101,947 | +3,899 | 7,693,276 | 1.3% | 23.57B | 2 |
| 15 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,813 | -3,091 | 805,698 | 7.3% | 23.57B | 2 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,421 | +525 | 11,277,972 | 0.5% | 140.63B | 2 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,358 | -9,011 | 738,372 | 6.0% | 119.40B | 3 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,137 | +907 | 727,836 | 5.5% | 7.77B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 44,751 | -851 | 8,574,730 | 0.5% | 8.02B | 1 |
| 20 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 41,953 | -32,775 | 739,164 | 5.0% | 8.90B | 1 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,547 | +181 | 363,486 | 7.7% | 24.01B | 2 |
| 22 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,745 | -96 | 1,117,033 | 2.2% | 127.70B | 2 |
| 23 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 25,411 | +471 | 4,174,533 | 0.6% | 11.34B | 8 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 25,026 | -1,144 | 241,727 | 7.3% | — | 1 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,082 | -14,386 | 943,056 | 2.0% | 1.66B | 1 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 18,020 | -2,504 | 44,417 | 12.5% | 12.25B | 3 |
| 27 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,986 | +468 | 796,051 | 1.8% | 11.25B | 10 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,787 | +76 | 648,696 | 2.1% | 23.57B | 2 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,134 | -483 | 549,696 | 2.3% | 70.60B | 2 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,712 | +9 | 5,046,323 | 0.2% | 122.61B | 1 |
| 31 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,509 | +562 | 4,939,915 | 0.2% | 122.61B | 1 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,590 | +5 | 158,477 | 4.5% | 9.15B | 1 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,459 | +511 | 495,275 | 1.9% | 9.15B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,227 | +61 | 521,067 | 1.8% | 7.24B | 8 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,628 | +29 | 84,840 | 5.2% | — | 5 |
| 36 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,560 | -138 | 5,388,127 | 0.2% | 22.25B | 1 |
| 37 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,556 | -345 | 20,531 | 7.1% | 27.43B | 3 |
| 38 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,528 | +82 | 602,743 | 1.2% | 22.64B | 1 |
| 39 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,421 | -10 | 34,765 | 6.2% | 72.01B | 1 |
| 40 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,294 | 0 | 76,470 | 4.7% | — | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,614 | -33 | 117,385 | 3.5% | 8.42B | 7 |
| 42 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,284 | +159 | 356,360 | 1.4% | 125.03B | 1 |
| 43 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,915 | +439 | 14,443 | 5.2% | 1.51B | 6 |
| 44 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,675 | -228 | 151,047 | 2.3% | 2.25B | 7 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,586 | +41 | 81,757 | 3.1% | 7.04B | 4 |
| 46 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,541 | +209 | 20,573 | 4.6% | 3.83B | 5 |
| 47 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,375 | +539 | 258,694 | 1.5% | 4.76B | 5 |
| 48 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,241 | -9 | 139,902 | 2.2% | 7.48B | 5 |
| 49 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,133 | -470 | 20,910 | 4.2% | 572.6M | 5 |
| 50 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,706 | -13 | 5,164,522 | 0.1% | 22.25B | 1 |
| 51 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,566 | +62 | 909,704 | 0.5% | 23.57B | 2 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,556 | +14 | 377,209 | 1.0% | 7.24B | 8 |
| 53 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,538 | +20 | 153,530 | 1.8% | 7.24B | 4 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,492 | -34 | 139,222 | 1.9% | 7.40B | 3 |
| 55 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,205 | +29 | 62,358 | 2.6% | 1.60B | 5 |
| 56 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,050 | -54 | 169,218 | 1.5% | 11.17B | 16 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,997 | +30 | 39,882 | 2.9% | 2.61B | 3 |
| 58 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,877 | +45 | 53,325 | 2.5% | 8.03B | 7 |
| 59 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,783 | +140 | 36,763 | 2.8% | 56.7M | 1 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,240 | +318 | 43,341 | 2.3% | 13.29B | 3 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,156 | +16 | 95,335 | 1.6% | 2.89B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,151 | +82 | 26,816 | 2.5% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,728 | +26 | 34,464 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,697 | +66 | 5,303,473 | 0.0% | 7.25B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,561 | +24 | 179,428 | 0.9% | 12.25B | 6 |
| 66 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,551 | -15 | 156,914 | 1.0% | 23.57B | 2 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,345 | +54 | 52,052 | 1.5% | 7.77B | 1 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,316 | +25 | 230,352 | 0.7% | 35.13B | 4 |
| 69 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,124 | -215 | 22,459 | 1.7% | 4.30B | 2 |
| 70 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,077 | +45 | 101,906 | 1.0% | 30.68B | 1 |
| 71 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,033 | -45 | 51,418 | 1.3% | 9.24B | 4 |
| 72 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,016 | +6 | 358,021 | 0.4% | — | 3 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,004 | +9 | 80,361 | 1.1% | 7.45B | 1 |
| 74 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,920 | +4 | 107,930 | 0.9% | 7.45B | 1 |
| 75 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,892 | +16 | 159,658 | 0.7% | 1.10B | 1 |
| 76 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,826 | +10 | 19,868 | 1.5% | 12.19B | 2 |
| 77 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,813 | +6 | 34,626 | 1.3% | 22.64B | 1 |
| 78 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,811 | +8 | 186,426 | 0.6% | 6.74B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,802 | +12 | 303,071 | 0.4% | 6.74B | 2 |
| 80 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,789 | -3 | 415,653 | 0.3% | 1.20B | 1 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,737 | +10 | 147,148 | 0.7% | 13.02B | 1 |
| 82 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,734 | 0 | 40,629 | 1.2% | 70.55B | 3 |
| 83 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,680 | +23 | 9,384 | 1.5% | 4.30B | 3 |
| 84 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,606 | +3 | 418,985 | 0.3% | 353.4M | 1 |
| 85 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,605 | +7 | 54,428 | 1.0% | 7.24B | 5 |
| 86 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,570 | +5 | 400,489 | 0.3% | 3.21B | 1 |
| 87 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,547 | -30 | 9,372 | 1.4% | 9.82B | 1 |
| 88 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,525 | +5 | 53,197 | 1.0% | 7.24B | 1 |
| 89 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,514 | +166 | 10,973 | 1.4% | 9.15B | 1 |
| 90 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,450 | +81 | 31,641 | 1.1% | 33.12B | 1 |
| 91 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,445 | +17 | 801,966 | 0.2% | — | 3 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,405 | +18 | 174,864 | 0.5% | 11.51B | 7 |
| 93 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,311 | +86 | 20,113 | 1.1% | 1.20B | 2 |
| 94 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,229 | -55 | 671,097 | 0.2% | 7.45B | 2 |
| 95 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,151 | -41 | 23,842 | 0.9% | 11.17B | 5 |
| 96 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,146 | +213 | 219,028 | 0.4% | 12.19B | 3 |
| 97 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,116 | +15 | 9,180 | 1.0% | 28.84B | 3 |
| 98 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,078 | -5 | 15,396 | 0.9% | 353.4M | 2 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,034 | -16 | 58,478 | 0.7% | 1.35B | 3 |
| 100 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,028 | +12 | 56,387 | 0.7% | 7.55B | 1 |
| 101 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 993 | -26 | 31,680 | 0.8% | 11.17B | 5 |
| 102 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 986 | +15 | 453,460 | 0.2% | 40.43B | 1 |
| 103 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 980 | +533 | 85,287 | 0.5% | 9.15B | 1 |
| 104 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 850 | +11 | 44,923 | 0.6% | 12.19B | 2 |
| 105 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 840 | +29 | 233,500 | 0.3% | — | 2 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 782 | +75 | 14,681 | 0.7% | 4.33B | 3 |
| 107 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 743 | -26 | 112,152 | 0.4% | 7.29B | 2 |
| 108 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 725 | +8 | 82,108 | 0.4% | 8.03B | 3 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 702 | +10 | 96,424 | 0.4% | 1.35B | 8 |
| 110 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 695 | +201 | 1,936 | 0.7% | 27.23B | 3 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 673 | -5 | 16,866 | 0.6% | 1.54B | 4 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 607 | +23 | 27,896 | 0.5% | 9.24B | 2 |
| 113 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 604 | -9 | 22,103 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 565 | -75 | 20,737 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 543 | +29 | 3,574 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 503 | +4 | 4,325 | 0.5% | 8.03B | 3 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 443 | -2 | 1,604 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 414 | +3 | 12,194 | 0.4% | 27.23B | 2 |
| 119 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 361 | 0 | 12,374 | 0.3% | 31.59B | 6 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 340 | -7 | 32,867 | 0.3% | 40.43B | 2 |
| 121 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 327 | -12 | 2,830 | 0.3% | 4.02B | 2 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 326 | +12 | 37,870 | 0.2% | 27.23B | 3 |
| 123 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 321 | -1 | 5,547 | 0.3% | 11.51B | 5 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 300 | -5 | 107,241 | 0.1% | — | 3 |
| 125 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 287 | -8 | 22,104 | 0.2% | 2.61B | 2 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 284 | -34 | 39,424 | 0.2% | 7.48B | 2 |
| 127 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 273 | -2 | 322,248 | 0.1% | 7.24B | 2 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 245 | +4 | 41,908 | 0.2% | 11.17B | 1 |
| 129 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 242 | +17 | 70,532 | 0.1% | 8.03B | 3 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 227 | -5 | 19,697 | 0.2% | 68.98B | 2 |
| 131 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 221 | +8 | 5,065 | 0.2% | 70.55B | 3 |
| 132 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 213 | -19 | 5,175 | 0.2% | 437.8M | 1 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 210 | +1 | 44,655 | 0.1% | 7.70B | 5 |
| 134 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 202 | -3 | 16,632 | 0.2% | 7.29B | 2 |
| 135 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 184 | -29 | 12,711 | 0.2% | 70.55B | 2 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 181 | -5 | 2,559 | 0.2% | — | 1 |
| 137 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 165 | -2 | 28,420 | 0.1% | 46.70B | 6 |
| 138 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 161 | 0 | 7,476 | 0.1% | 31.59B | 6 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 153 | -4 | 5,501 | 0.1% | 353.4M | 2 |
| 140 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 150 | -3 | 3,146 | 0.1% | 560.9M | 2 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 144 | +3 | 1,159 | 0.1% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 96 | +1 | 38,719 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 89 | -2 | 7,255 | 0.1% | 1.20B | 2 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 74 | -1 | 1,316 | 0.1% | 560.9M | 1 |
| 145 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | 0 | 402 | 0.0% | 437.8M | 1 |
| 146 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 45 | 0 | 2,856 | 0.0% | 31.59B | 6 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 42 | -1 | 437 | 0.0% | 321.0M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 39 | +4 | 263 | 0.0% | 15.17B | 3 |
| 149 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 36 | +3 | 204 | 0.0% | 8.16B | 3 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | -5 | 228 | 0.0% | 437.8M | 1 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | 0 | 279 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 165 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 12 | +2 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | -9 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,488,808 | 306,751,394 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 472,649 | 6,063,523 | 7 | 7.7% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 176,787 | 368,551 | 6 | 37.7% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 89,321 | 2,641,421 | 11 | 3.3% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 75,610 | 6,399,664 | 12 | 1.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 54,483 | 1,417,262 | 5 | 3.6% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 23,676 | 399,172 | 10 | 4.7% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,257 | 563,751 | 13 | 2.9% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,386 | 1,446,041 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,133 | 446,798 | 6 | 2.4% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,738 | 370,184 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,294 | 76,470 | 1 | 4.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,108 | 201,464 | 3 | 2.7% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,586 | 81,757 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,440 | 493,232 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,153 | 859,388 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,829 | 699,457 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,492 | 139,222 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,818 | 661,092 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,812 | 1,162,404 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,695 | 105,947 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,736 | 154,902 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,547 | 9,372 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 579 | 24,215 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,829,024 | 59,768,582 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 390,552 | 4,683,972 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 172,495 | 239,724 | 11 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,137 | 727,836 | 18 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 25,411 | 4,174,533 | 23 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 25,026 | 241,727 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 18,020 | 44,417 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,556 | 20,531 | 37 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,294 | 76,470 | 40 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,614 | 117,385 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,586 | 81,757 | 45 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,556 | 377,209 | 52 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,538 | 153,530 | 53 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,492 | 139,222 | 54 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,877 | 53,325 | 58 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,783 | 36,763 | 59 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,077 | 101,906 | 70 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,016 | 358,021 | 72 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,004 | 80,361 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,892 | 159,658 | 75 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,547 | 9,372 | 87 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,445 | 801,966 | 91 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,034 | 58,478 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 361 | 12,374 | 119 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 37.7% | 176,787 | 368,551 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 7.7% | 472,649 | 6,063,523 | 2 |
| 3 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4.7% | 23,676 | 399,172 | 7 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | 4.7% | 8,294 | 76,470 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.6% | 54,483 | 1,417,262 | 6 |
| 6 | [utter-project](https://huggingface.co/utter-project) | 3.3% | 89,321 | 2,641,421 | 4 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,586 | 81,757 | 14 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.9% | 19,257 | 563,751 | 8 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 8,108 | 201,464 | 13 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,738 | 370,184 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 13,133 | 446,798 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,488,808 | 306,751,394 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,492 | 139,222 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,547 | 9,372 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,695 | 105,947 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.2% | 75,610 | 6,399,664 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,386 | 1,446,041 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,440 | 493,232 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,736 | 154,902 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,829 | 699,457 | 17 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,153 | 859,388 | 16 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,818 | 661,092 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 579 | 24,215 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,812 | 1,162,404 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
