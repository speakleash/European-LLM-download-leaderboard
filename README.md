# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-16
- **Generated at:** 2026-10-16T11:02:46Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,216,093 | -41,727 | 58,669,338 | 3.8% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,638,050 | +8,218 | 65,653,849 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 621,652 | -32,071 | 731,762 | 74.7% | 8.90B | 1 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 480,680 | -5,370 | 4,465,948 | 10.5% | 8.05B | 2 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 479,347 | -7,475 | 45,981,694 | 1.0% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 328,042 | +8,731 | 3,871,892 | 8.3% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 325,210 | -1,434 | 16,529,948 | 2.0% | 12.25B | 3 |
| 8 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 304,690 | -7,506 | 2,985,215 | 9.9% | 24.01B | 1 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 293,914 | -3,768 | 4,886,964 | 5.9% | 24.01B | 2 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 260,135 | +11,781 | 5,543,688 | 4.6% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,180 | +2,968 | 32,470,904 | 0.8% | 46.70B | 2 |
| 12 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,060 | -54 | 927,201 | 22.5% | 1.66B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 227,362 | -2,597 | 5,709,566 | 3.9% | 4.25B | 7 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 223,040 | +1,858 | 2,306,870 | 9.3% | 8.92B | 6 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 187,366 | -13,582 | 598,525 | 26.8% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 98,796 | -5,684 | 8,547,792 | 1.1% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,305 | -1,218 | 715,424 | 9.4% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,289 | +440 | 1,107,119 | 6.2% | 127.70B | 2 |
| 19 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 71,149 | +694 | 73,133 | 41.1% | — | 1 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,975 | -287 | 764,436 | 8.2% | 23.57B | 2 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,795 | +962 | 7,623,659 | 0.9% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,005 | +1,060 | 11,250,179 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,554 | +200 | 118,591 | 25.0% | 12.77B | 5 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,586 | -655 | 236,622 | 9.1% | — | 1 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 27,703 | -585 | 696,102 | 3.5% | 7.77B | 8 |
| 26 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 25,079 | +13,284 | 348,661 | 5.6% | 24.01B | 2 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,184 | +23 | 43,281 | 16.9% | 12.25B | 3 |
| 28 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 21,319 | -360 | 4,156,558 | 0.5% | 11.34B | 8 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,299 | +197 | 543,004 | 3.3% | 70.60B | 2 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,627 | +475 | 154,746 | 7.7% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,580 | -1,290 | 639,162 | 2.1% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,718 | -54 | 784,919 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,304 | -216 | 80,271 | 7.4% | — | 5 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,819 | -526 | 487,803 | 2.0% | 9.15B | 1 |
| 35 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,369 | +52 | 514,451 | 1.9% | 7.24B | 8 |
| 36 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,431 | +90 | 4,930,974 | 0.2% | 122.61B | 1 |
| 37 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,115 | +37 | 137,449 | 3.8% | 7.48B | 5 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,286 | -26 | 5,382,422 | 0.1% | 22.25B | 1 |
| 39 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,456 | +91 | 17,710 | 5.5% | 572.6M | 5 |
| 40 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,761 | -4 | 147,515 | 2.3% | 2.25B | 7 |
| 41 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,472 | +63 | 50,969 | 3.6% | 8.03B | 7 |
| 42 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,398 | +4,787 | 81,233 | 3.0% | 7.04B | 4 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,301 | -81 | 111,701 | 2.5% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,167 | -1 | 136,612 | 2.2% | 7.40B | 3 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,003 | -77 | 352,150 | 1.1% | 125.03B | 1 |
| 46 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,840 | +3 | 167,048 | 1.8% | 11.17B | 16 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,734 | -125 | 154,825 | 1.9% | 23.57B | 2 |
| 48 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,683 | -53 | 374,466 | 1.0% | 7.24B | 8 |
| 49 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,672 | +212 | 12,630 | 4.1% | 27.43B | 3 |
| 50 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,617 | -10,755 | 5,161,949 | 0.1% | 22.25B | 1 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,365 | -10 | 150,701 | 1.7% | 7.24B | 4 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,987 | -15 | 254,801 | 1.1% | 4.76B | 5 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,968 | -16 | 5,034,773 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,825 | +16 | 906,214 | 0.4% | 23.57B | 2 |
| 55 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,623 | +14 | 27,591 | 2.8% | 72.01B | 1 |
| 56 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,486 | +42 | 37,207 | 2.5% | 2.61B | 3 |
| 57 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,398 | -80 | 67,566 | 2.0% | 14.08B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,270 | +97 | 59,486 | 2.1% | 1.60B | 5 |
| 59 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,219 | -123 | 670,510 | 0.4% | 7.45B | 2 |
| 60 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,142 | -44 | 400,159 | 0.6% | 3.21B | 1 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,139 | -6 | 93,388 | 1.6% | 2.89B | 1 |
| 62 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,124 | -46 | 415,108 | 0.6% | 1.20B | 1 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,104 | -45 | 418,603 | 0.6% | 353.4M | 1 |
| 64 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,939 | +146 | 9,736 | 2.7% | 1.51B | 6 |
| 65 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,639 | +7 | 24,977 | 2.1% | 22.64B | 1 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,606 | +11 | 86,494 | 1.4% | 2.22B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,537 | -10 | 84,465 | 1.4% | 9.15B | 1 |
| 68 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,516 | +97 | 41,330 | 1.8% | 13.29B | 3 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,489 | +15 | 50,758 | 1.7% | 7.77B | 1 |
| 70 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,445 | +76 | 34,486 | 1.8% | 56.7M | 1 |
| 71 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,420 | 0 | 178,304 | 0.9% | 12.25B | 6 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,242 | +2 | 30,843 | 1.7% | 33.12B | 1 |
| 73 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,021 | +14 | 18,582 | 1.7% | 12.19B | 2 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,861 | -9 | 79,083 | 1.0% | 7.45B | 1 |
| 75 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,859 | +17 | 452,810 | 0.3% | 40.43B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,844 | +1 | 100,568 | 0.9% | 30.68B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,838 | -2 | 106,712 | 0.9% | 7.45B | 1 |
| 78 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,797 | -381 | 50,115 | 1.2% | 9.24B | 4 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,766 | +2 | 356,717 | 0.4% | — | 3 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,752 | +10 | 15,867 | 1.5% | 3.83B | 5 |
| 81 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,664 | -4 | 32,584 | 1.3% | 14.03B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,647 | +1 | 158,395 | 0.6% | 1.10B | 1 |
| 83 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,624 | +2 | 33,459 | 1.2% | 22.64B | 1 |
| 84 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,591 | -26 | 55,793 | 1.0% | 7.55B | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,581 | +4 | 301,897 | 0.4% | 6.74B | 2 |
| 86 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,555 | -9 | 23,269 | 1.3% | 11.17B | 5 |
| 87 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,553 | +30 | 5,301,410 | 0.0% | 7.25B | 1 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,541 | -4 | 185,240 | 0.5% | 6.74B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,533 | 0 | 53,436 | 1.0% | 7.24B | 5 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,520 | -2 | 146,020 | 0.6% | 13.02B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,469 | +39 | 174,116 | 0.5% | 11.51B | 7 |
| 92 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,446 | -5 | 52,249 | 0.9% | 7.24B | 1 |
| 93 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,417 | +85 | 8,505 | 1.3% | 9.82B | 1 |
| 94 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,384 | +31 | 8,390 | 1.3% | 4.30B | 3 |
| 95 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,362 | +22 | 20,901 | 1.1% | 4.30B | 2 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,352 | +157 | 19,519 | 1.1% | 1.20B | 2 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,294 | +19 | 228,674 | 0.4% | 35.13B | 4 |
| 98 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,237 | -6 | 31,140 | 0.9% | 11.17B | 5 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,133 | +14 | 57,783 | 0.7% | 1.35B | 3 |
| 100 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,110 | -4 | 800,921 | 0.1% | — | 3 |
| 101 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,092 | -16 | 10,167 | 1.0% | 9.15B | 1 |
| 102 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,084 | +20 | 39,464 | 0.8% | 70.55B | 3 |
| 103 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,076 | -3,197 | 111,842 | 0.5% | 7.29B | 2 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,027 | +5 | 14,816 | 0.9% | 353.4M | 2 |
| 105 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 807 | -37 | 16,406 | 0.7% | 1.54B | 4 |
| 106 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 710 | -35 | 8,266 | 0.7% | 28.84B | 3 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 676 | +5 | 81,654 | 0.4% | 8.03B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 664 | -23 | 95,931 | 0.3% | 1.35B | 8 |
| 109 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 606 | +84 | 218,212 | 0.2% | 12.19B | 3 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 597 | -13 | 4,067 | 0.6% | 8.03B | 3 |
| 111 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 527 | +4 | 232,831 | 0.2% | — | 2 |
| 112 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 465 | -124 | 20,293 | 0.4% | 3.20B | 2 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 453 | +18 | 27,463 | 0.4% | 9.24B | 2 |
| 114 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 445 | +7 | 14,030 | 0.4% | 4.33B | 3 |
| 115 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 421 | +2 | 44,194 | 0.3% | 12.19B | 2 |
| 116 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 412 | -8 | 322,144 | 0.1% | 7.24B | 2 |
| 117 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 411 | +1 | 3,192 | 0.4% | 30.68B | 1 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 407 | -1 | 32,669 | 0.3% | 40.43B | 2 |
| 119 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 393 | +2 | 1,317 | 0.4% | — | 1 |
| 120 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 361 | +6 | 7,422 | 0.3% | 31.59B | 6 |
| 121 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 358 | -21 | 39,266 | 0.3% | 7.48B | 2 |
| 122 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 356 | +7 | 1,445 | 0.4% | 27.23B | 3 |
| 123 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 355 | +48 | 11,897 | 0.3% | 27.23B | 2 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 336 | +23 | 37,680 | 0.2% | 27.23B | 3 |
| 125 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 329 | -3 | 21,627 | 0.3% | 9.24B | 2 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 313 | -6 | 21,930 | 0.3% | 2.61B | 2 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 300 | +4 | 107,070 | 0.1% | — | 3 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 299 | +5 | 41,776 | 0.2% | 11.17B | 1 |
| 129 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 298 | -2 | 3,075 | 0.3% | 560.9M | 2 |
| 130 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 269 | +1 | 5,337 | 0.3% | 11.51B | 5 |
| 131 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 269 | -2 | 12,628 | 0.2% | 70.55B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 263 | -13 | 70,366 | 0.2% | 8.03B | 3 |
| 133 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 244 | 0 | 5,100 | 0.2% | 437.8M | 1 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 243 | -20 | 44,546 | 0.2% | 7.70B | 5 |
| 135 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 218 | +1 | 19,552 | 0.2% | 68.98B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 213 | +1 | 2,460 | 0.2% | — | 1 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 212 | +1 | 16,514 | 0.2% | 7.29B | 2 |
| 139 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 205 | +2 | 2,578 | 0.2% | 4.02B | 2 |
| 140 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 203 | -3 | 4,991 | 0.2% | 70.55B | 3 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 155 | +4 | 5,411 | 0.1% | 353.4M | 2 |
| 142 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 151 | -4 | 28,334 | 0.1% | 46.70B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | -4 | 38,665 | 0.1% | 70.55B | 3 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 135 | -3 | 1,053 | 0.1% | — | 1 |
| 145 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 146 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 118 | 0 | 7,218 | 0.1% | 1.20B | 2 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 80 | -1 | 408 | 0.1% | 321.0M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 49 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 149 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | +3 | 1,264 | 0.0% | 560.9M | 1 |
| 150 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 39 | +1 | 12,034 | 0.0% | 31.59B | 6 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +2 | 207 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 29 | +1 | 233 | 0.0% | 15.17B | 3 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 25 | +2 | 373 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 24 | 0 | 175 | 0.0% | 8.16B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 124 | 0.0% | 7.24B | 1 |
| 156 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 151 | 0.0% | 437.8M | 1 |
| 157 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | 0 | 264 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,094,136 | 302,913,718 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,138,401 | 5,811,618 | 7 | 19.3% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 492,049 | 2,597,632 | 11 | 18.2% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 72,447 | 6,350,350 | 12 | 1.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 71,149 | 73,133 | 1 | 41.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,315 | 244,530 | 6 | 16.9% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,219 | 1,379,854 | 5 | 2.6% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,742 | 395,193 | 10 | 6.0% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,739 | 1,438,712 | 11 | 1.2% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,347 | 438,327 | 6 | 2.5% |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,975 | 548,088 | 13 | 2.0% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,371 | 362,918 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,918 | 856,305 | 3 | 0.7% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,004 | 154,060 | 2 | 2.4% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 5,902 | 195,513 | 3 | 2.0% |
| 16 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,398 | 81,233 | 1 | 3.0% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,167 | 136,612 | 1 | 2.2% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,095 | 696,610 | 2 | 0.6% |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,708 | 489,655 | 3 | 0.8% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,347 | 658,614 | 2 | 0.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,308 | 104,168 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,155 | 1,160,374 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,797 | 153,714 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,417 | 8,505 | 1 | 1.3% |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 677 | 23,793 | 4 | 0.5% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,216,093 | 58,669,338 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 621,652 | 731,762 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,060 | 927,201 | 12 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 71,149 | 73,133 | 19 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,554 | 118,591 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 27,703 | 696,102 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,184 | 43,281 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 21,319 | 4,156,558 | 28 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,472 | 50,969 | 41 |
| 10 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,398 | 81,233 | 42 |
| 11 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,301 | 111,701 | 43 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,167 | 136,612 | 44 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,683 | 374,466 | 48 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,672 | 12,630 | 49 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,365 | 150,701 | 51 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,398 | 67,566 | 57 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,219 | 670,510 | 59 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 3B Preview | 3,142 | 400,159 | 60 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,844 | 100,568 | 76 |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,766 | 356,717 | 79 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,647 | 158,395 | 82 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,417 | 8,505 | 93 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,133 | 57,783 | 99 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,110 | 800,921 | 100 |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 361 | 7,422 | 120 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 41.1% | 71,149 | 73,133 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 19.3% | 1,138,401 | 5,811,618 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 18.2% | 492,049 | 2,597,632 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 16.9% | 58,315 | 244,530 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,742 | 395,193 | 8 |
| 6 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,398 | 81,233 | 16 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,219 | 1,379,854 | 7 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,347 | 438,327 | 10 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,371 | 362,918 | 12 |
| 10 | [Almawave](https://huggingface.co/Almawave) | 2.4% | 6,004 | 154,060 | 14 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 7,094,136 | 302,913,718 | 1 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,167 | 136,612 | 17 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,975 | 548,088 | 11 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.0% | 5,902 | 195,513 | 15 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,417 | 8,505 | 24 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 17,739 | 1,438,712 | 9 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,308 | 104,168 | 21 |
| 18 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 72,447 | 6,350,350 | 4 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,708 | 489,655 | 19 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,918 | 856,305 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,797 | 153,714 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,095 | 696,610 | 18 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 677 | 23,793 | 25 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,347 | 658,614 | 20 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,155 | 1,160,374 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
