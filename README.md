# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-24
- **Generated at:** 2026-09-24T11:25:00Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,502,296 | -7,053 | 57,079,896 | 4.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,788,347 | +6,586 | 64,312,328 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 646,455 | -5,516 | 3,635,945 | 17.3% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 611,492 | +2,404 | 45,636,522 | 1.3% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 496,246 | +10,555 | 4,672,324 | 10.4% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 488,335 | -882 | 4,098,674 | 11.6% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 483,765 | +1,842 | 16,272,807 | 3.0% | 12.25B | 3 |
| 8 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 332,529 | +32,935 | 347,192 | 74.4% | 8.90B | 1 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 310,557 | +13,987 | 508,629 | 51.0% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 305,168 | +4,084 | 2,785,157 | 10.6% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 288,826 | -6,545 | 5,537,207 | 5.1% | 4.25B | 7 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 283,734 | -6,720 | 32,292,208 | 0.9% | 46.70B | 2 |
| 13 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 279,817 | -5,965 | 416,086 | 54.2% | 353.4M | 1 |
| 14 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 278,619 | -5,952 | 412,581 | 54.4% | 1.20B | 1 |
| 15 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 271,197 | -5,826 | 397,583 | 54.5% | 3.21B | 1 |
| 16 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 199,655 | +1,860 | 5,381,746 | 3.6% | 24.01B | 1 |
| 17 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 197,924 | +8,219 | 2,150,544 | 8.8% | 8.92B | 6 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 185,161 | -1,857 | 4,140,121 | 4.4% | 11.34B | 8 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 152,183 | -588 | 8,489,830 | 1.8% | 8.02B | 1 |
| 20 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 99,430 | +7,281 | 1,046,729 | 8.7% | 127.70B | 2 |
| 21 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 97,278 | +157 | 526,939 | 15.5% | 70.60B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,403 | +1,096 | 629,908 | 10.5% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,703 | -333 | 712,559 | 9.1% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,910 | +323 | 7,566,677 | 0.9% | 23.57B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 57,520 | -382 | 744,421 | 6.8% | 1.66B | 1 |
| 26 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 52,412 | -1,909 | 648,318 | 7.0% | 119.40B | 3 |
| 27 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 42,696 | -777 | 11,198,659 | 0.4% | 140.63B | 2 |
| 28 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 32,367 | -605 | 675,148 | 4.2% | 7.77B | 8 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 25,653 | +655 | 140,412 | 10.7% | 9.15B | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 22,044 | -106 | 479,361 | 3.8% | 9.15B | 1 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,230 | -186 | 5,158,069 | 0.4% | 22.25B | 1 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,802 | +290 | 24,944 | 14.2% | 72.01B | 1 |
| 33 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,035 | +870 | 325,341 | 4.0% | 24.01B | 2 |
| 34 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,914 | -22 | 774,481 | 1.8% | 11.25B | 10 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,003 | +279 | 70,389 | 8.2% | — | 5 |
| 36 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,357 | +42 | 5,300,254 | 0.2% | 7.25B | 1 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,506 | +1,032 | 208,662 | 4.1% | — | 1 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,391 | -438 | 348,199 | 2.8% | 125.03B | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,839 | +203 | 505,718 | 1.8% | 7.24B | 8 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,739 | +135 | 130,730 | 3.4% | 7.48B | 5 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,098 | -130 | 107,972 | 3.4% | 8.42B | 5 |
| 42 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,815 | +249 | 4,923,542 | 0.1% | 122.61B | 1 |
| 43 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,305 | +231 | 47,221 | 3.6% | 8.03B | 7 |
| 44 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,197 | -4 | 163,272 | 2.0% | 11.17B | 16 |
| 45 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,165 | +158 | 65,777 | 3.1% | 12.77B | 4 |
| 46 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,100 | +79 | 111,047 | 2.4% | 7.29B | 2 |
| 47 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,912 | +789 | 904,125 | 0.5% | 23.57B | 2 |
| 48 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,445 | +21 | 28,754 | 3.5% | 33.12B | 1 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,383 | +250 | 143,159 | 1.8% | 2.25B | 7 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,169 | +135 | 5,376,336 | 0.1% | 22.25B | 1 |
| 51 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,141 | +100 | 668,658 | 0.5% | 7.45B | 2 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,928 | +92 | 371,008 | 0.8% | 7.24B | 8 |
| 53 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,826 | -40 | 251,812 | 1.1% | 4.76B | 5 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,805 | +112 | 132,640 | 1.6% | 7.40B | 3 |
| 55 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,674 | +70 | 91,059 | 1.9% | 2.89B | 1 |
| 56 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,646 | +19 | 54,433 | 2.4% | 7.55B | 1 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,162 | +24 | 31,066 | 2.4% | 14.03B | 1 |
| 58 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,121 | +270 | 65,645 | 1.9% | 14.08B | 1 |
| 59 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,868 | -28 | 56,986 | 1.8% | 1.60B | 5 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,851 | +105 | 147,380 | 1.2% | 7.24B | 4 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,723 | +96 | 34,765 | 2.0% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,525 | +48 | 5,031,520 | 0.0% | 122.61B | 1 |
| 63 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,268 | -8 | 83,653 | 1.2% | 9.15B | 1 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,215 | +73 | 39,290 | 1.6% | 321.0M | 2 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,110 | +35 | 151,399 | 0.8% | 23.57B | 2 |
| 66 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,929 | +63 | 48,701 | 1.3% | 9.24B | 4 |
| 67 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,889 | +55 | 32,221 | 1.4% | 22.64B | 1 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,846 | +95 | 7,487 | 1.7% | 1.51B | 6 |
| 69 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,822 | -182 | 14,537 | 1.6% | 3.83B | 5 |
| 70 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,748 | +168 | 11,783 | 1.6% | 572.6M | 5 |
| 71 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,743 | +30 | 77,692 | 1.0% | 7.45B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,699 | +2 | 22,777 | 1.4% | 22.64B | 1 |
| 73 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,543 | +67 | 105,390 | 0.8% | 7.45B | 1 |
| 74 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,498 | +60 | 99,187 | 0.8% | 30.68B | 1 |
| 75 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,488 | -23 | 9,224 | 1.4% | 9.15B | 1 |
| 76 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,450 | -48 | 22,082 | 1.2% | 11.17B | 5 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,445 | +61 | 176,268 | 0.5% | 12.25B | 6 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,435 | +66 | 355,369 | 0.3% | — | 3 |
| 79 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,421 | -11 | 12,006 | 1.3% | 31.59B | 6 |
| 80 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,404 | +97 | 84,585 | 0.8% | 2.22B | 1 |
| 81 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,403 | +22 | 172,983 | 0.5% | 11.51B | 7 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,354 | +58 | 157,171 | 0.5% | 1.10B | 1 |
| 83 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,338 | +286 | 451,802 | 0.2% | 40.43B | 1 |
| 84 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,327 | +207 | 48,942 | 0.9% | 7.77B | 1 |
| 85 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,299 | -6 | 30,183 | 1.0% | 11.17B | 5 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,291 | +58 | 300,683 | 0.3% | 6.74B | 2 |
| 87 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,230 | +79 | 16,892 | 1.1% | 12.19B | 2 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,227 | +61 | 184,061 | 0.4% | 6.74B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,226 | +57 | 144,851 | 0.5% | 13.02B | 1 |
| 90 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,210 | -13 | 19,697 | 1.0% | 4.30B | 2 |
| 91 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,201 | -29 | 19,353 | 1.0% | 12.25B | 3 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,171 | +96 | 7,378 | 1.1% | 9.82B | 1 |
| 93 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,133 | 0 | 2,810 | 1.1% | 31.59B | 6 |
| 94 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,121 | +14 | 32,282 | 0.8% | 56.7M | 1 |
| 95 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,104 | +23 | 95,460 | 0.6% | 1.35B | 8 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,102 | -70 | 7,874 | 1.0% | 28.84B | 3 |
| 97 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,095 | +25 | 7,252 | 1.0% | 4.30B | 3 |
| 98 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,057 | +45 | 800,163 | 0.1% | — | 3 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,056 | +59 | 56,906 | 0.7% | 1.35B | 3 |
| 100 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,018 | +39 | 227,662 | 0.3% | 35.13B | 4 |
| 101 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,008 | +21 | 81,134 | 0.6% | 8.03B | 3 |
| 102 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,003 | +2 | 8,304 | 0.9% | 27.43B | 3 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 961 | -49 | 38,520 | 0.7% | 70.55B | 3 |
| 104 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 909 | +13 | 37,424 | 0.7% | 27.23B | 3 |
| 105 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 822 | +177 | 18,487 | 0.7% | 1.20B | 2 |
| 106 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 784 | +102 | 14,021 | 0.7% | 353.4M | 2 |
| 107 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 782 | +23 | 19,926 | 0.7% | 3.20B | 2 |
| 108 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 780 | +62 | 52,270 | 0.5% | 7.24B | 5 |
| 109 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 699 | -3 | 70,157 | 0.4% | 8.03B | 3 |
| 110 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 687 | +59 | 51,144 | 0.5% | 7.24B | 1 |
| 111 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 648 | +1 | 217,762 | 0.2% | 12.19B | 3 |
| 112 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 628 | -120 | 1,179 | 0.6% | 27.23B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 622 | +36 | 232,554 | 0.2% | — | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 589 | +8 | 43,860 | 0.4% | 12.19B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 587 | +15 | 2,862 | 0.6% | 30.68B | 1 |
| 116 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 557 | +32 | 1,324 | 0.5% | 31.58B | 2 |
| 117 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 551 | 0 | 12,412 | 0.5% | 70.55B | 2 |
| 118 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 532 | +78 | 2,919 | 0.5% | 560.9M | 2 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 512 | -2 | 32,377 | 0.4% | 40.43B | 2 |
| 120 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 494 | +26 | 3,590 | 0.5% | 8.03B | 3 |
| 121 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 494 | +1 | 39,053 | 0.4% | 7.48B | 2 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 483 | -24 | 321,864 | 0.1% | 7.24B | 2 |
| 123 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 450 | +67 | 75,992 | 0.3% | 7.04B | 4 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 446 | +11 | 27,173 | 0.4% | 9.24B | 2 |
| 125 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 428 | +6 | 13,708 | 0.4% | 4.33B | 3 |
| 126 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 420 | +4 | 44,367 | 0.3% | 7.70B | 5 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 410 | +4 | 106,840 | 0.2% | — | 3 |
| 128 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 399 | +25 | 15,673 | 0.3% | 1.54B | 4 |
| 129 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 397 | -6 | 7,230 | 0.4% | 31.59B | 6 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | -19 | 21,647 | 0.3% | 2.61B | 2 |
| 131 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 339 | +11 | 11,649 | 0.3% | 27.23B | 2 |
| 132 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 312 | -17 | 2,407 | 0.3% | 4.02B | 2 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 305 | +8 | 1,073 | 0.3% | — | 1 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 283 | +21 | 41,542 | 0.2% | 11.17B | 1 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 254 | +17 | 16,373 | 0.2% | 7.29B | 2 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 227 | +2 | 21,343 | 0.2% | 9.24B | 2 |
| 137 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 222 | +13 | 19,383 | 0.2% | 68.98B | 2 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 202 | 0 | 5,288 | 0.2% | 353.4M | 2 |
| 139 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 196 | +30 | 38,582 | 0.1% | 70.55B | 3 |
| 140 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 190 | -19 | 4,864 | 0.2% | 437.8M | 1 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 176 | +3 | 5,114 | 0.2% | 11.51B | 5 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 175 | +3 | 2,299 | 0.2% | — | 1 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 149 | +5 | 7,130 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 134 | +3 | 4,805 | 0.1% | 70.55B | 3 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 134 | +3 | 28,210 | 0.1% | 46.70B | 6 |
| 146 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 132 | +34 | 2,024 | 0.1% | — | 1 |
| 147 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105 | +3 | 967 | 0.1% | — | 1 |
| 148 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 102 | -1 | 1,230 | 0.1% | 560.9M | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 71 | 0 | 183 | 0.1% | 437.8M | 1 |
| 150 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 41 | -4 | 340 | 0.0% | 321.0M | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 36 | -3 | 251 | 0.0% | 437.8M | 1 |
| 152 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 26 | 0 | 140 | 0.0% | 437.8M | 1 |
| 153 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 350 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 17 | 0 | 211 | 0.0% | 15.17B | 3 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 107 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 14 | 0 | 155 | 0.0% | 8.16B | 3 |
| 157 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 11 | 0 | 6,035 | 0.0% | 12.25B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,467,602 | 297,640,578 | 30 | 2.8% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 941,360 | 5,031,556 | 7 | 18.3% |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 835,975 | 1,424,222 | 11 | 54.8% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 438,522 | 2,266,424 | 11 | 18.5% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 236,155 | 6,295,024 | 12 | 3.7% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 39,927 | 1,351,428 | 5 | 2.8% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 18,537 | 427,656 | 6 | 3.5% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,925 | 537,329 | 13 | 2.0% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,812 | 188,680 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 9,294 | 354,312 | 14 | 2.0% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,012 | 191,392 | 3 | 2.7% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,427 | 851,740 | 3 | 0.8% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,960 | 366,664 | 10 | 1.3% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 4,525 | 150,230 | 2 | 1.8% |
| 15 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,411 | 692,872 | 2 | 0.6% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,807 | 486,083 | 3 | 0.6% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,805 | 132,640 | 1 | 1.6% |
| 18 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,508 | 23,370 | 4 | 2.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,726 | 656,052 | 2 | 0.4% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,311 | 1,158,940 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,160 | 152,366 | 2 | 0.9% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,116 | 102,415 | 4 | 1.0% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,171 | 7,378 | 1 | 1.1% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 450 | 75,992 | 1 | 0.3% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 132 | 2,024 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,502,296 | 57,079,896 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 488,335 | 4,098,674 | 6 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 310,557 | 508,629 | 9 |
| 4 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 279,817 | 416,086 | 13 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 185,161 | 4,140,121 | 18 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 32,367 | 675,148 | 28 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,098 | 107,972 | 41 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,305 | 47,221 | 43 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,165 | 65,777 | 45 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,100 | 111,047 | 46 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,141 | 668,658 | 51 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,928 | 371,008 | 52 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,805 | 132,640 | 54 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,674 | 91,059 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,121 | 65,645 | 58 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,498 | 99,187 | 74 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,445 | 176,268 | 77 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,435 | 355,369 | 78 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,421 | 12,006 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,354 | 157,171 | 82 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,171 | 7,378 | 92 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,104 | 95,460 | 95 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,057 | 800,163 | 98 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 450 | 75,992 | 123 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 132 | 2,024 | 146 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 54.8% | 835,975 | 1,424,222 | 3 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 18.5% | 438,522 | 2,266,424 | 4 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 18.3% | 941,360 | 5,031,556 | 2 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 3.7% | 236,155 | 6,295,024 | 5 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.5% | 18,537 | 427,656 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,812 | 188,680 | 9 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,467,602 | 297,640,578 | 1 |
| 8 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,508 | 23,370 | 18 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.8% | 39,927 | 1,351,428 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 8,012 | 191,392 | 11 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.0% | 9,294 | 354,312 | 10 |
| 12 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,925 | 537,329 | 8 |
| 13 | [Almawave](https://huggingface.co/Almawave) | 1.8% | 4,525 | 150,230 | 14 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.6% | 3,805 | 132,640 | 17 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 5,960 | 366,664 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.1% | 1,171 | 7,378 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.0% | 2,116 | 102,415 | 22 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.9% | 2,160 | 152,366 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,427 | 851,740 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.6% | 3,807 | 486,083 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,411 | 692,872 | 15 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 2,726 | 656,052 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 450 | 75,992 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,311 | 1,158,940 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 132 | 2,024 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
