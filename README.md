# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-14
- **Generated at:** 2026-10-14T11:30:06Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,274,955 | -17,834 | 58,554,675 | 3.9% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,626,049 | -9,787 | 65,492,190 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 685,739 | -14,183 | 729,327 | 82.7% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 505,652 | -8,626 | 45,962,033 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 487,804 | -2,291 | 4,438,226 | 10.7% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 335,256 | -14,460 | 16,513,864 | 2.0% | 12.25B | 3 |
| 7 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 319,871 | -8,090 | 2,982,143 | 10.4% | 24.01B | 1 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 307,285 | -3,154 | 3,835,792 | 7.8% | 13.95B | 6 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 296,489 | -17,640 | 4,866,321 | 6.0% | 24.01B | 2 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,076 | -2,438 | 5,522,976 | 4.5% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 246,377 | -4,932 | 32,448,116 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 231,317 | -442 | 5,696,610 | 4.0% | 4.25B | 7 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,223 | -22 | 926,510 | 22.5% | 1.66B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 219,427 | +787 | 2,292,106 | 9.2% | 8.92B | 6 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 214,014 | -14,464 | 597,609 | 30.7% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 108,075 | -5,497 | 8,544,181 | 1.3% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 77,792 | -1,138 | 713,584 | 9.6% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,525 | +778 | 1,105,417 | 6.1% | 127.70B | 2 |
| 19 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,860 | +1,352 | 7,617,483 | 0.9% | 23.57B | 2 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,208 | -93 | 759,790 | 8.3% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 69,526 | +786 | 71,464 | 40.5% | — | 1 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 59,516 | +539 | 11,244,681 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,191 | +16,221 | 117,925 | 24.9% | 12.77B | 5 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 31,313 | +14,020 | 236,210 | 9.3% | — | 1 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,518 | -75 | 693,566 | 3.6% | 7.77B | 8 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,109 | +316 | 43,164 | 16.8% | 12.25B | 3 |
| 27 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 21,627 | -1,312 | 4,155,213 | 0.5% | 11.34B | 8 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,045 | -656 | 541,369 | 3.3% | 70.60B | 2 |
| 29 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,938 | -43 | 5,161,684 | 0.4% | 22.25B | 1 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,616 | +331 | 153,084 | 7.8% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,753 | -71 | 638,443 | 2.3% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,684 | -2 | 784,033 | 1.5% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,281 | -52 | 79,068 | 7.4% | — | 5 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,658 | -440 | 487,379 | 2.2% | 9.15B | 1 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,703 | +222 | 334,518 | 2.7% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,232 | +31 | 513,526 | 1.8% | 7.24B | 8 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,353 | +54 | 4,930,203 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,022 | -470 | 137,180 | 3.8% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,195 | +72 | 5,381,865 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,312 | -42 | 17,492 | 5.4% | 572.6M | 5 |
| 41 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,784 | -11 | 147,240 | 2.3% | 2.25B | 7 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,607 | +130 | 111,470 | 2.7% | 8.42B | 7 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,372 | -331 | 351,788 | 1.2% | 125.03B | 1 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,322 | +122 | 50,705 | 3.5% | 8.03B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,316 | -23 | 136,299 | 2.2% | 7.40B | 3 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,967 | +42 | 154,750 | 1.9% | 23.57B | 2 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,799 | -8 | 166,739 | 1.8% | 11.17B | 16 |
| 48 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,748 | +8 | 374,195 | 1.0% | 7.24B | 8 |
| 49 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,447 | -5 | 12,320 | 4.0% | 27.43B | 3 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,357 | 0 | 150,405 | 1.7% | 7.24B | 4 |
| 51 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,271 | +2 | 111,783 | 2.0% | 7.29B | 2 |
| 52 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,008 | -60 | 5,034,577 | 0.1% | 122.61B | 1 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,867 | +46 | 254,519 | 1.1% | 4.76B | 5 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,816 | -42 | 905,983 | 0.4% | 23.57B | 2 |
| 55 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,723 | 0 | 67,382 | 2.2% | 14.08B | 1 |
| 56 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,521 | -1,573 | 27,167 | 2.8% | 72.01B | 1 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,444 | +136 | 37,004 | 2.5% | 2.61B | 3 |
| 58 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,436 | -210 | 670,461 | 0.4% | 7.45B | 2 |
| 59 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,186 | -64 | 400,129 | 0.6% | 3.21B | 1 |
| 60 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,172 | +1 | 93,195 | 1.6% | 2.89B | 1 |
| 61 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,172 | -71 | 415,079 | 0.6% | 1.20B | 1 |
| 62 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,162 | -58 | 59,269 | 2.0% | 1.60B | 5 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,156 | -65 | 418,578 | 0.6% | 353.4M | 1 |
| 64 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,749 | +25 | 9,484 | 2.5% | 1.51B | 6 |
| 65 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,717 | 0 | 86,317 | 1.5% | 2.22B | 1 |
| 66 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,606 | +23 | 24,825 | 2.1% | 22.64B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,553 | +15 | 84,455 | 1.4% | 9.15B | 1 |
| 68 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,428 | +694 | 178,188 | 0.9% | 12.25B | 6 |
| 69 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,395 | +3 | 41,124 | 1.7% | 13.29B | 3 |
| 70 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,350 | +15 | 50,576 | 1.6% | 7.77B | 1 |
| 71 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,258 | +94 | 34,214 | 1.7% | 56.7M | 1 |
| 72 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,166 | -108 | 50,004 | 1.4% | 9.24B | 4 |
| 73 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,082 | -6 | 30,658 | 1.6% | 33.12B | 1 |
| 74 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,008 | -68 | 18,478 | 1.7% | 12.19B | 2 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,872 | -6 | 78,975 | 1.0% | 7.45B | 1 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,842 | -4 | 106,602 | 0.9% | 7.45B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,838 | -5 | 100,453 | 0.9% | 30.68B | 1 |
| 78 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,831 | -7 | 452,756 | 0.3% | 40.43B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,755 | -3 | 356,591 | 0.4% | — | 3 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,714 | -98 | 15,756 | 1.5% | 3.83B | 5 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,643 | +1 | 158,298 | 0.6% | 1.10B | 1 |
| 82 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,632 | +1 | 55,753 | 1.0% | 7.55B | 1 |
| 83 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,616 | -28 | 33,352 | 1.2% | 22.64B | 1 |
| 84 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,606 | +31 | 32,453 | 1.2% | 14.03B | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,575 | -3 | 301,790 | 0.4% | 6.74B | 2 |
| 86 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,568 | -13 | 23,181 | 1.3% | 11.17B | 5 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,540 | +2 | 185,142 | 0.5% | 6.74B | 1 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,527 | -5 | 53,329 | 1.0% | 7.24B | 5 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,520 | 0 | 145,925 | 0.6% | 13.02B | 1 |
| 90 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,447 | +4 | 52,156 | 1.0% | 7.24B | 1 |
| 91 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,431 | -241 | 5,301,221 | 0.0% | 7.25B | 1 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,390 | -24 | 20,843 | 1.2% | 4.30B | 2 |
| 93 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,359 | -11 | 8,320 | 1.3% | 4.30B | 3 |
| 94 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,353 | -3 | 173,934 | 0.5% | 11.51B | 7 |
| 95 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,240 | -20 | 31,074 | 0.9% | 11.17B | 5 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,214 | -119 | 19,340 | 1.0% | 1.20B | 2 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,214 | -30 | 228,537 | 0.4% | 35.13B | 4 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,125 | -43 | 10,058 | 1.0% | 9.15B | 1 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,116 | -5 | 57,736 | 0.7% | 1.35B | 3 |
| 100 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,108 | -8 | 800,861 | 0.1% | — | 3 |
| 101 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,041 | -323 | 8,094 | 1.0% | 9.82B | 1 |
| 102 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,026 | -12 | 39,348 | 0.7% | 70.55B | 3 |
| 103 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,026 | -105 | 14,770 | 0.9% | 353.4M | 2 |
| 104 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 838 | +4 | 16,385 | 0.7% | 1.54B | 4 |
| 105 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 817 | -11 | 8,236 | 0.8% | 28.84B | 3 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 686 | -22 | 95,909 | 0.4% | 1.35B | 8 |
| 107 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 663 | -83 | 20,285 | 0.6% | 3.20B | 2 |
| 108 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 662 | -6 | 81,617 | 0.4% | 8.03B | 3 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 611 | +15 | 4,034 | 0.6% | 8.03B | 3 |
| 110 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 604 | -10 | 76,416 | 0.3% | 7.04B | 4 |
| 111 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 525 | +10 | 218,100 | 0.2% | 12.19B | 3 |
| 112 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 523 | -2 | 232,817 | 0.2% | — | 2 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 428 | +1 | 27,428 | 0.3% | 9.24B | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 428 | -15 | 44,163 | 0.3% | 12.19B | 2 |
| 115 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 424 | -12 | 13,995 | 0.4% | 4.33B | 3 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 416 | -15 | 32,652 | 0.3% | 40.43B | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 416 | -2 | 3,069 | 0.4% | 560.9M | 2 |
| 118 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 416 | -5 | 322,125 | 0.1% | 7.24B | 2 |
| 119 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 411 | -13 | 3,179 | 0.4% | 30.68B | 1 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 409 | -5 | 39,233 | 0.3% | 7.48B | 2 |
| 121 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 389 | +1 | 1,297 | 0.4% | — | 1 |
| 122 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 380 | -16 | 7,394 | 0.4% | 31.59B | 6 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 352 | +20 | 1,436 | 0.3% | 27.23B | 3 |
| 124 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 316 | +2 | 21,603 | 0.3% | 9.24B | 2 |
| 125 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 307 | -9 | 37,641 | 0.2% | 27.23B | 3 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 303 | -27 | 21,901 | 0.2% | 2.61B | 2 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 300 | -6 | 107,047 | 0.1% | — | 3 |
| 128 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 297 | 0 | 11,833 | 0.3% | 27.23B | 2 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 293 | -11 | 41,765 | 0.2% | 11.17B | 1 |
| 130 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 275 | -18 | 70,351 | 0.2% | 8.03B | 3 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 262 | -2 | 44,533 | 0.2% | 7.70B | 5 |
| 132 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 261 | -4 | 5,318 | 0.2% | 11.51B | 5 |
| 133 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 245 | +2 | 5,099 | 0.2% | 437.8M | 1 |
| 134 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 243 | -12 | 12,580 | 0.2% | 70.55B | 2 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 228 | -4 | 19,539 | 0.2% | 68.98B | 2 |
| 136 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | -2 | 1,501 | 0.2% | 31.58B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 212 | +1 | 2,445 | 0.2% | — | 1 |
| 138 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 206 | -22 | 4,988 | 0.2% | 70.55B | 3 |
| 139 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 200 | -4 | 2,566 | 0.2% | 4.02B | 2 |
| 140 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 194 | -8 | 16,492 | 0.2% | 7.29B | 2 |
| 141 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 160 | +14 | 28,331 | 0.1% | 46.70B | 6 |
| 142 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 147 | -1 | 5,399 | 0.1% | 353.4M | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 143 | -7 | 38,661 | 0.1% | 70.55B | 3 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140 | 0 | 1,046 | 0.1% | — | 1 |
| 145 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 146 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 117 | -4 | 7,213 | 0.1% | 1.20B | 2 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 82 | 0 | 406 | 0.1% | 321.0M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 47 | -823 | 2,834 | 0.0% | 31.59B | 6 |
| 149 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 38 | -895 | 12,033 | 0.0% | 31.59B | 6 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 37 | +1 | 1,261 | 0.0% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | 0 | 205 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 27 | -3 | 231 | 0.0% | 15.17B | 3 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | 0 | 371 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 23 | -3 | 174 | 0.0% | 8.16B | 3 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -1 | 151 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | 0 | 119 | 0.0% | 7.24B | 1 |
| 157 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | 0 | 263 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,174,076 | 302,428,405 | 30 | 2.4% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,208,884 | 5,778,821 | 7 | 20.6% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 520,380 | 2,592,931 | 11 | 19.3% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 72,108 | 6,345,751 | 12 | 1.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 69,526 | 71,464 | 1 | 40.5% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,517 | 243,676 | 6 | 17.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,899 | 1,376,790 | 5 | 2.6% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,666 | 394,784 | 10 | 6.0% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,415 | 1,437,869 | 11 | 1.1% |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,848 | 547,175 | 13 | 2.4% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,882 | 437,454 | 6 | 2.4% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,499 | 362,197 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,150 | 856,038 | 3 | 0.7% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,440 | 153,699 | 2 | 2.5% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,278 | 195,236 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,316 | 136,299 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,164 | 696,320 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,703 | 489,365 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,330 | 658,381 | 2 | 0.4% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,299 | 104,037 | 4 | 1.1% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,159 | 1,160,264 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,802 | 153,645 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,041 | 8,094 | 1 | 1.0% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 693 | 23,762 | 4 | 0.6% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 604 | 76,416 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,274,955 | 58,554,675 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 685,739 | 729,327 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,223 | 926,510 | 13 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 69,526 | 71,464 | 21 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,191 | 117,925 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,518 | 693,566 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,109 | 43,164 | 26 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 21,627 | 4,155,213 | 27 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,607 | 111,470 | 42 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,322 | 50,705 | 44 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,316 | 136,299 | 45 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,748 | 374,195 | 48 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,447 | 12,320 | 49 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,357 | 150,405 | 50 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,723 | 67,382 | 55 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,436 | 670,461 | 58 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 3B Preview | 3,186 | 400,129 | 59 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,838 | 100,453 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,755 | 356,591 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,643 | 158,298 | 81 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,116 | 57,736 | 99 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,108 | 800,861 | 100 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,041 | 8,094 | 101 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 604 | 76,416 | 110 |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 380 | 7,394 | 122 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 40.5% | 69,526 | 71,464 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 20.6% | 1,208,884 | 5,778,821 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 19.3% | 520,380 | 2,592,931 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 17.0% | 58,517 | 243,676 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,666 | 394,784 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,899 | 1,376,790 | 7 |
| 7 | [Almawave](https://huggingface.co/Almawave) | 2.5% | 6,440 | 153,699 | 14 |
| 8 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,499 | 362,197 | 12 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.4% | 15,848 | 547,175 | 10 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 12,882 | 437,454 | 11 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.4% | 7,174,076 | 302,428,405 | 1 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,316 | 136,299 | 16 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,278 | 195,236 | 15 |
| 14 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,415 | 1,437,869 | 9 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,299 | 104,037 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 72,108 | 6,345,751 | 4 |
| 17 | [domyn](https://huggingface.co/domyn) | 1.0% | 1,041 | 8,094 | 23 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,703 | 489,365 | 18 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 7,150 | 856,038 | 13 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,802 | 153,645 | 22 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,164 | 696,320 | 17 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 693 | 23,762 | 24 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,330 | 658,381 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 604 | 76,416 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,159 | 1,160,264 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
