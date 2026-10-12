# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-12
- **Generated at:** 2026-10-12T14:54:47Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,303,138 | -16,606 | 58,425,199 | 3.9% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,647,272 | -3,114 | 65,349,123 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 699,496 | +629 | 726,900 | 84.6% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 512,835 | -9,414 | 45,934,562 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 490,061 | +4,914 | 4,409,164 | 10.9% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 374,929 | -16,346 | 16,506,255 | 2.3% | 12.25B | 3 |
| 7 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 332,572 | +13,915 | 2,976,381 | 10.8% | 24.01B | 1 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 329,510 | -20,244 | 4,848,697 | 6.7% | 24.01B | 2 |
| 9 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 314,201 | -2,880 | 3,817,865 | 8.0% | 13.95B | 6 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 254,556 | -250 | 5,516,742 | 4.5% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,040 | -3,868 | 32,437,442 | 0.8% | 46.70B | 2 |
| 12 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 241,994 | -13,514 | 597,064 | 34.7% | 22.64B | 1 |
| 13 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,064 | +90 | 925,875 | 22.5% | 1.66B | 1 |
| 14 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,733 | +698 | 5,682,518 | 4.0% | 4.25B | 7 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 217,685 | -6,346 | 2,281,403 | 9.1% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 121,682 | -8,960 | 8,541,712 | 1.4% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 79,710 | -774 | 711,431 | 9.8% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,463 | +268 | 1,103,632 | 6.0% | 127.70B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,285 | -535 | 755,063 | 8.3% | 23.57B | 2 |
| 20 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,015 | +1,088 | 7,611,209 | 0.9% | 23.57B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 67,899 | +887 | 69,837 | 40.0% | — | 1 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,771 | +234 | 11,241,645 | 0.5% | 140.63B | 2 |
| 23 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 29,376 | -11,798 | 4,153,566 | 0.7% | 11.34B | 8 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 27,425 | +453 | 690,491 | 3.5% | 7.77B | 8 |
| 25 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,504 | -1,725 | 539,886 | 3.4% | 70.60B | 2 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 20,898 | +563 | 39,853 | 14.9% | 12.25B | 3 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,952 | +66 | 5,161,445 | 0.4% | 22.25B | 1 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,964 | +416 | 149,266 | 7.2% | 9.15B | 1 |
| 29 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 17,115 | -18 | 221,515 | 5.3% | — | 1 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,880 | -605 | 637,942 | 2.3% | 23.57B | 2 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,746 | -89 | 783,219 | 1.6% | 11.25B | 10 |
| 32 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 13,521 | +8,522 | 76,902 | 7.6% | 12.77B | 5 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,181 | -159 | 78,048 | 7.4% | — | 5 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,100 | -152 | 486,660 | 2.2% | 9.15B | 1 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,335 | -493 | 333,778 | 2.6% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,157 | +46 | 512,767 | 1.8% | 7.24B | 8 |
| 37 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,405 | -3,042 | 136,898 | 4.0% | 7.48B | 5 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,169 | +114 | 4,929,577 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,072 | +22 | 5,381,480 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,274 | +64 | 17,313 | 5.3% | 572.6M | 5 |
| 41 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,942 | -251 | 26,906 | 4.7% | 72.01B | 1 |
| 42 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,790 | -183 | 351,395 | 1.3% | 125.03B | 1 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,770 | +140 | 147,051 | 2.3% | 2.25B | 7 |
| 44 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,469 | +61 | 111,096 | 2.6% | 8.42B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,359 | +30 | 135,948 | 2.3% | 7.40B | 3 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,137 | +306 | 50,314 | 3.4% | 8.03B | 7 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,994 | +5 | 154,611 | 2.0% | 23.57B | 2 |
| 48 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,863 | +32 | 166,498 | 1.8% | 11.17B | 16 |
| 49 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,784 | +33 | 373,920 | 1.0% | 7.24B | 8 |
| 50 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,401 | -3 | 12,213 | 3.9% | 27.43B | 3 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,361 | +2 | 150,117 | 1.7% | 7.24B | 4 |
| 52 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,294 | -17 | 111,757 | 2.0% | 7.29B | 2 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,137 | -44 | 5,034,364 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,098 | -18 | 905,791 | 0.4% | 23.57B | 2 |
| 55 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,723 | +3 | 67,292 | 2.2% | 14.08B | 1 |
| 56 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,699 | +93 | 254,225 | 1.0% | 4.76B | 5 |
| 57 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,670 | +14 | 670,374 | 0.5% | 7.45B | 2 |
| 58 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,480 | -1 | 418,559 | 0.7% | 353.4M | 1 |
| 59 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,451 | -5 | 400,110 | 0.7% | 3.21B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,448 | -8 | 415,058 | 0.7% | 1.20B | 1 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,335 | +33 | 36,652 | 2.4% | 2.61B | 3 |
| 62 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,228 | +115 | 59,135 | 2.0% | 1.60B | 5 |
| 63 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,157 | +27 | 92,989 | 1.6% | 2.89B | 1 |
| 64 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,715 | -54 | 86,225 | 1.5% | 2.22B | 1 |
| 65 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,687 | +47 | 9,340 | 2.5% | 1.51B | 6 |
| 66 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,569 | +34 | 24,672 | 2.1% | 22.64B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,541 | +7 | 84,434 | 1.4% | 9.15B | 1 |
| 68 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,309 | +106 | 40,926 | 1.6% | 13.29B | 3 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,296 | +77 | 50,472 | 1.5% | 7.77B | 1 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,252 | +7 | 49,868 | 1.5% | 9.24B | 4 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,059 | -64 | 18,311 | 1.7% | 12.19B | 2 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,033 | +44 | 30,556 | 1.6% | 33.12B | 1 |
| 73 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,951 | +55 | 33,880 | 1.5% | 56.7M | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,879 | +3 | 78,857 | 1.1% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,838 | +6 | 106,479 | 0.9% | 7.45B | 1 |
| 76 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,829 | +22 | 452,713 | 0.3% | 40.43B | 1 |
| 77 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,824 | +16 | 15,581 | 1.6% | 3.83B | 5 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,821 | +23 | 100,320 | 0.9% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,756 | +16 | 356,472 | 0.4% | — | 3 |
| 80 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,676 | +4 | 5,301,107 | 0.0% | 7.25B | 1 |
| 81 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,657 | +13 | 177,298 | 0.6% | 12.25B | 6 |
| 82 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,644 | -8 | 33,244 | 1.2% | 22.64B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,643 | +3 | 158,193 | 0.6% | 1.10B | 1 |
| 84 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,636 | +5 | 55,713 | 1.1% | 7.55B | 1 |
| 85 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,593 | -36 | 23,118 | 1.3% | 11.17B | 5 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,577 | +13 | 301,685 | 0.4% | 6.74B | 2 |
| 87 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,537 | +2 | 53,231 | 1.0% | 7.24B | 5 |
| 88 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,537 | +19 | 185,036 | 0.5% | 6.74B | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,523 | +17 | 145,820 | 0.6% | 13.02B | 1 |
| 90 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,444 | +3 | 52,060 | 0.9% | 7.24B | 1 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,396 | -60 | 20,730 | 1.2% | 4.30B | 2 |
| 92 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,362 | +229 | 32,190 | 1.0% | 14.03B | 1 |
| 93 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,353 | -9 | 8,027 | 1.3% | 9.82B | 1 |
| 94 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,347 | +4 | 173,862 | 0.5% | 11.51B | 7 |
| 95 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,329 | +82 | 8,226 | 1.2% | 4.30B | 3 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,301 | +26 | 19,265 | 1.1% | 1.20B | 2 |
| 97 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,282 | +12 | 31,025 | 1.0% | 11.17B | 5 |
| 98 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,240 | +24 | 228,437 | 0.4% | 35.13B | 4 |
| 99 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,150 | +5 | 9,970 | 1.0% | 9.15B | 1 |
| 100 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,135 | +6 | 57,694 | 0.7% | 1.35B | 3 |
| 101 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,133 | +35 | 800,805 | 0.1% | — | 3 |
| 102 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,057 | +18 | 14,646 | 0.9% | 353.4M | 2 |
| 103 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,004 | +34 | 39,251 | 0.7% | 70.55B | 3 |
| 104 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 933 | 0 | 12,033 | 0.8% | 31.59B | 6 |
| 105 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 870 | 0 | 2,834 | 0.8% | 31.59B | 6 |
| 106 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 863 | -26 | 8,222 | 0.8% | 28.84B | 3 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 808 | +8 | 16,331 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 744 | -17 | 20,276 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 682 | +23 | 95,858 | 0.3% | 1.35B | 8 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 658 | +10 | 81,567 | 0.4% | 8.03B | 3 |
| 111 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 632 | +3 | 76,386 | 0.4% | 7.04B | 4 |
| 112 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 606 | +25 | 3,991 | 0.6% | 8.03B | 3 |
| 113 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 535 | +19 | 232,811 | 0.2% | — | 2 |
| 114 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 526 | -73 | 44,152 | 0.4% | 12.19B | 2 |
| 115 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 522 | +13 | 27,416 | 0.4% | 9.24B | 2 |
| 116 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 471 | -9 | 218,000 | 0.1% | 12.19B | 3 |
| 117 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | +7 | 13,974 | 0.4% | 4.33B | 3 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 449 | +17 | 32,647 | 0.3% | 40.43B | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 437 | -22 | 21,854 | 0.4% | 2.61B | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 434 | +7 | 322,107 | 0.1% | 7.24B | 2 |
| 121 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 431 | +5 | 3,064 | 0.4% | 560.9M | 2 |
| 122 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 427 | +24 | 39,225 | 0.3% | 7.48B | 2 |
| 123 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 419 | +22 | 3,166 | 0.4% | 30.68B | 1 |
| 124 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 396 | 0 | 7,390 | 0.4% | 31.59B | 6 |
| 125 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 383 | +8 | 1,275 | 0.4% | — | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 382 | +6 | 11,823 | 0.3% | 27.23B | 2 |
| 127 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 346 | +8 | 21,588 | 0.3% | 9.24B | 2 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 317 | -3 | 37,628 | 0.2% | 27.23B | 3 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 316 | +23 | 41,758 | 0.2% | 11.17B | 1 |
| 130 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 316 | +3 | 107,034 | 0.2% | — | 3 |
| 131 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 299 | +8 | 70,345 | 0.2% | 8.03B | 3 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 284 | +1 | 44,512 | 0.2% | 7.70B | 5 |
| 133 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 263 | -35 | 12,557 | 0.2% | 70.55B | 2 |
| 134 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 258 | +6 | 5,301 | 0.2% | 11.51B | 5 |
| 135 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 256 | +29 | 1,327 | 0.3% | 27.23B | 3 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 238 | +2 | 19,528 | 0.2% | 68.98B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 234 | -9 | 16,489 | 0.2% | 7.29B | 2 |
| 138 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 233 | +19 | 5,082 | 0.2% | 437.8M | 1 |
| 139 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 230 | +2 | 1,501 | 0.2% | 31.58B | 2 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 229 | -1 | 2,554 | 0.2% | 4.02B | 2 |
| 141 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 222 | +3 | 4,967 | 0.2% | 70.55B | 3 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 211 | -1 | 2,432 | 0.2% | — | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | 0 | 38,651 | 0.1% | 70.55B | 3 |
| 144 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 154 | +10 | 5,393 | 0.1% | 353.4M | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 148 | +2 | 28,298 | 0.1% | 46.70B | 6 |
| 146 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 137 | +7 | 1,038 | 0.1% | — | 1 |
| 147 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | -4 | 6,167 | 0.1% | 12.25B | 3 |
| 148 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 127 | +7 | 7,209 | 0.1% | 1.20B | 2 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 86 | +1 | 405 | 0.1% | 321.0M | 1 |
| 150 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 34 | +3 | 230 | 0.0% | 15.17B | 3 |
| 151 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 33 | 0 | 1,255 | 0.0% | 560.9M | 1 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | -2 | 205 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 29 | +3 | 174 | 0.0% | 8.16B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 25 | +1 | 371 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | -2 | 150 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | -2 | 118 | 0.0% | 7.24B | 1 |
| 157 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | -4 | 263 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,340,201 | 302,012,730 | 30 | 2.4% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,227,788 | 5,745,090 | 7 | 21.0% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 532,687 | 2,571,784 | 11 | 19.9% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 80,270 | 6,341,372 | 12 | 1.2% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 67,899 | 69,837 | 1 | 40.0% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 37,769 | 1,373,374 | 5 | 2.6% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 25,717 | 390,353 | 10 | 5.2% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 18,022 | 1,437,018 | 11 | 1.2% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 17,898 | 202,332 | 6 | 5.9% |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,390 | 546,529 | 13 | 2.5% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,412 | 436,461 | 6 | 2.3% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,528 | 361,467 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,387 | 855,710 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,438 | 153,517 | 2 | 2.5% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,180 | 194,833 | 3 | 2.1% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,359 | 135,948 | 1 | 2.3% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,218 | 696,027 | 2 | 0.7% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,703 | 489,049 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,333 | 658,157 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,429 | 23,758 | 4 | 2.0% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,303 | 103,890 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,222 | 1,160,178 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,817 | 153,552 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,353 | 8,027 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 632 | 76,386 | 1 | 0.4% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,303,138 | 58,425,199 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 699,496 | 726,900 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 241,994 | 597,064 | 12 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 67,899 | 69,837 | 21 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 29,376 | 4,153,566 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 27,425 | 690,491 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 20,898 | 39,853 | 26 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 13,521 | 76,902 | 32 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,469 | 111,096 | 44 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,359 | 135,948 | 45 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,137 | 50,314 | 46 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,784 | 373,920 | 49 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,401 | 12,213 | 50 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,361 | 150,117 | 51 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,723 | 67,292 | 55 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,670 | 670,374 | 57 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 3,480 | 418,559 | 58 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,821 | 100,320 | 78 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,756 | 356,472 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,643 | 158,193 | 83 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,353 | 8,027 | 93 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,135 | 57,694 | 100 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,133 | 800,805 | 101 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 933 | 12,033 | 104 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 632 | 76,386 | 111 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 40.0% | 67,899 | 69,837 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.0% | 1,227,788 | 5,745,090 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 19.9% | 532,687 | 2,571,784 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 5.9% | 17,898 | 202,332 | 9 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5.2% | 25,717 | 390,353 | 7 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 37,769 | 1,373,374 | 6 |
| 7 | [Almawave](https://huggingface.co/Almawave) | 2.5% | 6,438 | 153,517 | 14 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.5% | 16,390 | 546,529 | 10 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,528 | 361,467 | 12 |
| 10 | [mistralai](https://huggingface.co/mistralai) | 2.4% | 7,340,201 | 302,012,730 | 1 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.3% | 12,412 | 436,461 | 11 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.3% | 5,359 | 135,948 | 16 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.1% | 6,180 | 194,833 | 15 |
| 14 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.0% | 2,429 | 23,758 | 20 |
| 15 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,353 | 8,027 | 24 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.2% | 80,270 | 6,341,372 | 4 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.2% | 18,022 | 1,437,018 | 8 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,303 | 103,890 | 21 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,703 | 489,049 | 18 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,387 | 855,710 | 13 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,817 | 153,552 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.7% | 5,218 | 696,027 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,333 | 658,157 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.4% | 632 | 76,386 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,222 | 1,160,178 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
