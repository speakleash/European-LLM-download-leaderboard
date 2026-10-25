# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-25
- **Generated at:** 2026-10-25T11:01:20Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,905,726 | -13,374 | 59,130,716 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,780,710 | -6 | 66,169,817 | 2.7% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 472,468 | +28,114 | 46,126,536 | 1.0% | 7.24B | 2 |
| 4 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 443,437 | -20,039 | 4,588,421 | 9.5% | 8.05B | 2 |
| 5 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 410,655 | +16,018 | 4,064,248 | 9.9% | 13.95B | 6 |
| 6 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 331,302 | -30,145 | 734,635 | 39.7% | 8.90B | 1 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 308,312 | +11,029 | 16,601,367 | 1.8% | 12.25B | 3 |
| 8 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 282,446 | +4,228 | 32,589,382 | 0.9% | 46.70B | 2 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,641 | -13,438 | 4,926,843 | 4.5% | 24.01B | 2 |
| 10 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 215,365 | -3,969 | 5,769,276 | 3.7% | 4.25B | 7 |
| 11 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 195,608 | -6,602 | 2,996,541 | 6.3% | 24.01B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 192,564 | -2,970 | 2,364,459 | 7.8% | 8.92B | 6 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 189,544 | +2,872 | 934,568 | 18.3% | 1.66B | 1 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 181,449 | -4,058 | 5,575,051 | 3.2% | 24.01B | 1 |
| 15 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 84,011 | -707 | 7,654,900 | 1.1% | 23.57B | 2 |
| 16 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 80,710 | +10,233 | 146,900 | 32.7% | 12.77B | 5 |
| 17 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 74,008 | -23 | 76,070 | 42.0% | — | 1 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,387 | -1,713 | 722,309 | 8.4% | 119.40B | 3 |
| 19 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 68,022 | -12,427 | 600,156 | 9.7% | 22.64B | 1 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,018 | +122 | 784,777 | 7.7% | 23.57B | 2 |
| 21 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,459 | -473 | 11,266,916 | 0.6% | 140.63B | 2 |
| 22 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,760 | -5,064 | 8,558,592 | 0.7% | 8.02B | 1 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 51,410 | -7,067 | 1,112,015 | 4.2% | 127.70B | 2 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 37,930 | +37 | 713,969 | 4.7% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,957 | +225 | 358,638 | 7.2% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,548 | -1,080 | 238,244 | 8.1% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,508 | +8 | 43,892 | 17.0% | 12.25B | 3 |
| 28 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,212 | -288 | 4,161,591 | 0.5% | 11.34B | 8 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 19,591 | -413 | 547,819 | 3.0% | 70.60B | 2 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,211 | +262 | 644,637 | 1.9% | 23.57B | 2 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,420 | -438 | 156,560 | 5.2% | 9.15B | 1 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,283 | -56 | 789,088 | 1.5% | 11.25B | 10 |
| 33 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,351 | +47 | 5,044,031 | 0.2% | 122.61B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,583 | +49 | 19,916 | 9.7% | 27.43B | 3 |
| 35 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,224 | -51 | 517,609 | 1.8% | 7.24B | 8 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,029 | -431 | 82,483 | 6.0% | — | 5 |
| 37 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,829 | +141 | 490,659 | 1.8% | 9.15B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,222 | -31 | 4,934,607 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,069 | +145 | 5,384,705 | 0.1% | 22.25B | 1 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,432 | +81 | 138,679 | 3.1% | 7.48B | 5 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,740 | -676 | 19,668 | 5.6% | 572.6M | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,684 | +57 | 115,079 | 3.1% | 8.42B | 7 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,558 | +137 | 354,096 | 1.2% | 125.03B | 1 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,456 | +10 | 81,464 | 3.0% | 7.04B | 4 |
| 45 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,408 | +586 | 30,413 | 4.1% | 72.01B | 1 |
| 46 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,399 | +16 | 148,767 | 2.2% | 2.25B | 7 |
| 47 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,975 | -20 | 137,910 | 2.1% | 7.40B | 3 |
| 48 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,732 | +144 | 156,195 | 1.8% | 23.57B | 2 |
| 49 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,575 | -36 | 168,201 | 1.7% | 11.17B | 16 |
| 50 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,414 | -123 | 5,162,936 | 0.1% | 22.25B | 1 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,408 | +37 | 152,046 | 1.7% | 7.24B | 4 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,328 | -19 | 375,594 | 0.9% | 7.24B | 8 |
| 53 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,102 | +181 | 11,940 | 3.7% | 1.51B | 6 |
| 54 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,831 | -424 | 51,895 | 2.5% | 8.03B | 7 |
| 55 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,827 | +39 | 60,950 | 2.4% | 1.60B | 5 |
| 56 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,788 | +26 | 38,737 | 2.7% | 2.61B | 3 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,566 | -105 | 255,716 | 1.0% | 4.76B | 5 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,106 | +596 | 34,195 | 2.3% | 14.03B | 1 |
| 59 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,092 | +56 | 907,331 | 0.3% | 23.57B | 2 |
| 60 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,081 | +552 | 17,736 | 2.6% | 3.83B | 5 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,040 | +9 | 94,273 | 1.6% | 2.89B | 1 |
| 62 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,957 | +48 | 35,282 | 2.2% | 56.7M | 1 |
| 63 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,723 | +67 | 42,119 | 1.9% | 13.29B | 3 |
| 64 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,682 | -16 | 25,623 | 2.1% | 22.64B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,463 | -5 | 178,833 | 0.9% | 12.25B | 6 |
| 66 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,351 | +39 | 31,131 | 1.8% | 33.12B | 1 |
| 67 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,287 | -500 | 415,476 | 0.4% | 1.20B | 1 |
| 68 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,139 | +191 | 19,237 | 1.8% | 12.19B | 2 |
| 69 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,112 | -514 | 400,315 | 0.4% | 3.21B | 1 |
| 70 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,072 | -505 | 418,779 | 0.4% | 353.4M | 1 |
| 71 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,030 | +131 | 5,302,377 | 0.0% | 7.25B | 1 |
| 72 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,007 | -95 | 51,264 | 1.3% | 7.77B | 1 |
| 73 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,935 | +52 | 50,728 | 1.3% | 9.24B | 4 |
| 74 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,935 | -78 | 670,794 | 0.3% | 7.45B | 2 |
| 75 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,914 | +174 | 21,673 | 1.6% | 4.30B | 2 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,876 | +3 | 101,169 | 0.9% | 30.68B | 1 |
| 77 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,849 | +19 | 357,319 | 0.4% | — | 3 |
| 78 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,847 | +16 | 79,662 | 1.0% | 7.45B | 1 |
| 79 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,791 | +14 | 107,284 | 0.9% | 7.45B | 1 |
| 80 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,693 | +41 | 8,961 | 1.6% | 4.30B | 3 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,685 | +26 | 158,952 | 0.7% | 1.10B | 1 |
| 82 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,680 | +91 | 229,386 | 0.5% | 35.13B | 4 |
| 83 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,679 | +7 | 34,000 | 1.3% | 22.64B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,670 | +18 | 302,442 | 0.4% | 6.74B | 2 |
| 85 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,614 | +21 | 185,761 | 0.6% | 6.74B | 1 |
| 86 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,605 | +20 | 146,543 | 0.7% | 13.02B | 1 |
| 87 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,552 | +12 | 56,041 | 1.0% | 7.55B | 1 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,545 | +16 | 53,908 | 1.0% | 7.24B | 5 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,518 | -9 | 8,945 | 1.4% | 9.82B | 1 |
| 90 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,464 | +19 | 52,693 | 1.0% | 7.24B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,427 | -20 | 174,502 | 0.5% | 11.51B | 7 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,389 | -14 | 23,565 | 1.1% | 11.17B | 5 |
| 93 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,337 | +17 | 39,952 | 1.0% | 70.55B | 3 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,277 | +80 | 19,800 | 1.1% | 1.20B | 2 |
| 95 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,198 | -9 | 31,450 | 0.9% | 11.17B | 5 |
| 96 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,188 | +40 | 801,384 | 0.1% | — | 3 |
| 97 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,164 | +19 | 10,416 | 1.1% | 9.15B | 1 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,038 | -21 | 58,150 | 0.7% | 1.35B | 3 |
| 99 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 951 | +17 | 14,995 | 0.8% | 353.4M | 2 |
| 100 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 880 | -176 | 453,112 | 0.2% | 40.43B | 1 |
| 101 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 876 | +11 | 111,957 | 0.4% | 7.29B | 2 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 795 | -18 | 218,592 | 0.2% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 757 | +1 | 8,659 | 0.7% | 28.84B | 3 |
| 104 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 722 | -150 | 16,609 | 0.6% | 1.54B | 4 |
| 105 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 665 | -14 | 81,854 | 0.4% | 8.03B | 3 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 617 | -10 | 14,366 | 0.5% | 4.33B | 3 |
| 107 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 588 | -11 | 44,537 | 0.4% | 12.19B | 2 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 586 | -43 | 96,153 | 0.3% | 1.35B | 8 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 564 | +18 | 4,213 | 0.5% | 8.03B | 3 |
| 110 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 483 | -21 | 21,863 | 0.4% | 9.24B | 2 |
| 111 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 447 | -16 | 3,359 | 0.4% | 30.68B | 1 |
| 112 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 401 | -22 | 20,388 | 0.3% | 3.20B | 2 |
| 113 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 389 | +14 | 1,475 | 0.4% | — | 1 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 387 | -5 | 32,794 | 0.3% | 40.43B | 2 |
| 115 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 347 | -54 | 84,512 | 0.2% | 9.15B | 1 |
| 116 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 345 | +2 | 12,003 | 0.3% | 27.23B | 2 |
| 117 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 331 | -26 | 27,544 | 0.3% | 9.24B | 2 |
| 118 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 331 | +21 | 1,514 | 0.3% | 27.23B | 3 |
| 119 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 326 | +1 | 232,912 | 0.1% | — | 2 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 325 | -29 | 22,010 | 0.3% | 2.61B | 2 |
| 121 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 323 | +18 | 37,759 | 0.2% | 27.23B | 3 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 319 | -1 | 322,200 | 0.1% | 7.24B | 2 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 290 | +6 | 107,144 | 0.1% | — | 3 |
| 124 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 287 | +4 | 5,424 | 0.3% | 11.51B | 5 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 283 | +2 | 39,345 | 0.2% | 7.48B | 2 |
| 126 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 280 | +13 | 2,693 | 0.3% | 4.02B | 2 |
| 127 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 278 | +4 | 41,838 | 0.2% | 11.17B | 1 |
| 128 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 259 | +3 | 5,126 | 0.2% | 437.8M | 1 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 258 | -1 | 12,682 | 0.2% | 70.55B | 2 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 231 | +5 | 19,628 | 0.2% | 68.98B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 207 | -5 | 44,587 | 0.1% | 7.70B | 5 |
| 132 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 204 | -3 | 5,022 | 0.2% | 70.55B | 3 |
| 133 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 204 | -13 | 7,454 | 0.2% | 31.59B | 6 |
| 134 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 199 | -1 | 2,511 | 0.2% | — | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 186 | +11 | 16,575 | 0.2% | 7.29B | 2 |
| 136 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 176 | +4 | 70,409 | 0.1% | 8.03B | 3 |
| 137 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 171 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 154 | -1 | 5,449 | 0.1% | 353.4M | 2 |
| 139 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 148 | -4 | 3,090 | 0.1% | 560.9M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 148 | 0 | 28,366 | 0.1% | 46.70B | 6 |
| 141 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 128 | -9 | 1,112 | 0.1% | — | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 104 | -6 | 38,698 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 102 | -2 | 7,237 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 84 | +6 | 429 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 53 | +3 | 1,284 | 0.1% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 47 | +12 | 2,853 | 0.0% | 31.59B | 6 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 40 | +1 | 390 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | +2 | 251 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | 0 | 189 | 0.0% | 8.16B | 3 |
| 151 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 28 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | 0 | 213 | 0.0% | 437.8M | 1 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 127 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | -3 | 269 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 12 | -1 | 153 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,676,171 | 304,748,368 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 813,661 | 5,950,632 | 7 | 13.4% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 319,222 | 2,615,986 | 11 | 11.8% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 84,422 | 273,898 | 6 | 22.6% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 74,008 | 76,070 | 1 | 42.0% |
| 6 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 68,698 | 6,368,613 | 12 | 1.1% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 46,603 | 1,399,906 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,250 | 397,243 | 10 | 6.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,939 | 558,932 | 13 | 3.2% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,384 | 1,441,735 | 11 | 1.0% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,857 | 442,600 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,312 | 366,273 | 14 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,174 | 199,011 | 3 | 2.4% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,573 | 857,740 | 3 | 0.6% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,456 | 81,464 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,975 | 137,910 | 1 | 2.1% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,904 | 491,256 | 3 | 0.8% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,647 | 697,794 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,519 | 659,761 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,394 | 104,968 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,035 | 1,161,068 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,624 | 154,303 | 2 | 0.6% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,518 | 8,945 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 450 | 23,842 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,905,726 | 59,130,716 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 443,437 | 4,588,421 | 4 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 189,544 | 934,568 | 13 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 80,710 | 146,900 | 16 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 74,008 | 76,070 | 17 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 37,930 | 713,969 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,508 | 43,892 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,212 | 4,161,591 | 28 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,583 | 19,916 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,684 | 115,079 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,456 | 81,464 | 44 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,975 | 137,910 | 47 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,408 | 152,046 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,328 | 375,594 | 52 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,831 | 51,895 | 54 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 2,957 | 35,282 | 62 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 1,935 | 670,794 | 74 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,876 | 101,169 | 76 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,849 | 357,319 | 77 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,685 | 158,952 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,518 | 8,945 | 89 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,188 | 801,384 | 96 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,038 | 58,150 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 204 | 7,454 | 133 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 42.0% | 74,008 | 76,070 | 5 |
| 2 | [cjvt](https://huggingface.co/cjvt) | 22.6% | 84,422 | 273,898 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 13.4% | 813,661 | 5,950,632 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 11.8% | 319,222 | 2,615,986 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,250 | 397,243 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 20,939 | 558,932 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 46,603 | 1,399,906 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,456 | 81,464 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 13,857 | 442,600 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,312 | 366,273 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,174 | 199,011 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,676,171 | 304,748,368 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,975 | 137,910 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,518 | 8,945 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,394 | 104,968 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 68,698 | 6,368,613 | 6 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,384 | 1,441,735 | 10 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,904 | 491,256 | 17 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.6% | 1,624 | 154,303 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,647 | 697,794 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,573 | 857,740 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,519 | 659,761 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 450 | 23,842 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,035 | 1,161,068 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
