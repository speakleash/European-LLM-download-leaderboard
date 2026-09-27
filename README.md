# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-27
- **Generated at:** 2026-09-27T11:44:12Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,388,766 | -55,824 | 57,291,973 | 4.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,746,002 | -44,389 | 64,435,135 | 2.7% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 595,832 | -19,960 | 3,662,944 | 15.8% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 589,516 | -1,913 | 45,661,508 | 1.3% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 509,357 | -1,453 | 4,707,158 | 10.6% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 506,750 | -220 | 4,170,080 | 11.9% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 475,739 | +4,867 | 16,309,521 | 2.9% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 420,632 | +26,996 | 435,503 | 78.5% | 8.90B | 1 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 346,983 | +11,513 | 545,325 | 53.8% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 307,533 | +318 | 2,809,183 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 279,850 | -7,126 | 5,562,622 | 4.9% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 270,651 | -4,742 | 32,312,985 | 0.8% | 46.70B | 2 |
| 13 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 212,707 | +5,204 | 2,182,533 | 9.3% | 8.92B | 6 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 204,415 | +1,829 | 5,399,199 | 3.7% | 24.01B | 1 |
| 15 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 193,417 | -28,472 | 416,743 | 37.4% | 353.4M | 1 |
| 16 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 192,730 | -28,125 | 413,227 | 37.6% | 1.20B | 1 |
| 17 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 188,566 | -26,438 | 398,238 | 37.8% | 3.21B | 1 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 168,089 | -7,294 | 4,143,555 | 4.0% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 153,839 | -623 | 8,504,915 | 1.8% | 8.02B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 117,528 | +6,114 | 1,068,286 | 10.1% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 95,660 | -238 | 528,945 | 15.2% | 70.60B | 2 |
| 22 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,152 | +88 | 718,764 | 8.9% | 23.57B | 2 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,776 | +40 | 745,316 | 6.8% | 1.66B | 1 |
| 24 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,397 | -8,368 | 630,567 | 7.9% | 23.57B | 2 |
| 25 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,463 | -8,341 | 7,571,658 | 0.7% | 23.57B | 2 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,579 | -1,247 | 655,633 | 6.7% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,969 | +287 | 11,202,613 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 30,476 | -719 | 676,263 | 3.9% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,768 | -346 | 143,458 | 11.4% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,447 | +16 | 5,158,669 | 0.4% | 22.25B | 1 |
| 31 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,386 | -672 | 480,147 | 3.3% | 9.15B | 1 |
| 32 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 19,343 | +19,178 | 21,240 | 16.0% | — | 1 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,720 | -11 | 25,038 | 14.2% | 72.01B | 1 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,189 | +86 | 776,380 | 1.8% | 11.25B | 10 |
| 35 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,683 | +420 | 211,346 | 4.7% | — | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,066 | -232 | 71,692 | 8.2% | — | 5 |
| 37 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,445 | -2,856 | 325,865 | 3.2% | 24.01B | 2 |
| 38 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,436 | +20 | 5,300,395 | 0.2% | 7.25B | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,414 | +257 | 506,787 | 1.9% | 7.24B | 8 |
| 40 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,361 | -418 | 348,699 | 2.5% | 125.03B | 1 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 8,102 | +17 | 131,322 | 3.5% | 7.48B | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,322 | +205 | 108,625 | 3.5% | 8.42B | 5 |
| 43 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,119 | -88 | 4,924,649 | 0.1% | 122.61B | 1 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,412 | -22 | 48,161 | 3.7% | 8.03B | 7 |
| 45 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,333 | +897 | 29,682 | 4.1% | 33.12B | 1 |
| 46 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,274 | +48 | 163,791 | 2.0% | 11.17B | 16 |
| 47 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,015 | -14 | 111,122 | 2.4% | 7.29B | 2 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,814 | -402 | 66,194 | 2.9% | 12.77B | 4 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,420 | +83 | 143,541 | 1.8% | 2.25B | 7 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,354 | -34 | 904,322 | 0.4% | 23.57B | 2 |
| 51 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,171 | +147 | 5,376,839 | 0.1% | 22.25B | 1 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,144 | +476 | 54,978 | 2.7% | 7.55B | 1 |
| 53 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,100 | 0 | 668,972 | 0.5% | 7.45B | 2 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,099 | +103 | 133,200 | 1.8% | 7.40B | 3 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,071 | +94 | 252,287 | 1.2% | 4.76B | 5 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,999 | +46 | 371,418 | 0.8% | 7.24B | 8 |
| 57 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,708 | -49 | 91,337 | 1.9% | 2.89B | 1 |
| 58 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,618 | +466 | 31,566 | 2.8% | 14.03B | 1 |
| 59 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,433 | +1,275 | 152,755 | 1.4% | 23.57B | 2 |
| 60 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,228 | +88 | 65,906 | 1.9% | 14.08B | 1 |
| 61 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,080 | +97 | 147,798 | 1.2% | 7.24B | 4 |
| 62 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,988 | +96 | 13,162 | 2.6% | 572.6M | 5 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,940 | +60 | 35,032 | 2.2% | 2.61B | 3 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,756 | +36 | 57,316 | 1.8% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,685 | -2 | 84,205 | 1.5% | 9.15B | 1 |
| 66 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,566 | +1 | 5,031,776 | 0.1% | 122.61B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,212 | -16 | 39,473 | 1.6% | 321.0M | 2 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,132 | -25 | 7,920 | 2.0% | 1.51B | 6 |
| 69 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,061 | +40 | 48,844 | 1.4% | 9.24B | 4 |
| 70 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,002 | +40 | 32,374 | 1.5% | 22.64B | 1 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,868 | +25 | 77,872 | 1.1% | 7.45B | 1 |
| 72 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,849 | -31 | 14,688 | 1.6% | 3.83B | 5 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,807 | +62 | 23,062 | 1.5% | 22.64B | 1 |
| 74 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,736 | -10 | 452,252 | 0.3% | 40.43B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,671 | +42 | 105,554 | 0.8% | 7.45B | 1 |
| 76 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,660 | +89 | 84,845 | 0.9% | 2.22B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,621 | +34 | 99,343 | 0.8% | 30.68B | 1 |
| 78 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,605 | +23 | 49,295 | 1.1% | 7.77B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,552 | +44 | 355,529 | 0.3% | — | 3 |
| 80 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,541 | +106 | 17,231 | 1.3% | 12.19B | 2 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,539 | +50 | 176,435 | 0.6% | 12.25B | 6 |
| 82 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,498 | +25 | 22,230 | 1.2% | 11.17B | 5 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,435 | +40 | 157,336 | 0.6% | 1.10B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,402 | +45 | 300,830 | 0.3% | 6.74B | 2 |
| 85 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,388 | +3 | 173,106 | 0.5% | 11.51B | 7 |
| 86 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,380 | 0 | 12,006 | 1.2% | 31.59B | 6 |
| 87 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,339 | +45 | 144,993 | 0.5% | 13.02B | 1 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,334 | +38 | 184,195 | 0.5% | 6.74B | 1 |
| 89 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,331 | +34 | 30,319 | 1.0% | 11.17B | 5 |
| 90 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,289 | -56 | 9,264 | 1.2% | 9.15B | 1 |
| 91 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,241 | +19 | 57,136 | 0.8% | 1.35B | 3 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,223 | +39 | 7,487 | 1.1% | 9.82B | 1 |
| 93 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,202 | -13 | 19,779 | 1.0% | 4.30B | 2 |
| 94 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,171 | +109 | 19,503 | 1.0% | 12.25B | 3 |
| 95 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,137 | +2 | 32,339 | 0.9% | 56.7M | 1 |
| 96 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,094 | -51 | 95,585 | 0.6% | 1.35B | 8 |
| 97 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,050 | -27 | 7,292 | 1.0% | 4.30B | 3 |
| 98 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,038 | +10 | 227,744 | 0.3% | 35.13B | 4 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,031 | +22 | 800,254 | 0.1% | — | 3 |
| 100 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,016 | -56 | 7,940 | 0.9% | 28.84B | 3 |
| 101 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 980 | -3 | 2,823 | 1.0% | 31.59B | 6 |
| 102 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 969 | -3 | 8,340 | 0.9% | 27.43B | 3 |
| 103 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 899 | +47 | 52,414 | 0.6% | 7.24B | 5 |
| 104 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 897 | -21 | 37,442 | 0.7% | 27.23B | 3 |
| 105 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 854 | -75 | 38,630 | 0.6% | 70.55B | 3 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 830 | +2 | 18,535 | 0.7% | 1.20B | 2 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 828 | -44 | 81,206 | 0.5% | 8.03B | 3 |
| 108 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 799 | +44 | 51,277 | 0.5% | 7.24B | 1 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 784 | +2 | 14,055 | 0.7% | 353.4M | 2 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 765 | +2 | 19,991 | 0.6% | 3.20B | 2 |
| 111 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 701 | -29 | 70,243 | 0.4% | 8.03B | 3 |
| 112 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 658 | +5 | 43,964 | 0.5% | 12.19B | 2 |
| 113 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 620 | +11 | 15,906 | 0.5% | 1.54B | 4 |
| 114 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 611 | -18 | 217,799 | 0.2% | 12.19B | 3 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 606 | +2 | 2,919 | 0.6% | 30.68B | 1 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 581 | -48 | 232,598 | 0.2% | — | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 547 | -2 | 2,946 | 0.5% | 560.9M | 2 |
| 118 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 535 | +41 | 3,698 | 0.5% | 8.03B | 3 |
| 119 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 497 | -15 | 12,427 | 0.4% | 70.55B | 2 |
| 120 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 486 | +2 | 32,419 | 0.4% | 40.43B | 2 |
| 121 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 480 | -36 | 1,330 | 0.5% | 31.58B | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 479 | +7 | 39,068 | 0.3% | 7.48B | 2 |
| 123 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 460 | +14 | 321,900 | 0.1% | 7.24B | 2 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 445 | -9 | 27,214 | 0.3% | 9.24B | 2 |
| 125 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 442 | +3 | 76,021 | 0.3% | 7.04B | 4 |
| 126 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 439 | -16 | 13,757 | 0.4% | 4.33B | 3 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 406 | 0 | 7,274 | 0.4% | 31.59B | 6 |
| 128 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 403 | -6 | 44,385 | 0.3% | 7.70B | 5 |
| 129 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 391 | +21 | 21,708 | 0.3% | 2.61B | 2 |
| 130 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 381 | +30 | 11,717 | 0.3% | 27.23B | 2 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 338 | +63 | 41,626 | 0.2% | 11.17B | 1 |
| 132 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 317 | -4 | 1,186 | 0.3% | 27.23B | 3 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 316 | -28 | 106,869 | 0.2% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 310 | +8 | 2,426 | 0.3% | 4.02B | 2 |
| 135 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 299 | +1 | 1,092 | 0.3% | — | 1 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 265 | +16 | 21,395 | 0.2% | 9.24B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 260 | -3 | 16,389 | 0.2% | 7.29B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 235 | +8 | 19,407 | 0.2% | 68.98B | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 196 | +1 | 38,597 | 0.1% | 70.55B | 3 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 189 | -16 | 5,298 | 0.2% | 353.4M | 2 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 188 | -6 | 5,143 | 0.2% | 11.51B | 5 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 179 | +1 | 2,318 | 0.2% | — | 1 |
| 143 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 174 | -3 | 4,868 | 0.2% | 437.8M | 1 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 146 | +3 | 4,822 | 0.1% | 70.55B | 3 |
| 145 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 145 | -1 | 7,137 | 0.1% | 1.20B | 2 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | +5 | 28,224 | 0.1% | 46.70B | 6 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 113 | 0 | 986 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 100 | 0 | 1,231 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 72 | -1 | 185 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 48 | +2 | 348 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 40 | +1 | 255 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | 0 | 142 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +1 | 351 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 18 | -1 | 213 | 0.0% | 15.17B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | +2 | 109 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | 0 | 156 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,227,105 | 298,284,936 | 30 | 2.8% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,047,731 | 5,195,336 | 7 | 19.8% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 580,886 | 1,426,599 | 11 | 38.1% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 477,498 | 2,311,847 | 11 | 19.8% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 220,638 | 6,303,862 | 12 | 3.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,723 | 1,353,770 | 5 | 2.7% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 20,399 | 430,761 | 6 | 3.8% |
| 8 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 19,343 | 21,240 | 1 | 16.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,193 | 538,355 | 13 | 2.1% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 9,792 | 355,347 | 14 | 2.2% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,474 | 189,563 | 6 | 3.3% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,204 | 192,078 | 3 | 2.8% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,639 | 852,398 | 3 | 0.8% |
| 14 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,978 | 367,276 | 10 | 1.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,888 | 150,751 | 2 | 1.9% |
| 16 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,459 | 693,318 | 2 | 0.6% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,108 | 486,524 | 3 | 0.7% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,099 | 133,200 | 1 | 1.8% |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,246 | 23,433 | 4 | 2.6% |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,954 | 656,359 | 2 | 0.4% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,335 | 152,721 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,260 | 102,631 | 4 | 1.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,163 | 1,159,128 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,223 | 7,487 | 1 | 1.1% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 442 | 76,021 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,388,766 | 57,291,973 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 506,750 | 4,170,080 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 346,983 | 545,325 | 9 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 193,417 | 416,743 | 15 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 168,089 | 4,143,555 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 30,476 | 676,263 | 28 |
| 7 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 19,343 | 21,240 | 32 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,322 | 108,625 | 42 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,412 | 48,161 | 44 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,015 | 111,122 | 47 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,814 | 66,194 | 48 |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,100 | 668,972 | 53 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,099 | 133,200 | 54 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,999 | 371,418 | 56 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,708 | 91,337 | 57 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,228 | 65,906 | 60 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,621 | 99,343 | 77 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,552 | 355,529 | 79 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,539 | 176,435 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,435 | 157,336 | 83 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,380 | 12,006 | 86 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,241 | 57,136 | 91 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,223 | 7,487 | 92 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,031 | 800,254 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 442 | 76,021 | 125 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 38.1% | 580,886 | 1,426,599 | 3 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 19.8% | 477,498 | 2,311,847 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 19.8% | 1,047,731 | 5,195,336 | 2 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | 16.0% | 19,343 | 21,240 | 8 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.8% | 20,399 | 430,761 | 7 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 3.4% | 220,638 | 6,303,862 | 5 |
| 7 | [cjvt](https://huggingface.co/cjvt) | 3.3% | 9,474 | 189,563 | 11 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,204 | 192,078 | 12 |
| 9 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,227,105 | 298,284,936 | 1 |
| 10 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.7% | 38,723 | 1,353,770 | 6 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.6% | 3,246 | 23,433 | 19 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.2% | 9,792 | 355,347 | 10 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,193 | 538,355 | 9 |
| 14 | [Almawave](https://huggingface.co/Almawave) | 1.9% | 4,888 | 150,751 | 15 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.8% | 4,099 | 133,200 | 18 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,978 | 367,276 | 14 |
| 17 | [domyn](https://huggingface.co/domyn) | 1.1% | 1,223 | 7,487 | 24 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,260 | 102,631 | 22 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,335 | 152,721 | 21 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,639 | 852,398 | 13 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.7% | 4,108 | 486,524 | 17 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,459 | 693,318 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 2,954 | 656,359 | 20 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 442 | 76,021 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,163 | 1,159,128 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
