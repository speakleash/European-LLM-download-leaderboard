# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-29
- **Generated at:** 2026-09-29T12:27:46Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,383,022 | -8,569 | 57,444,120 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,647,928 | -41,140 | 64,524,747 | 2.5% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 582,963 | -6,613 | 45,680,866 | 1.3% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 549,841 | -27,818 | 3,680,289 | 14.5% | 13.95B | 6 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 519,356 | +8,201 | 4,725,231 | 10.8% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 502,312 | -2,625 | 4,200,483 | 11.7% | 8.05B | 2 |
| 7 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 487,916 | +32,137 | 502,878 | 80.9% | 8.90B | 1 |
| 8 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 467,091 | -370 | 16,326,898 | 2.8% | 12.25B | 3 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 374,181 | +13,062 | 572,586 | 55.6% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 310,350 | +1,961 | 2,827,244 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 285,208 | +3,195 | 5,576,602 | 5.0% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 267,471 | +1,353 | 32,327,981 | 0.8% | 46.70B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 246,628 | +40,654 | 5,445,768 | 4.4% | 24.01B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 227,095 | +6,025 | 2,203,649 | 9.9% | 8.92B | 6 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,858 | +612 | 8,510,141 | 1.8% | 8.02B | 1 |
| 16 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 150,466 | -9,015 | 4,144,641 | 3.5% | 11.34B | 8 |
| 17 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 148,450 | -28,601 | 416,964 | 28.7% | 353.4M | 1 |
| 18 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 148,092 | -28,302 | 413,438 | 28.8% | 1.20B | 1 |
| 19 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 145,737 | -26,869 | 398,447 | 29.2% | 3.21B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 132,052 | +7,638 | 1,084,253 | 11.2% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 95,725 | +117 | 530,384 | 15.2% | 70.60B | 2 |
| 22 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,363 | -399 | 723,721 | 8.8% | 23.57B | 2 |
| 23 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 65,938 | +15,861 | 67,835 | 39.3% | — | 1 |
| 24 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 58,109 | +229 | 746,049 | 6.9% | 1.66B | 1 |
| 25 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,190 | +1,168 | 7,575,154 | 0.7% | 23.57B | 2 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 53,423 | +1,807 | 661,354 | 7.0% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,374 | +939 | 11,205,182 | 0.4% | 140.63B | 2 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 41,230 | -7,917 | 631,326 | 5.6% | 23.57B | 2 |
| 29 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,023 | +1,271 | 678,310 | 4.1% | 7.77B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,286 | -379 | 143,993 | 11.2% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,486 | -42 | 5,158,971 | 0.4% | 22.25B | 1 |
| 32 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,116 | -646 | 481,011 | 3.1% | 9.15B | 1 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,812 | +86 | 25,139 | 14.2% | 72.01B | 1 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,741 | -399 | 777,343 | 1.8% | 11.25B | 10 |
| 35 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,107 | -23 | 212,302 | 4.8% | — | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,255 | +229 | 72,498 | 8.3% | — | 5 |
| 37 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,486 | +26 | 5,300,474 | 0.2% | 7.25B | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,994 | +281 | 507,635 | 2.0% | 7.24B | 8 |
| 39 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,183 | -96 | 349,124 | 2.5% | 125.03B | 1 |
| 40 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,426 | -2,172 | 326,196 | 2.2% | 24.01B | 2 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,016 | +834 | 132,362 | 3.9% | 7.48B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,490 | +227 | 4,925,202 | 0.1% | 122.61B | 1 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,029 | -367 | 108,925 | 3.4% | 8.42B | 7 |
| 44 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,693 | -10 | 30,084 | 4.4% | 33.12B | 1 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,492 | +11 | 48,450 | 3.7% | 8.03B | 7 |
| 46 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,345 | -18 | 164,182 | 2.0% | 11.17B | 16 |
| 47 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,053 | -26 | 111,286 | 2.4% | 7.29B | 2 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,601 | +127 | 66,632 | 2.8% | 12.77B | 5 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,501 | +33 | 143,798 | 1.8% | 2.25B | 7 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,451 | +143 | 5,377,240 | 0.1% | 22.25B | 1 |
| 51 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,328 | +136 | 133,551 | 1.9% | 7.40B | 3 |
| 52 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,301 | -24 | 904,597 | 0.4% | 23.57B | 2 |
| 53 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,282 | +99 | 669,346 | 0.6% | 7.45B | 2 |
| 54 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,224 | -5 | 55,100 | 2.7% | 7.55B | 1 |
| 55 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,156 | +32 | 371,796 | 0.9% | 7.24B | 8 |
| 56 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,082 | -50 | 252,573 | 1.2% | 4.76B | 5 |
| 57 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,803 | +34 | 91,573 | 2.0% | 2.89B | 1 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,640 | -7 | 31,623 | 2.8% | 14.03B | 1 |
| 59 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,501 | +38 | 152,848 | 1.4% | 23.57B | 2 |
| 60 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,424 | +95 | 66,104 | 2.1% | 14.08B | 1 |
| 61 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,416 | +844 | 5,032,781 | 0.1% | 122.61B | 1 |
| 62 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,333 | +286 | 13,592 | 2.9% | 572.6M | 5 |
| 63 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,251 | +59 | 148,116 | 1.3% | 7.24B | 4 |
| 64 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,112 | +106 | 35,242 | 2.3% | 2.61B | 3 |
| 65 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,808 | +129 | 57,628 | 1.8% | 1.60B | 5 |
| 66 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,517 | -149 | 84,223 | 1.4% | 9.15B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,322 | +112 | 39,679 | 1.7% | 321.0M | 2 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,169 | +43 | 48,967 | 1.5% | 9.24B | 4 |
| 69 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,086 | +29 | 32,494 | 1.6% | 22.64B | 1 |
| 70 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,066 | -65 | 7,993 | 1.9% | 1.51B | 6 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,961 | +43 | 78,005 | 1.1% | 7.45B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,935 | +63 | 23,228 | 1.6% | 22.64B | 1 |
| 73 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,850 | -3 | 14,766 | 1.6% | 3.83B | 5 |
| 74 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,845 | +89 | 85,030 | 1.0% | 2.22B | 1 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,784 | +10 | 452,344 | 0.3% | 40.43B | 1 |
| 76 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,772 | +141 | 17,478 | 1.5% | 12.19B | 2 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,764 | +53 | 105,674 | 0.9% | 7.45B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,695 | +17 | 99,466 | 0.8% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,640 | +27 | 355,655 | 0.4% | — | 3 |
| 80 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,612 | +16 | 176,559 | 0.6% | 12.25B | 6 |
| 81 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,603 | 0 | 49,376 | 1.1% | 7.77B | 1 |
| 82 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,525 | -14 | 22,322 | 1.2% | 11.17B | 5 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,522 | +32 | 157,453 | 0.6% | 1.10B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,482 | +48 | 300,945 | 0.4% | 6.74B | 2 |
| 85 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,426 | +31 | 145,109 | 0.6% | 13.02B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,422 | +30 | 184,313 | 0.5% | 6.74B | 1 |
| 87 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,393 | +12 | 173,200 | 0.5% | 11.51B | 7 |
| 88 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,383 | +3 | 12,009 | 1.2% | 31.59B | 6 |
| 89 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,375 | +29 | 30,424 | 1.1% | 11.17B | 5 |
| 90 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,315 | +38 | 9,377 | 1.2% | 9.15B | 1 |
| 91 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,313 | +61 | 7,591 | 1.2% | 9.82B | 1 |
| 92 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,277 | +72 | 32,534 | 1.0% | 56.7M | 1 |
| 93 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,248 | +26 | 19,867 | 1.0% | 4.30B | 2 |
| 94 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,246 | 0 | 57,201 | 0.8% | 1.35B | 3 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,154 | -15 | 19,575 | 1.0% | 12.25B | 3 |
| 96 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,095 | -8 | 95,630 | 0.6% | 1.35B | 8 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,048 | +17 | 227,810 | 0.3% | 35.13B | 4 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,026 | -24 | 800,330 | 0.1% | — | 3 |
| 99 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,022 | +22 | 8,002 | 0.9% | 28.84B | 3 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,008 | -55 | 7,337 | 0.9% | 4.30B | 3 |
| 101 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 985 | +125 | 18,698 | 0.8% | 1.20B | 2 |
| 102 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 981 | +22 | 52,529 | 0.6% | 7.24B | 5 |
| 103 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 981 | +1 | 2,828 | 1.0% | 31.59B | 6 |
| 104 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 972 | +2 | 8,365 | 0.9% | 27.43B | 3 |
| 105 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 907 | -1 | 37,475 | 0.7% | 27.23B | 3 |
| 106 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 891 | +96 | 14,192 | 0.8% | 353.4M | 2 |
| 107 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 889 | +25 | 51,391 | 0.6% | 7.24B | 1 |
| 108 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 865 | +20 | 38,689 | 0.6% | 70.55B | 3 |
| 109 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 835 | 0 | 81,271 | 0.5% | 8.03B | 3 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 762 | +4 | 20,016 | 0.6% | 3.20B | 2 |
| 111 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 671 | +2 | 43,989 | 0.5% | 12.19B | 2 |
| 112 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 658 | +19 | 15,962 | 0.6% | 1.54B | 4 |
| 113 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 623 | -22 | 70,255 | 0.4% | 8.03B | 3 |
| 114 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 575 | -19 | 217,817 | 0.2% | 12.19B | 3 |
| 115 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 542 | -10 | 232,619 | 0.2% | — | 2 |
| 116 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 534 | -85 | 2,947 | 0.5% | 30.68B | 1 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 528 | -22 | 2,964 | 0.5% | 560.9M | 2 |
| 118 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 526 | +68 | 1,398 | 0.5% | 31.58B | 2 |
| 119 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 493 | -32 | 3,720 | 0.5% | 8.03B | 3 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 486 | -24 | 32,460 | 0.4% | 40.43B | 2 |
| 121 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 486 | 0 | 12,446 | 0.4% | 70.55B | 2 |
| 122 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 479 | +40 | 76,094 | 0.3% | 7.04B | 4 |
| 123 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 460 | +13 | 13,799 | 0.4% | 4.33B | 3 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 454 | -7 | 27,234 | 0.4% | 9.24B | 2 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 446 | -19 | 39,077 | 0.3% | 7.48B | 2 |
| 126 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 416 | -39 | 321,918 | 0.1% | 7.24B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 414 | +12 | 7,300 | 0.4% | 31.59B | 6 |
| 128 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 408 | +7 | 21,730 | 0.3% | 2.61B | 2 |
| 129 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 387 | -17 | 44,398 | 0.3% | 7.70B | 5 |
| 130 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 381 | 0 | 11,725 | 0.3% | 27.23B | 2 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 342 | +5 | 41,640 | 0.2% | 11.17B | 1 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 298 | +6 | 1,107 | 0.3% | — | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 293 | -15 | 106,884 | 0.1% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 292 | -14 | 2,437 | 0.3% | 4.02B | 2 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 273 | +8 | 16,403 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 265 | +5 | 21,414 | 0.2% | 9.24B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 240 | +1 | 19,419 | 0.2% | 68.98B | 2 |
| 138 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 206 | -109 | 1,188 | 0.2% | 27.23B | 3 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 202 | +1 | 38,608 | 0.1% | 70.55B | 3 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 198 | +2 | 5,312 | 0.2% | 353.4M | 2 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 194 | +5 | 5,157 | 0.2% | 11.51B | 5 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 189 | +8 | 2,336 | 0.2% | — | 1 |
| 143 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 146 | +2 | 4,830 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 145 | +3 | 7,144 | 0.1% | 1.20B | 2 |
| 145 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 144 | -24 | 4,871 | 0.1% | 437.8M | 1 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | +4 | 28,234 | 0.1% | 46.70B | 6 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 122 | +1 | 999 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 96 | -5 | 1,232 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 67 | -1 | 186 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 47 | +2 | 350 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 37 | -1 | 256 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | -1 | 142 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 19 | +1 | 214 | 0.0% | 15.17B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | -2 | 353 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -2 | 111 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 17 | +2 | 158 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 9 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,132,858 | 298,756,563 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,111,014 | 5,295,235 | 7 | 20.6% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 503,953 | 2,342,841 | 11 | 20.6% |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 448,979 | 1,428,029 | 11 | 29.4% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 204,281 | 6,309,107 | 12 | 3.2% |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 65,938 | 67,835 | 1 | 39.3% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 40,397 | 1,356,288 | 5 | 2.8% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 20,962 | 431,756 | 6 | 3.9% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,554 | 539,109 | 13 | 2.1% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 10,150 | 356,169 | 14 | 2.2% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,303 | 190,240 | 6 | 3.2% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 8,007 | 853,025 | 3 | 0.8% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,862 | 192,400 | 3 | 2.7% |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,873 | 367,599 | 10 | 1.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,269 | 151,134 | 2 | 2.1% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,572 | 693,714 | 2 | 0.6% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,370 | 486,875 | 3 | 0.7% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,328 | 133,551 | 1 | 1.9% |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,304 | 23,535 | 4 | 2.7% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,122 | 656,600 | 2 | 0.4% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,341 | 152,831 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,265 | 102,785 | 4 | 1.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,101 | 1,159,252 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,313 | 7,591 | 1 | 1.2% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 479 | 76,094 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,383,022 | 57,444,120 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 502,312 | 4,200,483 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 374,181 | 572,586 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 150,466 | 4,144,641 | 16 |
| 5 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 148,450 | 416,964 | 17 |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 65,938 | 67,835 | 23 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,023 | 678,310 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,029 | 108,925 | 43 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Viking 33B | 5,693 | 30,084 | 44 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,053 | 111,286 | 47 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,601 | 66,632 | 48 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,328 | 133,551 | 51 |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,282 | 669,346 | 53 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,156 | 371,796 | 55 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,803 | 91,573 | 57 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,424 | 66,104 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,695 | 99,466 | 78 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,640 | 355,655 | 79 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,612 | 176,559 | 80 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,522 | 157,453 | 83 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,383 | 12,009 | 88 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,313 | 7,591 | 91 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,246 | 57,201 | 94 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,026 | 800,330 | 98 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 479 | 76,094 | 122 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.3% | 65,938 | 67,835 | 6 |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | 29.4% | 448,979 | 1,428,029 | 4 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 20.6% | 503,953 | 2,342,841 | 3 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 20.6% | 1,111,014 | 5,295,235 | 2 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.9% | 20,962 | 431,756 | 8 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,303 | 190,240 | 11 |
| 7 | [speakleash](https://huggingface.co/speakleash) | 3.2% | 204,281 | 6,309,107 | 5 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.8% | 40,397 | 1,356,288 | 7 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,132,858 | 298,756,563 | 1 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 7,862 | 192,400 | 13 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.7% | 3,304 | 23,535 | 19 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.2% | 10,150 | 356,169 | 10 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,554 | 539,109 | 9 |
| 14 | [Almawave](https://huggingface.co/Almawave) | 2.1% | 5,269 | 151,134 | 15 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,328 | 133,551 | 18 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,873 | 367,599 | 14 |
| 17 | [domyn](https://huggingface.co/domyn) | 1.2% | 1,313 | 7,591 | 24 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,265 | 102,785 | 22 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,341 | 152,831 | 21 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 8,007 | 853,025 | 12 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.7% | 4,370 | 486,875 | 17 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,572 | 693,714 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,122 | 656,600 | 20 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 479 | 76,094 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,101 | 1,159,252 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
