# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-27
- **Generated at:** 2026-10-27T11:51:17Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,897,551 | -1,795 | 59,256,839 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,831,711 | +36,108 | 66,301,807 | 2.8% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 506,374 | +17,783 | 46,175,082 | 1.1% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 448,964 | +21,362 | 4,120,355 | 10.6% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 413,891 | -9,164 | 4,597,534 | 8.8% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 300,924 | +10,595 | 32,619,342 | 0.9% | 46.70B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 294,377 | -2,228 | 16,611,320 | 1.8% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 270,038 | -29,524 | 735,428 | 32.3% | 8.90B | 1 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 222,621 | +135 | 4,934,388 | 4.4% | 24.01B | 2 |
| 10 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 216,260 | +2,327 | 5,784,371 | 3.7% | 4.25B | 7 |
| 11 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 191,963 | +1,856 | 937,497 | 18.5% | 1.66B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 191,548 | +2,450 | 2,383,863 | 7.7% | 8.92B | 6 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 181,923 | -6,822 | 2,999,015 | 5.9% | 24.01B | 1 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 177,710 | -180 | 5,580,369 | 3.1% | 24.01B | 1 |
| 15 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 100,290 | +9,742 | 166,696 | 37.6% | 12.77B | 5 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 89,323 | +3,431 | 7,662,197 | 1.2% | 23.57B | 2 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,042 | +510 | 790,027 | 7.8% | 23.57B | 2 |
| 18 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 67,074 | +1,492 | 11,270,642 | 0.6% | 140.63B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,879 | -621 | 724,661 | 8.1% | 119.40B | 3 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 54,787 | +44 | 8,561,293 | 0.6% | 8.02B | 1 |
| 21 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 43,308 | -11,903 | 600,906 | 6.2% | 22.64B | 1 |
| 22 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 40,011 | +1,655 | 716,646 | 4.9% | 7.77B | 8 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,038 | -6,118 | 1,113,203 | 3.1% | 127.70B | 2 |
| 24 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,711 | +412 | 359,707 | 7.3% | 24.01B | 2 |
| 25 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 28,318 | -26,528 | 76,125 | 16.1% | — | 1 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 26,578 | -455 | 238,631 | 7.8% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,472 | +31 | 44,011 | 17.0% | 12.25B | 3 |
| 28 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,691 | +2,005 | 4,164,672 | 0.5% | 11.34B | 8 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 18,853 | -293 | 548,395 | 2.9% | 70.60B | 2 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,800 | +381 | 645,603 | 2.0% | 23.57B | 2 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,702 | +516 | 790,492 | 1.5% | 11.25B | 10 |
| 32 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,339 | +148 | 157,063 | 5.2% | 9.15B | 1 |
| 33 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,075 | +54 | 5,044,944 | 0.3% | 122.61B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,675 | +56 | 20,031 | 9.7% | 27.43B | 3 |
| 35 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,146 | -4 | 518,327 | 1.8% | 7.24B | 8 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,062 | +103 | 82,964 | 6.0% | — | 5 |
| 37 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,988 | +40 | 491,430 | 1.9% | 9.15B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,662 | +293 | 4,935,561 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,347 | +175 | 5,385,378 | 0.2% | 22.25B | 1 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,507 | -12 | 138,962 | 3.1% | 7.48B | 5 |
| 41 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,198 | +484 | 32,245 | 5.4% | 72.01B | 1 |
| 42 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,017 | +398 | 20,256 | 5.8% | 572.6M | 5 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,688 | +130 | 115,482 | 3.1% | 8.42B | 7 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,823 | +171 | 354,734 | 1.3% | 125.03B | 1 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,493 | +16 | 81,525 | 3.0% | 7.04B | 4 |
| 46 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,457 | +133 | 149,109 | 2.2% | 2.25B | 7 |
| 47 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,928 | +93 | 138,255 | 2.1% | 7.40B | 3 |
| 48 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,786 | +452 | 12,738 | 4.2% | 1.51B | 6 |
| 49 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,440 | -84 | 168,432 | 1.7% | 11.17B | 16 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,413 | +11 | 152,361 | 1.7% | 7.24B | 4 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,344 | +5 | 375,957 | 0.9% | 7.24B | 8 |
| 52 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,324 | -20 | 5,163,158 | 0.1% | 22.25B | 1 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,064 | +100 | 908,504 | 0.4% | 23.57B | 2 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,904 | +79 | 39,011 | 2.8% | 2.61B | 3 |
| 55 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,860 | +366 | 18,573 | 3.3% | 3.83B | 5 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,858 | +33 | 61,324 | 2.4% | 1.60B | 5 |
| 57 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,810 | -20 | 52,128 | 2.5% | 8.03B | 7 |
| 58 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,739 | +189 | 156,532 | 1.5% | 23.57B | 2 |
| 59 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,586 | +61 | 256,035 | 1.0% | 4.76B | 5 |
| 60 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,147 | +117 | 35,572 | 2.3% | 56.7M | 1 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,112 | +78 | 94,573 | 1.6% | 2.89B | 1 |
| 62 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,891 | +172 | 42,407 | 2.0% | 13.29B | 3 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,657 | +7 | 25,791 | 2.1% | 22.64B | 1 |
| 64 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,656 | -3 | 34,262 | 2.0% | 14.03B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,445 | -1 | 178,943 | 0.9% | 12.25B | 6 |
| 66 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,255 | -12 | 415,511 | 0.4% | 1.20B | 1 |
| 67 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,127 | +208 | 21,950 | 1.7% | 4.30B | 2 |
| 68 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,120 | +26 | 5,302,548 | 0.0% | 7.25B | 1 |
| 69 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,087 | -9 | 400,355 | 0.4% | 3.21B | 1 |
| 70 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,048 | -6 | 418,823 | 0.4% | 353.4M | 1 |
| 71 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,027 | +17 | 51,359 | 1.3% | 7.77B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,000 | -61 | 19,334 | 1.7% | 12.19B | 2 |
| 73 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,980 | +20 | 50,890 | 1.3% | 9.24B | 4 |
| 74 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,920 | +20 | 101,327 | 1.0% | 30.68B | 1 |
| 75 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,885 | +10 | 357,479 | 0.4% | — | 3 |
| 76 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,869 | +85 | 229,639 | 0.6% | 35.13B | 4 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,868 | +13 | 79,803 | 1.0% | 7.45B | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,819 | +28 | 107,428 | 0.9% | 7.45B | 1 |
| 79 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,747 | -94 | 670,875 | 0.2% | 7.45B | 2 |
| 80 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,723 | +22 | 9,031 | 1.6% | 4.30B | 3 |
| 81 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,713 | +13 | 34,147 | 1.3% | 22.64B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,698 | +15 | 159,089 | 0.7% | 1.10B | 1 |
| 83 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,686 | +13 | 302,573 | 0.4% | 6.74B | 2 |
| 84 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,632 | +5 | 185,888 | 0.6% | 6.74B | 1 |
| 85 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,620 | +9 | 146,671 | 0.7% | 13.02B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,545 | -3 | 54,015 | 1.0% | 7.24B | 5 |
| 87 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,475 | -7 | 8,998 | 1.4% | 9.82B | 1 |
| 88 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,460 | -6 | 52,799 | 1.0% | 7.24B | 1 |
| 89 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,455 | +47 | 40,105 | 1.0% | 70.55B | 3 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,441 | +11 | 174,582 | 0.5% | 11.51B | 7 |
| 91 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,361 | +3 | 23,634 | 1.1% | 11.17B | 5 |
| 92 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,326 | -246 | 31,390 | 1.0% | 33.12B | 1 |
| 93 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,291 | +11 | 19,852 | 1.1% | 1.20B | 2 |
| 94 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,186 | +3 | 801,489 | 0.1% | — | 3 |
| 95 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,166 | -3 | 10,459 | 1.1% | 9.15B | 1 |
| 96 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,139 | -7 | 31,495 | 0.9% | 11.17B | 5 |
| 97 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,090 | +125 | 9,049 | 1.0% | 28.84B | 3 |
| 98 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,077 | -59 | 56,155 | 0.7% | 7.55B | 1 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,027 | -12 | 58,205 | 0.6% | 1.35B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 973 | +18 | 15,044 | 0.8% | 353.4M | 2 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 877 | -11 | 453,182 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 824 | +7 | 218,629 | 0.3% | 12.19B | 3 |
| 103 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 814 | -34 | 111,980 | 0.4% | 7.29B | 2 |
| 104 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 787 | +19 | 44,765 | 0.5% | 12.19B | 2 |
| 105 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 751 | +19 | 16,675 | 0.6% | 1.54B | 4 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 670 | -1 | 81,901 | 0.4% | 8.03B | 3 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 638 | +15 | 14,419 | 0.6% | 4.33B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 597 | +12 | 96,207 | 0.3% | 1.35B | 8 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 546 | +16 | 4,248 | 0.5% | 8.03B | 3 |
| 110 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 495 | +11 | 21,893 | 0.4% | 9.24B | 2 |
| 111 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 482 | +9 | 3,420 | 0.5% | 30.68B | 1 |
| 112 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 433 | +9 | 20,427 | 0.4% | 3.20B | 2 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 419 | +60 | 233,033 | 0.1% | — | 2 |
| 114 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 412 | +18 | 1,509 | 0.4% | — | 1 |
| 115 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 370 | -10 | 32,820 | 0.3% | 40.43B | 2 |
| 116 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 345 | +10 | 1,532 | 0.3% | 27.23B | 3 |
| 117 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 338 | +3 | 27,569 | 0.3% | 9.24B | 2 |
| 118 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 326 | +12 | 2,755 | 0.3% | 4.02B | 2 |
| 119 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 321 | +10 | 84,526 | 0.2% | 9.15B | 1 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 314 | 0 | 22,030 | 0.3% | 2.61B | 2 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 314 | +14 | 5,459 | 0.3% | 11.51B | 5 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 312 | -24 | 37,782 | 0.2% | 27.23B | 3 |
| 123 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 306 | 0 | 322,216 | 0.1% | 7.24B | 2 |
| 124 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 298 | +4 | 12,018 | 0.3% | 27.23B | 2 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 287 | -2 | 107,165 | 0.1% | — | 3 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 284 | -1 | 39,354 | 0.2% | 7.48B | 2 |
| 127 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 271 | +3 | 5,141 | 0.3% | 437.8M | 1 |
| 128 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 257 | +1 | 12,691 | 0.2% | 70.55B | 2 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 223 | +4 | 41,850 | 0.2% | 11.17B | 1 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 222 | -5 | 19,636 | 0.2% | 68.98B | 2 |
| 131 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 217 | +12 | 5,041 | 0.2% | 70.55B | 3 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 215 | -7 | 44,611 | 0.1% | 7.70B | 5 |
| 133 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 200 | 0 | 2,525 | 0.2% | — | 1 |
| 134 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 199 | -5 | 7,459 | 0.2% | 31.59B | 6 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 190 | +1 | 16,583 | 0.2% | 7.29B | 2 |
| 136 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 180 | +7 | 70,425 | 0.1% | 8.03B | 3 |
| 137 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 173 | 0 | 1,503 | 0.2% | 31.58B | 2 |
| 138 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 157 | +6 | 3,117 | 0.2% | 560.9M | 2 |
| 139 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 154 | +5 | 28,381 | 0.1% | 46.70B | 6 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 149 | -4 | 5,455 | 0.1% | 353.4M | 2 |
| 141 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 145 | +67 | 12,151 | 0.1% | 31.59B | 6 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 6,171 | 0.1% | 12.25B | 3 |
| 143 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 124 | -5 | 1,121 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 104 | +2 | 7,242 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 100 | -4 | 38,704 | 0.1% | 70.55B | 3 |
| 146 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 84 | +1 | 432 | 0.1% | 321.0M | 1 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 70 | +7 | 1,302 | 0.1% | 560.9M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 48 | +1 | 2,854 | 0.0% | 31.59B | 6 |
| 149 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | +3 | 397 | 0.0% | 437.8M | 1 |
| 150 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 41 | 0 | 254 | 0.0% | 15.17B | 3 |
| 151 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 36 | 0 | 192 | 0.0% | 8.16B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | +2 | 219 | 0.0% | 437.8M | 1 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | -2 | 131 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +3 | 274 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | +2 | 155 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,767,369 | 305,231,037 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 725,643 | 5,965,169 | 7 | 12.0% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 296,137 | 2,621,986 | 11 | 10.9% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 104,111 | 294,002 | 6 | 26.4% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 69,408 | 6,375,264 | 12 | 1.1% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 48,742 | 1,403,116 | 5 | 3.2% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,230 | 397,646 | 10 | 6.1% |
| 8 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 28,318 | 76,125 | 1 | 16.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,590 | 560,250 | 13 | 3.3% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 15,699 | 1,442,594 | 11 | 1.0% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,193 | 443,679 | 6 | 2.2% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,482 | 367,247 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,187 | 199,447 | 3 | 2.4% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,493 | 81,525 | 1 | 3.0% |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,434 | 858,106 | 3 | 0.6% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,950 | 491,648 | 3 | 0.8% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,928 | 138,255 | 1 | 2.1% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,650 | 698,173 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,571 | 660,052 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,479 | 105,193 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,114 | 1,161,323 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,624 | 154,412 | 2 | 0.6% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,475 | 8,998 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 565 | 23,967 | 4 | 0.5% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,897,551 | 59,256,839 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 413,891 | 4,597,534 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 191,963 | 937,497 | 11 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 100,290 | 166,696 | 15 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 40,011 | 716,646 | 22 |
| 6 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 28,318 | 76,125 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,472 | 44,011 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,691 | 4,164,672 | 28 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,675 | 20,031 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,688 | 115,482 | 43 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,493 | 81,525 | 45 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,928 | 138,255 | 47 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,413 | 152,361 | 50 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,344 | 375,957 | 51 |
| 15 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,810 | 52,128 | 57 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,147 | 35,572 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,920 | 101,327 | 74 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,885 | 357,479 | 75 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,868 | 79,803 | 77 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,698 | 159,089 | 82 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,475 | 8,998 | 87 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,186 | 801,489 | 94 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,027 | 58,205 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 199 | 7,459 | 134 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 26.4% | 104,111 | 294,002 | 4 |
| 2 | [openeurollm](https://huggingface.co/openeurollm) | 16.1% | 28,318 | 76,125 | 8 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 12.0% | 725,643 | 5,965,169 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 10.9% | 296,137 | 2,621,986 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,230 | 397,646 | 7 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,590 | 560,250 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.2% | 48,742 | 1,403,116 | 6 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,493 | 81,525 | 14 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,482 | 367,247 | 12 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,187 | 199,447 | 13 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.2% | 12,193 | 443,679 | 11 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,767,369 | 305,231,037 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,928 | 138,255 | 17 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,475 | 8,998 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,479 | 105,193 | 20 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 69,408 | 6,375,264 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 15,699 | 1,442,594 | 10 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,950 | 491,648 | 16 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.6% | 1,624 | 154,412 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,650 | 698,173 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,434 | 858,106 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,571 | 660,052 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 565 | 23,967 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,114 | 1,161,323 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
