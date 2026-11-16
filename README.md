# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-16
- **Generated at:** 2026-11-16T09:01:19Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 207

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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,021,775 | +9,748 | 60,805,659 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,159,669 | -34,791 | 66,958,424 | 1.7% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 667,840 | 0 | 4,560,252 | 14.3% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 551,470 | -899 | 46,553,497 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 359,851 | -1,309 | 32,856,363 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 264,373 | 0 | 2,577,933 | 9.9% | 8.92B | 6 |
| 7 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213,120 | 0 | 332,031 | 49.3% | 12.77B | 5 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 210,956 | 0 | 5,927,721 | 3.5% | 3.85B | 7 |
| 9 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 201,288 | -13,785 | 4,696,239 | 4.2% | 8.05B | 2 |
| 10 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 145,331 | -1,224 | 16,687,585 | 0.9% | 12.25B | 3 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140,087 | -4,001 | 5,041,492 | 2.7% | 24.01B | 2 |
| 12 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 122,675 | 0 | 4,290,187 | 2.8% | 11.34B | 13 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,616 | +4,598 | 5,656,809 | 1.8% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 101,326 | -780 | 7,732,991 | 1.3% | 23.57B | 2 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,418 | +202 | 8,612,489 | 0.7% | 8.02B | 1 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,827 | +41 | 11,297,423 | 0.4% | 140.63B | 2 |
| 17 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 38,770 | +97 | 741,157 | 4.6% | 7.77B | 8 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,252 | -2,243 | 807,720 | 4.2% | 23.57B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,162 | 0 | 751,343 | 4.1% | 119.40B | 3 |
| 20 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,373 | 0 | 3,012,289 | 0.8% | 24.01B | 1 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,727 | 0 | 369,773 | 4.4% | 24.01B | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,733 | -155 | 948,064 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 17,522 | +637 | 803,455 | 1.9% | 11.25B | 10 |
| 24 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,626 | 0 | 16,686 | 14.2% | — | 2 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,453 | 0 | 749,384 | 1.8% | 8.90B | 5 |
| 26 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,332 | +181 | 699,360 | 1.9% | 7.29B | 1 |
| 27 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,084 | 0 | 1,123,039 | 1.2% | 127.70B | 2 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,703 | -17 | 4,946,542 | 0.3% | 122.61B | 1 |
| 29 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 13,624 | 0 | 35,434 | 10.1% | 78.10B | 2 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,815 | -20 | 5,047,833 | 0.2% | 122.61B | 1 |
| 31 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,462 | +1,199 | 249,586 | 3.6% | — | 1 |
| 32 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,974 | -172 | 652,172 | 1.6% | 23.57B | 2 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,967 | -101 | 499,402 | 1.8% | 9.15B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,571 | -66 | 525,863 | 1.7% | 7.24B | 8 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,374 | +122 | 5,392,215 | 0.2% | 22.25B | 1 |
| 36 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,472 | 0 | 36,685 | 6.2% | 72.01B | 4 |
| 37 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,053 | 0 | 552,042 | 1.2% | 70.60B | 2 |
| 38 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,807 | 0 | 88,568 | 4.1% | — | 5 |
| 39 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,608 | 0 | 23,533 | 6.2% | 3.83B | 5 |
| 40 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 7,485 | +210 | 262,428 | 2.1% | 4.76B | 8 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,452 | 0 | 17,379 | 6.3% | 1.51B | 6 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,265 | -1,273 | 120,481 | 3.3% | 8.42B | 7 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,061 | 0 | 359,498 | 1.5% | 125.03B | 1 |
| 44 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,704 | 0 | 605,427 | 1.0% | 22.64B | 1 |
| 45 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,398 | 0 | 161,604 | 2.4% | 9.15B | 1 |
| 46 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,277 | 0 | 24,143 | 5.1% | 572.6M | 5 |
| 47 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,146 | 0 | 6,146 | 5.8% | 11.17B | 14 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,948 | -39 | 57,152 | 3.8% | 8.03B | 7 |
| 49 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,847 | -1 | 138,604 | 2.5% | 2.89B | 1 |
| 50 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,648 | -40 | 153,627 | 2.2% | 2.25B | 7 |
| 51 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,601 | +2 | 159,558 | 2.2% | 351.6M | 1 |
| 52 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,360 | +173 | 65,382 | 3.2% | 1.60B | 9 |
| 53 | OpenEuroLLM Prelude-base 9B | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 4,773 | +4,773 | 78,823 | 2.7% | 9.09B | 1 |
| 54 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,695 | 0 | 39,255 | 3.4% | 56.7M | 1 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,645 | +16 | 911,052 | 0.5% | 23.57B | 2 |
| 56 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,444 | -43 | 155,495 | 1.7% | 7.24B | 4 |
| 57 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,236 | -6 | 125,260 | 1.9% | 8.54B | 2 |
| 58 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,226 | -37 | 141,189 | 1.8% | 7.40B | 3 |
| 59 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,088 | -47 | 378,866 | 0.9% | 7.24B | 8 |
| 60 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,082 | 0 | 29,128 | 3.2% | 22.64B | 1 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,979 | -10 | 41,640 | 2.8% | 2.61B | 3 |
| 62 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,909 | 0 | 141,496 | 1.6% | 7.48B | 12 |
| 63 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,907 | +19 | 5,166,157 | 0.1% | 22.25B | 1 |
| 64 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,585 | +10 | 55,302 | 2.3% | 7.77B | 3 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,541 | 0 | 44,956 | 2.4% | 13.29B | 3 |
| 66 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,378 | 0 | 22,921 | 2.7% | 27.43B | 3 |
| 67 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,253 | -11 | 96,868 | 1.7% | 2.89B | 1 |
| 68 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,186 | 0 | 3,229 | 3.1% | 3.93B | 2 |
| 69 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,129 | -8 | 13,387 | 2.8% | 9.15B | 1 |
| 70 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,020 | -110 | 170,408 | 1.1% | 11.17B | 16 |
| 71 | Velvet 14B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,788 | +2,788 | 70,552 | 1.6% | 14.08B | 1 |
| 72 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,779 | +56 | 5,304,295 | 0.1% | 7.25B | 1 |
| 73 | Velvet 2B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,751 | +2,751 | 89,438 | 1.5% | 2.22B | 1 |
| 74 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,744 | 0 | 21,394 | 2.3% | 12.19B | 2 |
| 75 | AI Sweden Llama 3 8B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 2,496 | — | 95,570 | 1.3% | 8.03B | 10 |
| 76 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,475 | +144 | 86,948 | 1.3% | 9.15B | 1 |
| 77 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,442 | -70 | 157,479 | 0.9% | 23.57B | 2 |
| 78 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,358 | -22 | 231,141 | 0.7% | 35.13B | 4 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,237 | 0 | 102,866 | 1.1% | 30.68B | 1 |
| 80 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,138 | 0 | 23,401 | 1.7% | 4.30B | 2 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,120 | -1 | 358,974 | 0.5% | — | 3 |
| 82 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,100 | +1 | 81,313 | 1.2% | 7.45B | 1 |
| 83 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,084 | +8 | 52,323 | 1.4% | 9.24B | 4 |
| 84 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,067 | +2 | 454,954 | 0.4% | 40.43B | 1 |
| 85 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,040 | +8 | 160,550 | 0.8% | 1.10B | 1 |
| 86 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,999 | +3 | 108,834 | 1.0% | 7.45B | 1 |
| 87 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,924 | +1 | 35,502 | 1.4% | 22.64B | 1 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,924 | +6 | 187,273 | 0.7% | 6.74B | 1 |
| 89 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,923 | +6 | 303,941 | 0.5% | 6.74B | 2 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,859 | +6 | 147,991 | 0.7% | 13.02B | 1 |
| 91 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,765 | -4 | 180,214 | 0.6% | 12.25B | 6 |
| 92 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,658 | -3 | 802,645 | 0.2% | — | 3 |
| 93 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,637 | 0 | 10,167 | 1.5% | 9.82B | 1 |
| 94 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,613 | -7 | 41,160 | 1.1% | 70.55B | 3 |
| 95 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,564 | 0 | 44,931 | 1.1% | 12.25B | 3 |
| 96 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,538 | -17 | 55,098 | 1.0% | 7.24B | 5 |
| 97 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,522 | -7 | 416,679 | 0.3% | 1.20B | 1 |
| 98 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,491 | 0 | 1,491 | 1.5% | 3.93B | 1 |
| 99 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,478 | -19 | 53,850 | 1.0% | 7.24B | 1 |
| 100 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,470 | -532 | 34,772 | 1.1% | 14.03B | 1 |
| 101 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,437 | +7 | 420,085 | 0.3% | 353.4M | 1 |
| 102 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,415 | +18 | 20,979 | 1.2% | 1.20B | 2 |
| 103 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,385 | +18 | 16,228 | 1.2% | 353.4M | 2 |
| 104 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,376 | 0 | 9,794 | 1.3% | 4.30B | 3 |
| 105 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,305 | 0 | 9,585 | 1.2% | 28.84B | 3 |
| 106 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,298 | +15 | 401,483 | 0.3% | 3.21B | 1 |
| 107 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,181 | 0 | 9,784 | 1.1% | 40.43B | 2 |
| 108 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,178 | +5 | 175,385 | 0.4% | 11.51B | 9 |
| 109 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,167 | +2 | 57,017 | 0.7% | 7.55B | 1 |
| 110 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,095 | -6 | 58,968 | 0.7% | 1.35B | 3 |
| 111 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,081 | +9 | 45,328 | 0.7% | 12.19B | 2 |
| 112 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,067 | +1 | 31,946 | 0.8% | 33.12B | 1 |
| 113 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 997 | 0 | 219,257 | 0.3% | 12.19B | 3 |
| 114 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 994 | -10 | 671,566 | 0.1% | 7.45B | 2 |
| 115 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 885 | 0 | 2,925 | 0.9% | 40.43B | 2 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 884 | 0 | 233,721 | 0.3% | — | 2 |
| 117 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 829 | 0 | 14,898 | 0.7% | 4.33B | 3 |
| 118 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 829 | -16 | 24,187 | 0.7% | 11.17B | 5 |
| 119 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 823 | -19 | 82,131 | 0.5% | 7.04B | 4 |
| 120 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 816 | 0 | 1,768 | 0.8% | 608.3M | 1 |
| 121 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 801 | -4 | 96,784 | 0.4% | 1.35B | 8 |
| 122 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 760 | +84 | 82,455 | 0.4% | 8.03B | 3 |
| 123 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 739 | 0 | 112,596 | 0.3% | 7.29B | 2 |
| 124 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 713 | -2 | 31,948 | 0.5% | 11.17B | 5 |
| 125 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 713 | +8 | 17,152 | 0.6% | 1.54B | 4 |
| 126 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 640 | 0 | 2,117 | 0.6% | 27.23B | 3 |
| 127 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 631 | -6 | 20,956 | 0.5% | 3.20B | 2 |
| 128 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 625 | 0 | 806 | 0.6% | 437.8M | 2 |
| 129 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 599 | 0 | 3,801 | 0.6% | 30.68B | 1 |
| 130 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 584 | -15 | 28,072 | 0.5% | 9.24B | 2 |
| 131 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | 0 | 563 | 0.6% | 3.93B | 1 |
| 132 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | 0 | 563 | 0.6% | 3.93B | 1 |
| 133 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 562 | 0 | 562 | 0.6% | 3.93B | 1 |
| 134 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 561 | 0 | 561 | 0.6% | 3.93B | 1 |
| 135 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | 0 | 12,588 | 0.5% | 31.59B | 6 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 528 | -36 | 22,252 | 0.4% | 9.24B | 2 |
| 137 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 437 | +15 | 5,782 | 0.4% | 11.51B | 5 |
| 138 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 434 | 0 | 4,517 | 0.4% | 8.03B | 3 |
| 139 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 428 | 0 | 1,762 | 0.4% | — | 1 |
| 140 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | 0 | 1,155 | 0.4% | 437.8M | 1 |
| 141 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 393 | +19 | 12,301 | 0.4% | 27.23B | 2 |
| 142 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 389 | 0 | 3,469 | 0.4% | 560.9M | 2 |
| 143 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 302 | -15 | 22,255 | 0.2% | 2.61B | 2 |
| 144 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 302 | 0 | 2,883 | 0.3% | 4.02B | 2 |
| 145 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 292 | -6 | 107,375 | 0.1% | — | 3 |
| 146 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 280 | 0 | 37,971 | 0.2% | 27.23B | 3 |
| 147 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 278 | +2 | 70,652 | 0.2% | 8.03B | 3 |
| 148 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 265 | 0 | 32,977 | 0.2% | 40.43B | 2 |
| 149 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 265 | +12 | 1,139 | 0.3% | 9.15B | 2 |
| 150 | OpenEuroLLM Prelude SFT Excellent v0.2 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 227 | — | 227 | 0.2% | 9.09B | 1 |
| 151 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 219 | +1 | 42,002 | 0.2% | 11.17B | 1 |
| 152 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 206 | -8 | 19,774 | 0.2% | 68.98B | 2 |
| 153 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 196 | +3 | 16,714 | 0.2% | 7.29B | 2 |
| 154 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 189 | 0 | 29,848 | 0.1% | 1.01B | 1 |
| 155 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | 0 | 3,006 | 0.2% | 31.59B | 6 |
| 156 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 186 | -12 | 322,353 | 0.0% | 7.24B | 2 |
| 157 | Alfred 40B (1023) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 172 | — | 78,640 | 0.1% | — | 1 |
| 158 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 170 | -11 | 39,478 | 0.1% | 7.48B | 2 |
| 159 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | 0 | 170 | 0.2% | 7.77B | 1 |
| 160 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 167 | 0 | 1,223 | 0.2% | — | 1 |
| 161 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 160 | +3 | 44,717 | 0.1% | 7.70B | 5 |
| 162 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 157 | -1 | 28,499 | 0.1% | 46.70B | 6 |
| 163 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | +10 | 5,562 | 0.1% | 353.4M | 2 |
| 164 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 137 | 0 | 2,947 | 0.1% | 40.43B | 2 |
| 165 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 12,771 | 0.1% | 70.55B | 2 |
| 166 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 129 | 0 | 2,602 | 0.1% | — | 1 |
| 167 | GPT-SW3 1.3B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 127 | — | 306,783 | 0.0% | 1.47B | 4 |
| 168 | Bielik-One 11B v3.1 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 115 | — | 115 | 0.1% | 11.17B | 1 |
| 169 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 113 | 0 | 7,511 | 0.1% | 31.59B | 6 |
| 170 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 113 | 0 | 5,218 | 0.1% | 437.8M | 1 |
| 171 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 112 | -3 | 5,111 | 0.1% | 70.55B | 3 |
| 172 | Velvet2 3B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 100 | — | 115 | 0.1% | 3.89B | 1 |
| 173 | Alfred 40B (0723) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 99 | — | 5,541 | 0.1% | — | 1 |
| 174 | Bielik-One 7B v3.0 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 95 | — | 95 | 0.1% | 7.48B | 1 |
| 175 | OpenEuroLLM Prelude-long 9B | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 90 | — | 90 | 0.1% | 9.09B | 1 |
| 176 | Bielik-One 11B v3.0 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 83 | — | 83 | 0.1% | 11.17B | 1 |
| 177 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 38,759 | 0.1% | 70.55B | 3 |
| 178 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 65 | +7 | 7,290 | 0.1% | 1.20B | 2 |
| 179 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 62 | 0 | 438 | 0.1% | 437.8M | 1 |
| 180 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 59 | 0 | 266 | 0.1% | 437.8M | 1 |
| 181 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | 0 | 1,326 | 0.1% | 560.9M | 1 |
| 182 | OpenEuroLLM Prelude SFT Excellent v0.1 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 57 | — | 57 | 0.1% | 9.10B | 1 |
| 183 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | 0 | 207 | 0.1% | 437.8M | 1 |
| 184 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 51 | 0 | 390 | 0.1% | 7.77B | 2 |
| 185 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 48 | 0 | 973 | 0.0% | 40.43B | 2 |
| 186 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 47 | 0 | 457 | 0.0% | 321.0M | 1 |
| 187 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 44 | 0 | 221 | 0.0% | 8.16B | 3 |
| 188 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 43 | 0 | 308 | 0.0% | 437.8M | 1 |
| 189 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 42 | 0 | 1,463 | 0.0% | 8.03B | 1 |
| 190 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 41 | 0 | 277 | 0.0% | 15.17B | 3 |
| 191 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 40 | -6 | 621 | 0.0% | 6.25B | 2 |
| 192 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 39 | 0 | 230 | 0.0% | 40.43B | 2 |
| 193 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +1 | 154 | 0.0% | 7.24B | 1 |
| 194 | NorwAI Magistral 24B reasoning | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 28 | — | 547,889 | 0.0% | 23.85B | 1 |
| 195 | NorwAI Mistral-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 25 | — | 111,668 | 0.0% | 7.54B | 3 |
| 196 | GPT-SW3 20B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 22 | — | 141,983 | 0.0% | 20.92B | 5 |
| 197 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 17 | 0 | 379 | 0.0% | 12.25B | 1 |
| 198 | GPT-SW3 126M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 10 | — | 893,762 | 0.0% | 186.1M | 4 |
| 199 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 200 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 201 | GPT-SW3 40B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | — | 59,796 | 0.0% | 39.93B | 2 |
| 202 | GPT-SW3 6.7B v2 | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | — | 276,937 | 0.0% | 7.11B | 7 |
| 203 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 204 | GPT-SW3 356M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | — | 334,511 | 0.0% | 470.6M | 4 |
| 205 | GPT-SW3 6.7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | — | 68,906 | 0.0% | 7.11B | 1 |
| 206 | NorwAI Llama2-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | — | 65,548 | 0.0% | 7.03B | 1 |
| 207 | NorwAI Mixtral-8x7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | — | 2,172 | 0.0% | 47.00B | 2 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,080,197 | 310,077,644 | 32 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 254,603 | 6,099,405 | 7 | 4.1% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 217,468 | 462,550 | 6 | 38.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 180,357 | 6,544,962 | 16 | 2.7% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 72,247 | 2,674,429 | 12 | 2.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 52,886 | 1,456,057 | 13 | 3.4% |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,099 | 594,459 | 5 | 2.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,123 | 1,457,197 | 12 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,214 | 570,974 | 13 | 2.3% |
| 10 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 14,447 | 117,565 | 2 | 6.6% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,623 | 453,188 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,843 | 377,549 | 16 | 2.7% |
| 13 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,563 | 17,136 | 7 | 7.3% |
| 14 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,595 | 204,676 | 3 | 2.5% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,965 | 403,261 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,823 | 495,814 | 3 | 1.0% |
| 17 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Almawave | IT | 5,639 | 160,105 | 3 | 2.2% |
| 18 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 5,147 | 79,197 | 4 | 2.9% |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,093 | 861,713 | 3 | 0.5% |
| 20 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,274 | 701,219 | 2 | 0.5% |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 4,043 | 662,915 | 2 | 0.5% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 3,040 | 1,163,515 | 4 | 0.2% |
| 23 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,921 | 107,165 | 4 | 1.4% |
| 24 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden | SE | 2,661 | 2,178,248 | 8 | 0.1% |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,896 | 155,752 | 2 | 0.7% |
| 26 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 862 | 24,614 | 4 | 0.7% |
| 27 | [lightonai](https://huggingface.co/lightonai) | LightOn | FR | 271 | 84,181 | 2 | 0.1% |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI / NTNU | NO | 53 | 727,277 | 4 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,021,775 | 60,805,659 | 1 |
| 2 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 213,120 | 332,031 | 7 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 201,288 | 4,696,239 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 122,675 | 4,290,187 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 38,770 | 741,157 | 17 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,733 | 948,064 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 13,624 | 35,434 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,265 | 120,481 | 42 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,948 | 57,152 | 48 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,847 | 138,604 | 49 |
| 11 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude-base 9B | 4,773 | 78,823 | 53 |
| 12 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,695 | 39,255 | 54 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,444 | 155,495 | 56 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,088 | 378,866 | 59 |
| 15 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,378 | 22,921 | 66 |
| 16 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,186 | 3,229 | 68 |
| 17 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Velvet 14B | 2,788 | 70,552 | 71 |
| 18 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden Llama 3 8B | 2,496 | 95,570 | 75 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,237 | 102,866 | 79 |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,120 | 358,974 | 81 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,100 | 81,313 | 82 |
| 22 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,040 | 160,550 | 85 |
| 23 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,765 | 180,214 | 91 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,658 | 802,645 | 92 |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,095 | 58,968 | 110 |
| 26 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 135 |
| 27 | [lightonai](https://huggingface.co/lightonai) | Alfred 40B (1023) | 172 | 78,640 | 157 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI Magistral 24B reasoning | 28 | 547,889 | 194 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.7% | 217,468 | 462,550 | 3 |
| 2 | [domyn](https://huggingface.co/domyn) | 7.3% | 8,563 | 17,136 | 13 |
| 3 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 6.6% | 14,447 | 117,565 | 10 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 4.1% | 254,603 | 6,099,405 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.4% | 52,886 | 1,456,057 | 6 |
| 6 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,099 | 594,459 | 7 |
| 7 | [openeurollm](https://huggingface.co/openeurollm) | 2.9% | 5,147 | 79,197 | 18 |
| 8 | [speakleash](https://huggingface.co/speakleash) | 2.7% | 180,357 | 6,544,962 | 4 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,843 | 377,549 | 12 |
| 10 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 72,247 | 2,674,429 | 5 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,595 | 204,676 | 14 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,623 | 453,188 | 11 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.3% | 15,214 | 570,974 | 9 |
| 14 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2.2% | 5,639 | 160,105 | 17 |
| 15 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,080,197 | 310,077,644 | 1 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,921 | 107,165 | 23 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 5,965 | 403,261 | 15 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,123 | 1,457,197 | 8 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,823 | 495,814 | 16 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,896 | 155,752 | 25 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 862 | 24,614 | 26 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,274 | 701,219 | 20 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 4,043 | 662,915 | 21 |
| 24 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,093 | 861,713 | 19 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 3,040 | 1,163,515 | 22 |
| 26 | [lightonai](https://huggingface.co/lightonai) | 0.1% | 271 | 84,181 | 27 |
| 27 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0.1% | 2,661 | 2,178,248 | 24 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | 0.0% | 53 | 727,277 | 28 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
