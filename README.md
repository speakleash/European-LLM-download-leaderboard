# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-10
- **Generated at:** 2026-11-10T14:36:37Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,956,256 | +4,127 | 60,375,769 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,429,915 | -39,645 | 66,771,292 | 2.1% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 647,483 | +15,590 | 4,463,421 | 14.2% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 537,573 | +20,598 | 46,471,272 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 347,582 | +5,889 | 32,784,565 | 1.1% | 46.70B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 283,148 | -20,460 | 4,690,241 | 5.9% | 8.05B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,402 | +1,533 | 2,534,377 | 9.6% | 8.92B | 6 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 227,082 | -166 | 303,971 | 56.2% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 202,999 | -1,062 | 5,884,696 | 3.4% | 3.85B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 163,493 | +1,990 | 5,011,522 | 3.2% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 158,591 | +1,301 | 16,664,498 | 0.9% | 12.25B | 3 |
| 12 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 106,810 | -438 | 7,717,709 | 1.4% | 23.57B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,505 | -628 | 5,620,754 | 1.8% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 65,247 | +11,583 | 4,218,786 | 1.5% | 11.34B | 8 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 60,646 | +508 | 8,602,288 | 0.7% | 8.02B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 51,859 | -1,410 | 806,611 | 5.7% | 23.57B | 2 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 46,291 | +817 | 11,287,867 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,919 | +321 | 736,081 | 5.5% | 7.77B | 8 |
| 19 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 36,514 | -22,663 | 3,009,771 | 1.2% | 24.01B | 1 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,805 | +4 | 366,557 | 7.0% | 24.01B | 2 |
| 21 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,678 | -78 | 744,009 | 3.9% | 119.40B | 3 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,107 | -521 | 245,537 | 7.0% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,458 | -99 | 945,313 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,788 | -104 | 1,120,347 | 1.4% | 127.70B | 2 |
| 25 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,447 | +26 | 799,630 | 1.8% | 11.25B | 10 |
| 26 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,369 | +106 | 4,943,924 | 0.3% | 122.61B | 1 |
| 27 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 13,268 | -1,326 | 740,097 | 1.6% | 8.90B | 1 |
| 28 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,754 | -11 | 5,047,107 | 0.2% | 122.61B | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,576 | +57 | 650,488 | 1.7% | 23.57B | 2 |
| 30 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 11,108 | -563 | 550,913 | 1.7% | 70.60B | 2 |
| 31 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,090 | -84 | 523,834 | 1.8% | 7.24B | 8 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,969 | -360 | 160,142 | 4.2% | 9.15B | 1 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,780 | +240 | 497,367 | 1.8% | 9.15B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,383 | +1 | 22,594 | 8.5% | 27.43B | 3 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,947 | +41 | 5,390,403 | 0.2% | 22.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,776 | +183 | 86,801 | 4.7% | — | 5 |
| 37 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,364 | -132 | 119,453 | 3.8% | 8.42B | 7 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,240 | +56 | 35,146 | 6.1% | 72.01B | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,068 | -38 | 604,107 | 1.0% | 22.64B | 1 |
| 40 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,706 | +3 | 16,029 | 5.8% | 1.51B | 6 |
| 41 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,656 | +47 | 358,029 | 1.5% | 125.03B | 1 |
| 42 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 6,104 | +133 | 260,325 | 1.7% | 4.76B | 5 |
| 43 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,894 | +105 | 21,470 | 4.9% | 3.83B | 5 |
| 44 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,799 | +727 | 152,820 | 2.3% | 2.25B | 7 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,616 | +9 | 82,001 | 3.1% | 7.04B | 4 |
| 46 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5,342 | -141 | 44,738 | 3.7% | 12.25B | 3 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,273 | +22 | 55,556 | 3.4% | 8.03B | 7 |
| 48 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,192 | +73 | 22,492 | 4.2% | 572.6M | 5 |
| 49 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,065 | +462 | 64,182 | 3.1% | 1.60B | 5 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,692 | -1 | 910,472 | 0.5% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,487 | -24 | 154,590 | 1.8% | 7.24B | 4 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,453 | +33 | 140,390 | 1.9% | 7.40B | 3 |
| 53 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,415 | +351 | 38,288 | 3.2% | 56.7M | 1 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,223 | -78 | 378,123 | 0.9% | 7.24B | 8 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,205 | +12 | 40,834 | 3.0% | 2.61B | 3 |
| 56 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,092 | -57 | 140,978 | 1.7% | 7.48B | 5 |
| 57 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,980 | -46 | 5,165,410 | 0.1% | 22.25B | 1 |
| 58 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,748 | 0 | 28,412 | 2.9% | 22.64B | 1 |
| 59 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,683 | -79 | 44,575 | 2.5% | 13.29B | 3 |
| 60 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,355 | -72 | 169,847 | 1.2% | 11.17B | 16 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,258 | -30 | 96,238 | 1.7% | 2.89B | 1 |
| 62 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,017 | +23 | 12,985 | 2.7% | 9.15B | 1 |
| 63 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,752 | +15 | 5,303,854 | 0.1% | 7.25B | 1 |
| 64 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,597 | +19 | 157,202 | 1.0% | 23.57B | 2 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,574 | -2 | 179,867 | 0.9% | 12.25B | 6 |
| 66 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,550 | +506 | 53,009 | 1.7% | 7.77B | 1 |
| 67 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,501 | -158 | 34,622 | 1.9% | 14.03B | 1 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,395 | -16 | 230,827 | 0.7% | 35.13B | 4 |
| 69 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,239 | +8 | 20,549 | 1.9% | 12.19B | 2 |
| 70 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,170 | +4 | 86,604 | 1.2% | 9.15B | 1 |
| 71 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,096 | -1 | 102,408 | 1.0% | 30.68B | 1 |
| 72 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,045 | -17 | 358,512 | 0.4% | — | 3 |
| 73 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,044 | +11 | 22,772 | 1.7% | 4.30B | 2 |
| 74 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,026 | +4 | 51,889 | 1.3% | 9.24B | 4 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,023 | -2 | 80,874 | 1.1% | 7.45B | 1 |
| 76 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,964 | -8 | 160,152 | 0.8% | 1.10B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,933 | -3 | 108,405 | 0.9% | 7.45B | 1 |
| 78 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,854 | -9 | 35,091 | 1.4% | 22.64B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,852 | -12 | 303,532 | 0.5% | 6.74B | 2 |
| 80 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,846 | -9 | 186,877 | 0.6% | 6.74B | 1 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,782 | -12 | 147,597 | 0.7% | 13.02B | 1 |
| 82 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,757 | -26 | 40,998 | 1.2% | 70.55B | 3 |
| 83 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,686 | +48 | 9,711 | 1.5% | 9.82B | 1 |
| 84 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,559 | -22 | 54,785 | 1.0% | 7.24B | 5 |
| 85 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,531 | +27 | 20,789 | 1.3% | 1.20B | 2 |
| 86 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,495 | -25 | 802,298 | 0.2% | — | 3 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,494 | -21 | 53,549 | 1.0% | 7.24B | 1 |
| 88 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,443 | -116 | 9,665 | 1.3% | 4.30B | 3 |
| 89 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,381 | -5 | 16,022 | 1.2% | 353.4M | 2 |
| 90 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,308 | +229 | 9,528 | 1.2% | 28.84B | 3 |
| 91 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,264 | +276 | 453,973 | 0.2% | 40.43B | 1 |
| 92 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,263 | -29 | 31,812 | 1.0% | 33.12B | 1 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,253 | -2 | 175,112 | 0.5% | 11.51B | 7 |
| 94 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,192 | -4 | 219,189 | 0.4% | 12.19B | 3 |
| 95 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,107 | -22 | 56,819 | 0.7% | 7.55B | 1 |
| 96 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,042 | +39 | 416,098 | 0.2% | 1.20B | 1 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,018 | +12 | 58,709 | 0.6% | 1.35B | 3 |
| 98 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,004 | +43 | 45,155 | 0.7% | 12.19B | 2 |
| 99 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 963 | -33 | 671,317 | 0.1% | 7.45B | 2 |
| 100 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 931 | +26 | 419,486 | 0.2% | 353.4M | 1 |
| 101 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 913 | -43 | 24,023 | 0.7% | 11.17B | 5 |
| 102 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 826 | -11 | 233,636 | 0.2% | — | 2 |
| 103 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 812 | -33 | 31,829 | 0.6% | 11.17B | 5 |
| 104 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 783 | +4 | 14,757 | 0.7% | 4.33B | 3 |
| 105 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 782 | +10 | 400,889 | 0.2% | 3.21B | 1 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 772 | -29 | 96,627 | 0.4% | 1.35B | 8 |
| 107 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 772 | -31 | 2,099 | 0.8% | 27.23B | 3 |
| 108 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 748 | -23 | 112,504 | 0.4% | 7.29B | 2 |
| 109 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 700 | +2 | 17,030 | 0.6% | 1.54B | 4 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 697 | -19 | 82,259 | 0.4% | 8.03B | 3 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 604 | -12 | 22,191 | 0.5% | 9.24B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 597 | -9 | 28,013 | 0.5% | 9.24B | 2 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 580 | -18 | 20,855 | 0.5% | 3.20B | 2 |
| 114 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 545 | -3 | 3,709 | 0.5% | 30.68B | 1 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 473 | -40 | 4,462 | 0.5% | 8.03B | 3 |
| 116 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 431 | -2 | 1,704 | 0.4% | — | 1 |
| 117 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 428 | 0 | 12,461 | 0.4% | 31.59B | 6 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 420 | -11 | 12,243 | 0.4% | 27.23B | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 350 | +8 | 22,204 | 0.3% | 2.61B | 2 |
| 120 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 350 | -6 | 3,413 | 0.3% | 560.9M | 2 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 335 | +12 | 5,636 | 0.3% | 11.51B | 5 |
| 122 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 307 | -1 | 2,861 | 0.3% | 4.02B | 2 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 282 | -8 | 107,314 | 0.1% | — | 3 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 276 | 0 | 37,904 | 0.2% | 27.23B | 3 |
| 125 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 270 | -16 | 32,915 | 0.2% | 40.43B | 2 |
| 126 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 256 | +2 | 70,600 | 0.2% | 8.03B | 3 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 238 | -25 | 39,462 | 0.2% | 7.48B | 2 |
| 128 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 206 | -15 | 322,312 | 0.0% | 7.24B | 2 |
| 129 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 205 | +9 | 16,694 | 0.2% | 7.29B | 2 |
| 130 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 201 | -23 | 41,958 | 0.1% | 11.17B | 1 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 198 | -9 | 19,726 | 0.2% | 68.98B | 2 |
| 132 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | 0 | 3,002 | 0.2% | 31.59B | 6 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 181 | -3 | 44,693 | 0.1% | 7.70B | 5 |
| 134 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 178 | -1 | 12,735 | 0.2% | 70.55B | 2 |
| 135 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 160 | -4 | 1,197 | 0.2% | — | 1 |
| 136 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 159 | +1 | 28,456 | 0.1% | 46.70B | 6 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 150 | -6 | 2,579 | 0.1% | — | 1 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 132 | -12 | 5,524 | 0.1% | 353.4M | 2 |
| 139 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 124 | 0 | 7,490 | 0.1% | 31.59B | 6 |
| 140 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 121 | -6 | 5,086 | 0.1% | 70.55B | 3 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 114 | -20 | 5,195 | 0.1% | 437.8M | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 83 | 0 | 38,734 | 0.1% | 70.55B | 3 |
| 143 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 68 | -1 | 1,323 | 0.1% | 560.9M | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 58 | -9 | 7,266 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 39 | -1 | 443 | 0.0% | 321.0M | 1 |
| 146 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | +1 | 244 | 0.0% | 437.8M | 1 |
| 147 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 38 | -1 | 409 | 0.0% | 437.8M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 37 | -3 | 267 | 0.0% | 15.17B | 3 |
| 149 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 37 | -3 | 211 | 0.0% | 8.16B | 3 |
| 150 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +3 | 148 | 0.0% | 7.24B | 1 |
| 151 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | 0 | 178 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 289 | 0.0% | 437.8M | 1 |
| 153 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | -2 | 1,509 | 0.0% | 31.58B | 2 |
| 154 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 155 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 156 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 0 | 0 | 0 | 0.0% | — | 0 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,264,880 | 308,253,916 | 30 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 333,556 | 6,076,388 | 7 | 5.4% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 231,436 | 433,748 | 6 | 43.4% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 114,914 | 6,456,140 | 12 | 1.8% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 87,526 | 2,658,971 | 11 | 3.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 55,802 | 1,428,798 | 5 | 3.7% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,877 | 568,393 | 13 | 3.3% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,691 | 1,451,639 | 11 | 0.9% |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,296 | 450,634 | 6 | 2.6% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,798 | 373,230 | 14 | 2.5% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 10,633 | 400,514 | 10 | 2.1% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,783 | 203,608 | 3 | 2.9% |
| 13 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,616 | 82,001 | 1 | 3.1% |
| 14 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,592 | 494,626 | 3 | 0.9% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,919 | 860,596 | 3 | 0.5% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,453 | 140,390 | 1 | 1.9% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,429 | 700,435 | 2 | 0.6% |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,897 | 662,044 | 2 | 0.5% |
| 19 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,801 | 1,162,974 | 4 | 0.2% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,715 | 106,595 | 4 | 1.3% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,790 | 155,336 | 2 | 0.7% |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,686 | 9,711 | 1 | 1.5% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 745 | 24,462 | 4 | 0.6% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,956,256 | 60,375,769 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 283,148 | 4,690,241 | 6 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 227,082 | 303,971 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 65,247 | 4,218,786 | 14 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,919 | 736,081 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 24,107 | 245,537 | 22 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,383 | 22,594 | 34 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,364 | 119,453 | 37 |
| 9 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,616 | 82,001 | 45 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 5,342 | 44,738 | 46 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,273 | 55,556 | 47 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,487 | 154,590 | 51 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,453 | 140,390 | 52 |
| 14 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,415 | 38,288 | 53 |
| 15 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,223 | 378,123 | 54 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,096 | 102,408 | 71 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,045 | 358,512 | 72 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,023 | 80,874 | 75 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,964 | 160,152 | 76 |
| 20 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,686 | 9,711 | 83 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,495 | 802,298 | 86 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,018 | 58,709 | 97 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 428 | 12,461 | 117 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 156 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 43.4% | 231,436 | 433,748 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 5.4% | 333,556 | 6,076,388 | 2 |
| 3 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.7% | 55,802 | 1,428,798 | 6 |
| 4 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,877 | 568,393 | 7 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.2% | 87,526 | 2,658,971 | 5 |
| 6 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,616 | 82,001 | 13 |
| 7 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,783 | 203,608 | 12 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,296 | 450,634 | 9 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,798 | 373,230 | 10 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.1% | 10,633 | 400,514 | 11 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,264,880 | 308,253,916 | 1 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,453 | 140,390 | 16 |
| 13 | [speakleash](https://huggingface.co/speakleash) | 1.8% | 114,914 | 6,456,140 | 4 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,686 | 9,711 | 22 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,715 | 106,595 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,691 | 1,451,639 | 8 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,592 | 494,626 | 14 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,790 | 155,336 | 21 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 745 | 24,462 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,429 | 700,435 | 17 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,919 | 860,596 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,897 | 662,044 | 18 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,801 | 1,162,974 | 19 |
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
