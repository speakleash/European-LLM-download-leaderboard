# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-06
- **Generated at:** 2026-10-06T13:04:13Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,383,724 | -4,396 | 58,019,032 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,601,542 | -59,212 | 64,925,968 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 697,138 | +15,422 | 718,652 | 85.2% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 554,270 | -7,655 | 45,771,224 | 1.2% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 497,851 | -29,049 | 4,801,169 | 10.2% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 493,575 | +491 | 4,311,965 | 11.2% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 480,923 | -500 | 16,463,887 | 2.9% | 12.25B | 3 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 416,084 | -14,389 | 3,764,691 | 10.8% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 327,777 | -13,504 | 594,552 | 47.2% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 310,932 | -5,555 | 2,882,734 | 10.4% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 270,180 | +5,354 | 32,391,416 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,689 | +1,259 | 5,640,659 | 4.5% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 258,656 | +2,041 | 5,489,644 | 4.6% | 24.01B | 1 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,988 | +622 | 922,845 | 22.7% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,859 | +355 | 2,248,291 | 9.6% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 147,354 | -771 | 8,531,996 | 1.7% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 95,620 | -7,150 | 1,091,434 | 8.0% | 127.70B | 2 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 88,130 | -8,568 | 4,149,850 | 2.1% | 11.34B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 80,315 | +11,367 | 701,993 | 10.0% | 119.40B | 3 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,956 | +99 | 742,771 | 8.8% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,264 | +3 | 68,193 | 39.4% | — | 1 |
| 22 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,134 | -420 | 7,594,008 | 0.8% | 23.57B | 2 |
| 23 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 54,154 | -7,031 | 535,567 | 8.5% | 70.60B | 2 |
| 24 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,336 | +857 | 11,221,128 | 0.4% | 140.63B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,524 | +184 | 683,421 | 3.6% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,067 | -3,337 | 147,222 | 8.5% | 9.15B | 1 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,395 | +233 | 5,160,179 | 0.4% | 22.25B | 1 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,300 | -3 | 633,160 | 2.5% | 23.57B | 2 |
| 29 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 18,296 | +589 | 217,690 | 5.8% | — | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,120 | -614 | 484,312 | 2.6% | 9.15B | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,671 | -82 | 780,624 | 1.7% | 11.25B | 10 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,929 | +405 | 75,827 | 7.9% | — | 5 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 12,477 | -253 | 26,672 | 9.8% | 72.01B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,068 | +101 | 510,348 | 1.8% | 7.24B | 8 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 10,999 | +180 | 134,956 | 4.7% | 7.48B | 5 |
| 36 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 10,978 | +3,146 | 29,641 | 8.5% | 12.25B | 3 |
| 37 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,638 | -810 | 328,377 | 2.0% | 24.01B | 2 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,401 | +176 | 4,927,725 | 0.2% | 122.61B | 1 |
| 39 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,108 | -300 | 350,287 | 1.6% | 125.03B | 1 |
| 40 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,363 | +248 | 5,380,032 | 0.1% | 22.25B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,984 | +463 | 16,729 | 5.1% | 572.6M | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,681 | +9 | 109,930 | 2.7% | 8.42B | 7 |
| 43 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,680 | -72 | 49,508 | 3.8% | 8.03B | 7 |
| 44 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,533 | -13 | 30,210 | 4.2% | 33.12B | 1 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,479 | +221 | 145,756 | 2.2% | 2.25B | 7 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,026 | +71 | 134,920 | 2.1% | 7.40B | 3 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,931 | +21 | 154,403 | 1.9% | 23.57B | 2 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,838 | -20 | 165,399 | 1.8% | 11.17B | 16 |
| 49 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,768 | -10 | 111,461 | 2.3% | 7.29B | 2 |
| 50 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,532 | -62 | 67,324 | 2.7% | 12.77B | 5 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,508 | +75 | 372,902 | 1.0% | 7.24B | 8 |
| 52 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,504 | +12 | 12,010 | 4.0% | 27.43B | 3 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,394 | +117 | 253,506 | 1.2% | 4.76B | 5 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,115 | +38 | 905,266 | 0.4% | 23.57B | 2 |
| 55 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 4,079 | +88 | 66,773 | 2.4% | 14.08B | 1 |
| 56 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,064 | -40 | 669,928 | 0.5% | 7.45B | 2 |
| 57 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,037 | +786 | 414,692 | 0.8% | 1.20B | 1 |
| 58 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,996 | +61 | 5,033,750 | 0.1% | 122.61B | 1 |
| 59 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,883 | +779 | 418,203 | 0.7% | 353.4M | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,878 | +77 | 149,159 | 1.6% | 7.24B | 4 |
| 61 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,846 | +784 | 399,749 | 0.8% | 3.21B | 1 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,815 | -76 | 92,318 | 2.0% | 2.89B | 1 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,432 | +39 | 36,023 | 2.5% | 2.61B | 3 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,989 | +38 | 58,262 | 1.9% | 1.60B | 5 |
| 65 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,524 | +19 | 84,329 | 1.4% | 9.15B | 1 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,449 | +83 | 85,693 | 1.3% | 2.22B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,433 | +78 | 40,267 | 1.7% | 13.29B | 3 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,222 | -11 | 49,466 | 1.5% | 9.24B | 4 |
| 69 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,204 | +64 | 8,638 | 2.0% | 1.51B | 6 |
| 70 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,174 | +69 | 55,463 | 1.4% | 7.55B | 1 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,127 | -17 | 32,881 | 1.6% | 22.64B | 1 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,127 | -56 | 18,079 | 1.8% | 12.19B | 2 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,039 | +8 | 23,756 | 1.6% | 22.64B | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,858 | +8 | 78,445 | 1.0% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,818 | +17 | 106,106 | 0.9% | 7.45B | 1 |
| 76 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,806 | -3 | 452,506 | 0.3% | 40.43B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,803 | +12 | 99,929 | 0.9% | 30.68B | 1 |
| 78 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,742 | +28 | 49,761 | 1.2% | 7.77B | 1 |
| 79 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,741 | +43 | 15,135 | 1.5% | 3.83B | 5 |
| 80 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,708 | -15 | 356,070 | 0.4% | — | 3 |
| 81 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,653 | +38 | 5,300,851 | 0.0% | 7.25B | 1 |
| 82 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,619 | -9 | 176,935 | 0.6% | 12.25B | 6 |
| 83 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,605 | -88 | 33,189 | 1.2% | 56.7M | 1 |
| 84 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,599 | +19 | 22,769 | 1.3% | 11.17B | 5 |
| 85 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,590 | -11 | 157,828 | 0.6% | 1.10B | 1 |
| 86 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,577 | -24 | 31,747 | 1.2% | 14.03B | 1 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,543 | -13 | 301,331 | 0.4% | 6.74B | 2 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,508 | +15 | 7,858 | 1.4% | 9.82B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,486 | -10 | 145,473 | 0.6% | 13.02B | 1 |
| 90 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,476 | -16 | 184,672 | 0.5% | 6.74B | 1 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,438 | -21 | 20,356 | 1.2% | 4.30B | 2 |
| 92 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,318 | -3 | 30,752 | 1.0% | 11.17B | 5 |
| 93 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,288 | -30 | 173,502 | 0.5% | 11.51B | 7 |
| 94 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,286 | +37 | 52,886 | 0.8% | 7.24B | 5 |
| 95 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,285 | 0 | 12,013 | 1.1% | 31.59B | 6 |
| 96 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,193 | +31 | 51,730 | 0.8% | 7.24B | 1 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,143 | +79 | 228,149 | 0.3% | 35.13B | 4 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,131 | -38 | 57,471 | 0.7% | 1.35B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,074 | -29 | 800,562 | 0.1% | — | 3 |
| 100 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,016 | +7 | 18,832 | 0.9% | 1.20B | 2 |
| 101 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 996 | -38 | 7,744 | 0.9% | 4.30B | 3 |
| 102 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 975 | -2 | 8,084 | 0.9% | 28.84B | 3 |
| 103 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 933 | -109 | 9,493 | 0.9% | 9.15B | 1 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 911 | +17 | 14,371 | 0.8% | 353.4M | 2 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 864 | -5 | 2,828 | 0.8% | 31.59B | 6 |
| 106 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 856 | +14 | 38,929 | 0.6% | 70.55B | 3 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 782 | -27 | 16,217 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 742 | -35 | 20,181 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 741 | -20 | 95,734 | 0.4% | 1.35B | 8 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 662 | -2 | 44,081 | 0.5% | 12.19B | 2 |
| 111 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 610 | -10 | 81,414 | 0.3% | 8.03B | 3 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 559 | -10 | 217,896 | 0.2% | 12.19B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 522 | +38 | 232,728 | 0.2% | — | 2 |
| 114 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 522 | -12 | 3,854 | 0.5% | 8.03B | 3 |
| 115 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 519 | +14 | 76,199 | 0.3% | 7.04B | 4 |
| 116 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 481 | 0 | 1,497 | 0.5% | 31.58B | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 477 | -20 | 3,005 | 0.5% | 560.9M | 2 |
| 118 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 468 | -3 | 13,916 | 0.4% | 4.33B | 3 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 465 | +3 | 32,562 | 0.4% | 40.43B | 2 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 462 | -10 | 21,829 | 0.4% | 2.61B | 2 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 453 | +6 | 27,304 | 0.4% | 9.24B | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 421 | -15 | 39,159 | 0.3% | 7.48B | 2 |
| 123 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 417 | +5 | 322,026 | 0.1% | 7.24B | 2 |
| 124 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 395 | -19 | 12,528 | 0.4% | 70.55B | 2 |
| 125 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 379 | +10 | 11,792 | 0.3% | 27.23B | 2 |
| 126 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 378 | +15 | 7,354 | 0.4% | 31.59B | 6 |
| 127 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 363 | -22 | 3,040 | 0.4% | 30.68B | 1 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 359 | -4 | 37,577 | 0.3% | 27.23B | 3 |
| 129 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 336 | +15 | 1,185 | 0.3% | — | 1 |
| 130 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 321 | +4 | 21,527 | 0.3% | 9.24B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 315 | -14 | 44,452 | 0.2% | 7.70B | 5 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 309 | -3 | 41,670 | 0.2% | 11.17B | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 299 | +8 | 106,960 | 0.1% | — | 3 |
| 134 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 292 | -14 | 70,296 | 0.2% | 8.03B | 3 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 264 | +12 | 16,447 | 0.2% | 7.29B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 252 | -5 | 19,479 | 0.2% | 68.98B | 2 |
| 137 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 250 | -19 | 2,519 | 0.2% | 4.02B | 2 |
| 138 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 213 | +2 | 5,241 | 0.2% | 11.51B | 5 |
| 139 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213 | -10 | 1,241 | 0.2% | 27.23B | 3 |
| 140 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 208 | -3 | 2,387 | 0.2% | — | 1 |
| 141 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 193 | 0 | 4,990 | 0.2% | 437.8M | 1 |
| 142 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 188 | -5 | 5,355 | 0.2% | 353.4M | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 182 | -4 | 38,630 | 0.1% | 70.55B | 3 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 170 | +32 | 4,882 | 0.2% | 70.55B | 3 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | -1 | 28,259 | 0.1% | 46.70B | 6 |
| 146 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 147 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 135 | -7 | 7,172 | 0.1% | 1.20B | 2 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 127 | +1 | 1,021 | 0.1% | — | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 85 | +2 | 397 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 72 | -4 | 1,246 | 0.1% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 59 | +2 | 200 | 0.1% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 30 | +1 | 225 | 0.0% | 15.17B | 3 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | -1 | 147 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 24 | -1 | 169 | 0.0% | 8.16B | 3 |
| 155 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 23 | -1 | 260 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 115 | 0.0% | 7.24B | 1 |
| 157 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 359 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,868,717 | 300,534,108 | 30 | 2.6% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,267,273 | 5,633,358 | 7 | 22.1% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 625,511 | 2,555,490 | 11 | 23.6% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 141,816 | 6,326,879 | 12 | 2.2% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,264 | 68,193 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,016 | 1,364,006 | 5 | 2.6% |
| 7 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 18,749 | 1,433,641 | 11 | 1.2% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 17,380 | 544,782 | 13 | 2.7% |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 16,963 | 434,006 | 6 | 3.2% |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 15,430 | 378,936 | 10 | 3.2% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,306 | 358,942 | 14 | 2.5% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,850 | 192,006 | 6 | 3.0% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,740 | 854,479 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,528 | 152,466 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,417 | 193,541 | 3 | 2.2% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,026 | 134,920 | 1 | 2.1% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,925 | 694,928 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,552 | 487,973 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,251 | 657,401 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,008 | 23,692 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,220 | 103,363 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,147 | 1,159,729 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,872 | 153,205 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,508 | 7,858 | 1 | 1.4% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 519 | 76,199 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,383,724 | 58,019,032 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 697,138 | 718,652 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 327,777 | 594,552 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 88,130 | 4,149,850 | 18 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,264 | 68,193 | 21 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,524 | 683,421 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 10,978 | 29,641 | 36 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,681 | 109,930 | 42 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,680 | 49,508 | 43 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,026 | 134,920 | 46 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,768 | 111,461 | 49 |
| 12 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,532 | 67,324 | 50 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,508 | 372,902 | 51 |
| 14 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 4,079 | 66,773 | 55 |
| 15 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,064 | 669,928 | 56 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 4,037 | 414,692 | 57 |
| 17 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 3,878 | 149,159 | 60 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,803 | 99,929 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,708 | 356,070 | 80 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,590 | 157,828 | 85 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,508 | 7,858 | 88 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,285 | 12,013 | 95 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,131 | 57,471 | 98 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,074 | 800,562 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 519 | 76,199 | 115 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,264 | 68,193 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 23.6% | 625,511 | 2,555,490 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 22.1% | 1,267,273 | 5,633,358 | 2 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 3.2% | 15,430 | 378,936 | 10 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.2% | 16,963 | 434,006 | 9 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.0% | 8,850 | 192,006 | 12 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.7% | 17,380 | 544,782 | 8 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.6% | 7,868,717 | 300,534,108 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,016 | 1,364,006 | 6 |
| 10 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,528 | 152,466 | 14 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,306 | 358,942 | 11 |
| 12 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 3,008 | 23,692 | 20 |
| 13 | [speakleash](https://huggingface.co/speakleash) | 2.2% | 141,816 | 6,326,879 | 4 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.2% | 6,417 | 193,541 | 15 |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 5,026 | 134,920 | 16 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,508 | 7,858 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 18,749 | 1,433,641 | 7 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,220 | 103,363 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,740 | 854,479 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,552 | 487,973 | 18 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,872 | 153,205 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,925 | 694,928 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,251 | 657,401 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 519 | 76,199 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,147 | 1,159,729 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
