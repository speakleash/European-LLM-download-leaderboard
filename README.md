# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-21
- **Generated at:** 2026-10-21T11:27:30Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,039,457 | -36,513 | 58,932,515 | 3.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,745,584 | +9,009 | 65,980,029 | 2.6% | 7.24B | 1 |
| 3 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 472,386 | -2,509 | 4,537,081 | 10.2% | 8.05B | 2 |
| 4 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 459,165 | -33,422 | 733,635 | 55.1% | 8.90B | 1 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 436,076 | +1,810 | 46,037,963 | 0.9% | 7.24B | 2 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 382,788 | +373 | 3,981,079 | 9.4% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 320,922 | -6,087 | 16,570,325 | 1.9% | 12.25B | 3 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 275,549 | -6,509 | 4,912,864 | 5.5% | 24.01B | 2 |
| 9 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 266,980 | +1,898 | 32,536,712 | 0.8% | 46.70B | 2 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 237,986 | -15,244 | 2,990,158 | 7.7% | 24.01B | 1 |
| 11 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,573 | -2,043 | 2,340,533 | 9.2% | 8.92B | 6 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 222,810 | -2,646 | 5,743,294 | 3.8% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 200,144 | -7,144 | 5,565,063 | 3.5% | 24.01B | 1 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 185,460 | -45,908 | 929,147 | 18.0% | 1.66B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 120,998 | -13,782 | 599,552 | 17.3% | 22.64B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 79,187 | +2,225 | 7,641,411 | 1.0% | 23.57B | 2 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,153 | -70 | 1,110,066 | 6.2% | 127.70B | 2 |
| 18 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 74,052 | +483 | 76,040 | 42.1% | — | 1 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,855 | -394 | 719,233 | 9.0% | 119.40B | 3 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,422 | -3,321 | 8,553,962 | 0.8% | 8.02B | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,806 | -300 | 776,287 | 8.1% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,012 | +1,649 | 11,259,766 | 0.6% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,353 | +124 | 119,657 | 24.7% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 37,356 | +497 | 709,824 | 4.6% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 31,082 | +263 | 355,300 | 6.8% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,776 | -38 | 237,723 | 9.1% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,442 | +73 | 43,735 | 17.0% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,649 | -241 | 546,853 | 3.3% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,891 | -193 | 4,159,436 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,011 | -666 | 155,905 | 6.6% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,624 | +213 | 642,647 | 2.0% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,051 | -26 | 787,381 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,617 | -291 | 81,670 | 6.9% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,513 | -131 | 516,398 | 1.9% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,425 | +32 | 19,689 | 9.5% | 27.43B | 3 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,989 | -49 | 489,578 | 1.9% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,404 | +114 | 4,933,063 | 0.2% | 122.61B | 1 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,744 | +84 | 5,383,622 | 0.1% | 22.25B | 1 |
| 39 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,731 | -472 | 138,147 | 3.2% | 7.48B | 5 |
| 40 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,671 | +1,426 | 5,038,982 | 0.1% | 122.61B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,097 | +161 | 18,520 | 6.0% | 572.6M | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,046 | +275 | 114,353 | 3.3% | 8.42B | 7 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,681 | -76 | 148,242 | 2.3% | 2.25B | 7 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,486 | +3 | 81,396 | 3.0% | 7.04B | 4 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,463 | +45 | 353,243 | 1.2% | 125.03B | 1 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,252 | -2 | 137,432 | 2.2% | 7.40B | 3 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,104 | -264 | 51,516 | 3.4% | 8.03B | 7 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,904 | +11 | 167,802 | 1.8% | 11.17B | 16 |
| 49 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,750 | -31 | 5,162,577 | 0.1% | 22.25B | 1 |
| 50 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,564 | +365 | 29,054 | 3.5% | 72.01B | 1 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,498 | -125 | 375,163 | 0.9% | 7.24B | 8 |
| 52 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,454 | -18 | 151,498 | 1.8% | 7.24B | 4 |
| 53 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,378 | -51 | 155,667 | 1.7% | 23.57B | 2 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,762 | -9 | 38,272 | 2.7% | 2.61B | 3 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,753 | -155 | 906,866 | 0.4% | 23.57B | 2 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,712 | -47 | 60,449 | 2.3% | 1.60B | 5 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,697 | +36 | 255,248 | 1.0% | 4.76B | 5 |
| 58 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,383 | -15 | 10,635 | 3.1% | 1.51B | 6 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,182 | -17 | 93,926 | 1.6% | 2.89B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,944 | -64 | 415,403 | 0.6% | 1.20B | 1 |
| 61 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,779 | -78 | 400,251 | 0.6% | 3.21B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,753 | +17 | 25,377 | 2.2% | 22.64B | 1 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,742 | -87 | 418,708 | 0.5% | 353.4M | 1 |
| 64 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,717 | +93 | 34,886 | 2.0% | 56.7M | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,686 | +12 | 41,751 | 1.9% | 13.29B | 3 |
| 66 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,674 | -19 | 51,047 | 1.8% | 7.77B | 1 |
| 67 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,516 | +11 | 178,642 | 0.9% | 12.25B | 6 |
| 68 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,485 | -17 | 84,490 | 1.3% | 9.15B | 1 |
| 69 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,397 | -254 | 670,665 | 0.3% | 7.45B | 2 |
| 70 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,359 | -11 | 33,368 | 1.8% | 14.03B | 1 |
| 71 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,258 | -18 | 30,964 | 1.7% | 33.12B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,110 | +21 | 18,842 | 1.8% | 12.19B | 2 |
| 73 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,971 | -63 | 16,346 | 1.7% | 3.83B | 5 |
| 74 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,958 | -9 | 452,991 | 0.4% | 40.43B | 1 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,879 | -14 | 100,919 | 0.9% | 30.68B | 1 |
| 76 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,873 | +14 | 50,443 | 1.2% | 9.24B | 4 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,861 | -12 | 79,413 | 1.0% | 7.45B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,840 | +14 | 357,070 | 0.4% | — | 3 |
| 79 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,820 | -8 | 107,031 | 0.9% | 7.45B | 1 |
| 80 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,803 | +32 | 21,403 | 1.5% | 4.30B | 2 |
| 81 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,671 | +4 | 33,769 | 1.2% | 22.64B | 1 |
| 82 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,668 | +12 | 5,301,777 | 0.0% | 7.25B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,653 | -19 | 158,699 | 0.6% | 1.10B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,646 | +3 | 302,204 | 0.4% | 6.74B | 2 |
| 85 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,633 | -9 | 55,923 | 1.0% | 7.55B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,594 | +1 | 185,532 | 0.6% | 6.74B | 1 |
| 87 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,581 | +2 | 146,313 | 0.6% | 13.02B | 1 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,575 | +97 | 8,777 | 1.4% | 9.82B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,567 | -6 | 53,713 | 1.0% | 7.24B | 5 |
| 90 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,561 | +170 | 8,707 | 1.4% | 4.30B | 3 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,512 | +34 | 174,376 | 0.6% | 11.51B | 7 |
| 92 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,490 | -3 | 52,519 | 1.0% | 7.24B | 1 |
| 93 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,435 | +20 | 228,997 | 0.4% | 35.13B | 4 |
| 94 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,428 | -48 | 23,444 | 1.2% | 11.17B | 5 |
| 95 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,356 | -18 | 19,636 | 1.1% | 1.20B | 2 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,245 | 0 | 31,333 | 0.9% | 11.17B | 5 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,234 | +45 | 58,029 | 0.8% | 1.35B | 3 |
| 98 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,228 | +22 | 39,697 | 0.9% | 70.55B | 3 |
| 99 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,139 | -11 | 10,321 | 1.0% | 9.15B | 1 |
| 100 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,095 | +38 | 801,153 | 0.1% | — | 3 |
| 101 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,056 | -16 | 111,929 | 0.5% | 7.29B | 2 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,011 | -8 | 14,907 | 0.9% | 353.4M | 2 |
| 103 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 868 | +15 | 16,510 | 0.7% | 1.54B | 4 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 795 | +13 | 8,613 | 0.7% | 28.84B | 3 |
| 105 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 744 | -3 | 218,450 | 0.2% | 12.19B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 690 | -1 | 81,767 | 0.4% | 8.03B | 3 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 653 | -17 | 96,047 | 0.3% | 1.35B | 8 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 648 | -8 | 14,286 | 0.6% | 4.33B | 3 |
| 109 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 608 | +33 | 44,422 | 0.4% | 12.19B | 2 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 600 | +13 | 4,136 | 0.6% | 8.03B | 3 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 497 | +28 | 21,824 | 0.4% | 9.24B | 2 |
| 112 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 465 | +2 | 3,281 | 0.5% | 30.68B | 1 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 446 | +2 | 20,338 | 0.4% | 3.20B | 2 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 415 | +8 | 32,768 | 0.3% | 40.43B | 2 |
| 115 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 362 | +6 | 232,865 | 0.1% | — | 2 |
| 116 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 357 | -7 | 27,503 | 0.3% | 9.24B | 2 |
| 117 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | +11 | 11,980 | 0.3% | 27.23B | 2 |
| 118 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 339 | -1 | 21,980 | 0.3% | 2.61B | 2 |
| 119 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 336 | -14 | 322,182 | 0.1% | 7.24B | 2 |
| 120 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 320 | +2 | 1,376 | 0.3% | — | 1 |
| 121 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 316 | +1 | 1,490 | 0.3% | 27.23B | 3 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 304 | -4 | 37,704 | 0.2% | 27.23B | 3 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 303 | -23 | 39,318 | 0.2% | 7.48B | 2 |
| 124 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 299 | -11 | 41,814 | 0.2% | 11.17B | 1 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 299 | +10 | 107,117 | 0.1% | — | 3 |
| 126 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 283 | -7 | 3,088 | 0.3% | 560.9M | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 280 | +16 | 7,446 | 0.3% | 31.59B | 6 |
| 128 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 268 | +11 | 5,369 | 0.3% | 11.51B | 5 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 262 | +9 | 12,658 | 0.2% | 70.55B | 2 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 252 | 0 | 5,113 | 0.2% | 437.8M | 1 |
| 131 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 245 | +8 | 2,645 | 0.2% | 4.02B | 2 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 244 | 0 | 44,578 | 0.2% | 7.70B | 5 |
| 133 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 237 | +4 | 70,389 | 0.1% | 8.03B | 3 |
| 134 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 235 | +12 | 19,599 | 0.2% | 68.98B | 2 |
| 135 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 226 | -2 | 1,501 | 0.2% | 31.58B | 2 |
| 136 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 214 | +4 | 5,015 | 0.2% | 70.55B | 3 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 211 | 0 | 2,497 | 0.2% | — | 1 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 191 | +3 | 16,545 | 0.2% | 7.29B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 159 | +4 | 5,438 | 0.2% | 353.4M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 154 | -5 | 28,358 | 0.1% | 46.70B | 6 |
| 141 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 145 | +6 | 38,690 | 0.1% | 70.55B | 3 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 114 | -3 | 7,234 | 0.1% | 1.20B | 2 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 112 | +7 | 1,073 | 0.1% | — | 1 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 82 | +1 | 415 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 47 | +2 | 1,276 | 0.0% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 37 | +2 | 244 | 0.0% | 15.17B | 3 |
| 149 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | 0 | 382 | 0.0% | 437.8M | 1 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 32 | +3 | 185 | 0.0% | 8.16B | 3 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | +1 | 211 | 0.0% | 437.8M | 1 |
| 152 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 28 | -6 | 12,034 | 0.0% | 31.59B | 6 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +2 | 126 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 266 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | 0 | 152 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,895,890 | 303,969,123 | 30 | 2.3% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 970,215 | 5,892,124 | 7 | 16.2% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 377,255 | 2,606,631 | 11 | 13.9% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 74,052 | 76,040 | 1 | 42.1% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 71,251 | 6,361,197 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,160 | 246,142 | 6 | 16.8% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 48,084 | 1,394,872 | 5 | 3.2% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,263 | 396,497 | 10 | 6.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,922 | 557,466 | 13 | 3.2% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,280 | 1,440,396 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,017 | 440,465 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,632 | 364,923 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,593 | 198,249 | 3 | 2.5% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,078 | 857,109 | 3 | 0.6% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,486 | 81,396 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,252 | 137,432 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,834 | 697,345 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,828 | 490,544 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,486 | 659,274 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,413 | 104,629 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,991 | 1,160,734 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,887 | 154,076 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,575 | 8,777 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 577 | 23,817 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,039,457 | 58,932,515 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 472,386 | 4,537,081 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 185,460 | 929,147 | 14 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 74,052 | 76,040 | 18 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,353 | 119,657 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 37,356 | 709,824 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,442 | 43,735 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,891 | 4,159,436 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,425 | 19,689 | 35 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,046 | 114,353 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,486 | 81,396 | 44 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,252 | 137,432 | 46 |
| 13 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,104 | 51,516 | 47 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,498 | 375,163 | 51 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,454 | 151,498 | 52 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 2,944 | 415,403 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,397 | 670,665 | 69 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,879 | 100,919 | 75 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,840 | 357,070 | 78 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,653 | 158,699 | 83 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,575 | 8,777 | 88 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,234 | 58,029 | 97 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,095 | 801,153 | 100 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 280 | 7,446 | 127 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 42.1% | 74,052 | 76,040 | 4 |
| 2 | [cjvt](https://huggingface.co/cjvt) | 16.8% | 58,160 | 246,142 | 6 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 16.2% | 970,215 | 5,892,124 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 13.9% | 377,255 | 2,606,631 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,263 | 396,497 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.2% | 48,084 | 1,394,872 | 7 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 20,922 | 557,466 | 9 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,486 | 81,396 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,017 | 440,465 | 11 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,593 | 198,249 | 13 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,632 | 364,923 | 12 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.3% | 6,895,890 | 303,969,123 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,252 | 137,432 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,575 | 8,777 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,413 | 104,629 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,280 | 1,440,396 | 10 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 71,251 | 6,361,197 | 5 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,828 | 490,544 | 18 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,887 | 154,076 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 6,078 | 857,109 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,834 | 697,345 | 17 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 577 | 23,817 | 24 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,486 | 659,274 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,991 | 1,160,734 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
