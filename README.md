# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-04
- **Generated at:** 2026-11-04T14:02:18Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,849,875 | +20,851 | 59,860,654 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,665,600 | -24,768 | 66,585,534 | 2.5% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 578,459 | +7,726 | 46,348,715 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 567,216 | +1,894 | 4,330,066 | 12.8% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 375,356 | -15,196 | 4,685,082 | 7.8% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 329,889 | -132 | 32,719,872 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 217,185 | -1,964 | 2,464,756 | 8.5% | 8.92B | 6 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,899 | +622 | 5,841,683 | 3.4% | 3.85B | 7 |
| 9 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 181,652 | +9,157 | 248,959 | 52.1% | 12.77B | 5 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 180,765 | -2,786 | 4,980,598 | 3.6% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 178,312 | -6,749 | 16,641,167 | 1.1% | 12.25B | 3 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 123,743 | -7,511 | 3,005,300 | 4.0% | 24.01B | 1 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 115,617 | -3,262 | 5,604,213 | 2.0% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 108,698 | +6,751 | 7,702,339 | 1.4% | 23.57B | 2 |
| 15 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,391 | -2,422 | 805,830 | 7.0% | 23.57B | 2 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,311 | -110 | 11,279,177 | 0.5% | 140.63B | 2 |
| 17 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 47,508 | +2,371 | 730,707 | 5.7% | 7.77B | 8 |
| 18 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,860 | -891 | 8,575,705 | 0.5% | 8.02B | 1 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,654 | -11,704 | 739,262 | 4.6% | 119.40B | 3 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,682 | +135 | 364,011 | 7.7% | 24.01B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,578 | -167 | 1,117,839 | 2.2% | 127.70B | 2 |
| 22 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 25,407 | -4 | 4,175,241 | 0.6% | 11.34B | 8 |
| 23 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,249 | -777 | 241,905 | 7.1% | — | 1 |
| 24 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 22,788 | -19,165 | 739,344 | 2.7% | 8.90B | 1 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,733 | -349 | 943,529 | 2.0% | 1.66B | 1 |
| 26 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,040 | +54 | 796,604 | 1.8% | 11.25B | 10 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,949 | +162 | 649,077 | 2.1% | 23.57B | 2 |
| 28 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 14,972 | -3,048 | 44,473 | 10.4% | 12.25B | 3 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 14,428 | -706 | 549,886 | 2.2% | 70.60B | 2 |
| 30 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,887 | +378 | 4,940,577 | 0.3% | 122.61B | 1 |
| 31 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,709 | -3 | 5,046,446 | 0.2% | 122.61B | 1 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,712 | +122 | 158,887 | 4.5% | 9.15B | 1 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,243 | -216 | 495,523 | 1.9% | 9.15B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,147 | -80 | 521,450 | 1.8% | 7.24B | 8 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,387 | -241 | 85,122 | 5.1% | — | 5 |
| 36 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,546 | -10 | 20,550 | 7.1% | 27.43B | 3 |
| 37 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,464 | -96 | 5,388,451 | 0.2% | 22.25B | 1 |
| 38 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,463 | +169 | 76,656 | 4.8% | — | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,368 | -160 | 602,892 | 1.2% | 22.64B | 1 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,238 | -183 | 34,908 | 6.1% | 72.01B | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,818 | +204 | 117,733 | 3.6% | 8.42B | 7 |
| 42 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,423 | +508 | 15,047 | 5.6% | 1.51B | 6 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,380 | +96 | 356,641 | 1.4% | 125.03B | 1 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,615 | +29 | 81,808 | 3.1% | 7.04B | 4 |
| 45 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,561 | +20 | 20,684 | 4.6% | 3.83B | 5 |
| 46 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,528 | -147 | 151,251 | 2.2% | 2.25B | 7 |
| 47 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,497 | +122 | 258,992 | 1.5% | 4.76B | 5 |
| 48 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,088 | -153 | 139,970 | 2.1% | 7.48B | 5 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,627 | +61 | 909,876 | 0.5% | 23.57B | 2 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,545 | +7 | 153,688 | 1.8% | 7.24B | 4 |
| 51 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,530 | +38 | 139,435 | 1.9% | 7.40B | 3 |
| 52 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,515 | -191 | 5,164,678 | 0.1% | 22.25B | 1 |
| 53 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,505 | -628 | 21,071 | 3.7% | 572.6M | 5 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,479 | -77 | 377,371 | 0.9% | 7.24B | 8 |
| 55 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,334 | +129 | 62,593 | 2.7% | 1.60B | 5 |
| 56 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,004 | +7 | 40,014 | 2.9% | 2.61B | 3 |
| 57 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,984 | +201 | 37,168 | 2.9% | 56.7M | 1 |
| 58 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,922 | -128 | 169,311 | 1.5% | 11.17B | 16 |
| 59 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,876 | -1 | 53,379 | 2.5% | 8.03B | 7 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,732 | +492 | 43,978 | 2.6% | 13.29B | 3 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,270 | +114 | 95,576 | 1.7% | 2.89B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,145 | -6 | 26,893 | 2.5% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,742 | +14 | 34,488 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,697 | 0 | 5,303,541 | 0.0% | 7.25B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,563 | +2 | 179,491 | 0.9% | 12.25B | 6 |
| 66 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,543 | -8 | 156,937 | 1.0% | 23.57B | 2 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,425 | +80 | 52,182 | 1.6% | 7.77B | 1 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,283 | -33 | 230,415 | 0.7% | 35.13B | 4 |
| 69 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,143 | +19 | 22,496 | 1.7% | 4.30B | 2 |
| 70 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,055 | -22 | 101,974 | 1.0% | 30.68B | 1 |
| 71 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,030 | +14 | 358,094 | 0.4% | — | 3 |
| 72 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,025 | -8 | 51,481 | 1.3% | 9.24B | 4 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,002 | -2 | 80,436 | 1.1% | 7.45B | 1 |
| 74 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,903 | +11 | 159,723 | 0.7% | 1.10B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,900 | -20 | 107,996 | 0.9% | 7.45B | 1 |
| 76 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,834 | +8 | 19,905 | 1.5% | 12.19B | 2 |
| 77 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,825 | +14 | 186,490 | 0.6% | 6.74B | 1 |
| 78 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,820 | +7 | 34,693 | 1.4% | 22.64B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,813 | +11 | 303,138 | 0.4% | 6.74B | 2 |
| 80 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,749 | +15 | 40,677 | 1.2% | 70.55B | 3 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,743 | +6 | 147,209 | 0.7% | 13.02B | 1 |
| 82 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,672 | -8 | 9,415 | 1.5% | 4.30B | 3 |
| 83 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,603 | +292 | 20,433 | 1.3% | 1.20B | 2 |
| 84 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,602 | -3 | 54,481 | 1.0% | 7.24B | 5 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,546 | -1 | 9,400 | 1.4% | 9.82B | 1 |
| 86 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,540 | +26 | 11,031 | 1.4% | 9.15B | 1 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,525 | 0 | 53,249 | 1.0% | 7.24B | 1 |
| 88 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,456 | +6 | 31,664 | 1.1% | 33.12B | 1 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,452 | +7 | 802,012 | 0.2% | — | 3 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,398 | -7 | 174,898 | 0.5% | 11.51B | 7 |
| 91 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,326 | +248 | 15,695 | 1.1% | 353.4M | 2 |
| 92 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,216 | -13 | 671,135 | 0.2% | 7.45B | 2 |
| 93 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,147 | +1 | 219,042 | 0.4% | 12.19B | 3 |
| 94 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,125 | +9 | 9,207 | 1.0% | 28.84B | 3 |
| 95 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,111 | +131 | 85,440 | 0.6% | 9.15B | 1 |
| 96 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,092 | -59 | 23,853 | 0.9% | 11.17B | 5 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,043 | +9 | 58,509 | 0.7% | 1.35B | 3 |
| 98 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,026 | -2 | 56,488 | 0.7% | 7.55B | 1 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 989 | +3 | 453,491 | 0.2% | 40.43B | 1 |
| 100 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 981 | -808 | 415,672 | 0.2% | 1.20B | 1 |
| 101 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 959 | -34 | 31,698 | 0.7% | 11.17B | 5 |
| 102 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 874 | +24 | 44,954 | 0.6% | 12.19B | 2 |
| 103 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 868 | +125 | 112,322 | 0.4% | 7.29B | 2 |
| 104 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 844 | +4 | 233,572 | 0.3% | — | 2 |
| 105 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 807 | -799 | 419,009 | 0.2% | 353.4M | 1 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 774 | -8 | 14,689 | 0.7% | 4.33B | 3 |
| 107 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 769 | -801 | 400,517 | 0.2% | 3.21B | 1 |
| 108 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 757 | +62 | 1,998 | 0.7% | 27.23B | 3 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 737 | +35 | 96,469 | 0.4% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 710 | -15 | 82,123 | 0.4% | 8.03B | 3 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 672 | -1 | 16,883 | 0.6% | 1.54B | 4 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 630 | +23 | 27,932 | 0.5% | 9.24B | 2 |
| 113 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 608 | +4 | 22,134 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 573 | +8 | 20,751 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 551 | +8 | 3,590 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 501 | -2 | 4,354 | 0.5% | 8.03B | 3 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 434 | -9 | 1,616 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 422 | +8 | 12,213 | 0.4% | 27.23B | 2 |
| 119 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 361 | 0 | 12,374 | 0.3% | 31.59B | 6 |
| 120 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 319 | -7 | 37,887 | 0.2% | 27.23B | 3 |
| 121 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 315 | -12 | 2,833 | 0.3% | 4.02B | 2 |
| 122 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 311 | -10 | 5,549 | 0.3% | 11.51B | 5 |
| 123 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 310 | -30 | 32,871 | 0.2% | 40.43B | 2 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 292 | -8 | 107,251 | 0.1% | — | 3 |
| 125 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 291 | +4 | 22,118 | 0.2% | 2.61B | 2 |
| 126 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 278 | +128 | 3,281 | 0.3% | 560.9M | 2 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 277 | -7 | 39,426 | 0.2% | 7.48B | 2 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 242 | -3 | 41,912 | 0.2% | 11.17B | 1 |
| 129 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 240 | -2 | 70,535 | 0.1% | 8.03B | 3 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 234 | -39 | 322,259 | 0.1% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 223 | -4 | 19,702 | 0.2% | 68.98B | 2 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 211 | +1 | 44,659 | 0.1% | 7.70B | 5 |
| 133 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 199 | -3 | 16,644 | 0.2% | 7.29B | 2 |
| 134 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 187 | -34 | 5,065 | 0.2% | 70.55B | 3 |
| 135 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 187 | -26 | 5,176 | 0.2% | 437.8M | 1 |
| 136 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 185 | +1 | 12,713 | 0.2% | 70.55B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 177 | -4 | 2,564 | 0.2% | — | 1 |
| 138 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | -2 | 28,422 | 0.1% | 46.70B | 6 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 149 | -4 | 5,503 | 0.1% | 353.4M | 2 |
| 140 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 146 | -15 | 7,476 | 0.1% | 31.59B | 6 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140 | -4 | 1,161 | 0.1% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 91 | -5 | 38,721 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 83 | -6 | 7,255 | 0.1% | 1.20B | 2 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 71 | -3 | 1,316 | 0.1% | 560.9M | 1 |
| 145 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 45 | -1 | 403 | 0.0% | 437.8M | 1 |
| 146 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 45 | 0 | 2,856 | 0.0% | 31.59B | 6 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 41 | -1 | 438 | 0.0% | 321.0M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | -1 | 263 | 0.0% | 15.17B | 3 |
| 149 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 35 | -1 | 204 | 0.0% | 8.16B | 3 |
| 150 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 145 | 0.0% | 7.24B | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | -3 | 228 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | 0 | 280 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 166 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 12 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,464,466 | 306,970,844 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 437,299 | 6,066,022 | 7 | 7.1% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 185,998 | 377,959 | 6 | 38.9% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 88,102 | 2,643,371 | 11 | 3.2% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 75,437 | 6,402,071 | 12 | 1.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 56,760 | 1,420,502 | 5 | 3.7% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 20,578 | 399,360 | 10 | 4.1% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,461 | 564,206 | 13 | 2.9% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,185 | 1,447,791 | 11 | 0.9% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,132 | 447,111 | 6 | 2.4% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,939 | 370,830 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,463 | 76,656 | 1 | 4.8% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,306 | 201,818 | 3 | 2.8% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,615 | 81,808 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,471 | 493,422 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,118 | 859,567 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,713 | 699,630 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,530 | 139,435 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,843 | 661,232 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,811 | 1,162,537 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,679 | 106,031 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,780 | 154,978 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,546 | 9,400 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 564 | 24,215 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,849,875 | 59,860,654 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 375,356 | 4,685,082 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 181,652 | 248,959 | 9 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 47,508 | 730,707 | 17 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 25,407 | 4,175,241 | 22 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 24,249 | 241,905 | 23 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 14,972 | 44,473 | 28 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,546 | 20,550 | 36 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,463 | 76,656 | 38 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,818 | 117,733 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,615 | 81,808 | 44 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,545 | 153,688 | 50 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,530 | 139,435 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,479 | 377,371 | 54 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,984 | 37,168 | 57 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,876 | 53,379 | 59 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,055 | 101,974 | 70 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,030 | 358,094 | 71 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,002 | 80,436 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,903 | 159,723 | 74 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,546 | 9,400 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,452 | 802,012 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,043 | 58,509 | 97 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 361 | 12,374 | 119 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.9% | 185,998 | 377,959 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 7.1% | 437,299 | 6,066,022 | 2 |
| 3 | [openeurollm](https://huggingface.co/openeurollm) | 4.8% | 8,463 | 76,656 | 12 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4.1% | 20,578 | 399,360 | 7 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.7% | 56,760 | 1,420,502 | 6 |
| 6 | [utter-project](https://huggingface.co/utter-project) | 3.2% | 88,102 | 2,643,371 | 4 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,615 | 81,808 | 14 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.9% | 19,461 | 564,206 | 8 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,306 | 201,818 | 13 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,939 | 370,830 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 13,132 | 447,111 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,464,466 | 306,970,844 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,530 | 139,435 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,546 | 9,400 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,679 | 106,031 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.2% | 75,437 | 6,402,071 | 5 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,471 | 493,422 | 15 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,185 | 1,447,791 | 9 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,780 | 154,978 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,713 | 699,630 | 17 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,118 | 859,567 | 16 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,843 | 661,232 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 564 | 24,215 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,811 | 1,162,537 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
