# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-24
- **Generated at:** 2026-10-24T10:36:56Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,919,100 | -12,276 | 59,072,753 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,780,716 | +33,752 | 66,126,919 | 2.7% | 7.24B | 1 |
| 3 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 463,476 | +5,050 | 4,574,335 | 9.9% | 8.05B | 2 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 444,354 | +16,650 | 46,088,247 | 1.0% | 7.24B | 2 |
| 5 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 394,637 | +20,902 | 4,040,113 | 9.5% | 13.95B | 6 |
| 6 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 361,447 | -30,792 | 734,069 | 43.3% | 8.90B | 1 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 297,283 | -5,915 | 16,581,400 | 1.8% | 12.25B | 3 |
| 8 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 278,218 | +12,647 | 32,578,473 | 0.9% | 46.70B | 2 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 239,079 | -8,218 | 4,923,921 | 4.8% | 24.01B | 2 |
| 10 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 219,334 | +4,051 | 5,762,855 | 3.7% | 4.25B | 7 |
| 11 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 202,210 | -5,785 | 2,994,613 | 6.5% | 24.01B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 195,534 | -4,371 | 2,356,636 | 8.0% | 8.92B | 6 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 186,672 | +1,638 | 931,389 | 18.1% | 1.66B | 1 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 185,507 | -2,439 | 5,572,731 | 3.3% | 24.01B | 1 |
| 15 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 84,718 | +2,482 | 7,652,691 | 1.1% | 23.57B | 2 |
| 16 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 80,449 | -13,364 | 599,981 | 11.5% | 22.64B | 1 |
| 17 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 74,031 | +4 | 76,055 | 42.0% | — | 1 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,100 | -914 | 721,514 | 8.7% | 119.40B | 3 |
| 19 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 70,477 | +10,813 | 136,585 | 29.8% | 12.77B | 5 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 67,896 | +947 | 782,371 | 7.7% | 23.57B | 2 |
| 21 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,932 | +1,854 | 11,265,599 | 0.6% | 140.63B | 2 |
| 22 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,824 | -3,841 | 8,557,595 | 0.7% | 8.02B | 1 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,477 | -6,726 | 1,111,443 | 4.8% | 127.70B | 2 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 37,893 | +1,129 | 713,395 | 4.7% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,732 | +492 | 358,252 | 7.1% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 28,628 | -723 | 238,125 | 8.5% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,500 | +65 | 43,868 | 17.0% | 12.25B | 3 |
| 28 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,500 | +297 | 4,161,163 | 0.5% | 11.34B | 8 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 20,004 | -431 | 547,605 | 3.1% | 70.60B | 2 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,949 | +338 | 644,195 | 1.9% | 23.57B | 2 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,858 | -2,055 | 156,429 | 5.4% | 9.15B | 1 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,339 | -151 | 788,626 | 1.5% | 11.25B | 10 |
| 33 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,304 | +1,555 | 5,043,900 | 0.2% | 122.61B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,534 | +46 | 19,850 | 9.6% | 27.43B | 3 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,460 | -291 | 82,360 | 6.3% | — | 5 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,275 | +165 | 517,288 | 1.8% | 7.24B | 8 |
| 37 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,688 | +124 | 490,285 | 1.8% | 9.15B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,253 | +174 | 4,934,168 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,924 | +281 | 5,384,394 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,416 | +55 | 19,625 | 6.2% | 572.6M | 5 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,351 | -173 | 138,430 | 3.1% | 7.48B | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,627 | -44 | 114,940 | 3.1% | 8.42B | 7 |
| 43 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,446 | +7 | 81,448 | 3.0% | 7.04B | 4 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,421 | +106 | 353,819 | 1.2% | 125.03B | 1 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,383 | +143 | 148,656 | 2.2% | 2.25B | 7 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,995 | +35 | 137,775 | 2.1% | 7.40B | 3 |
| 47 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,822 | +555 | 29,792 | 3.7% | 72.01B | 1 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,611 | -60 | 168,083 | 1.7% | 11.17B | 16 |
| 49 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,588 | +88 | 156,006 | 1.8% | 23.57B | 2 |
| 50 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,537 | -106 | 5,162,827 | 0.1% | 22.25B | 1 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,371 | +50 | 151,877 | 1.7% | 7.24B | 4 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,347 | +23 | 375,473 | 0.9% | 7.24B | 8 |
| 53 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,255 | -150 | 51,753 | 2.8% | 8.03B | 7 |
| 54 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,921 | +536 | 11,561 | 3.5% | 1.51B | 6 |
| 55 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,788 | +151 | 60,838 | 2.4% | 1.60B | 5 |
| 56 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,762 | +49 | 38,619 | 2.7% | 2.61B | 3 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,671 | +22 | 255,631 | 1.0% | 4.76B | 5 |
| 58 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,036 | +107 | 907,220 | 0.3% | 23.57B | 2 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,031 | +25 | 94,177 | 1.6% | 2.89B | 1 |
| 60 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,909 | +178 | 35,211 | 2.2% | 56.7M | 1 |
| 61 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,787 | -66 | 415,455 | 0.5% | 1.20B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,698 | +9 | 25,555 | 2.1% | 22.64B | 1 |
| 63 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,656 | +113 | 41,979 | 1.9% | 13.29B | 3 |
| 64 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,626 | -69 | 400,297 | 0.5% | 3.21B | 1 |
| 65 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,577 | -80 | 418,760 | 0.5% | 353.4M | 1 |
| 66 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,529 | +569 | 17,138 | 2.2% | 3.83B | 5 |
| 67 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,510 | +134 | 33,588 | 1.9% | 14.03B | 1 |
| 68 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,468 | +18 | 178,775 | 0.9% | 12.25B | 6 |
| 69 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,312 | +43 | 31,081 | 1.8% | 33.12B | 1 |
| 70 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,102 | -70 | 51,207 | 1.4% | 7.77B | 1 |
| 71 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,013 | -75 | 670,763 | 0.3% | 7.45B | 2 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,948 | -53 | 18,967 | 1.6% | 12.19B | 2 |
| 73 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,899 | +158 | 5,302,189 | 0.0% | 7.25B | 1 |
| 74 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,883 | +44 | 50,627 | 1.3% | 9.24B | 4 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,873 | +42 | 101,106 | 0.9% | 30.68B | 1 |
| 76 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,831 | +12 | 79,595 | 1.0% | 7.45B | 1 |
| 77 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,830 | +32 | 357,251 | 0.4% | — | 3 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,777 | +36 | 107,218 | 0.9% | 7.45B | 1 |
| 79 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,740 | +5 | 21,458 | 1.4% | 4.30B | 2 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,672 | +31 | 33,942 | 1.2% | 22.64B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,659 | +37 | 158,873 | 0.6% | 1.10B | 1 |
| 82 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,652 | +70 | 8,910 | 1.5% | 4.30B | 3 |
| 83 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,652 | +38 | 302,378 | 0.4% | 6.74B | 2 |
| 84 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,593 | +29 | 185,696 | 0.6% | 6.74B | 1 |
| 85 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,589 | +126 | 229,270 | 0.5% | 35.13B | 4 |
| 86 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,585 | +33 | 146,479 | 0.6% | 13.02B | 1 |
| 87 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,540 | +13 | 55,990 | 1.0% | 7.55B | 1 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,529 | +9 | 53,844 | 1.0% | 7.24B | 5 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,527 | +48 | 8,920 | 1.4% | 9.82B | 1 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,447 | +10 | 174,482 | 0.5% | 11.51B | 7 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,445 | +12 | 52,632 | 0.9% | 7.24B | 1 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,403 | +11 | 23,532 | 1.1% | 11.17B | 5 |
| 93 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,320 | +50 | 39,877 | 0.9% | 70.55B | 3 |
| 94 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,207 | +27 | 31,421 | 0.9% | 11.17B | 5 |
| 95 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,197 | +7 | 19,699 | 1.0% | 1.20B | 2 |
| 96 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,148 | +31 | 801,327 | 0.1% | — | 3 |
| 97 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,145 | +12 | 10,385 | 1.0% | 9.15B | 1 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,059 | -127 | 58,123 | 0.7% | 1.35B | 3 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,056 | -219 | 453,080 | 0.2% | 40.43B | 1 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 934 | +11 | 14,969 | 0.8% | 353.4M | 2 |
| 101 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 872 | -10 | 16,583 | 0.7% | 1.54B | 4 |
| 102 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 865 | -38 | 111,935 | 0.4% | 7.29B | 2 |
| 103 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 813 | +105 | 218,581 | 0.3% | 12.19B | 3 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 756 | +8 | 8,644 | 0.7% | 28.84B | 3 |
| 105 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 679 | +6 | 81,833 | 0.4% | 8.03B | 3 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 629 | 0 | 96,125 | 0.3% | 1.35B | 8 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 627 | -20 | 14,349 | 0.5% | 4.33B | 3 |
| 108 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 599 | +2 | 44,493 | 0.4% | 12.19B | 2 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 546 | -32 | 4,194 | 0.5% | 8.03B | 3 |
| 110 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 504 | +9 | 21,850 | 0.4% | 9.24B | 2 |
| 111 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 463 | +2 | 3,343 | 0.4% | 30.68B | 1 |
| 112 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 423 | 0 | 20,353 | 0.4% | 3.20B | 2 |
| 113 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 401 | -441 | 84,498 | 0.2% | 9.15B | 1 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 392 | -8 | 32,789 | 0.3% | 40.43B | 2 |
| 115 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 375 | +37 | 1,455 | 0.4% | — | 1 |
| 116 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 357 | +8 | 27,532 | 0.3% | 9.24B | 2 |
| 117 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 354 | +4 | 22,002 | 0.3% | 2.61B | 2 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 343 | +7 | 11,997 | 0.3% | 27.23B | 2 |
| 119 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 325 | -9 | 232,899 | 0.1% | — | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 320 | -3 | 322,193 | 0.1% | 7.24B | 2 |
| 121 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 310 | -1 | 1,490 | 0.3% | 27.23B | 3 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 305 | +15 | 37,735 | 0.2% | 27.23B | 3 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 284 | -3 | 107,133 | 0.1% | — | 3 |
| 124 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 283 | +8 | 5,409 | 0.3% | 11.51B | 5 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 281 | +13 | 39,336 | 0.2% | 7.48B | 2 |
| 126 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 274 | -5 | 41,832 | 0.2% | 11.17B | 1 |
| 127 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 267 | +8 | 2,679 | 0.3% | 4.02B | 2 |
| 128 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 259 | +6 | 12,679 | 0.2% | 70.55B | 2 |
| 129 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 256 | +1 | 5,122 | 0.2% | 437.8M | 1 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 226 | -5 | 19,616 | 0.2% | 68.98B | 2 |
| 131 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 217 | -27 | 7,452 | 0.2% | 31.59B | 6 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 212 | -6 | 44,586 | 0.1% | 7.70B | 5 |
| 133 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 207 | -4 | 5,021 | 0.2% | 70.55B | 3 |
| 134 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 200 | -4 | 2,507 | 0.2% | — | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 175 | -9 | 16,564 | 0.2% | 7.29B | 2 |
| 136 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 172 | -68 | 70,402 | 0.1% | 8.03B | 3 |
| 137 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 171 | -6 | 1,501 | 0.2% | 31.58B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 155 | -3 | 5,448 | 0.1% | 353.4M | 2 |
| 139 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 152 | -32 | 3,089 | 0.1% | 560.9M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 148 | -4 | 28,364 | 0.1% | 46.70B | 6 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 137 | +16 | 1,109 | 0.1% | — | 1 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 110 | -1 | 38,697 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 104 | -3 | 7,237 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 78 | -2 | 422 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 50 | +2 | 1,281 | 0.0% | 560.9M | 1 |
| 147 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | +3 | 389 | 0.0% | 437.8M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 36 | +1 | 249 | 0.0% | 15.17B | 3 |
| 149 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 35 | -8 | 2,841 | 0.0% | 31.59B | 6 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | +2 | 189 | 0.0% | 8.16B | 3 |
| 151 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 28 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -2 | 213 | 0.0% | 437.8M | 1 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +1 | 127 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +1 | 269 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | 0 | 153 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,675,534 | 304,521,768 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 863,615 | 5,934,125 | 7 | 14.3% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 330,173 | 2,611,715 | 11 | 12.2% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 74,270 | 263,373 | 6 | 20.4% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 74,031 | 76,055 | 1 | 42.0% |
| 6 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 69,149 | 6,366,735 | 12 | 1.1% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 46,826 | 1,399,127 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,194 | 397,077 | 10 | 6.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,615 | 558,222 | 13 | 3.1% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,702 | 1,441,310 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,526 | 441,559 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,219 | 365,860 | 14 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,120 | 198,862 | 3 | 2.4% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,621 | 857,576 | 3 | 0.6% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,446 | 81,448 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,995 | 137,775 | 1 | 2.1% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,837 | 491,048 | 3 | 0.8% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,667 | 697,666 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,482 | 659,629 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,405 | 104,887 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,983 | 1,160,975 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,688 | 154,248 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,527 | 8,920 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 451 | 23,828 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,919,100 | 59,072,753 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 463,476 | 4,574,335 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 186,672 | 931,389 | 13 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 74,031 | 76,055 | 17 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 70,477 | 136,585 | 19 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 37,893 | 713,395 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,500 | 43,868 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,500 | 4,161,163 | 28 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,534 | 19,850 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,627 | 114,940 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,446 | 81,448 | 43 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,995 | 137,775 | 46 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,371 | 151,877 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,347 | 375,473 | 52 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,255 | 51,753 | 53 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 2,909 | 35,211 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,013 | 670,763 | 71 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,873 | 101,106 | 75 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,830 | 357,251 | 77 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,659 | 158,873 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,527 | 8,920 | 89 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,148 | 801,327 | 96 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,059 | 58,123 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 217 | 7,452 | 131 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 42.0% | 74,031 | 76,055 | 5 |
| 2 | [cjvt](https://huggingface.co/cjvt) | 20.4% | 74,270 | 263,373 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 14.3% | 863,615 | 5,934,125 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 12.2% | 330,173 | 2,611,715 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,194 | 397,077 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.1% | 20,615 | 558,222 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 46,826 | 1,399,127 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,446 | 81,448 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,526 | 441,559 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,219 | 365,860 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,120 | 198,862 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,675,534 | 304,521,768 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,995 | 137,775 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,527 | 8,920 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,405 | 104,887 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,702 | 1,441,310 | 10 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 69,149 | 6,366,735 | 6 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,837 | 491,048 | 17 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,688 | 154,248 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,621 | 857,576 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,667 | 697,666 | 18 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,482 | 659,629 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 451 | 23,828 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,983 | 1,160,975 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
