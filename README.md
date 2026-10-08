# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-08
- **Generated at:** 2026-10-08T13:06:38Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,375,454 | +69 | 58,172,980 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,565,545 | -5,540 | 65,065,728 | 2.4% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 699,040 | -1,210 | 723,318 | 84.9% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 585,310 | +35,085 | 45,828,421 | 1.3% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 492,164 | -1,441 | 4,344,276 | 11.1% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 469,547 | -5,220 | 16,484,585 | 2.8% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 431,425 | -33,238 | 4,822,613 | 8.8% | 24.01B | 2 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 382,024 | -16,312 | 3,785,778 | 9.8% | 13.95B | 6 |
| 9 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 298,584 | -6,393 | 2,898,431 | 10.0% | 24.01B | 1 |
| 10 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 296,375 | -17,277 | 595,016 | 42.6% | 22.64B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 276,194 | +194 | 32,414,516 | 0.8% | 46.70B | 2 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,960 | +946 | 5,502,211 | 4.6% | 24.01B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 249,496 | -6,126 | 5,655,729 | 4.3% | 4.25B | 7 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 232,546 | +332 | 924,129 | 22.7% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,527 | +2,106 | 2,261,159 | 9.7% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 142,412 | -3,206 | 8,534,831 | 1.6% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 86,627 | -4,901 | 1,099,624 | 7.2% | 127.70B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 82,197 | -687 | 707,474 | 10.2% | 119.40B | 3 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,749 | -176 | 747,535 | 8.7% | 23.57B | 2 |
| 20 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 69,293 | -9,373 | 4,151,050 | 1.6% | 11.34B | 8 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,841 | +2,369 | 7,601,188 | 0.9% | 23.57B | 2 |
| 22 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,322 | +57 | 68,259 | 39.4% | — | 1 |
| 23 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 54,357 | +410 | 11,231,556 | 0.5% | 140.63B | 2 |
| 24 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 31,511 | -13,879 | 537,141 | 4.9% | 70.60B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 29,883 | +977 | 687,489 | 3.8% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,277 | -361 | 147,944 | 8.2% | 9.15B | 1 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,690 | +93 | 5,160,721 | 0.4% | 22.25B | 1 |
| 28 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,546 | +179 | 219,404 | 6.1% | — | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,526 | -628 | 633,574 | 2.4% | 23.57B | 2 |
| 30 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 17,091 | +3,085 | 35,824 | 12.6% | 12.25B | 3 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,465 | -122 | 781,520 | 1.6% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,051 | +14 | 76,883 | 7.9% | — | 5 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,823 | -670 | 485,031 | 2.4% | 9.15B | 1 |
| 34 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,838 | +3,196 | 332,291 | 2.7% | 24.01B | 2 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 11,777 | +355 | 135,865 | 5.0% | 7.48B | 5 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,231 | +69 | 511,234 | 1.8% | 7.24B | 8 |
| 37 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 9,772 | -1,505 | 26,730 | 7.7% | 72.01B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,743 | +278 | 4,928,453 | 0.2% | 122.61B | 1 |
| 39 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,799 | -184 | 350,666 | 1.5% | 125.03B | 1 |
| 40 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,787 | +164 | 5,380,678 | 0.1% | 22.25B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,128 | +120 | 17,051 | 5.2% | 572.6M | 5 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,040 | +246 | 146,474 | 2.5% | 2.25B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,622 | +13 | 110,185 | 2.7% | 8.42B | 7 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,229 | -303 | 49,698 | 3.5% | 8.03B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,225 | +86 | 135,274 | 2.2% | 7.40B | 3 |
| 46 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,972 | +127 | 165,862 | 1.9% | 11.17B | 16 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,967 | -16 | 154,491 | 2.0% | 23.57B | 2 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,801 | +71 | 67,819 | 2.9% | 12.77B | 5 |
| 49 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,780 | -54 | 111,638 | 2.3% | 7.29B | 2 |
| 50 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,664 | +59 | 373,269 | 1.0% | 7.24B | 8 |
| 51 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,383 | -126 | 12,092 | 3.9% | 27.43B | 3 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,330 | +33 | 253,756 | 1.2% | 4.76B | 5 |
| 53 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,190 | +33 | 414,959 | 0.8% | 1.20B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,127 | -14 | 905,480 | 0.4% | 23.57B | 2 |
| 55 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,116 | +36 | 5,033,986 | 0.1% | 122.61B | 1 |
| 56 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,103 | +107 | 149,503 | 1.6% | 7.24B | 4 |
| 57 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,022 | +19 | 418,456 | 0.8% | 353.4M | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 4,022 | -37 | 66,954 | 2.4% | 14.08B | 1 |
| 59 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,980 | +16 | 399,998 | 0.8% | 3.21B | 1 |
| 60 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,931 | -78 | 670,085 | 0.5% | 7.45B | 2 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,457 | -103 | 92,546 | 1.8% | 2.89B | 1 |
| 62 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,417 | -40 | 36,258 | 2.5% | 2.61B | 3 |
| 63 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,174 | +35 | 58,588 | 2.0% | 1.60B | 5 |
| 64 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,610 | +76 | 85,887 | 1.4% | 2.22B | 1 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,498 | -34 | 84,350 | 1.4% | 9.15B | 1 |
| 66 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,468 | +203 | 9,030 | 2.3% | 1.51B | 6 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,305 | -265 | 40,542 | 1.6% | 13.29B | 3 |
| 68 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,226 | +28 | 55,558 | 1.4% | 7.55B | 1 |
| 69 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,191 | -26 | 49,599 | 1.5% | 9.24B | 4 |
| 70 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,190 | +72 | 24,037 | 1.8% | 22.64B | 1 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,140 | +10 | 33,015 | 1.6% | 22.64B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,117 | -45 | 18,170 | 1.8% | 12.19B | 2 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,868 | -9 | 78,588 | 1.0% | 7.45B | 1 |
| 74 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,825 | -3 | 106,236 | 0.9% | 7.45B | 1 |
| 75 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,824 | -1,964 | 30,279 | 1.4% | 33.12B | 1 |
| 76 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,822 | +128 | 15,397 | 1.6% | 3.83B | 5 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,809 | +5 | 100,074 | 0.9% | 30.68B | 1 |
| 78 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,806 | +13 | 452,588 | 0.3% | 40.43B | 1 |
| 79 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,802 | +7 | 49,883 | 1.2% | 7.77B | 1 |
| 80 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,765 | +36 | 33,459 | 1.3% | 56.7M | 1 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,733 | +18 | 356,214 | 0.4% | — | 3 |
| 82 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,697 | +21 | 5,300,960 | 0.0% | 7.25B | 1 |
| 83 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,639 | 0 | 177,069 | 0.6% | 12.25B | 6 |
| 84 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,632 | -7 | 22,860 | 1.3% | 11.17B | 5 |
| 85 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,617 | +19 | 157,960 | 0.6% | 1.10B | 1 |
| 86 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,565 | 0 | 31,790 | 1.2% | 14.03B | 1 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,562 | +12 | 301,460 | 0.4% | 6.74B | 2 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,512 | +16 | 145,603 | 0.6% | 13.02B | 1 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,511 | -11 | 7,914 | 1.4% | 9.82B | 1 |
| 90 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,504 | +4 | 184,803 | 0.5% | 6.74B | 1 |
| 91 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,401 | +59 | 53,015 | 0.9% | 7.24B | 5 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,344 | -79 | 20,419 | 1.1% | 4.30B | 2 |
| 93 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,322 | -25 | 30,826 | 1.0% | 11.17B | 5 |
| 94 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,308 | +62 | 51,850 | 0.9% | 7.24B | 1 |
| 95 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,291 | 0 | 12,023 | 1.2% | 31.59B | 6 |
| 96 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,231 | -51 | 173,572 | 0.4% | 11.51B | 7 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,160 | -1 | 228,238 | 0.4% | 35.13B | 4 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,146 | -12 | 57,554 | 0.7% | 1.35B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,101 | +11 | 800,651 | 0.1% | — | 3 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,084 | +40 | 7,871 | 1.0% | 4.30B | 3 |
| 101 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,064 | +82 | 18,950 | 0.9% | 1.20B | 2 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 975 | +77 | 14,490 | 0.9% | 353.4M | 2 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 946 | +80 | 39,081 | 0.7% | 70.55B | 3 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 925 | -55 | 8,149 | 0.9% | 28.84B | 3 |
| 105 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 867 | -46 | 9,597 | 0.8% | 9.15B | 1 |
| 106 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 864 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 798 | -4 | 16,264 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 740 | +3 | 20,208 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 694 | -7 | 95,773 | 0.4% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 639 | +17 | 81,472 | 0.4% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 605 | +67 | 76,308 | 0.3% | 7.04B | 4 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 597 | -74 | 44,120 | 0.4% | 12.19B | 2 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 522 | +8 | 3,875 | 0.5% | 8.03B | 3 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 497 | -21 | 232,754 | 0.1% | — | 2 |
| 115 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 492 | -58 | 217,920 | 0.2% | 12.19B | 3 |
| 116 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 488 | +27 | 27,354 | 0.4% | 9.24B | 2 |
| 117 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 481 | -2 | 1,499 | 0.5% | 31.58B | 2 |
| 118 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 458 | -12 | 3,013 | 0.4% | 560.9M | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 454 | -5 | 21,836 | 0.4% | 2.61B | 2 |
| 120 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 451 | -8 | 13,932 | 0.4% | 4.33B | 3 |
| 121 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 443 | -15 | 32,579 | 0.3% | 40.43B | 2 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 419 | -8 | 322,053 | 0.1% | 7.24B | 2 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 414 | -9 | 39,173 | 0.3% | 7.48B | 2 |
| 124 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 379 | -10 | 12,534 | 0.3% | 70.55B | 2 |
| 125 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 377 | -9 | 3,085 | 0.4% | 30.68B | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 376 | -1 | 11,801 | 0.3% | 27.23B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 370 | -2 | 7,364 | 0.3% | 31.59B | 6 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 369 | -2 | 37,602 | 0.3% | 27.23B | 3 |
| 129 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 355 | +10 | 1,220 | 0.4% | — | 1 |
| 130 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 317 | +4 | 21,538 | 0.3% | 9.24B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 305 | -8 | 44,473 | 0.2% | 7.70B | 5 |
| 132 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 302 | -3 | 106,988 | 0.1% | — | 3 |
| 133 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 282 | -1 | 70,306 | 0.2% | 8.03B | 3 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 273 | -1 | 41,685 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 251 | +1 | 16,467 | 0.2% | 7.29B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 251 | -4 | 19,498 | 0.2% | 68.98B | 2 |
| 137 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 231 | -3 | 2,543 | 0.2% | 4.02B | 2 |
| 138 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 228 | +6 | 5,258 | 0.2% | 11.51B | 5 |
| 139 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 212 | +2 | 2,404 | 0.2% | — | 1 |
| 140 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 203 | -6 | 1,244 | 0.2% | 27.23B | 3 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 177 | +4 | 5,006 | 0.2% | 437.8M | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 173 | -1 | 38,635 | 0.1% | 70.55B | 3 |
| 143 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 173 | -9 | 5,363 | 0.2% | 353.4M | 2 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 171 | -3 | 4,887 | 0.2% | 70.55B | 3 |
| 145 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 28,270 | 0.1% | 46.70B | 6 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130 | +1 | 1,027 | 0.1% | — | 1 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 127 | -3 | 7,181 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 87 | 0 | 399 | 0.1% | 321.0M | 1 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 41 | -4 | 200 | 0.0% | 437.8M | 1 |
| 151 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | -27 | 1,248 | 0.0% | 560.9M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | 0 | 227 | 0.0% | 15.17B | 3 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | 0 | 171 | 0.0% | 8.16B | 3 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | -6 | 148 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | -3 | 261 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +1 | 118 | 0.0% | 7.24B | 1 |
| 157 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 16 | -1 | 360 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,732,075 | 301,074,789 | 30 | 2.6% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,242,905 | 5,672,943 | 7 | 21.5% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 593,891 | 2,561,185 | 11 | 22.3% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 123,928 | 6,332,076 | 12 | 1.9% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,322 | 68,259 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,974 | 1,369,013 | 5 | 2.7% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 21,614 | 385,438 | 10 | 4.5% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 19,327 | 1,435,269 | 11 | 1.3% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,975 | 545,436 | 13 | 2.6% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,950 | 434,644 | 6 | 2.4% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,289 | 359,819 | 14 | 2.5% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,102 | 192,736 | 6 | 3.1% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,624 | 854,909 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,632 | 152,841 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,341 | 193,831 | 3 | 2.2% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,225 | 135,274 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,083 | 695,322 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,633 | 488,366 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,295 | 657,674 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,006 | 23,714 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,243 | 103,557 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,151 | 1,159,891 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,840 | 153,327 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,511 | 7,914 | 1 | 1.4% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 605 | 76,308 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,375,454 | 58,172,980 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 699,040 | 723,318 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 296,375 | 595,016 | 10 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 69,293 | 4,151,050 | 20 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,322 | 68,259 | 22 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 29,883 | 687,489 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 17,091 | 35,824 | 30 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,622 | 110,185 | 43 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,229 | 49,698 | 44 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,225 | 135,274 | 45 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,801 | 67,819 | 48 |
| 12 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,780 | 111,638 | 49 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,664 | 373,269 | 50 |
| 14 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 4,190 | 414,959 | 53 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,103 | 149,503 | 56 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 4,022 | 66,954 | 58 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,931 | 670,085 | 60 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,809 | 100,074 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,733 | 356,214 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,617 | 157,960 | 85 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,511 | 7,914 | 89 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,291 | 12,023 | 95 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,146 | 57,554 | 98 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,101 | 800,651 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 605 | 76,308 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,322 | 68,259 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 22.3% | 593,891 | 2,561,185 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.5% | 1,242,905 | 5,672,943 | 2 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4.5% | 21,614 | 385,438 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.1% | 9,102 | 192,736 | 12 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 39,974 | 1,369,013 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.6% | 16,975 | 545,436 | 9 |
| 8 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,632 | 152,841 | 14 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.6% | 7,732,075 | 301,074,789 | 1 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,289 | 359,819 | 11 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 3,006 | 23,714 | 20 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 12,950 | 434,644 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,225 | 135,274 | 16 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.2% | 6,341 | 193,831 | 15 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.9% | 123,928 | 6,332,076 | 4 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,511 | 7,914 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.3% | 19,327 | 1,435,269 | 8 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,243 | 103,557 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,624 | 854,909 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,633 | 488,366 | 18 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,840 | 153,327 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,083 | 695,322 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,295 | 657,674 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 605 | 76,308 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,151 | 1,159,891 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
