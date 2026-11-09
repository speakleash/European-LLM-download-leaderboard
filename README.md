# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-09
- **Generated at:** 2026-11-09T15:42:06Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,952,129 | +18,976 | 60,301,868 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,469,560 | -44,635 | 66,739,306 | 2.2% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 631,893 | +13,142 | 4,438,368 | 13.9% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 516,975 | +1,702 | 46,440,555 | 1.1% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 341,693 | +5,085 | 32,774,060 | 1.0% | 46.70B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 303,608 | -17,310 | 4,689,642 | 6.3% | 8.05B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,869 | +355 | 2,527,249 | 9.6% | 8.92B | 6 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 227,248 | +8,671 | 295,479 | 57.5% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 204,061 | -1,644 | 5,879,056 | 3.4% | 3.85B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 161,503 | -2,742 | 5,004,806 | 3.2% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 157,290 | +2,164 | 16,660,014 | 0.9% | 12.25B | 3 |
| 12 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 107,248 | -352 | 7,715,248 | 1.4% | 23.57B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,133 | -1,149 | 5,617,980 | 1.8% | 24.01B | 1 |
| 14 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 60,138 | -640 | 8,599,987 | 0.7% | 8.02B | 1 |
| 15 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 59,177 | -25,184 | 3,009,228 | 1.9% | 24.01B | 1 |
| 16 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 53,664 | +9,542 | 4,206,587 | 1.2% | 11.34B | 8 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 53,269 | -1,907 | 806,469 | 5.9% | 23.57B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,598 | +373 | 735,257 | 5.5% | 7.77B | 8 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,474 | +42 | 11,285,884 | 0.4% | 140.63B | 2 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,801 | +39 | 366,060 | 7.0% | 24.01B | 2 |
| 21 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,756 | -577 | 743,225 | 3.9% | 119.40B | 3 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,628 | -307 | 245,222 | 7.1% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,557 | -307 | 945,088 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,892 | -223 | 1,119,813 | 1.4% | 127.70B | 2 |
| 25 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,421 | +1 | 799,140 | 1.8% | 11.25B | 10 |
| 26 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 14,594 | -896 | 739,948 | 1.7% | 8.90B | 1 |
| 27 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,263 | +127 | 4,943,538 | 0.3% | 122.61B | 1 |
| 28 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,765 | +8 | 5,047,016 | 0.2% | 122.61B | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,519 | -53 | 650,241 | 1.7% | 23.57B | 2 |
| 30 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 11,671 | -531 | 550,798 | 1.8% | 70.60B | 2 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,329 | -171 | 159,987 | 4.4% | 9.15B | 1 |
| 32 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,174 | -76 | 523,492 | 1.8% | 7.24B | 8 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,540 | -213 | 496,625 | 1.8% | 9.15B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,382 | +63 | 22,582 | 8.5% | 27.43B | 3 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,906 | +77 | 5,390,134 | 0.2% | 22.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,593 | -67 | 86,428 | 4.6% | — | 5 |
| 37 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,496 | +564 | 119,237 | 3.9% | 8.42B | 7 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,184 | -46 | 35,087 | 6.1% | 72.01B | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,106 | -214 | 603,901 | 1.0% | 22.64B | 1 |
| 40 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,703 | +11 | 15,961 | 5.8% | 1.51B | 6 |
| 41 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,609 | +61 | 357,788 | 1.4% | 125.03B | 1 |
| 42 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,971 | +177 | 259,993 | 1.7% | 4.76B | 5 |
| 43 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,789 | +179 | 21,311 | 4.8% | 3.83B | 5 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,607 | -1 | 81,973 | 3.1% | 7.04B | 4 |
| 45 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5,483 | -788 | 44,703 | 3.8% | 12.25B | 3 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,251 | +60 | 55,160 | 3.4% | 8.03B | 7 |
| 47 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,119 | +117 | 22,330 | 4.2% | 572.6M | 5 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,072 | -41 | 151,926 | 2.0% | 2.25B | 7 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,693 | +54 | 910,380 | 0.5% | 23.57B | 2 |
| 50 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,603 | +187 | 63,575 | 2.8% | 1.60B | 5 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,511 | -33 | 154,447 | 1.8% | 7.24B | 4 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,420 | -62 | 140,156 | 1.8% | 7.40B | 3 |
| 53 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,301 | -96 | 378,008 | 0.9% | 7.24B | 8 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,193 | +1 | 40,712 | 3.0% | 2.61B | 3 |
| 55 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,149 | +2 | 140,872 | 1.7% | 7.48B | 5 |
| 56 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,064 | -40 | 37,847 | 2.9% | 56.7M | 1 |
| 57 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,026 | -51 | 5,165,328 | 0.1% | 22.25B | 1 |
| 58 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,762 | -40 | 44,510 | 2.6% | 13.29B | 3 |
| 59 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,748 | -60 | 28,313 | 2.9% | 22.64B | 1 |
| 60 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,427 | -85 | 169,749 | 1.3% | 11.17B | 16 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,288 | -28 | 96,140 | 1.7% | 2.89B | 1 |
| 62 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,994 | -251 | 12,922 | 2.7% | 9.15B | 1 |
| 63 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,737 | +16 | 5,303,799 | 0.1% | 7.25B | 1 |
| 64 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,659 | -114 | 34,603 | 2.0% | 14.03B | 1 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,578 | +13 | 157,155 | 1.0% | 23.57B | 2 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,576 | -13 | 179,805 | 0.9% | 12.25B | 6 |
| 67 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,411 | +33 | 230,790 | 0.7% | 35.13B | 4 |
| 68 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,231 | -8 | 20,514 | 1.9% | 12.19B | 2 |
| 69 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,166 | -6 | 86,589 | 1.2% | 9.15B | 1 |
| 70 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,097 | -2 | 102,333 | 1.0% | 30.68B | 1 |
| 71 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,062 | -7 | 358,452 | 0.4% | — | 3 |
| 72 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,044 | -252 | 52,422 | 1.3% | 7.77B | 1 |
| 73 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,033 | -53 | 22,712 | 1.7% | 4.30B | 2 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,025 | +6 | 80,803 | 1.1% | 7.45B | 1 |
| 75 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,022 | -10 | 51,827 | 1.3% | 9.24B | 4 |
| 76 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,972 | +7 | 160,087 | 0.8% | 1.10B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,936 | 0 | 108,339 | 0.9% | 7.45B | 1 |
| 78 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,864 | +1 | 303,475 | 0.5% | 6.74B | 2 |
| 79 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,863 | +8 | 35,028 | 1.4% | 22.64B | 1 |
| 80 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,855 | +5 | 186,813 | 0.6% | 6.74B | 1 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,794 | +9 | 147,537 | 0.7% | 13.02B | 1 |
| 82 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,783 | +6 | 40,979 | 1.3% | 70.55B | 3 |
| 83 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,638 | +5 | 9,643 | 1.5% | 9.82B | 1 |
| 84 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,581 | -5 | 54,736 | 1.0% | 7.24B | 5 |
| 85 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,559 | -88 | 9,626 | 1.4% | 4.30B | 3 |
| 86 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,520 | +3 | 802,265 | 0.2% | — | 3 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,515 | -8 | 53,503 | 1.0% | 7.24B | 1 |
| 88 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,504 | -19 | 20,733 | 1.2% | 1.20B | 2 |
| 89 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,386 | -24 | 15,988 | 1.2% | 353.4M | 2 |
| 90 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,292 | -157 | 31,784 | 1.0% | 33.12B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,255 | -24 | 175,079 | 0.5% | 11.51B | 7 |
| 92 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,196 | -10 | 219,182 | 0.4% | 12.19B | 3 |
| 93 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,129 | -56 | 56,799 | 0.7% | 7.55B | 1 |
| 94 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,079 | -34 | 9,283 | 1.0% | 28.84B | 3 |
| 95 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,006 | -4 | 58,666 | 0.6% | 1.35B | 3 |
| 96 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,003 | +48 | 416,043 | 0.2% | 1.20B | 1 |
| 97 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 996 | -40 | 671,283 | 0.1% | 7.45B | 2 |
| 98 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 988 | -1 | 453,657 | 0.2% | 40.43B | 1 |
| 99 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 961 | +42 | 45,105 | 0.7% | 12.19B | 2 |
| 100 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 956 | -95 | 24,012 | 0.8% | 11.17B | 5 |
| 101 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 905 | +9 | 419,442 | 0.2% | 353.4M | 1 |
| 102 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 845 | -37 | 31,809 | 0.6% | 11.17B | 5 |
| 103 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 837 | +1 | 233,627 | 0.3% | — | 2 |
| 104 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 803 | +14 | 2,090 | 0.8% | 27.23B | 3 |
| 105 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 801 | +14 | 96,605 | 0.4% | 1.35B | 8 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 779 | -14 | 14,738 | 0.7% | 4.33B | 3 |
| 107 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 772 | +12 | 400,862 | 0.2% | 3.21B | 1 |
| 108 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 771 | -29 | 112,490 | 0.4% | 7.29B | 2 |
| 109 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 716 | +6 | 82,239 | 0.4% | 8.03B | 3 |
| 110 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 698 | +11 | 17,010 | 0.6% | 1.54B | 4 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 616 | -11 | 22,188 | 0.5% | 9.24B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 606 | +8 | 28,000 | 0.5% | 9.24B | 2 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 598 | +9 | 20,838 | 0.5% | 3.20B | 2 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 548 | -7 | 3,686 | 0.5% | 30.68B | 1 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 513 | -23 | 4,454 | 0.5% | 8.03B | 3 |
| 116 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 433 | -6 | 1,693 | 0.4% | — | 1 |
| 117 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 431 | -5 | 12,241 | 0.4% | 27.23B | 2 |
| 118 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 428 | -1 | 12,461 | 0.4% | 31.59B | 6 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 356 | -17 | 3,411 | 0.3% | 560.9M | 2 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 342 | +4 | 22,192 | 0.3% | 2.61B | 2 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 323 | -2 | 5,617 | 0.3% | 11.51B | 5 |
| 122 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 308 | +3 | 2,858 | 0.3% | 4.02B | 2 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 290 | -7 | 107,314 | 0.1% | — | 3 |
| 124 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 286 | -5 | 32,904 | 0.2% | 40.43B | 2 |
| 125 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 276 | -1 | 37,898 | 0.2% | 27.23B | 3 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 263 | -16 | 39,459 | 0.2% | 7.48B | 2 |
| 127 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 254 | -1 | 70,586 | 0.1% | 8.03B | 3 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 224 | -11 | 41,954 | 0.2% | 11.17B | 1 |
| 129 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 221 | +1 | 322,307 | 0.1% | 7.24B | 2 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 207 | -5 | 19,726 | 0.2% | 68.98B | 2 |
| 131 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 196 | 0 | 16,679 | 0.2% | 7.29B | 2 |
| 132 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | 0 | 3,002 | 0.2% | 31.59B | 6 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 184 | -6 | 44,682 | 0.1% | 7.70B | 5 |
| 134 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 179 | -7 | 12,731 | 0.2% | 70.55B | 2 |
| 135 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 164 | +10 | 1,194 | 0.2% | — | 1 |
| 136 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 158 | -2 | 28,449 | 0.1% | 46.70B | 6 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 156 | -5 | 2,579 | 0.2% | — | 1 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 144 | 0 | 5,524 | 0.1% | 353.4M | 2 |
| 139 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 134 | 0 | 5,194 | 0.1% | 437.8M | 1 |
| 140 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 127 | -27 | 5,081 | 0.1% | 70.55B | 3 |
| 141 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 124 | -1 | 7,490 | 0.1% | 31.59B | 6 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 83 | -1 | 38,728 | 0.1% | 70.55B | 3 |
| 143 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 69 | -3 | 1,323 | 0.1% | 560.9M | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 67 | -5 | 7,266 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 40 | 0 | 443 | 0.0% | 321.0M | 1 |
| 146 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 40 | +2 | 267 | 0.0% | 15.17B | 3 |
| 147 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 40 | +2 | 211 | 0.0% | 8.16B | 3 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | -3 | 408 | 0.0% | 437.8M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 38 | -1 | 242 | 0.0% | 437.8M | 1 |
| 150 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | +1 | 177 | 0.0% | 437.8M | 1 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | 0 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 288 | 0.0% | 437.8M | 1 |
| 153 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 154 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 155 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 156 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 0 | -8,485 | 0 | 0.0% | — | 0 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,278,147 | 308,043,870 | 30 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 355,668 | 6,075,077 | 7 | 5.8% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 231,645 | 425,142 | 6 | 44.1% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 103,012 | 6,441,879 | 12 | 1.6% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 88,280 | 2,656,966 | 11 | 3.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 53,988 | 1,426,166 | 5 | 3.5% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,623 | 567,906 | 13 | 3.2% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,525 | 450,115 | 6 | 2.6% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,363 | 1,450,897 | 11 | 0.9% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,920 | 372,880 | 14 | 2.5% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 10,936 | 400,334 | 10 | 2.2% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,943 | 203,378 | 3 | 2.9% |
| 13 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,621 | 494,437 | 3 | 0.9% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,607 | 81,973 | 1 | 3.1% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,957 | 860,425 | 3 | 0.5% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,522 | 700,315 | 2 | 0.6% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,420 | 140,156 | 1 | 1.8% |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,926 | 661,927 | 2 | 0.5% |
| 19 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,854 | 1,162,932 | 4 | 0.2% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,725 | 106,497 | 4 | 1.3% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,807 | 155,271 | 2 | 0.7% |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,638 | 9,643 | 1 | 1.5% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 747 | 24,462 | 4 | 0.6% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,952,129 | 60,301,868 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 303,608 | 4,689,642 | 6 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 227,248 | 295,479 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 53,664 | 4,206,587 | 16 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,598 | 735,257 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 24,628 | 245,222 | 22 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,382 | 22,582 | 34 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,496 | 119,237 | 37 |
| 9 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,607 | 81,973 | 44 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 5,483 | 44,703 | 45 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,251 | 55,160 | 46 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,511 | 154,447 | 51 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,420 | 140,156 | 52 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,301 | 378,008 | 53 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,064 | 37,847 | 56 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,097 | 102,333 | 70 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,062 | 358,452 | 71 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,025 | 80,803 | 74 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,972 | 160,087 | 76 |
| 20 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,638 | 9,643 | 83 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,520 | 802,265 | 86 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,006 | 58,666 | 95 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 428 | 12,461 | 118 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 156 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 44.1% | 231,645 | 425,142 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 5.8% | 355,668 | 6,075,077 | 2 |
| 3 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.5% | 53,988 | 1,426,166 | 6 |
| 4 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 21,623 | 567,906 | 7 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.2% | 88,280 | 2,656,966 | 5 |
| 6 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,607 | 81,973 | 14 |
| 7 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,943 | 203,378 | 12 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,525 | 450,115 | 8 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,920 | 372,880 | 10 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.2% | 10,936 | 400,334 | 11 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,278,147 | 308,043,870 | 1 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.8% | 4,420 | 140,156 | 17 |
| 13 | [speakleash](https://huggingface.co/speakleash) | 1.6% | 103,012 | 6,441,879 | 4 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,638 | 9,643 | 22 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,725 | 106,497 | 20 |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,621 | 494,437 | 13 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,363 | 1,450,897 | 9 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,807 | 155,271 | 21 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 747 | 24,462 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,522 | 700,315 | 16 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,957 | 860,425 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,926 | 661,927 | 18 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,854 | 1,162,932 | 19 |
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
