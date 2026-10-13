# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-13
- **Generated at:** 2026-10-13T13:52:49Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,292,789 | -10,349 | 58,491,407 | 3.9% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,635,836 | -11,436 | 65,419,491 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 699,922 | +426 | 727,776 | 84.6% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 514,278 | +1,443 | 45,951,467 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 490,095 | +34 | 4,424,174 | 10.8% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 349,716 | -25,213 | 16,509,991 | 2.1% | 12.25B | 3 |
| 7 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 327,961 | -4,611 | 2,980,295 | 10.6% | 24.01B | 1 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 314,129 | -15,381 | 4,857,291 | 6.3% | 24.01B | 2 |
| 9 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 310,439 | -3,762 | 3,824,308 | 7.9% | 13.95B | 6 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,514 | -1,042 | 5,519,838 | 4.5% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,309 | -1,731 | 32,442,763 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 231,759 | +2,026 | 5,688,600 | 4.0% | 4.25B | 7 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,245 | +181 | 926,234 | 22.5% | 1.66B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 228,478 | -13,516 | 597,371 | 32.8% | 22.64B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 218,640 | +955 | 2,286,694 | 9.2% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 113,572 | -8,110 | 8,543,025 | 1.3% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 78,930 | -780 | 712,233 | 9.7% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,747 | +284 | 1,104,265 | 6.0% | 127.70B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,301 | +16 | 757,479 | 8.3% | 23.57B | 2 |
| 20 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,508 | +2,493 | 7,614,760 | 0.9% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 68,740 | +841 | 70,678 | 40.3% | — | 1 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,977 | +206 | 11,242,790 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 37,970 | +24,449 | 101,571 | 18.8% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,593 | +1,168 | 692,133 | 3.6% | 7.77B | 8 |
| 25 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 23,793 | +2,895 | 42,765 | 16.7% | 12.25B | 3 |
| 26 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 22,939 | -6,437 | 4,154,541 | 0.5% | 11.34B | 8 |
| 27 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,701 | +197 | 540,721 | 3.4% | 70.60B | 2 |
| 28 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,981 | +29 | 5,161,587 | 0.4% | 22.25B | 1 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,285 | +1,321 | 151,793 | 7.7% | 9.15B | 1 |
| 30 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,293 | +178 | 221,982 | 5.4% | — | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,824 | -56 | 638,209 | 2.3% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,686 | -60 | 783,632 | 1.5% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,333 | +152 | 78,547 | 7.5% | — | 5 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,098 | -2 | 487,078 | 2.2% | 9.15B | 1 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,481 | +146 | 334,195 | 2.6% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,201 | +44 | 513,140 | 1.8% | 7.24B | 8 |
| 37 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,492 | +87 | 137,052 | 4.0% | 7.48B | 5 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,299 | +130 | 4,929,879 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,123 | +51 | 5,381,662 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,354 | +80 | 17,445 | 5.4% | 572.6M | 5 |
| 41 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,795 | +25 | 147,159 | 2.3% | 2.25B | 7 |
| 42 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,703 | -87 | 351,577 | 1.3% | 125.03B | 1 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,477 | +8 | 111,224 | 2.6% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,339 | -20 | 136,111 | 2.3% | 7.40B | 3 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,200 | +63 | 50,426 | 3.5% | 8.03B | 7 |
| 46 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,094 | -848 | 27,082 | 4.0% | 72.01B | 1 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,925 | -69 | 154,686 | 1.9% | 23.57B | 2 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,807 | -56 | 166,600 | 1.8% | 11.17B | 16 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,740 | -44 | 374,065 | 1.0% | 7.24B | 8 |
| 50 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,452 | +51 | 12,305 | 4.0% | 27.43B | 3 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,357 | -4 | 150,260 | 1.7% | 7.24B | 4 |
| 52 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,269 | -25 | 111,769 | 2.0% | 7.29B | 2 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,068 | -69 | 5,034,478 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,858 | -240 | 905,876 | 0.4% | 23.57B | 2 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,821 | +122 | 254,418 | 1.1% | 4.76B | 5 |
| 56 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,723 | 0 | 67,382 | 2.2% | 14.08B | 1 |
| 57 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,646 | -24 | 670,434 | 0.5% | 7.45B | 2 |
| 58 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,308 | -27 | 36,786 | 2.4% | 2.61B | 3 |
| 59 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,250 | -201 | 400,120 | 0.6% | 3.21B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,243 | -205 | 415,069 | 0.6% | 1.20B | 1 |
| 61 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,221 | -259 | 418,568 | 0.6% | 353.4M | 1 |
| 62 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,220 | -8 | 59,210 | 2.0% | 1.60B | 5 |
| 63 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,171 | +14 | 93,101 | 1.6% | 2.89B | 1 |
| 64 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,724 | +37 | 9,412 | 2.5% | 1.51B | 6 |
| 65 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,717 | +2 | 86,317 | 1.5% | 2.22B | 1 |
| 66 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,583 | +14 | 24,734 | 2.1% | 22.64B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,538 | -3 | 84,440 | 1.4% | 9.15B | 1 |
| 68 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,392 | +83 | 41,072 | 1.7% | 13.29B | 3 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,335 | +39 | 50,526 | 1.6% | 7.77B | 1 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,274 | +22 | 49,945 | 1.5% | 9.24B | 4 |
| 71 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,164 | +213 | 34,108 | 1.6% | 56.7M | 1 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,088 | +55 | 30,621 | 1.6% | 33.12B | 1 |
| 73 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,076 | +17 | 18,420 | 1.8% | 12.19B | 2 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,878 | -1 | 78,916 | 1.0% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,846 | +8 | 106,546 | 0.9% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,843 | +22 | 100,395 | 0.9% | 30.68B | 1 |
| 77 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,838 | +9 | 452,736 | 0.3% | 40.43B | 1 |
| 78 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,812 | -12 | 15,629 | 1.6% | 3.83B | 5 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,758 | +2 | 356,532 | 0.4% | — | 3 |
| 80 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,734 | +77 | 177,431 | 0.6% | 12.25B | 6 |
| 81 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,672 | -4 | 5,301,170 | 0.0% | 7.25B | 1 |
| 82 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,644 | 0 | 33,297 | 1.2% | 22.64B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,642 | -1 | 158,244 | 0.6% | 1.10B | 1 |
| 84 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,631 | -5 | 55,737 | 1.0% | 7.55B | 1 |
| 85 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,581 | -12 | 23,149 | 1.3% | 11.17B | 5 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,578 | +1 | 301,739 | 0.4% | 6.74B | 2 |
| 87 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,575 | +213 | 32,412 | 1.2% | 14.03B | 1 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,538 | +1 | 185,089 | 0.5% | 6.74B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,532 | -5 | 53,280 | 1.0% | 7.24B | 5 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,520 | -3 | 145,873 | 0.6% | 13.02B | 1 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,443 | -1 | 52,109 | 0.9% | 7.24B | 1 |
| 92 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,414 | +18 | 20,797 | 1.2% | 4.30B | 2 |
| 93 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,370 | +41 | 8,282 | 1.3% | 4.30B | 3 |
| 94 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,364 | +11 | 8,051 | 1.3% | 9.82B | 1 |
| 95 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,356 | +9 | 173,904 | 0.5% | 11.51B | 7 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,333 | +32 | 19,313 | 1.1% | 1.20B | 2 |
| 97 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,260 | -22 | 31,044 | 1.0% | 11.17B | 5 |
| 98 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,244 | +4 | 228,490 | 0.4% | 35.13B | 4 |
| 99 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,168 | +18 | 10,044 | 1.1% | 9.15B | 1 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,131 | +74 | 14,738 | 1.0% | 353.4M | 2 |
| 101 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,121 | -14 | 57,718 | 0.7% | 1.35B | 3 |
| 102 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,116 | -17 | 800,833 | 0.1% | — | 3 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,038 | +34 | 39,301 | 0.7% | 70.55B | 3 |
| 104 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 933 | 0 | 12,033 | 0.8% | 31.59B | 6 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 870 | 0 | 2,834 | 0.8% | 31.59B | 6 |
| 106 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 834 | +26 | 16,367 | 0.7% | 1.54B | 4 |
| 107 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 828 | -35 | 8,231 | 0.8% | 28.84B | 3 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 746 | +2 | 20,282 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 708 | +26 | 95,898 | 0.4% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 668 | +10 | 81,598 | 0.4% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 614 | -18 | 76,401 | 0.3% | 7.04B | 4 |
| 112 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 596 | -10 | 4,004 | 0.6% | 8.03B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 525 | -10 | 232,813 | 0.2% | — | 2 |
| 114 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 515 | +44 | 218,080 | 0.2% | 12.19B | 3 |
| 115 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 443 | -83 | 44,160 | 0.3% | 12.19B | 2 |
| 116 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 436 | -23 | 13,984 | 0.4% | 4.33B | 3 |
| 117 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 431 | -18 | 32,648 | 0.3% | 40.43B | 2 |
| 118 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 427 | -95 | 27,421 | 0.3% | 9.24B | 2 |
| 119 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 424 | +5 | 3,175 | 0.4% | 30.68B | 1 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 421 | -13 | 322,118 | 0.1% | 7.24B | 2 |
| 121 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 418 | -13 | 3,065 | 0.4% | 560.9M | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 414 | -13 | 39,225 | 0.3% | 7.48B | 2 |
| 123 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 396 | 0 | 7,390 | 0.4% | 31.59B | 6 |
| 124 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 388 | +5 | 1,287 | 0.4% | — | 1 |
| 125 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 332 | +76 | 1,410 | 0.3% | 27.23B | 3 |
| 126 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 330 | -107 | 21,865 | 0.3% | 2.61B | 2 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 316 | -1 | 37,636 | 0.2% | 27.23B | 3 |
| 128 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 314 | -32 | 21,592 | 0.3% | 9.24B | 2 |
| 129 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 306 | -10 | 107,043 | 0.1% | — | 3 |
| 130 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 304 | -12 | 41,758 | 0.2% | 11.17B | 1 |
| 131 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 297 | -85 | 11,826 | 0.3% | 27.23B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 293 | -6 | 70,345 | 0.2% | 8.03B | 3 |
| 133 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 265 | +7 | 5,312 | 0.3% | 11.51B | 5 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 264 | -20 | 44,527 | 0.2% | 7.70B | 5 |
| 135 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 255 | -8 | 12,562 | 0.2% | 70.55B | 2 |
| 136 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 243 | +10 | 5,095 | 0.2% | 437.8M | 1 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 232 | -6 | 19,532 | 0.2% | 68.98B | 2 |
| 138 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 230 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 139 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 228 | +6 | 4,984 | 0.2% | 70.55B | 3 |
| 140 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 211 | 0 | 2,437 | 0.2% | — | 1 |
| 141 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 204 | -25 | 2,565 | 0.2% | 4.02B | 2 |
| 142 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 202 | -32 | 16,489 | 0.2% | 7.29B | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 150 | -13 | 38,651 | 0.1% | 70.55B | 3 |
| 144 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 148 | -6 | 5,396 | 0.1% | 353.4M | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 146 | -2 | 28,303 | 0.1% | 46.70B | 6 |
| 146 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140 | +3 | 1,043 | 0.1% | — | 1 |
| 147 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 121 | -6 | 7,210 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 82 | -4 | 406 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 36 | +3 | 1,259 | 0.0% | 560.9M | 1 |
| 151 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 30 | -4 | 230 | 0.0% | 15.17B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | -1 | 205 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | -3 | 174 | 0.0% | 8.16B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | -1 | 371 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 151 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | -1 | 119 | 0.0% | 7.24B | 1 |
| 157 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | -1 | 263 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,265,200 | 302,220,893 | 30 | 2.4% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,227,702 | 5,762,239 | 7 | 20.9% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 520,851 | 2,576,196 | 11 | 19.5% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 73,932 | 6,343,760 | 12 | 1.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 68,740 | 70,678 | 1 | 40.3% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 42,472 | 227,211 | 6 | 13.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,992 | 1,375,202 | 5 | 2.6% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 28,697 | 393,494 | 10 | 5.8% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,753 | 1,437,598 | 11 | 1.2% |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,003 | 546,939 | 13 | 2.5% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,776 | 436,987 | 6 | 2.4% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,503 | 361,851 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,370 | 855,896 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,440 | 153,699 | 2 | 2.5% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,155 | 194,976 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,339 | 136,111 | 1 | 2.3% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,161 | 696,183 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,700 | 489,206 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,336 | 658,271 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,429 | 23,758 | 4 | 2.0% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,323 | 103,974 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,179 | 1,160,221 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,829 | 153,616 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,364 | 8,051 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 614 | 76,401 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,292,789 | 58,491,407 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 699,922 | 727,776 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,245 | 926,234 | 13 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 68,740 | 70,678 | 21 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 37,970 | 101,571 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,593 | 692,133 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 23,793 | 42,765 | 25 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 22,939 | 4,154,541 | 26 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,477 | 111,224 | 43 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,339 | 136,111 | 44 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,200 | 50,426 | 45 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,740 | 374,065 | 49 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,452 | 12,305 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,357 | 150,260 | 51 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,723 | 67,382 | 56 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,646 | 670,434 | 57 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 3B Preview | 3,250 | 400,120 | 59 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,843 | 100,395 | 76 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,758 | 356,532 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,642 | 158,244 | 83 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,364 | 8,051 | 94 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,121 | 57,718 | 101 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,116 | 800,833 | 102 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 933 | 12,033 | 104 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 614 | 76,401 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 40.3% | 68,740 | 70,678 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 20.9% | 1,227,702 | 5,762,239 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 19.5% | 520,851 | 2,576,196 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 13.0% | 42,472 | 227,211 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5.8% | 28,697 | 393,494 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,992 | 1,375,202 | 7 |
| 7 | [Almawave](https://huggingface.co/Almawave) | 2.5% | 6,440 | 153,699 | 14 |
| 8 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,503 | 361,851 | 12 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.5% | 16,003 | 546,939 | 10 |
| 10 | [mistralai](https://huggingface.co/mistralai) | 2.4% | 7,265,200 | 302,220,893 | 1 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.4% | 12,776 | 436,987 | 11 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.3% | 5,339 | 136,111 | 16 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,155 | 194,976 | 15 |
| 14 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.0% | 2,429 | 23,758 | 20 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,364 | 8,051 | 24 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 17,753 | 1,437,598 | 9 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 73,932 | 6,343,760 | 4 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,323 | 103,974 | 21 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,700 | 489,206 | 18 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,370 | 855,896 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,829 | 153,616 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,161 | 696,183 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,336 | 658,271 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 614 | 76,401 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,179 | 1,160,221 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
