# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-18
- **Generated at:** 2026-10-18T10:40:55Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,141,313 | -52,194 | 58,789,407 | 3.6% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,684,028 | +20,278 | 65,805,689 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 556,067 | -32,959 | 732,680 | 66.8% | 8.90B | 1 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 478,264 | -2,601 | 4,497,330 | 10.4% | 8.05B | 2 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 457,435 | -5,969 | 46,003,159 | 1.0% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 353,905 | +12,408 | 3,917,293 | 8.8% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 318,962 | -4,518 | 16,542,719 | 1.9% | 12.25B | 3 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 285,243 | -5,614 | 4,901,814 | 5.7% | 24.01B | 2 |
| 9 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 273,562 | -17,463 | 2,986,641 | 8.9% | 24.01B | 1 |
| 10 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,236 | +3,295 | 32,497,944 | 0.8% | 46.70B | 2 |
| 11 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,513 | +111 | 928,380 | 22.5% | 1.66B | 1 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 224,979 | -736 | 5,724,467 | 3.9% | 4.25B | 7 |
| 13 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 223,788 | +2,499 | 2,320,858 | 9.2% | 8.92B | 6 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 220,698 | -39,075 | 5,551,642 | 3.9% | 24.01B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 160,454 | -13,486 | 598,956 | 23.0% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 80,244 | -6,462 | 8,550,171 | 0.9% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,991 | -635 | 716,950 | 9.2% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,967 | +97 | 1,108,489 | 6.2% | 127.70B | 2 |
| 19 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,562 | +1,239 | 7,631,972 | 1.0% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 73,075 | +838 | 75,061 | 41.7% | — | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,367 | -140 | 769,810 | 8.2% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,312 | -310 | 11,253,722 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,186 | -580 | 119,099 | 24.7% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 35,204 | +950 | 705,618 | 4.4% | 7.77B | 8 |
| 25 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,667 | +60 | 237,144 | 9.1% | — | 1 |
| 26 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 25,614 | +205 | 349,411 | 5.7% | 24.01B | 2 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,282 | +59 | 43,453 | 16.9% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,796 | +44 | 544,856 | 3.4% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,554 | -541 | 4,157,454 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,521 | -568 | 155,371 | 7.3% | 9.15B | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,946 | +32 | 785,982 | 1.6% | 11.25B | 10 |
| 32 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,600 | -756 | 640,435 | 1.8% | 23.57B | 2 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,921 | -258 | 81,046 | 7.1% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,585 | +39 | 515,344 | 1.9% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,387 | -66 | 19,563 | 9.5% | 27.43B | 3 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,306 | -65 | 488,474 | 1.9% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,910 | +107 | 4,931,889 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,316 | +186 | 137,816 | 3.9% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,441 | +48 | 5,382,872 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,648 | +60 | 17,980 | 5.6% | 572.6M | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,610 | +1,288 | 113,251 | 3.1% | 8.42B | 7 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,061 | +5 | 148,005 | 2.4% | 2.25B | 7 |
| 43 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,449 | +13 | 81,312 | 3.0% | 7.04B | 4 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,433 | -29 | 51,241 | 3.6% | 8.03B | 7 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,205 | +71 | 352,695 | 1.1% | 125.03B | 1 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,199 | -36 | 136,984 | 2.2% | 7.40B | 3 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,927 | +24 | 167,402 | 1.8% | 11.17B | 16 |
| 48 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,754 | +18 | 5,162,272 | 0.1% | 22.25B | 1 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,676 | +4 | 374,803 | 1.0% | 7.24B | 8 |
| 50 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,533 | -52 | 155,211 | 1.8% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,454 | +50 | 151,074 | 1.8% | 7.24B | 4 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,068 | +43 | 254,953 | 1.1% | 4.76B | 5 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,021 | +41 | 5,035,030 | 0.1% | 122.61B | 1 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,903 | +121 | 37,797 | 2.8% | 2.61B | 3 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,803 | -65 | 906,425 | 0.4% | 23.57B | 2 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,702 | +54 | 60,028 | 2.3% | 1.60B | 5 |
| 57 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,618 | -5 | 27,719 | 2.8% | 72.01B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,221 | -37 | 67,776 | 1.9% | 14.08B | 1 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,190 | +15 | 93,631 | 1.6% | 2.89B | 1 |
| 60 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,187 | +45 | 10,086 | 2.9% | 1.51B | 6 |
| 61 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,996 | -51 | 670,578 | 0.4% | 7.45B | 2 |
| 62 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,955 | -92 | 415,243 | 0.6% | 1.20B | 1 |
| 63 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,878 | -186 | 400,191 | 0.6% | 3.21B | 1 |
| 64 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,859 | -171 | 418,660 | 0.6% | 353.4M | 1 |
| 65 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,687 | +20 | 25,130 | 2.1% | 22.64B | 1 |
| 66 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,652 | +81 | 41,547 | 1.9% | 13.29B | 3 |
| 67 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,619 | -6 | 86,699 | 1.4% | 2.22B | 1 |
| 68 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,594 | +49 | 50,890 | 1.7% | 7.77B | 1 |
| 69 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,536 | +2 | 84,473 | 1.4% | 9.15B | 1 |
| 70 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,521 | +16 | 34,624 | 1.9% | 56.7M | 1 |
| 71 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,491 | +25 | 178,473 | 0.9% | 12.25B | 6 |
| 72 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,365 | +462 | 33,306 | 1.8% | 14.03B | 1 |
| 73 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,252 | +10 | 30,884 | 1.7% | 33.12B | 1 |
| 74 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,088 | +18 | 18,684 | 1.8% | 12.19B | 2 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,921 | +26 | 452,892 | 0.3% | 40.43B | 1 |
| 76 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,881 | +79 | 16,063 | 1.6% | 3.83B | 5 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,880 | +8 | 79,232 | 1.0% | 7.45B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,870 | +7 | 100,703 | 0.9% | 30.68B | 1 |
| 79 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,869 | +18 | 106,855 | 0.9% | 7.45B | 1 |
| 80 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,854 | +26 | 50,267 | 1.2% | 9.24B | 4 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,810 | +21 | 356,864 | 0.4% | — | 3 |
| 82 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,751 | +33 | 21,309 | 1.4% | 4.30B | 2 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,670 | +13 | 158,535 | 0.6% | 1.10B | 1 |
| 84 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,643 | +3 | 33,589 | 1.2% | 22.64B | 1 |
| 85 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,627 | +10 | 55,852 | 1.0% | 7.55B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,617 | +18 | 302,028 | 0.4% | 6.74B | 2 |
| 87 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,580 | +20 | 23,367 | 1.3% | 11.17B | 5 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,571 | +26 | 53,568 | 1.0% | 7.24B | 5 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,567 | +12 | 185,360 | 0.5% | 6.74B | 1 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,551 | +15 | 146,142 | 0.6% | 13.02B | 1 |
| 91 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,532 | +1 | 5,301,522 | 0.0% | 7.25B | 1 |
| 92 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,488 | +24 | 52,379 | 1.0% | 7.24B | 1 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,467 | -39 | 174,207 | 0.5% | 11.51B | 7 |
| 94 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,429 | +20 | 8,571 | 1.3% | 9.82B | 1 |
| 95 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,396 | +2 | 8,434 | 1.3% | 4.30B | 3 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,362 | +11 | 19,575 | 1.1% | 1.20B | 2 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,323 | +11 | 228,789 | 0.4% | 35.13B | 4 |
| 98 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,273 | +26 | 31,243 | 1.0% | 11.17B | 5 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,182 | +18 | 57,875 | 0.7% | 1.35B | 3 |
| 100 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,148 | +27 | 10,263 | 1.0% | 9.15B | 1 |
| 101 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,137 | +3 | 39,551 | 0.8% | 70.55B | 3 |
| 102 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,064 | +3 | 111,865 | 0.5% | 7.29B | 2 |
| 103 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,020 | -92 | 800,989 | 0.1% | — | 3 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,006 | -28 | 14,846 | 0.9% | 353.4M | 2 |
| 105 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 836 | +23 | 16,455 | 0.7% | 1.54B | 4 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 703 | +42 | 96,000 | 0.4% | 1.35B | 8 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 698 | +17 | 81,713 | 0.4% | 8.03B | 3 |
| 108 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 635 | -4 | 218,297 | 0.2% | 12.19B | 3 |
| 109 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 602 | -84 | 8,300 | 0.6% | 28.84B | 3 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 601 | -2 | 4,089 | 0.6% | 8.03B | 3 |
| 111 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 482 | +8 | 20,325 | 0.4% | 3.20B | 2 |
| 112 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 481 | +4 | 14,084 | 0.4% | 4.33B | 3 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 476 | +17 | 27,488 | 0.4% | 9.24B | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 455 | -7 | 44,254 | 0.3% | 12.19B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 433 | +15 | 3,224 | 0.4% | 30.68B | 1 |
| 116 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 428 | +48 | 21,731 | 0.4% | 9.24B | 2 |
| 117 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 396 | -40 | 32,726 | 0.3% | 40.43B | 2 |
| 118 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 385 | +7 | 39,309 | 0.3% | 7.48B | 2 |
| 119 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 365 | +4 | 11,911 | 0.3% | 27.23B | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 364 | -32 | 322,169 | 0.1% | 7.24B | 2 |
| 121 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 360 | -141 | 232,837 | 0.1% | — | 2 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 336 | -2 | 37,691 | 0.2% | 27.23B | 3 |
| 123 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 332 | +15 | 21,954 | 0.3% | 2.61B | 2 |
| 124 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 317 | -41 | 1,480 | 0.3% | 27.23B | 3 |
| 125 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 308 | -64 | 1,341 | 0.3% | — | 1 |
| 126 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 299 | +2 | 41,783 | 0.2% | 11.17B | 1 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 297 | +3 | 107,083 | 0.1% | — | 3 |
| 128 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 288 | +2 | 3,083 | 0.3% | 560.9M | 2 |
| 129 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 268 | +1 | 5,347 | 0.3% | 11.51B | 5 |
| 130 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 258 | -6 | 12,637 | 0.2% | 70.55B | 2 |
| 131 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 257 | -3 | 70,374 | 0.2% | 8.03B | 3 |
| 132 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 256 | -66 | 7,422 | 0.2% | 31.59B | 6 |
| 133 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 249 | 0 | 5,108 | 0.2% | 437.8M | 1 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 244 | -4 | 44,557 | 0.2% | 7.70B | 5 |
| 135 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 227 | +8 | 19,568 | 0.2% | 68.98B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 217 | +4 | 2,474 | 0.2% | — | 1 |
| 138 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 208 | +21 | 2,604 | 0.2% | 4.02B | 2 |
| 139 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 204 | +2 | 4,999 | 0.2% | 70.55B | 3 |
| 140 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 200 | -2 | 16,520 | 0.2% | 7.29B | 2 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 156 | -3 | 5,422 | 0.1% | 353.4M | 2 |
| 142 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 153 | +3 | 28,342 | 0.1% | 46.70B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | -7 | 38,680 | 0.1% | 70.55B | 3 |
| 144 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 145 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 119 | -3 | 7,226 | 0.1% | 1.20B | 2 |
| 146 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 100 | -2 | 1,058 | 0.1% | — | 1 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 81 | 0 | 410 | 0.1% | 321.0M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | -6 | 2,836 | 0.0% | 31.59B | 6 |
| 149 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 41 | -1 | 1,269 | 0.0% | 560.9M | 1 |
| 150 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 34 | -5 | 12,034 | 0.0% | 31.59B | 6 |
| 151 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 32 | 0 | 236 | 0.0% | 15.17B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | +1 | 208 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | +1 | 377 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | 0 | 177 | 0.0% | 8.16B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 124 | 0.0% | 7.24B | 1 |
| 156 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 265 | 0.0% | 437.8M | 1 |
| 157 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | 0 | 151 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,975,334 | 303,373,954 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,071,461 | 5,846,714 | 7 | 18.0% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 464,595 | 2,602,051 | 11 | 17.2% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 73,075 | 75,061 | 1 | 41.7% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 72,985 | 6,354,926 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,011 | 245,317 | 6 | 16.8% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 46,176 | 1,390,131 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,914 | 395,648 | 10 | 6.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,264 | 555,960 | 13 | 3.1% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,287 | 1,439,457 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,137 | 439,623 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,594 | 363,849 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,239 | 197,117 | 3 | 2.4% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,745 | 856,665 | 3 | 0.7% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,840 | 154,475 | 2 | 2.3% |
| 16 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,449 | 81,312 | 1 | 3.0% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,199 | 136,984 | 1 | 2.2% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,040 | 696,972 | 2 | 0.6% |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,788 | 490,037 | 3 | 0.8% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,427 | 658,892 | 2 | 0.5% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,361 | 104,340 | 4 | 1.2% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,904 | 1,160,477 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,885 | 153,875 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,429 | 8,571 | 1 | 1.3% |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 561 | 23,793 | 4 | 0.5% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,141,313 | 58,789,407 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 556,067 | 732,680 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,513 | 928,380 | 11 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 73,075 | 75,061 | 20 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,186 | 119,099 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 35,204 | 705,618 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,282 | 43,453 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,554 | 4,157,454 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,387 | 19,563 | 35 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,610 | 113,251 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,449 | 81,312 | 43 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,433 | 51,241 | 44 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,199 | 136,984 | 46 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,676 | 374,803 | 49 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,454 | 151,074 | 51 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,221 | 67,776 | 58 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,996 | 670,578 | 61 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 2,955 | 415,243 | 62 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,870 | 100,703 | 78 |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,810 | 356,864 | 81 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,670 | 158,535 | 83 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,429 | 8,571 | 94 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,182 | 57,875 | 99 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,020 | 800,989 | 103 |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 256 | 7,422 | 132 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 41.7% | 73,075 | 75,061 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 18.0% | 1,071,461 | 5,846,714 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 17.2% | 464,595 | 2,602,051 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 16.8% | 58,011 | 245,317 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,914 | 395,648 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 46,176 | 1,390,131 | 7 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.1% | 20,264 | 555,960 | 9 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,449 | 81,312 | 16 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,137 | 439,623 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,594 | 363,849 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,239 | 197,117 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 6,975,334 | 303,373,954 | 1 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 2.3% | 5,840 | 154,475 | 15 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,199 | 136,984 | 17 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,429 | 8,571 | 24 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,361 | 104,340 | 21 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 72,985 | 6,354,926 | 5 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,287 | 1,439,457 | 10 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,788 | 490,037 | 19 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,885 | 153,875 | 23 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,745 | 856,665 | 14 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,040 | 696,972 | 18 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 561 | 23,793 | 25 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,427 | 658,892 | 20 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,904 | 1,160,477 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
