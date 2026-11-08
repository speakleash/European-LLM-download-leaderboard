# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-08
- **Generated at:** 2026-11-08T13:05:00Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,933,153 | +20,891 | 60,218,153 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,514,195 | -46,306 | 66,710,328 | 2.3% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 618,751 | +16,084 | 4,416,032 | 13.7% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 515,273 | -4,387 | 46,429,603 | 1.1% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 336,608 | +3,583 | 32,763,168 | 1.0% | 46.70B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 320,918 | -14,379 | 4,688,799 | 6.7% | 8.05B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 251,514 | -1,906 | 2,522,205 | 9.6% | 8.92B | 6 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 218,577 | +8,709 | 286,698 | 56.5% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,705 | -1,471 | 5,873,919 | 3.4% | 3.85B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 164,245 | -6,279 | 5,002,444 | 3.2% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 155,126 | -5,382 | 16,652,399 | 0.9% | 12.25B | 3 |
| 12 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 107,600 | -867 | 7,713,247 | 1.4% | 23.57B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 106,282 | -2,964 | 5,616,158 | 1.9% | 24.01B | 1 |
| 14 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 84,361 | -20,176 | 3,008,553 | 2.7% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 60,778 | -159 | 8,598,679 | 0.7% | 8.02B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 55,176 | -2,246 | 806,394 | 6.1% | 23.57B | 2 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,432 | -4,823 | 11,284,638 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,225 | -335 | 734,646 | 5.4% | 7.77B | 8 |
| 19 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 44,122 | +7,542 | 4,196,358 | 1.0% | 11.34B | 8 |
| 20 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,333 | -435 | 742,618 | 4.0% | 119.40B | 3 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,762 | +113 | 365,590 | 7.0% | 24.01B | 2 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,935 | -202 | 245,049 | 7.2% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,864 | -320 | 944,886 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,115 | -392 | 1,119,499 | 1.4% | 127.70B | 2 |
| 25 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,420 | +32 | 798,638 | 1.8% | 11.25B | 10 |
| 26 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,490 | -195 | 739,929 | 1.8% | 8.90B | 1 |
| 27 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,136 | +137 | 4,943,218 | 0.3% | 122.61B | 1 |
| 28 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,757 | -8 | 5,046,905 | 0.2% | 122.61B | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,572 | -3,439 | 649,916 | 1.7% | 23.57B | 2 |
| 30 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 12,202 | -602 | 550,633 | 1.9% | 70.60B | 2 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,500 | -31 | 159,825 | 4.4% | 9.15B | 1 |
| 32 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,250 | +12 | 523,074 | 1.8% | 7.24B | 8 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,753 | -130 | 496,409 | 1.8% | 9.15B | 1 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,319 | +1,867 | 22,493 | 8.4% | 27.43B | 3 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,829 | +44 | 5,389,854 | 0.2% | 22.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,660 | -169 | 86,252 | 4.6% | — | 5 |
| 37 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,485 | -10 | 76,761 | 4.8% | — | 1 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,230 | -33 | 35,086 | 6.1% | 72.01B | 1 |
| 39 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,932 | -128 | 118,519 | 3.6% | 8.42B | 7 |
| 40 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,320 | -858 | 603,775 | 1.0% | 22.64B | 1 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,692 | +8 | 15,911 | 5.8% | 1.51B | 6 |
| 42 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,548 | -27 | 357,594 | 1.4% | 125.03B | 1 |
| 43 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6,271 | -943 | 44,646 | 4.3% | 12.25B | 3 |
| 44 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,794 | +43 | 259,734 | 1.6% | 4.76B | 5 |
| 45 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,610 | +43 | 21,087 | 4.6% | 3.83B | 5 |
| 46 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,608 | +13 | 81,949 | 3.1% | 7.04B | 4 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,191 | +149 | 55,037 | 3.3% | 8.03B | 7 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,113 | -32 | 151,854 | 2.0% | 2.25B | 7 |
| 49 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,002 | +221 | 22,148 | 4.1% | 572.6M | 5 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,639 | -18 | 910,282 | 0.5% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,544 | -7 | 154,303 | 1.8% | 7.24B | 4 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,482 | -60 | 140,037 | 1.9% | 7.40B | 3 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,416 | +7 | 63,322 | 2.7% | 1.60B | 5 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,397 | -10 | 377,887 | 0.9% | 7.24B | 8 |
| 55 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,192 | +16 | 40,595 | 3.0% | 2.61B | 3 |
| 56 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,147 | -238 | 140,622 | 1.7% | 7.48B | 5 |
| 57 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,104 | -122 | 37,785 | 3.0% | 56.7M | 1 |
| 58 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,077 | -152 | 5,165,225 | 0.1% | 22.25B | 1 |
| 59 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,808 | +411 | 28,103 | 3.0% | 22.64B | 1 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,802 | +6 | 44,447 | 2.6% | 13.29B | 3 |
| 61 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,512 | -36 | 169,616 | 1.3% | 11.17B | 16 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,316 | -11 | 96,036 | 1.7% | 2.89B | 1 |
| 63 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,245 | +465 | 12,882 | 2.9% | 9.15B | 1 |
| 64 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,773 | +15 | 34,580 | 2.1% | 14.03B | 1 |
| 65 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,721 | +34 | 5,303,749 | 0.1% | 7.25B | 1 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,589 | +8 | 179,741 | 0.9% | 12.25B | 6 |
| 67 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,565 | +28 | 157,122 | 1.0% | 23.57B | 2 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,378 | -10 | 230,704 | 0.7% | 35.13B | 4 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,296 | -44 | 52,357 | 1.5% | 7.77B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,239 | +24 | 20,481 | 1.9% | 12.19B | 2 |
| 71 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,172 | +399 | 86,566 | 1.2% | 9.15B | 1 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,099 | +13 | 102,268 | 1.0% | 30.68B | 1 |
| 73 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,086 | -109 | 22,675 | 1.7% | 4.30B | 2 |
| 74 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,069 | +5 | 358,383 | 0.5% | — | 3 |
| 75 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,032 | +4 | 51,760 | 1.3% | 9.24B | 4 |
| 76 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,019 | +4 | 80,729 | 1.1% | 7.45B | 1 |
| 77 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,965 | +20 | 160,022 | 0.8% | 1.10B | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,936 | +6 | 108,268 | 0.9% | 7.45B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,863 | +10 | 303,408 | 0.5% | 6.74B | 2 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,855 | +7 | 34,961 | 1.4% | 22.64B | 1 |
| 81 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,850 | +8 | 186,750 | 0.6% | 6.74B | 1 |
| 82 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,785 | +10 | 147,471 | 0.7% | 13.02B | 1 |
| 83 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,777 | -25 | 40,924 | 1.3% | 70.55B | 3 |
| 84 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,647 | +1 | 9,583 | 1.5% | 4.30B | 3 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,633 | -12 | 9,616 | 1.5% | 9.82B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,586 | -3 | 54,683 | 1.0% | 7.24B | 5 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,523 | +1 | 53,453 | 1.0% | 7.24B | 1 |
| 88 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,523 | -113 | 20,703 | 1.3% | 1.20B | 2 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,517 | +8 | 802,222 | 0.2% | — | 3 |
| 90 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,449 | -1 | 31,762 | 1.1% | 33.12B | 1 |
| 91 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,410 | -23 | 15,947 | 1.2% | 353.4M | 2 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,279 | -22 | 175,054 | 0.5% | 11.51B | 7 |
| 93 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,206 | -12 | 219,171 | 0.4% | 12.19B | 3 |
| 94 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,185 | +10 | 56,776 | 0.8% | 7.55B | 1 |
| 95 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,113 | -2 | 9,279 | 1.0% | 28.84B | 3 |
| 96 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,051 | -2 | 23,973 | 0.8% | 11.17B | 5 |
| 97 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,036 | -68 | 671,257 | 0.1% | 7.45B | 2 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,010 | -17 | 58,634 | 0.6% | 1.35B | 3 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 989 | -4 | 453,626 | 0.2% | 40.43B | 1 |
| 100 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 955 | +11 | 415,982 | 0.2% | 1.20B | 1 |
| 101 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 919 | +13 | 45,054 | 0.6% | 12.19B | 2 |
| 102 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 896 | +42 | 419,417 | 0.2% | 353.4M | 1 |
| 103 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 882 | -20 | 31,784 | 0.7% | 11.17B | 5 |
| 104 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 836 | +3 | 233,607 | 0.3% | — | 2 |
| 105 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 800 | -25 | 112,485 | 0.4% | 7.29B | 2 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 793 | +5 | 14,728 | 0.7% | 4.33B | 3 |
| 107 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 789 | -31 | 2,067 | 0.8% | 27.23B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 787 | +11 | 96,578 | 0.4% | 1.35B | 8 |
| 109 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 760 | +5 | 400,833 | 0.2% | 3.21B | 1 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 710 | +8 | 82,211 | 0.4% | 8.03B | 3 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 687 | +8 | 16,974 | 0.6% | 1.54B | 4 |
| 112 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 627 | +3 | 22,174 | 0.5% | 9.24B | 2 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 598 | -2 | 27,991 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 589 | +14 | 20,818 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 555 | +5 | 3,669 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 536 | 0 | 4,428 | 0.5% | 8.03B | 3 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 439 | +2 | 1,680 | 0.4% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 436 | +7 | 12,238 | 0.4% | 27.23B | 2 |
| 119 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 429 | -9 | 12,461 | 0.4% | 31.59B | 6 |
| 120 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 373 | -2 | 3,408 | 0.4% | 560.9M | 2 |
| 121 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 338 | +6 | 22,181 | 0.3% | 2.61B | 2 |
| 122 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 325 | -1 | 5,602 | 0.3% | 11.51B | 5 |
| 123 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 305 | +2 | 2,853 | 0.3% | 4.02B | 2 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 297 | -4 | 107,308 | 0.1% | — | 3 |
| 125 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 291 | -2 | 32,895 | 0.2% | 40.43B | 2 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 279 | +8 | 39,454 | 0.2% | 7.48B | 2 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 277 | -10 | 37,892 | 0.2% | 27.23B | 3 |
| 128 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 255 | +5 | 70,579 | 0.1% | 8.03B | 3 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 235 | +2 | 41,941 | 0.2% | 11.17B | 1 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 220 | -3 | 322,296 | 0.1% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 212 | -2 | 19,721 | 0.2% | 68.98B | 2 |
| 132 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 196 | +4 | 16,673 | 0.2% | 7.29B | 2 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 190 | +1 | 44,678 | 0.1% | 7.70B | 5 |
| 134 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 186 | +2 | 12,726 | 0.2% | 70.55B | 2 |
| 135 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | -6 | 3,002 | 0.2% | 31.59B | 6 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 161 | -7 | 2,577 | 0.2% | — | 1 |
| 137 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 160 | -3 | 28,441 | 0.1% | 46.70B | 6 |
| 138 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 154 | 0 | 1,184 | 0.2% | — | 1 |
| 139 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 154 | -26 | 5,075 | 0.1% | 70.55B | 3 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 144 | -6 | 5,519 | 0.1% | 353.4M | 2 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 134 | -18 | 5,191 | 0.1% | 437.8M | 1 |
| 142 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 125 | 0 | 7,490 | 0.1% | 31.59B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 84 | 0 | 38,724 | 0.1% | 70.55B | 3 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 72 | 0 | 1,322 | 0.1% | 560.9M | 1 |
| 145 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 72 | -3 | 7,263 | 0.1% | 1.20B | 2 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 42 | -2 | 408 | 0.0% | 437.8M | 1 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 40 | +3 | 443 | 0.0% | 321.0M | 1 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 39 | +5 | 241 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | 0 | 265 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | 0 | 209 | 0.0% | 8.16B | 3 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | 0 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | +7 | 175 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | +5 | 287 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,315,506 | 307,856,608 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 374,144 | 6,073,593 | 7 | 6.1% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 222,951 | 416,209 | 6 | 43.2% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 93,433 | 6,429,718 | 12 | 1.4% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 89,805 | 2,655,628 | 11 | 3.3% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 53,914 | 1,425,378 | 5 | 3.5% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,670 | 567,623 | 13 | 3.2% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,753 | 449,783 | 6 | 2.7% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,416 | 1,450,550 | 11 | 0.9% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,014 | 372,513 | 14 | 2.5% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 11,886 | 400,114 | 10 | 2.4% |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,485 | 76,761 | 1 | 4.8% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,401 | 202,651 | 3 | 2.8% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,608 | 81,949 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,600 | 494,243 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,991 | 860,254 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,617 | 700,183 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,482 | 140,037 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,932 | 661,791 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,862 | 1,162,858 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,730 | 106,411 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,797 | 155,212 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,633 | 9,616 | 1 | 1.5% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 749 | 24,462 | 4 | 0.6% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,933,153 | 60,218,153 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 320,918 | 4,688,799 | 6 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 218,577 | 286,698 | 8 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,225 | 734,646 | 18 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 44,122 | 4,196,358 | 19 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 24,935 | 245,049 | 22 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,319 | 22,493 | 34 |
| 8 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,485 | 76,761 | 37 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,932 | 118,519 | 39 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 6,271 | 44,646 | 43 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,608 | 81,949 | 46 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,191 | 55,037 | 47 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,544 | 154,303 | 51 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,482 | 140,037 | 52 |
| 15 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,397 | 377,887 | 54 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,104 | 37,785 | 57 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,099 | 102,268 | 72 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,069 | 358,383 | 74 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,019 | 80,729 | 76 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,965 | 160,022 | 77 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,633 | 9,616 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,517 | 802,222 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,010 | 58,634 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 429 | 12,461 | 119 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 43.2% | 222,951 | 416,209 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 6.1% | 374,144 | 6,073,593 | 2 |
| 3 | [openeurollm](https://huggingface.co/openeurollm) | 4.8% | 8,485 | 76,761 | 12 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.5% | 53,914 | 1,425,378 | 6 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.3% | 89,805 | 2,655,628 | 5 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 21,670 | 567,623 | 7 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,608 | 81,949 | 14 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,401 | 202,651 | 13 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.7% | 14,753 | 449,783 | 8 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 12,014 | 372,513 | 10 |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.4% | 11,886 | 400,114 | 11 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,315,506 | 307,856,608 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,482 | 140,037 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,633 | 9,616 | 23 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.4% | 93,433 | 6,429,718 | 4 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,730 | 106,411 | 21 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,600 | 494,243 | 15 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,416 | 1,450,550 | 9 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,797 | 155,212 | 22 |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 749 | 24,462 | 24 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,617 | 700,183 | 17 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,991 | 860,254 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,932 | 661,791 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,862 | 1,162,858 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
