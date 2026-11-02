# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-02
- **Generated at:** 2026-11-02T15:13:48Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,826,182 | +11,177 | 59,678,461 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,709,543 | -32,059 | 66,518,300 | 2.6% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 562,861 | +2,708 | 46,309,348 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 553,863 | +12,882 | 4,282,736 | 12.6% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 404,903 | -6,020 | 4,682,839 | 8.5% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 322,839 | +4,361 | 32,696,291 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 222,223 | +69 | 2,454,273 | 8.7% | 8.92B | 6 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 200,794 | -1,387 | 5,826,225 | 3.4% | 3.85B | 7 |
| 9 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 189,570 | -5,750 | 16,635,576 | 1.1% | 12.25B | 3 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 181,534 | -1,382 | 4,969,113 | 3.6% | 24.01B | 2 |
| 11 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 163,229 | +8,706 | 230,375 | 49.4% | 12.77B | 5 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 138,229 | -7,216 | 3,004,047 | 4.5% | 24.01B | 1 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 119,985 | -2,850 | 5,598,321 | 2.1% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 98,048 | +1,168 | 7,687,080 | 1.3% | 23.57B | 2 |
| 15 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 74,728 | -33,058 | 739,023 | 8.9% | 8.90B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,904 | -1,201 | 805,573 | 7.6% | 23.57B | 2 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 59,369 | -4,464 | 737,308 | 7.1% | 119.40B | 3 |
| 18 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,896 | -240 | 11,276,474 | 0.5% | 140.63B | 2 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,602 | -1,247 | 8,573,699 | 0.5% | 8.02B | 1 |
| 20 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 44,230 | +268 | 725,879 | 5.4% | 7.77B | 8 |
| 21 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 35,468 | -158,545 | 942,663 | 3.4% | 1.66B | 1 |
| 22 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,366 | +159 | 362,886 | 7.6% | 24.01B | 2 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,841 | -419 | 1,116,550 | 2.2% | 127.70B | 2 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 26,170 | -1,049 | 241,413 | 7.7% | — | 1 |
| 25 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 24,940 | +4,854 | 4,173,402 | 0.6% | 11.34B | 8 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 20,524 | -2,513 | 44,342 | 14.2% | 12.25B | 3 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,711 | -129 | 648,467 | 2.1% | 23.57B | 2 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,617 | -502 | 549,442 | 2.4% | 70.60B | 2 |
| 29 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,518 | +1,257 | 795,177 | 1.7% | 11.25B | 10 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,703 | -5 | 5,046,198 | 0.2% | 122.61B | 1 |
| 31 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,947 | +359 | 4,939,152 | 0.2% | 122.61B | 1 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,585 | -208 | 158,235 | 4.5% | 9.15B | 1 |
| 33 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,166 | -45 | 520,656 | 1.8% | 7.24B | 8 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,948 | +120 | 493,955 | 1.8% | 9.15B | 1 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,599 | -77 | 84,574 | 5.2% | — | 5 |
| 36 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,901 | -2,551 | 20,487 | 7.4% | 27.43B | 3 |
| 37 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,698 | -102 | 5,387,797 | 0.2% | 22.25B | 1 |
| 38 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,446 | +20 | 602,425 | 1.2% | 22.64B | 1 |
| 39 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,431 | -156 | 34,703 | 6.3% | 72.01B | 1 |
| 40 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,294 | +59 | 76,470 | 4.7% | — | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,647 | -8 | 117,209 | 3.5% | 8.42B | 7 |
| 42 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,125 | +25 | 356,091 | 1.3% | 125.03B | 1 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,903 | -94 | 150,847 | 2.4% | 2.25B | 7 |
| 44 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,603 | -176 | 20,798 | 4.6% | 572.6M | 5 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,545 | 0 | 81,704 | 3.1% | 7.04B | 4 |
| 46 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,476 | -11 | 13,851 | 4.8% | 1.51B | 6 |
| 47 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,332 | +114 | 20,319 | 4.4% | 3.83B | 5 |
| 48 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,250 | +83 | 139,814 | 2.2% | 7.48B | 5 |
| 49 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,836 | +12 | 258,037 | 1.4% | 4.76B | 5 |
| 50 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,719 | +85 | 5,164,313 | 0.1% | 22.25B | 1 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,542 | -42 | 377,040 | 1.0% | 7.24B | 8 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,526 | -16 | 139,056 | 1.9% | 7.40B | 3 |
| 53 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,518 | -11 | 153,360 | 1.8% | 7.24B | 4 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,504 | +18 | 909,561 | 0.4% | 23.57B | 2 |
| 55 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,176 | +76 | 62,259 | 2.6% | 1.60B | 5 |
| 56 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,104 | -103 | 169,122 | 1.5% | 11.17B | 16 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,967 | -41 | 39,763 | 2.8% | 2.61B | 3 |
| 58 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,832 | +123 | 53,230 | 2.5% | 8.03B | 7 |
| 59 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,643 | -8 | 36,574 | 2.7% | 56.7M | 1 |
| 60 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,140 | -4 | 95,219 | 1.6% | 2.89B | 1 |
| 61 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,069 | +10 | 26,673 | 2.4% | 22.64B | 1 |
| 62 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,922 | +8 | 42,975 | 2.0% | 13.29B | 3 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,702 | -12 | 34,421 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,631 | +12 | 5,303,363 | 0.0% | 7.25B | 1 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,566 | -19 | 156,891 | 1.0% | 23.57B | 2 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,537 | +23 | 179,348 | 0.9% | 12.25B | 6 |
| 67 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,339 | +159 | 22,422 | 1.9% | 4.30B | 2 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,291 | +33 | 230,297 | 0.7% | 35.13B | 4 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,291 | +18 | 51,971 | 1.5% | 7.77B | 1 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,078 | +19 | 51,354 | 1.4% | 9.24B | 4 |
| 71 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,032 | +13 | 101,805 | 1.0% | 30.68B | 1 |
| 72 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,010 | +4 | 357,954 | 0.4% | — | 3 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,995 | +17 | 80,289 | 1.1% | 7.45B | 1 |
| 74 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,916 | +4 | 107,864 | 0.9% | 7.45B | 1 |
| 75 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,876 | +26 | 159,584 | 0.7% | 1.10B | 1 |
| 76 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,816 | +181 | 19,834 | 1.5% | 12.19B | 2 |
| 77 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,807 | +7 | 34,565 | 1.3% | 22.64B | 1 |
| 78 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,803 | +21 | 186,363 | 0.6% | 6.74B | 1 |
| 79 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,792 | +4 | 415,637 | 0.3% | 1.20B | 1 |
| 80 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,790 | +5 | 303,004 | 0.4% | 6.74B | 2 |
| 81 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,734 | +33 | 40,610 | 1.2% | 70.55B | 3 |
| 82 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,727 | +4 | 147,085 | 0.7% | 13.02B | 1 |
| 83 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,657 | -151 | 9,347 | 1.5% | 4.30B | 3 |
| 84 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,603 | +5 | 418,962 | 0.3% | 353.4M | 1 |
| 85 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,598 | -6 | 54,372 | 1.0% | 7.24B | 5 |
| 86 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,577 | +54 | 9,335 | 1.4% | 9.82B | 1 |
| 87 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,565 | +2 | 400,470 | 0.3% | 3.21B | 1 |
| 88 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,520 | +3 | 53,143 | 1.0% | 7.24B | 1 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,428 | +33 | 801,923 | 0.2% | — | 3 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,387 | -3 | 174,797 | 0.5% | 11.51B | 7 |
| 91 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,369 | +8 | 31,547 | 1.0% | 33.12B | 1 |
| 92 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,348 | +115 | 10,793 | 1.2% | 9.15B | 1 |
| 93 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,284 | -42 | 671,063 | 0.2% | 7.45B | 2 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,225 | 0 | 20,012 | 1.0% | 1.20B | 2 |
| 95 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,192 | -90 | 23,827 | 1.0% | 11.17B | 5 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,101 | +4 | 9,162 | 1.0% | 28.84B | 3 |
| 97 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,083 | +19 | 15,375 | 0.9% | 353.4M | 2 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,050 | +25 | 58,448 | 0.7% | 1.35B | 3 |
| 99 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,019 | -22 | 31,661 | 0.8% | 11.17B | 5 |
| 100 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,016 | -12 | 56,362 | 0.6% | 7.55B | 1 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 971 | +17 | 453,422 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 933 | +29 | 218,796 | 0.3% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 839 | -12 | 44,904 | 0.6% | 12.19B | 2 |
| 104 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 811 | +8 | 233,460 | 0.2% | — | 2 |
| 105 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 769 | +3 | 112,149 | 0.4% | 7.29B | 2 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 717 | +18 | 82,085 | 0.4% | 8.03B | 3 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 707 | -6 | 14,575 | 0.6% | 4.33B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 692 | +33 | 96,375 | 0.4% | 1.35B | 8 |
| 109 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 678 | +22 | 16,848 | 0.6% | 1.54B | 4 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 640 | +16 | 20,725 | 0.5% | 3.20B | 2 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 613 | +28 | 22,079 | 0.5% | 9.24B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 584 | +27 | 27,858 | 0.5% | 9.24B | 2 |
| 113 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 514 | +8 | 3,542 | 0.5% | 30.68B | 1 |
| 114 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 499 | +15 | 4,311 | 0.5% | 8.03B | 3 |
| 115 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 494 | 0 | 1,733 | 0.5% | 27.23B | 3 |
| 116 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 447 | +158 | 84,744 | 0.2% | 9.15B | 1 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 445 | +3 | 1,599 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 411 | +13 | 12,178 | 0.4% | 27.23B | 2 |
| 119 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 361 | 0 | 12,374 | 0.3% | 31.59B | 6 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 347 | -7 | 32,865 | 0.3% | 40.43B | 2 |
| 121 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 339 | -15 | 2,821 | 0.3% | 4.02B | 2 |
| 122 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 322 | +2 | 5,542 | 0.3% | 11.51B | 5 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 318 | +10 | 39,410 | 0.2% | 7.48B | 2 |
| 124 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 314 | +38 | 37,846 | 0.2% | 27.23B | 3 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 305 | +4 | 107,238 | 0.1% | — | 3 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 295 | -48 | 22,102 | 0.2% | 2.61B | 2 |
| 127 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 275 | -3 | 322,237 | 0.1% | 7.24B | 2 |
| 128 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 241 | +3 | 41,902 | 0.2% | 11.17B | 1 |
| 129 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 232 | +2 | 19,695 | 0.2% | 68.98B | 2 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 232 | -42 | 5,171 | 0.2% | 437.8M | 1 |
| 131 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 225 | +9 | 70,512 | 0.1% | 8.03B | 3 |
| 132 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 213 | +1 | 5,056 | 0.2% | 70.55B | 3 |
| 133 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 213 | +2 | 12,709 | 0.2% | 70.55B | 2 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 209 | -10 | 44,651 | 0.1% | 7.70B | 5 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 205 | -1 | 16,623 | 0.2% | 7.29B | 2 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 186 | -3 | 2,557 | 0.2% | — | 1 |
| 137 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 167 | +9 | 28,419 | 0.1% | 46.70B | 6 |
| 138 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 161 | -5 | 7,476 | 0.1% | 31.59B | 6 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 157 | -2 | 5,500 | 0.1% | 353.4M | 2 |
| 140 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 153 | -3 | 3,144 | 0.1% | 560.9M | 2 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 141 | +1 | 1,154 | 0.1% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 95 | +2 | 38,718 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 91 | -2 | 7,254 | 0.1% | 1.20B | 2 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 75 | -1 | 1,315 | 0.1% | 560.9M | 1 |
| 145 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | 0 | 402 | 0.0% | 437.8M | 1 |
| 146 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 45 | 0 | 2,856 | 0.0% | 31.59B | 6 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 43 | +3 | 437 | 0.0% | 321.0M | 1 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 38 | +6 | 228 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 35 | 0 | 258 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | +2 | 199 | 0.0% | 8.16B | 3 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | -1 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | +4 | 279 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +6 | 165 | 0.0% | 437.8M | 1 |
| 154 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 13 | -123 | 6,171 | 0.0% | 12.25B | 3 |
| 155 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | 0 | 1,507 | 0.0% | 31.58B | 2 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,499,438 | 306,531,421 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 520,090 | 6,060,975 | 7 | 8.4% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 167,433 | 358,881 | 6 | 36.5% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 103,441 | 2,637,786 | 11 | 3.8% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 74,151 | 6,396,196 | 12 | 1.1% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 53,742 | 1,414,984 | 5 | 3.5% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 26,143 | 398,933 | 10 | 5.2% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,513 | 563,169 | 13 | 2.9% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,841 | 1,445,281 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,944 | 446,467 | 6 | 2.4% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,730 | 369,772 | 14 | 2.5% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,294 | 76,470 | 1 | 4.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,174 | 201,270 | 3 | 2.7% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,545 | 81,704 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,406 | 493,032 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,195 | 859,216 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,817 | 699,277 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,526 | 139,056 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,800 | 660,958 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,776 | 1,162,316 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,614 | 105,804 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,742 | 154,823 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,577 | 9,335 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 577 | 24,213 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,826,182 | 59,678,461 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 404,903 | 4,682,839 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 163,229 | 230,375 | 11 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 44,230 | 725,879 | 20 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 35,468 | 942,663 | 21 |
| 6 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 24,940 | 4,173,402 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 20,524 | 44,342 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,901 | 20,487 | 36 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,294 | 76,470 | 40 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,647 | 117,209 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,545 | 81,704 | 45 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,542 | 377,040 | 51 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,526 | 139,056 | 52 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,518 | 153,360 | 53 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,832 | 53,230 | 58 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,643 | 36,574 | 59 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,032 | 101,805 | 71 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,010 | 357,954 | 72 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,995 | 80,289 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,876 | 159,584 | 75 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,577 | 9,335 | 86 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,428 | 801,923 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,050 | 58,448 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 361 | 12,374 | 119 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 36.5% | 167,433 | 358,881 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 8.4% | 520,090 | 6,060,975 | 2 |
| 3 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5.2% | 26,143 | 398,933 | 7 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | 4.7% | 8,294 | 76,470 | 12 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.8% | 103,441 | 2,637,786 | 4 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.5% | 53,742 | 1,414,984 | 6 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,545 | 81,704 | 14 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.9% | 19,513 | 563,169 | 8 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 8,174 | 201,270 | 13 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,730 | 369,772 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 12,944 | 446,467 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,499,438 | 306,531,421 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,526 | 139,056 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,577 | 9,335 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,614 | 105,804 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 74,151 | 6,396,196 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 14,841 | 1,445,281 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,406 | 493,032 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,742 | 154,823 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,817 | 699,277 | 17 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,195 | 859,216 | 16 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,800 | 660,958 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 577 | 24,213 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,776 | 1,162,316 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
