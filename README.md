# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-05
- **Generated at:** 2026-11-05T14:23:21Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,861,515 | +11,640 | 59,951,022 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,626,284 | -39,316 | 66,616,360 | 2.4% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 580,706 | +2,247 | 46,361,385 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 577,620 | +10,404 | 4,353,649 | 13.0% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 360,029 | -15,327 | 4,686,450 | 7.5% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 326,609 | -3,280 | 32,731,021 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 216,029 | -1,156 | 2,470,136 | 8.4% | 8.92B | 6 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,349 | -550 | 5,848,266 | 3.4% | 3.85B | 7 |
| 9 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 191,138 | +9,486 | 258,687 | 53.3% | 12.77B | 5 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 177,310 | -3,455 | 4,987,103 | 3.5% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 172,121 | -6,191 | 16,643,741 | 1.0% | 12.25B | 3 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 116,296 | -7,447 | 3,006,051 | 3.7% | 24.01B | 1 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 112,065 | -3,552 | 5,607,064 | 2.0% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 107,716 | -982 | 7,704,946 | 1.4% | 23.57B | 2 |
| 15 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 61,078 | -2,313 | 805,955 | 6.7% | 23.57B | 2 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 55,278 | -3,033 | 11,280,374 | 0.5% | 140.63B | 2 |
| 17 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 48,682 | +4,822 | 8,581,846 | 0.6% | 8.02B | 1 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 46,776 | -732 | 732,093 | 5.6% | 7.77B | 8 |
| 19 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,661 | -21 | 364,366 | 7.7% | 24.01B | 2 |
| 20 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,292 | -4,362 | 740,219 | 4.1% | 119.40B | 3 |
| 21 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 25,704 | +297 | 4,176,166 | 0.6% | 11.34B | 8 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 23,292 | -957 | 242,187 | 6.8% | — | 1 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 23,169 | -3,409 | 1,118,348 | 1.9% | 127.70B | 2 |
| 24 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,731 | -2 | 944,091 | 2.0% | 1.66B | 1 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,952 | -5,836 | 739,594 | 2.0% | 8.90B | 1 |
| 26 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,182 | +142 | 797,227 | 1.8% | 11.25B | 10 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,956 | +7 | 649,296 | 2.1% | 23.57B | 2 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 13,783 | -645 | 550,045 | 2.1% | 70.60B | 2 |
| 29 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,473 | +586 | 4,941,435 | 0.3% | 122.61B | 1 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,672 | -37 | 5,046,552 | 0.2% | 122.61B | 1 |
| 31 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11,813 | -3,159 | 44,526 | 8.2% | 12.25B | 3 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,595 | -117 | 159,176 | 4.5% | 9.15B | 1 |
| 33 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,267 | +120 | 522,052 | 1.8% | 7.24B | 8 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,224 | -19 | 495,810 | 1.9% | 9.15B | 1 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,182 | -205 | 85,391 | 5.0% | — | 5 |
| 36 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,617 | +249 | 603,370 | 1.2% | 22.64B | 1 |
| 37 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,530 | -16 | 20,570 | 7.1% | 27.43B | 3 |
| 38 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,484 | +21 | 76,680 | 4.8% | — | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,427 | -37 | 5,388,773 | 0.2% | 22.25B | 1 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,295 | +57 | 34,981 | 6.1% | 72.01B | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,122 | +304 | 118,144 | 3.7% | 8.42B | 7 |
| 42 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,452 | +29 | 15,168 | 5.6% | 1.51B | 6 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,414 | +34 | 356,891 | 1.4% | 125.03B | 1 |
| 44 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,732 | +235 | 259,347 | 1.6% | 4.76B | 5 |
| 45 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,674 | +113 | 20,857 | 4.7% | 3.83B | 5 |
| 46 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,617 | +2 | 81,846 | 3.1% | 7.04B | 4 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,420 | -108 | 151,537 | 2.2% | 2.25B | 7 |
| 48 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,772 | -316 | 140,153 | 2.0% | 7.48B | 5 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,610 | -17 | 909,978 | 0.5% | 23.57B | 2 |
| 50 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,582 | +52 | 139,675 | 1.9% | 7.40B | 3 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,535 | -10 | 153,855 | 1.8% | 7.24B | 4 |
| 52 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,521 | +16 | 21,334 | 3.7% | 572.6M | 5 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,447 | +113 | 62,907 | 2.7% | 1.60B | 5 |
| 54 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,447 | -68 | 5,164,917 | 0.1% | 22.25B | 1 |
| 55 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,421 | -58 | 377,502 | 0.9% | 7.24B | 8 |
| 56 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,185 | +201 | 37,487 | 3.0% | 56.7M | 1 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,113 | +109 | 40,242 | 2.9% | 2.61B | 3 |
| 58 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,039 | +163 | 53,658 | 2.6% | 8.03B | 7 |
| 59 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,847 | -75 | 169,413 | 1.4% | 11.17B | 16 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,758 | +26 | 44,218 | 2.6% | 13.29B | 3 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,276 | +6 | 95,711 | 1.7% | 2.89B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,095 | -50 | 26,993 | 2.4% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,753 | +11 | 34,520 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,690 | -7 | 5,303,595 | 0.0% | 7.25B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,549 | -14 | 179,555 | 0.9% | 12.25B | 6 |
| 66 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,503 | -40 | 156,964 | 1.0% | 23.57B | 2 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,402 | -23 | 52,240 | 1.6% | 7.77B | 1 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,302 | +19 | 230,504 | 0.7% | 35.13B | 4 |
| 69 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,143 | 0 | 22,534 | 1.7% | 4.30B | 2 |
| 70 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,066 | +11 | 102,061 | 1.0% | 30.68B | 1 |
| 71 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,045 | +15 | 358,178 | 0.4% | — | 3 |
| 72 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,021 | -4 | 51,555 | 1.3% | 9.24B | 4 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,003 | +1 | 80,518 | 1.1% | 7.45B | 1 |
| 74 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,925 | +22 | 159,808 | 0.7% | 1.10B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,916 | +16 | 108,075 | 0.9% | 7.45B | 1 |
| 76 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,840 | +6 | 19,964 | 1.5% | 12.19B | 2 |
| 77 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,834 | +14 | 34,771 | 1.4% | 22.64B | 1 |
| 78 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,828 | +15 | 303,215 | 0.5% | 6.74B | 2 |
| 79 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,826 | +1 | 186,567 | 0.6% | 6.74B | 1 |
| 80 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,798 | +49 | 40,775 | 1.3% | 70.55B | 3 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,759 | +16 | 147,287 | 0.7% | 13.02B | 1 |
| 82 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,742 | +139 | 20,586 | 1.4% | 1.20B | 2 |
| 83 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,674 | +134 | 11,207 | 1.5% | 9.15B | 1 |
| 84 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,650 | -22 | 9,458 | 1.5% | 4.30B | 3 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,601 | +55 | 9,477 | 1.5% | 9.82B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,591 | -11 | 54,535 | 1.0% | 7.24B | 5 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,525 | 0 | 53,306 | 1.0% | 7.24B | 1 |
| 88 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,482 | +156 | 15,877 | 1.3% | 353.4M | 2 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,474 | +22 | 802,077 | 0.2% | — | 3 |
| 90 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,465 | +9 | 31,712 | 1.1% | 33.12B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,414 | +16 | 174,965 | 0.5% | 11.51B | 7 |
| 92 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,213 | +66 | 219,114 | 0.4% | 12.19B | 3 |
| 93 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,201 | +175 | 56,710 | 0.8% | 7.55B | 1 |
| 94 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,197 | +86 | 85,539 | 0.6% | 9.15B | 1 |
| 95 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,167 | -49 | 671,175 | 0.2% | 7.45B | 2 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,105 | -20 | 9,228 | 1.0% | 28.84B | 3 |
| 97 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,061 | -31 | 23,897 | 0.9% | 11.17B | 5 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,025 | -18 | 58,553 | 0.6% | 1.35B | 3 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 988 | -1 | 453,533 | 0.2% | 40.43B | 1 |
| 100 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 942 | -17 | 31,744 | 0.7% | 11.17B | 5 |
| 101 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 895 | -86 | 415,758 | 0.2% | 1.20B | 1 |
| 102 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 881 | +7 | 44,987 | 0.6% | 12.19B | 2 |
| 103 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 844 | 0 | 233,580 | 0.3% | — | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 831 | -37 | 112,448 | 0.4% | 7.29B | 2 |
| 105 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 788 | +14 | 14,709 | 0.7% | 4.33B | 3 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 768 | +11 | 2,010 | 0.8% | 27.23B | 3 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 731 | -6 | 96,492 | 0.4% | 1.35B | 8 |
| 108 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 715 | -92 | 419,087 | 0.1% | 353.4M | 1 |
| 109 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 711 | +1 | 82,150 | 0.4% | 8.03B | 3 |
| 110 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 672 | -97 | 400,589 | 0.1% | 3.21B | 1 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 665 | -7 | 16,906 | 0.6% | 1.54B | 4 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 619 | -11 | 27,939 | 0.5% | 9.24B | 2 |
| 113 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 611 | +3 | 22,142 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 581 | +8 | 20,768 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 539 | -12 | 3,621 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 508 | +7 | 4,366 | 0.5% | 8.03B | 3 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 421 | -13 | 1,625 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 420 | -2 | 12,216 | 0.4% | 27.23B | 2 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | +116 | 3,404 | 0.4% | 560.9M | 2 |
| 120 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 375 | +14 | 12,398 | 0.3% | 31.59B | 6 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 333 | +22 | 5,583 | 0.3% | 11.51B | 5 |
| 122 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 310 | -5 | 2,836 | 0.3% | 4.02B | 2 |
| 123 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 309 | +18 | 22,141 | 0.3% | 2.61B | 2 |
| 124 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 306 | -4 | 32,880 | 0.2% | 40.43B | 2 |
| 125 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 294 | -25 | 37,888 | 0.2% | 27.23B | 3 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 289 | -3 | 107,262 | 0.1% | — | 3 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 272 | -5 | 39,441 | 0.2% | 7.48B | 2 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 241 | -1 | 41,918 | 0.2% | 11.17B | 1 |
| 129 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 238 | -2 | 70,538 | 0.1% | 8.03B | 3 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 220 | -14 | 322,265 | 0.1% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 219 | -4 | 19,709 | 0.2% | 68.98B | 2 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 200 | -11 | 44,664 | 0.1% | 7.70B | 5 |
| 133 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 191 | -8 | 16,645 | 0.2% | 7.29B | 2 |
| 134 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 187 | 0 | 5,178 | 0.2% | 437.8M | 1 |
| 135 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 184 | -3 | 5,070 | 0.2% | 70.55B | 3 |
| 136 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 182 | -3 | 12,713 | 0.2% | 70.55B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 173 | -4 | 2,568 | 0.2% | — | 1 |
| 138 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | 0 | 28,426 | 0.1% | 46.70B | 6 |
| 139 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 156 | +111 | 2,967 | 0.2% | 31.59B | 6 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 147 | -2 | 5,506 | 0.1% | 353.4M | 2 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 139 | -1 | 1,165 | 0.1% | — | 1 |
| 142 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 136 | -10 | 7,476 | 0.1% | 31.59B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 91 | 0 | 38,723 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 79 | -4 | 7,256 | 0.1% | 1.20B | 2 |
| 145 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 70 | -1 | 1,317 | 0.1% | 560.9M | 1 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | -1 | 403 | 0.0% | 437.8M | 1 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 40 | -1 | 439 | 0.0% | 321.0M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 36 | -2 | 263 | 0.0% | 15.17B | 3 |
| 149 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | -2 | 204 | 0.0% | 8.16B | 3 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 230 | 0.0% | 437.8M | 1 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -2 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | -1 | 281 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | -1 | 167 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | -2 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,414,714 | 307,178,434 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 415,706 | 6,068,429 | 7 | 6.7% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 195,467 | 387,814 | 6 | 40.1% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 87,545 | 2,645,954 | 11 | 3.2% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 75,942 | 6,405,372 | 12 | 1.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 55,892 | 1,422,283 | 5 | 3.7% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,481 | 564,637 | 13 | 2.9% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 17,382 | 399,546 | 10 | 3.5% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,426 | 1,448,953 | 11 | 0.9% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,558 | 447,879 | 6 | 2.5% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,029 | 371,376 | 14 | 2.6% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,594 | 202,249 | 3 | 2.8% |
| 13 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,484 | 76,680 | 1 | 4.8% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,617 | 81,846 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,510 | 493,662 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,086 | 859,768 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,641 | 699,767 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,582 | 139,675 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,873 | 661,393 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,826 | 1,162,628 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,674 | 106,149 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,756 | 155,045 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,601 | 9,477 | 1 | 1.5% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 677 | 24,350 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,861,515 | 59,951,022 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 360,029 | 4,686,450 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 191,138 | 258,687 | 9 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 46,776 | 732,093 | 18 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 25,704 | 4,176,166 | 21 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 23,292 | 242,187 | 22 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 11,813 | 44,526 | 31 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,530 | 20,570 | 37 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,484 | 76,680 | 38 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,122 | 118,144 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,617 | 81,846 | 46 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,582 | 139,675 | 50 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,535 | 153,855 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,421 | 377,502 | 55 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,185 | 37,487 | 56 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,039 | 53,658 | 58 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,066 | 102,061 | 70 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,045 | 358,178 | 71 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,003 | 80,518 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,925 | 159,808 | 74 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,601 | 9,477 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,474 | 802,077 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,025 | 58,553 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 375 | 12,398 | 120 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 40.1% | 195,467 | 387,814 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 6.7% | 415,706 | 6,068,429 | 2 |
| 3 | [openeurollm](https://huggingface.co/openeurollm) | 4.8% | 8,484 | 76,680 | 13 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.7% | 55,892 | 1,422,283 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 3.5% | 17,382 | 399,546 | 8 |
| 6 | [utter-project](https://huggingface.co/utter-project) | 3.2% | 87,545 | 2,645,954 | 4 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,617 | 81,846 | 14 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.9% | 19,481 | 564,637 | 7 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,594 | 202,249 | 12 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.6% | 12,029 | 371,376 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,558 | 447,879 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,414,714 | 307,178,434 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,582 | 139,675 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,601 | 9,477 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,674 | 106,149 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.2% | 75,942 | 6,405,372 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,426 | 1,448,953 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,510 | 493,662 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,756 | 155,045 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,641 | 699,767 | 17 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 677 | 24,350 | 24 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,086 | 859,768 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,873 | 661,393 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,826 | 1,162,628 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
