# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-10
- **Generated at:** 2026-10-10T12:11:18Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,331,029 | -15,677 | 58,291,708 | 4.0% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,624,974 | +32,321 | 65,204,008 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 697,845 | -796 | 724,534 | 84.6% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 598,691 | -36,511 | 45,915,409 | 1.3% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 484,218 | -1,778 | 4,370,226 | 10.8% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 407,729 | -39,884 | 16,498,165 | 2.5% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 379,203 | -34,721 | 4,838,949 | 7.7% | 24.01B | 2 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 321,872 | -33,965 | 3,798,683 | 8.3% | 13.95B | 6 |
| 9 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303,520 | +12,821 | 2,928,860 | 10.0% | 24.01B | 1 |
| 10 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 269,623 | -13,471 | 596,480 | 38.7% | 22.64B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 269,454 | -3,856 | 32,427,238 | 0.8% | 46.70B | 2 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 256,792 | -1,319 | 5,510,436 | 4.6% | 24.01B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 232,745 | -6,016 | 5,669,200 | 4.0% | 4.25B | 7 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 230,880 | +304 | 925,083 | 22.5% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,015 | +474 | 2,271,292 | 9.7% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 136,198 | -2,893 | 8,538,018 | 1.6% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 81,661 | -33 | 709,476 | 10.1% | 119.40B | 3 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,681 | -213 | 751,548 | 8.5% | 23.57B | 2 |
| 19 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,662 | -7,665 | 1,102,447 | 6.0% | 127.70B | 2 |
| 20 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,897 | -890 | 7,605,905 | 0.9% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,338 | +15 | 68,276 | 39.4% | — | 1 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,821 | +3,944 | 11,239,489 | 0.5% | 140.63B | 2 |
| 23 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 50,174 | -8,797 | 4,152,280 | 1.2% | 11.34B | 8 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,247 | -977 | 689,449 | 3.6% | 7.77B | 8 |
| 25 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 24,209 | -4,224 | 538,525 | 3.8% | 70.60B | 2 |
| 26 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,816 | +27 | 5,161,161 | 0.4% | 22.25B | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 19,541 | +871 | 38,433 | 14.1% | 12.25B | 3 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,194 | +2,471 | 637,385 | 2.5% | 23.57B | 2 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,952 | -581 | 148,366 | 7.2% | 9.15B | 1 |
| 30 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,728 | -768 | 220,132 | 5.5% | — | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,909 | -262 | 782,272 | 1.6% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,747 | -149 | 77,630 | 7.7% | — | 5 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,386 | -73 | 485,709 | 2.3% | 9.15B | 1 |
| 34 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 12,253 | +255 | 136,487 | 5.2% | 7.48B | 5 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,668 | +57 | 332,906 | 2.7% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,024 | -74 | 511,859 | 1.8% | 7.24B | 8 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,067 | +166 | 4,929,109 | 0.2% | 122.61B | 1 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,952 | +99 | 5,381,058 | 0.1% | 22.25B | 1 |
| 39 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,693 | -1,489 | 26,869 | 5.3% | 72.01B | 1 |
| 40 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,287 | -333 | 351,066 | 1.4% | 125.03B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,172 | +26 | 17,154 | 5.3% | 572.6M | 5 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,780 | -328 | 146,750 | 2.3% | 2.25B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,419 | -153 | 110,599 | 2.6% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,266 | +16 | 135,577 | 2.2% | 7.40B | 3 |
| 45 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,981 | +15 | 154,561 | 2.0% | 23.57B | 2 |
| 46 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,931 | +117 | 68,141 | 2.9% | 12.77B | 5 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,823 | -278 | 49,851 | 3.2% | 8.03B | 7 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,805 | -81 | 166,109 | 1.8% | 11.17B | 16 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,650 | -4 | 373,503 | 1.0% | 7.24B | 8 |
| 50 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,411 | -199 | 111,687 | 2.1% | 7.29B | 2 |
| 51 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,388 | -28 | 12,176 | 3.9% | 27.43B | 3 |
| 52 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,269 | +106 | 149,781 | 1.7% | 7.24B | 4 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,177 | +54 | 5,034,161 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,157 | -1 | 905,651 | 0.4% | 23.57B | 2 |
| 55 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,912 | -236 | 415,028 | 0.8% | 1.20B | 1 |
| 56 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,906 | -69 | 418,522 | 0.8% | 353.4M | 1 |
| 57 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,862 | -83 | 400,074 | 0.8% | 3.21B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,839 | -88 | 67,110 | 2.3% | 14.08B | 1 |
| 59 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,681 | -65 | 670,225 | 0.5% | 7.45B | 2 |
| 60 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,623 | -130 | 253,946 | 1.0% | 4.76B | 5 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,347 | -39 | 36,420 | 2.5% | 2.61B | 3 |
| 62 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,268 | +71 | 58,910 | 2.1% | 1.60B | 5 |
| 63 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,127 | -227 | 92,735 | 1.6% | 2.89B | 1 |
| 64 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,756 | +94 | 86,044 | 1.5% | 2.22B | 1 |
| 65 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,619 | +12 | 9,231 | 2.4% | 1.51B | 6 |
| 66 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,511 | -1 | 84,400 | 1.4% | 9.15B | 1 |
| 67 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,367 | +189 | 24,359 | 1.9% | 22.64B | 1 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,221 | +17 | 49,737 | 1.5% | 9.24B | 4 |
| 69 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,180 | -121 | 40,670 | 1.5% | 13.29B | 3 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,134 | +6 | 18,252 | 1.8% | 12.19B | 2 |
| 71 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,919 | +54 | 50,065 | 1.3% | 7.77B | 1 |
| 72 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,856 | -7 | 78,719 | 1.0% | 7.45B | 1 |
| 73 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,834 | +31 | 33,709 | 1.4% | 56.7M | 1 |
| 74 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,815 | -3 | 30,320 | 1.4% | 33.12B | 1 |
| 75 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,810 | 0 | 15,486 | 1.6% | 3.83B | 5 |
| 76 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,808 | -3 | 452,642 | 0.3% | 40.43B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,806 | -5 | 106,341 | 0.9% | 7.45B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,785 | 0 | 100,181 | 0.9% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,721 | +7 | 356,322 | 0.4% | — | 3 |
| 80 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,670 | -58 | 55,595 | 1.1% | 7.55B | 1 |
| 81 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,657 | -35 | 5,301,035 | 0.0% | 7.25B | 1 |
| 82 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,644 | -476 | 33,115 | 1.2% | 22.64B | 1 |
| 83 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,620 | -5 | 177,159 | 0.6% | 12.25B | 6 |
| 84 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,619 | +2 | 158,065 | 0.6% | 1.10B | 1 |
| 85 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,581 | -56 | 22,927 | 1.3% | 11.17B | 5 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,548 | +3 | 301,553 | 0.4% | 6.74B | 2 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,510 | +7 | 184,908 | 0.5% | 6.74B | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,501 | +5 | 145,694 | 0.6% | 13.02B | 1 |
| 89 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,488 | +55 | 53,106 | 1.0% | 7.24B | 5 |
| 90 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,483 | +143 | 20,599 | 1.2% | 4.30B | 2 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,394 | +55 | 51,939 | 0.9% | 7.24B | 1 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,376 | -5 | 7,988 | 1.3% | 9.82B | 1 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,342 | -17 | 173,777 | 0.5% | 11.51B | 7 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,256 | +116 | 19,189 | 1.1% | 1.20B | 2 |
| 95 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,245 | -66 | 30,906 | 1.0% | 11.17B | 5 |
| 96 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,185 | +15 | 228,329 | 0.4% | 35.13B | 4 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,131 | -17 | 57,630 | 0.7% | 1.35B | 3 |
| 98 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,123 | +42 | 7,937 | 1.0% | 4.30B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,086 | -11 | 800,707 | 0.1% | — | 3 |
| 100 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,004 | -6 | 31,812 | 0.8% | 14.03B | 1 |
| 101 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 980 | -309 | 12,032 | 0.9% | 31.59B | 6 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 977 | +12 | 14,537 | 0.9% | 353.4M | 2 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 939 | +6 | 39,148 | 0.7% | 70.55B | 3 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 896 | -8 | 8,175 | 0.8% | 28.84B | 3 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 870 | +6 | 2,834 | 0.8% | 31.59B | 6 |
| 106 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 846 | +7 | 9,639 | 0.8% | 9.15B | 1 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 801 | +6 | 16,289 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 732 | -13 | 20,230 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 647 | -32 | 95,793 | 0.3% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 630 | 0 | 81,503 | 0.3% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 620 | +13 | 76,344 | 0.4% | 7.04B | 4 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 598 | +4 | 44,136 | 0.4% | 12.19B | 2 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 535 | +10 | 3,892 | 0.5% | 8.03B | 3 |
| 114 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 510 | -4 | 27,393 | 0.4% | 9.24B | 2 |
| 115 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 501 | +16 | 217,967 | 0.2% | 12.19B | 3 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 501 | +1 | 232,771 | 0.2% | — | 2 |
| 117 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | +2 | 21,848 | 0.4% | 2.61B | 2 |
| 118 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 444 | -2 | 13,938 | 0.4% | 4.33B | 3 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 437 | -7 | 32,606 | 0.3% | 40.43B | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 428 | +10 | 322,078 | 0.1% | 7.24B | 2 |
| 121 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 418 | -18 | 3,035 | 0.4% | 560.9M | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 399 | +6 | 39,187 | 0.3% | 7.48B | 2 |
| 123 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 395 | 0 | 7,389 | 0.4% | 31.59B | 6 |
| 124 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 384 | -3 | 3,115 | 0.4% | 30.68B | 1 |
| 125 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 372 | -4 | 11,804 | 0.3% | 27.23B | 2 |
| 126 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 365 | +8 | 1,242 | 0.4% | — | 1 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 350 | +2 | 37,616 | 0.3% | 27.23B | 3 |
| 128 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 319 | +8 | 21,551 | 0.3% | 9.24B | 2 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 311 | -5 | 12,540 | 0.3% | 70.55B | 2 |
| 130 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 308 | +1 | 107,011 | 0.1% | — | 3 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 294 | -1 | 44,490 | 0.2% | 7.70B | 5 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 284 | -11 | 70,324 | 0.2% | 8.03B | 3 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 277 | -8 | 41,708 | 0.2% | 11.17B | 1 |
| 134 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 270 | -181 | 1,499 | 0.3% | 31.58B | 2 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 241 | +2 | 16,479 | 0.2% | 7.29B | 2 |
| 136 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 238 | +5 | 5,277 | 0.2% | 11.51B | 5 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 237 | +1 | 19,509 | 0.2% | 68.98B | 2 |
| 138 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 233 | +2 | 2,548 | 0.2% | 4.02B | 2 |
| 139 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 217 | +31 | 1,278 | 0.2% | 27.23B | 3 |
| 140 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 213 | +18 | 5,057 | 0.2% | 437.8M | 1 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 212 | +4 | 2,417 | 0.2% | — | 1 |
| 142 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 202 | +23 | 4,922 | 0.2% | 70.55B | 3 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 164 | -5 | 38,640 | 0.1% | 70.55B | 3 |
| 144 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 148 | +3 | 5,376 | 0.1% | 353.4M | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | +1 | 28,281 | 0.1% | 46.70B | 6 |
| 146 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 131 | +3 | 1,030 | 0.1% | — | 1 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 117 | -2 | 7,192 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 86 | -3 | 403 | 0.1% | 321.0M | 1 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | -1 | 203 | 0.0% | 437.8M | 1 |
| 151 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | -4 | 1,250 | 0.0% | 560.9M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | 0 | 227 | 0.0% | 15.17B | 3 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | 0 | 171 | 0.0% | 8.16B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | +2 | 366 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | -2 | 148 | 0.0% | 437.8M | 1 |
| 156 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 262 | 0.0% | 437.8M | 1 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 118 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,545,143 | 301,568,826 | 30 | 2.5% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,223,566 | 5,702,025 | 7 | 21.1% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 560,496 | 2,566,120 | 11 | 21.0% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 103,739 | 6,336,458 | 12 | 1.6% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,338 | 68,276 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,191 | 1,371,512 | 5 | 2.6% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 24,057 | 388,295 | 10 | 4.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 18,908 | 1,436,203 | 11 | 1.2% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,756 | 546,005 | 13 | 2.6% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 11,436 | 435,055 | 6 | 2.1% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,283 | 360,556 | 14 | 2.4% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,252 | 193,291 | 6 | 3.2% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,343 | 855,285 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,595 | 153,154 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,112 | 194,276 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,266 | 135,577 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,078 | 695,581 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,630 | 488,667 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,269 | 657,875 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,515 | 23,754 | 4 | 2.0% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,226 | 103,694 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,132 | 1,159,998 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,778 | 153,423 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,376 | 7,988 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 620 | 76,344 | 1 | 0.4% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,331,029 | 58,291,708 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 697,845 | 724,534 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 269,623 | 596,480 | 10 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,338 | 68,276 | 21 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 50,174 | 4,152,280 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,247 | 689,449 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 19,541 | 38,433 | 27 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,419 | 110,599 | 43 |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,266 | 135,577 | 44 |
| 10 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,931 | 68,141 | 46 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,823 | 49,851 | 47 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,650 | 373,503 | 49 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,411 | 111,687 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,269 | 149,781 | 52 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,912 | 415,028 | 55 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,839 | 67,110 | 58 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,681 | 670,225 | 59 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,785 | 100,181 | 78 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,721 | 356,322 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,619 | 158,065 | 84 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,376 | 7,988 | 92 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,131 | 57,630 | 97 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,086 | 800,707 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 980 | 12,032 | 101 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 620 | 76,344 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,338 | 68,276 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.1% | 1,223,566 | 5,702,025 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 21.0% | 560,496 | 2,566,120 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4.9% | 24,057 | 388,295 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.2% | 9,252 | 193,291 | 12 |
| 6 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,595 | 153,154 | 14 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,191 | 1,371,512 | 6 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.6% | 16,756 | 546,005 | 9 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.5% | 7,545,143 | 301,568,826 | 1 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,283 | 360,556 | 11 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,266 | 135,577 | 16 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.1% | 11,436 | 435,055 | 10 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,112 | 194,276 | 15 |
| 14 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.0% | 2,515 | 23,754 | 20 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.6% | 103,739 | 6,336,458 | 4 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,376 | 7,988 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 18,908 | 1,436,203 | 8 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,226 | 103,694 | 21 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,630 | 488,667 | 18 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,343 | 855,285 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,778 | 153,423 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,078 | 695,581 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,269 | 657,875 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.4% | 620 | 76,344 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,132 | 1,159,998 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
