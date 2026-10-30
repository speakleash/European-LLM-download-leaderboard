# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-30
- **Generated at:** 2026-10-30T12:27:44Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,812,856 | -27,133 | 59,438,073 | 3.0% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,798,035 | -16,675 | 66,427,202 | 2.7% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 556,631 | +9,438 | 46,258,331 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 505,934 | +15,253 | 4,204,384 | 11.8% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 406,304 | +1,114 | 4,636,751 | 8.6% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 314,168 | +3,600 | 32,662,362 | 1.0% | 46.70B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 245,967 | -22,663 | 16,626,233 | 1.5% | 12.25B | 3 |
| 8 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 216,573 | +8,246 | 2,433,571 | 8.5% | 8.92B | 6 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,883 | -9,202 | 5,806,978 | 3.5% | 4.25B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 196,585 | -11,163 | 4,956,029 | 3.9% | 24.01B | 2 |
| 11 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 193,462 | +229 | 940,072 | 18.6% | 1.66B | 1 |
| 12 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 172,830 | -33,302 | 736,919 | 20.7% | 8.90B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 160,305 | -6,700 | 3,002,498 | 5.2% | 24.01B | 1 |
| 14 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 132,577 | +11,269 | 199,455 | 44.3% | 12.77B | 5 |
| 15 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130,308 | -2,322 | 5,590,499 | 2.3% | 24.01B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 95,526 | +2,040 | 7,676,340 | 1.2% | 23.57B | 2 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,604 | +260 | 798,076 | 7.8% | 23.57B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,317 | -1,709 | 734,775 | 8.2% | 119.40B | 3 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,522 | -835 | 11,274,218 | 0.6% | 140.63B | 2 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 51,864 | +2,158 | 8,569,653 | 0.6% | 8.02B | 1 |
| 21 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 42,985 | +940 | 722,689 | 5.2% | 7.77B | 8 |
| 22 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 34,654 | +261 | 361,331 | 7.5% | 24.01B | 2 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 27,545 | +229 | 1,115,270 | 2.3% | 127.70B | 2 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,282 | -64 | 240,233 | 8.0% | — | 1 |
| 25 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,554 | +16 | 44,200 | 17.0% | 12.25B | 3 |
| 26 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,277 | -18 | 4,166,623 | 0.5% | 11.34B | 8 |
| 27 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,329 | -492 | 549,039 | 2.7% | 70.60B | 2 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,230 | +249 | 647,043 | 2.0% | 23.57B | 2 |
| 29 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,952 | +137 | 792,157 | 1.6% | 11.25B | 10 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,668 | +49 | 5,045,873 | 0.2% | 122.61B | 1 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,093 | -44 | 157,859 | 4.7% | 9.15B | 1 |
| 32 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,697 | -97 | 20,281 | 9.7% | 27.43B | 3 |
| 33 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,302 | +339 | 4,937,220 | 0.2% | 122.61B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,068 | -4 | 519,461 | 1.8% | 7.24B | 8 |
| 35 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,755 | +44 | 492,662 | 1.8% | 9.15B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,102 | -274 | 83,894 | 5.5% | — | 5 |
| 37 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,683 | +236 | 5,386,669 | 0.2% | 22.25B | 1 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,626 | -43 | 33,897 | 6.4% | 72.01B | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,220 | -8,711 | 601,496 | 1.2% | 22.64B | 1 |
| 40 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,146 | -209 | 76,277 | 4.6% | — | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,885 | +40 | 116,040 | 3.2% | 8.42B | 7 |
| 42 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,441 | -251 | 20,678 | 5.3% | 572.6M | 5 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,275 | -37 | 150,542 | 2.5% | 2.25B | 7 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,090 | +36 | 355,561 | 1.3% | 125.03B | 1 |
| 45 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,701 | -328 | 139,316 | 2.4% | 7.48B | 5 |
| 46 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,583 | +244 | 13,671 | 4.9% | 1.51B | 6 |
| 47 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,514 | +15 | 81,635 | 3.0% | 7.04B | 4 |
| 48 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,753 | -55 | 138,674 | 2.0% | 7.40B | 3 |
| 49 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,730 | +250 | 19,612 | 4.0% | 3.83B | 5 |
| 50 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,456 | +41 | 376,530 | 0.9% | 7.24B | 8 |
| 51 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,446 | +136 | 5,163,690 | 0.1% | 22.25B | 1 |
| 52 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,444 | +20 | 152,843 | 1.8% | 7.24B | 4 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,375 | +187 | 909,158 | 0.4% | 23.57B | 2 |
| 54 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,289 | -76 | 168,835 | 1.6% | 11.17B | 16 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,102 | +322 | 256,896 | 1.1% | 4.76B | 5 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,967 | +55 | 61,766 | 2.5% | 1.60B | 5 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,941 | +7 | 39,385 | 2.8% | 2.61B | 3 |
| 58 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,701 | +214 | 36,381 | 2.7% | 56.7M | 1 |
| 59 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,178 | -72 | 52,409 | 2.1% | 8.03B | 7 |
| 60 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,122 | +5 | 94,898 | 1.6% | 2.89B | 1 |
| 61 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,826 | -8 | 42,712 | 2.0% | 13.29B | 3 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,707 | +17 | 26,087 | 2.1% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,692 | +9 | 34,349 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,574 | +142 | 5,303,172 | 0.0% | 7.25B | 1 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,569 | -1,257 | 156,801 | 1.0% | 23.57B | 2 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,488 | +25 | 179,145 | 0.9% | 12.25B | 6 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,262 | +19 | 51,759 | 1.5% | 7.77B | 1 |
| 68 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,152 | +56 | 22,144 | 1.8% | 4.30B | 2 |
| 69 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,079 | +43 | 229,976 | 0.6% | 35.13B | 4 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,042 | +14 | 51,115 | 1.4% | 9.24B | 4 |
| 71 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,957 | +17 | 357,724 | 0.4% | — | 3 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,946 | -24 | 101,560 | 1.0% | 30.68B | 1 |
| 73 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,942 | -152 | 415,578 | 0.4% | 1.20B | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,927 | +11 | 80,049 | 1.1% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,869 | +9 | 107,651 | 0.9% | 7.45B | 1 |
| 76 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,772 | -7 | 9,181 | 1.6% | 4.30B | 3 |
| 77 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,768 | +11 | 34,359 | 1.3% | 22.64B | 1 |
| 78 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,760 | +21 | 159,311 | 0.7% | 1.10B | 1 |
| 79 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,744 | -133 | 418,898 | 0.3% | 353.4M | 1 |
| 80 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,736 | +13 | 302,790 | 0.4% | 6.74B | 2 |
| 81 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,721 | -151 | 400,419 | 0.3% | 3.21B | 1 |
| 82 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,706 | +26 | 186,113 | 0.6% | 6.74B | 1 |
| 83 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,676 | +20 | 146,882 | 0.7% | 13.02B | 1 |
| 84 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,601 | -171 | 19,531 | 1.3% | 12.19B | 2 |
| 85 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,569 | +29 | 40,370 | 1.1% | 70.55B | 3 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,554 | +6 | 54,177 | 1.0% | 7.24B | 5 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,486 | +10 | 52,966 | 1.0% | 7.24B | 1 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,446 | +20 | 9,138 | 1.3% | 9.82B | 1 |
| 89 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,365 | -95 | 670,973 | 0.2% | 7.45B | 2 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,353 | -35 | 174,673 | 0.5% | 11.51B | 7 |
| 91 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,335 | 0 | 31,467 | 1.0% | 33.12B | 1 |
| 92 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,332 | +37 | 801,717 | 0.1% | — | 3 |
| 93 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,290 | -33 | 23,718 | 1.0% | 11.17B | 5 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,203 | +5 | 19,930 | 1.0% | 1.20B | 2 |
| 95 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,123 | -7 | 10,531 | 1.0% | 9.15B | 1 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,084 | -23 | 31,584 | 0.8% | 11.17B | 5 |
| 97 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,080 | +7 | 9,119 | 1.0% | 28.84B | 3 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,051 | +10 | 58,319 | 0.7% | 1.35B | 3 |
| 99 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,027 | +34 | 15,250 | 0.9% | 353.4M | 2 |
| 100 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,012 | -62 | 56,288 | 0.6% | 7.55B | 1 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 920 | +11 | 453,310 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 855 | +5 | 218,696 | 0.3% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 830 | +18 | 44,834 | 0.6% | 12.19B | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 758 | -4 | 112,083 | 0.4% | 7.29B | 2 |
| 105 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 712 | +15 | 14,528 | 0.6% | 4.33B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 695 | +15 | 82,003 | 0.4% | 8.03B | 3 |
| 107 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 655 | +103 | 233,287 | 0.2% | — | 2 |
| 108 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 637 | -2 | 16,771 | 0.5% | 1.54B | 4 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 627 | +2 | 96,279 | 0.3% | 1.35B | 8 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 614 | +53 | 20,647 | 0.5% | 3.20B | 2 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 556 | +49 | 22,001 | 0.5% | 9.24B | 2 |
| 112 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 505 | -14 | 3,491 | 0.5% | 30.68B | 1 |
| 113 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 497 | 0 | 1,731 | 0.5% | 27.23B | 3 |
| 114 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 486 | +79 | 27,724 | 0.4% | 9.24B | 2 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 474 | -19 | 4,268 | 0.5% | 8.03B | 3 |
| 116 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 422 | -2 | 1,556 | 0.4% | — | 1 |
| 117 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 374 | -1 | 32,855 | 0.3% | 40.43B | 2 |
| 118 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 367 | -3 | 2,815 | 0.4% | 4.02B | 2 |
| 119 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 363 | +45 | 12,094 | 0.3% | 27.23B | 2 |
| 120 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 337 | +7 | 5,515 | 0.3% | 11.51B | 5 |
| 121 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 336 | +5 | 22,076 | 0.3% | 2.61B | 2 |
| 122 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 314 | -3 | 84,553 | 0.2% | 9.15B | 1 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 306 | -1 | 107,207 | 0.1% | — | 3 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 292 | -1 | 39,379 | 0.2% | 7.48B | 2 |
| 125 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 290 | -10 | 322,227 | 0.1% | 7.24B | 2 |
| 126 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 284 | -22 | 37,800 | 0.2% | 27.23B | 3 |
| 127 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 271 | -1 | 5,151 | 0.3% | 437.8M | 1 |
| 128 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 230 | +8 | 44,644 | 0.2% | 7.70B | 5 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 229 | +10 | 41,880 | 0.2% | 11.17B | 1 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 229 | -7 | 19,667 | 0.2% | 68.98B | 2 |
| 131 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 216 | -7 | 12,701 | 0.2% | 70.55B | 2 |
| 132 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 211 | 0 | 5,046 | 0.2% | 70.55B | 3 |
| 133 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 191 | +5 | 16,601 | 0.2% | 7.29B | 2 |
| 134 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 191 | -4 | 2,539 | 0.2% | — | 1 |
| 135 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 191 | +14 | 70,461 | 0.1% | 8.03B | 3 |
| 136 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 182 | -1 | 7,461 | 0.2% | 31.59B | 6 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 174 | -3 | 5,495 | 0.2% | 353.4M | 2 |
| 138 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 155 | 0 | 3,133 | 0.2% | 560.9M | 2 |
| 139 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 150 | -6 | 28,394 | 0.1% | 46.70B | 6 |
| 140 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 142 | 0 | 12,151 | 0.1% | 31.59B | 6 |
| 141 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 6,171 | 0.1% | 12.25B | 3 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 135 | +2 | 1,144 | 0.1% | — | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 101 | -2 | 7,249 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 93 | -5 | 38,709 | 0.1% | 70.55B | 3 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 80 | -1 | 432 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 78 | +9 | 1,313 | 0.1% | 560.9M | 1 |
| 147 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | +3 | 400 | 0.0% | 437.8M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,854 | 0.0% | 31.59B | 6 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | -1 | 221 | 0.0% | 437.8M | 1 |
| 150 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | -8 | 254 | 0.0% | 15.17B | 3 |
| 151 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 28 | -6 | 193 | 0.0% | 8.16B | 3 |
| 152 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | +1 | 132 | 0.0% | 7.24B | 1 |
| 153 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 275 | 0.0% | 437.8M | 1 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 158 | 0.0% | 437.8M | 1 |
| 155 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 6 | 0 | 1,503 | 0.0% | 31.58B | 2 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,634,873 | 305,927,604 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 621,843 | 6,010,567 | 7 | 10.2% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 261,856 | 2,629,776 | 11 | 9.6% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 136,651 | 327,519 | 6 | 32.0% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 67,649 | 6,382,424 | 12 | 1.0% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 52,816 | 1,411,155 | 5 | 3.5% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,285 | 398,276 | 10 | 6.1% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,617 | 561,712 | 13 | 3.3% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,214 | 1,444,347 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 11,865 | 444,859 | 6 | 2.2% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,609 | 368,490 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,146 | 76,277 | 1 | 4.6% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,407 | 200,063 | 3 | 2.5% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,514 | 81,635 | 1 | 3.0% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,161 | 858,673 | 3 | 0.5% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,142 | 492,306 | 3 | 0.9% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,753 | 138,674 | 1 | 2.0% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,746 | 698,757 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,693 | 660,514 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,522 | 1,161,878 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,510 | 105,498 | 4 | 1.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,678 | 154,598 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,446 | 9,138 | 1 | 1.3% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 373 | 23,969 | 4 | 0.3% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,812,856 | 59,438,073 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 406,304 | 4,636,751 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 193,462 | 940,072 | 11 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 132,577 | 199,455 | 14 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 42,985 | 722,689 | 21 |
| 6 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,554 | 44,200 | 25 |
| 7 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,277 | 4,166,623 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,697 | 20,281 | 32 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,146 | 76,277 | 40 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,885 | 116,040 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,514 | 81,635 | 47 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,753 | 138,674 | 48 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,456 | 376,530 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,444 | 152,843 | 52 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,701 | 36,381 | 58 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,178 | 52,409 | 59 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,957 | 357,724 | 71 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,946 | 101,560 | 72 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,927 | 80,049 | 74 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,760 | 159,311 | 78 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,446 | 9,138 | 88 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,332 | 801,717 | 92 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,051 | 58,319 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 182 | 7,461 | 136 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 32.0% | 136,651 | 327,519 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 10.2% | 621,843 | 6,010,567 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 9.6% | 261,856 | 2,629,776 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,285 | 398,276 | 7 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | 4.6% | 8,146 | 76,277 | 12 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.5% | 52,816 | 1,411,155 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,617 | 561,712 | 8 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,514 | 81,635 | 14 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,609 | 368,490 | 11 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,407 | 200,063 | 13 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.2% | 11,865 | 444,859 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,634,873 | 305,927,604 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.0% | 4,753 | 138,674 | 17 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,446 | 9,138 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,510 | 105,498 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.0% | 67,649 | 6,382,424 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,214 | 1,444,347 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,142 | 492,306 | 16 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,678 | 154,598 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,746 | 698,757 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,161 | 858,673 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,693 | 660,514 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.3% | 373 | 23,969 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,522 | 1,161,878 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
