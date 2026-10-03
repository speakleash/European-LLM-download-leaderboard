# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-03
- **Generated at:** 2026-10-03T11:21:17Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,392,191 | -4,830 | 57,792,293 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,713,023 | +14,877 | 64,756,176 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 618,390 | +32,539 | 636,261 | 84.0% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 564,635 | -1,334 | 45,734,257 | 1.2% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 545,926 | +2,360 | 4,784,622 | 11.2% | 24.01B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 503,647 | +8,548 | 16,438,714 | 3.0% | 12.25B | 3 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 495,863 | -1,423 | 4,264,515 | 11.4% | 8.05B | 2 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 466,751 | -15,276 | 3,719,799 | 12.2% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 369,115 | -13,825 | 593,831 | 53.2% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 323,360 | +7,005 | 2,859,273 | 10.9% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 270,078 | -460 | 32,368,507 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 262,046 | -6,974 | 5,619,970 | 4.6% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 255,980 | +1,032 | 5,474,148 | 4.6% | 24.01B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,308 | -435 | 2,228,101 | 9.8% | 8.92B | 6 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 150,477 | -896 | 8,526,516 | 1.7% | 8.02B | 1 |
| 16 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 118,301 | -8,749 | 1,089,121 | 9.9% | 127.70B | 2 |
| 17 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 114,721 | -9,223 | 4,147,890 | 2.7% | 11.34B | 8 |
| 18 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 78,461 | -14,235 | 533,284 | 12.4% | 70.60B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,499 | -35 | 733,767 | 8.7% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,251 | -14 | 68,176 | 39.4% | — | 1 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,505 | +1,026 | 7,586,740 | 0.8% | 23.57B | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,603 | +12 | 747,624 | 6.8% | 1.66B | 1 |
| 23 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,130 | -393 | 673,287 | 7.3% | 119.40B | 3 |
| 24 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,291 | -208 | 11,217,817 | 0.4% | 140.63B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 29,182 | -1,086 | 681,405 | 3.7% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 26,927 | -480 | 146,376 | 10.9% | 9.15B | 1 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,184 | -8,335 | 632,445 | 3.6% | 23.57B | 2 |
| 28 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,244 | -109 | 5,159,484 | 0.4% | 22.25B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,584 | -257 | 482,617 | 2.7% | 9.15B | 1 |
| 30 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,451 | +109 | 213,911 | 4.9% | — | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,439 | +443 | 26,150 | 12.2% | 72.01B | 1 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,093 | -157 | 779,192 | 1.7% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,774 | -39 | 74,834 | 7.9% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,044 | +31 | 509,148 | 1.8% | 7.24B | 8 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 10,801 | +168 | 134,450 | 4.6% | 7.48B | 5 |
| 36 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,001 | +277 | 327,300 | 2.1% | 24.01B | 2 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,206 | -127 | 4,926,958 | 0.2% | 122.61B | 1 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,204 | -478 | 349,839 | 1.8% | 125.03B | 1 |
| 39 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,197 | -15 | 49,361 | 4.1% | 8.03B | 7 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,991 | -37 | 109,477 | 2.9% | 8.42B | 7 |
| 41 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,555 | +209 | 5,378,794 | 0.1% | 22.25B | 1 |
| 42 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,550 | -179 | 30,171 | 4.3% | 33.12B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,000 | -119 | 164,859 | 1.9% | 11.17B | 16 |
| 44 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,924 | +228 | 144,757 | 2.0% | 2.25B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,908 | +287 | 134,410 | 2.1% | 7.40B | 3 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,884 | +7 | 154,305 | 1.9% | 23.57B | 2 |
| 47 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,878 | -30 | 111,369 | 2.3% | 7.29B | 2 |
| 48 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,630 | -33 | 67,083 | 2.8% | 12.77B | 5 |
| 49 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,457 | +191 | 15,058 | 3.9% | 572.6M | 5 |
| 50 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,308 | +52 | 372,368 | 0.9% | 7.24B | 8 |
| 51 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,300 | +40 | 253,094 | 1.2% | 4.76B | 5 |
| 52 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,202 | -16 | 669,729 | 0.5% | 7.45B | 2 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,086 | -136 | 904,984 | 0.4% | 23.57B | 2 |
| 54 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,911 | -44 | 91,995 | 2.0% | 2.89B | 1 |
| 55 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,842 | -540 | 55,322 | 2.5% | 7.55B | 1 |
| 56 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,825 | +36 | 5,033,411 | 0.1% | 122.61B | 1 |
| 57 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,797 | +91 | 66,486 | 2.3% | 14.08B | 1 |
| 58 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,629 | +102 | 148,713 | 1.5% | 7.24B | 4 |
| 59 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,455 | -178 | 31,695 | 2.6% | 14.03B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,357 | +33 | 413,835 | 0.7% | 1.20B | 1 |
| 61 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 3,334 | +2,153 | 21,857 | 2.7% | 12.25B | 3 |
| 62 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,302 | +46 | 35,666 | 2.4% | 2.61B | 3 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,216 | +30 | 417,353 | 0.6% | 353.4M | 1 |
| 64 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,177 | +29 | 398,898 | 0.6% | 3.21B | 1 |
| 65 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,897 | -17 | 57,982 | 1.8% | 1.60B | 5 |
| 66 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,507 | -8 | 84,294 | 1.4% | 9.15B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,359 | -88 | 39,988 | 1.7% | 321.0M | 2 |
| 68 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,220 | -12 | 49,235 | 1.5% | 9.24B | 4 |
| 69 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,189 | +91 | 85,410 | 1.2% | 2.22B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,172 | +17 | 17,986 | 1.8% | 12.19B | 2 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,155 | +1 | 32,713 | 1.6% | 22.64B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,042 | +9 | 23,555 | 1.7% | 22.64B | 1 |
| 73 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,999 | +48 | 8,342 | 1.8% | 1.51B | 6 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,960 | -60 | 78,247 | 1.1% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,814 | -26 | 105,902 | 0.9% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,800 | 0 | 99,729 | 0.9% | 30.68B | 1 |
| 77 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,796 | 0 | 452,436 | 0.3% | 40.43B | 1 |
| 78 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,724 | +63 | 49,660 | 1.2% | 7.77B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,719 | +13 | 355,893 | 0.4% | — | 3 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,710 | -117 | 14,967 | 1.5% | 3.83B | 5 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,622 | -17 | 176,765 | 0.6% | 12.25B | 6 |
| 82 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,617 | -306 | 5,300,700 | 0.0% | 7.25B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,592 | +2 | 157,664 | 0.6% | 1.10B | 1 |
| 84 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,580 | +51 | 32,894 | 1.2% | 56.7M | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,557 | +5 | 301,169 | 0.4% | 6.74B | 2 |
| 86 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,531 | -13 | 22,516 | 1.2% | 11.17B | 5 |
| 87 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,525 | +121 | 8,987 | 1.4% | 27.43B | 3 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,494 | +4 | 145,315 | 0.6% | 13.02B | 1 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,491 | +6 | 184,518 | 0.5% | 6.74B | 1 |
| 90 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,440 | +5 | 7,749 | 1.3% | 9.82B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,393 | -6 | 173,387 | 0.5% | 11.51B | 7 |
| 92 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,356 | +69 | 57,380 | 0.9% | 1.35B | 3 |
| 93 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,343 | -32 | 30,597 | 1.0% | 11.17B | 5 |
| 94 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,301 | -17 | 20,066 | 1.1% | 4.30B | 2 |
| 95 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,287 | -18 | 12,013 | 1.1% | 31.59B | 6 |
| 96 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,159 | +47 | 52,729 | 0.8% | 7.24B | 5 |
| 97 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,098 | +36 | 800,471 | 0.1% | — | 3 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,096 | +3 | 9,438 | 1.0% | 9.15B | 1 |
| 99 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,094 | -5 | 227,958 | 0.3% | 35.13B | 4 |
| 100 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,069 | +47 | 51,582 | 0.7% | 7.24B | 1 |
| 101 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,001 | -1 | 18,758 | 0.8% | 1.20B | 2 |
| 102 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 996 | -18 | 8,052 | 0.9% | 28.84B | 3 |
| 103 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 925 | -57 | 7,471 | 0.9% | 4.30B | 3 |
| 104 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 903 | +14 | 38,856 | 0.7% | 70.55B | 3 |
| 105 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 886 | -17 | 14,281 | 0.8% | 353.4M | 2 |
| 106 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 869 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 839 | -147 | 95,680 | 0.4% | 1.35B | 8 |
| 108 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 808 | +1 | 16,164 | 0.7% | 1.54B | 4 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 730 | -48 | 20,075 | 0.6% | 3.20B | 2 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 644 | -12 | 44,032 | 0.4% | 12.19B | 2 |
| 111 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 624 | +8 | 81,356 | 0.3% | 8.03B | 3 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 580 | -2 | 217,862 | 0.2% | 12.19B | 3 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 532 | +2 | 3,805 | 0.5% | 8.03B | 3 |
| 114 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 513 | -11 | 2,988 | 0.5% | 560.9M | 2 |
| 115 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 512 | -59 | 1,497 | 0.5% | 31.58B | 2 |
| 116 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 499 | -27 | 232,648 | 0.1% | — | 2 |
| 117 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 499 | +9 | 76,149 | 0.3% | 7.04B | 4 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 471 | -18 | 32,512 | 0.4% | 40.43B | 2 |
| 119 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 433 | -60 | 12,493 | 0.4% | 70.55B | 2 |
| 120 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 432 | -17 | 27,260 | 0.3% | 9.24B | 2 |
| 121 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 432 | -2 | 13,842 | 0.4% | 4.33B | 3 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 420 | +6 | 321,957 | 0.1% | 7.24B | 2 |
| 123 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 415 | +5 | 21,757 | 0.3% | 2.61B | 2 |
| 124 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 402 | +17 | 3,025 | 0.4% | 30.68B | 1 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 401 | -37 | 39,090 | 0.3% | 7.48B | 2 |
| 126 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 381 | -22 | 7,334 | 0.4% | 31.59B | 6 |
| 127 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 377 | -154 | 70,285 | 0.2% | 8.03B | 3 |
| 128 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 367 | -2 | 11,755 | 0.3% | 27.23B | 2 |
| 129 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 351 | -296 | 37,532 | 0.3% | 27.23B | 3 |
| 130 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 342 | -15 | 44,429 | 0.2% | 7.70B | 5 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 328 | -5 | 41,658 | 0.2% | 11.17B | 1 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 306 | +3 | 1,147 | 0.3% | — | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 292 | +14 | 106,928 | 0.1% | — | 3 |
| 134 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 275 | +5 | 21,464 | 0.2% | 9.24B | 2 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 262 | +11 | 19,459 | 0.2% | 68.98B | 2 |
| 136 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 260 | -5 | 2,465 | 0.3% | 4.02B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 258 | 0 | 16,416 | 0.2% | 7.29B | 2 |
| 138 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 229 | +1 | 1,238 | 0.2% | 27.23B | 3 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 213 | -3 | 5,210 | 0.2% | 11.51B | 5 |
| 140 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 210 | +12 | 5,341 | 0.2% | 353.4M | 2 |
| 141 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 203 | +4 | 2,365 | 0.2% | — | 1 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 193 | -9 | 38,623 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 145 | +2 | 7,160 | 0.1% | 1.20B | 2 |
| 144 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | 0 | 28,249 | 0.1% | 46.70B | 6 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 135 | -2 | 4,840 | 0.1% | 70.55B | 3 |
| 146 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 125 | -4 | 1,012 | 0.1% | — | 1 |
| 147 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 125 | -5 | 4,882 | 0.1% | 437.8M | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 88 | -4 | 1,239 | 0.1% | 560.9M | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 83 | -3 | 394 | 0.1% | 321.0M | 1 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | 0 | 190 | 0.1% | 437.8M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 34 | 0 | 258 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 145 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 28 | 0 | 223 | 0.0% | 15.17B | 3 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 24 | +1 | 166 | 0.0% | 8.16B | 3 |
| 155 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 356 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | +2 | 114 | 0.0% | 7.24B | 1 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,142,159 | 299,848,321 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,216,319 | 5,498,577 | 7 | 21.7% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 495,985 | 2,372,390 | 11 | 20.1% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 168,664 | 6,319,983 | 12 | 2.6% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,251 | 68,176 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,097 | 1,360,770 | 5 | 2.6% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 21,041 | 433,363 | 6 | 3.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,638 | 1,430,258 | 11 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 14,275 | 540,848 | 13 | 2.2% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 10,909 | 357,664 | 14 | 2.4% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,968 | 191,327 | 6 | 3.1% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,976 | 853,878 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,697 | 370,423 | 10 | 1.6% |
| 14 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,734 | 192,996 | 3 | 2.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 5,986 | 151,896 | 2 | 2.4% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,908 | 134,410 | 1 | 2.1% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,728 | 694,325 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,577 | 487,497 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,276 | 657,062 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,049 | 23,672 | 4 | 2.5% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,254 | 103,143 | 4 | 1.1% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,195 | 153,060 | 2 | 0.9% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,151 | 1,159,506 | 4 | 0.2% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,440 | 7,749 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 499 | 76,149 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,392,191 | 57,792,293 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 618,390 | 636,261 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 369,115 | 593,831 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 114,721 | 4,147,890 | 17 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,251 | 68,176 | 20 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 29,182 | 681,405 | 25 |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,197 | 49,361 | 39 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,991 | 109,477 | 40 |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,908 | 134,410 | 45 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,878 | 111,369 | 47 |
| 11 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,630 | 67,083 | 48 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,308 | 372,368 | 50 |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,202 | 669,729 | 52 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,911 | 91,995 | 54 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,797 | 66,486 | 57 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,357 | 413,835 | 60 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 3,334 | 21,857 | 61 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,800 | 99,729 | 76 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,719 | 355,893 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,592 | 157,664 | 83 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,440 | 7,749 | 90 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,356 | 57,380 | 92 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,287 | 12,013 | 95 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,098 | 800,471 | 97 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 499 | 76,149 | 117 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,251 | 68,176 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.7% | 1,216,319 | 5,498,577 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 20.1% | 495,985 | 2,372,390 | 3 |
| 4 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.9% | 21,041 | 433,363 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.1% | 8,968 | 191,327 | 11 |
| 6 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,142,159 | 299,848,321 | 1 |
| 7 | [speakleash](https://huggingface.co/speakleash) | 2.6% | 168,664 | 6,319,983 | 4 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,097 | 1,360,770 | 6 |
| 9 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.5% | 3,049 | 23,672 | 20 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 10,909 | 357,664 | 10 |
| 11 | [Almawave](https://huggingface.co/Almawave) | 2.4% | 5,986 | 151,896 | 15 |
| 12 | [ilsp](https://huggingface.co/ilsp) | 2.3% | 6,734 | 192,996 | 14 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 14,275 | 540,848 | 9 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,908 | 134,410 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.6% | 7,697 | 370,423 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,440 | 7,749 | 24 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,254 | 103,143 | 21 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,638 | 1,430,258 | 8 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,195 | 153,060 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,976 | 853,878 | 12 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,577 | 487,497 | 18 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,728 | 694,325 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,276 | 657,062 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 499 | 76,149 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,151 | 1,159,506 | 23 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
