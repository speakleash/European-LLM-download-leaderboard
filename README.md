# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-13
- **Generated at:** 2026-11-13T14:21:17Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 186

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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,993,525 | +13,986 | 60,610,126 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,296,636 | -48,696 | 66,867,954 | 1.9% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 676,387 | +4,972 | 4,528,451 | 14.6% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 547,688 | -2,095 | 46,520,142 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 363,071 | +1,856 | 32,821,391 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 256,064 | -1,159 | 2,555,360 | 9.6% | 8.92B | 6 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 241,394 | -14,222 | 4,693,775 | 5.0% | 8.05B | 2 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 212,049 | +8,592 | 330,277 | 49.3% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,636 | +318 | 5,908,073 | 3.4% | 3.85B | 7 |
| 10 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 156,884 | -1,956 | 16,676,878 | 0.9% | 12.25B | 3 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 150,930 | -6,184 | 5,029,347 | 2.9% | 24.01B | 2 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 106,761 | +2,283 | 5,633,651 | 1.9% | 24.01B | 1 |
| 13 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,961 | +57 | 7,726,339 | 1.4% | 23.57B | 2 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 101,249 | +11,897 | 4,267,663 | 2.3% | 11.34B | 9 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,214 | -796 | 8,609,554 | 0.7% | 8.02B | 1 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,890 | -578 | 11,293,052 | 0.4% | 140.63B | 2 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,269 | -2,349 | 807,399 | 5.0% | 23.57B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 44,411 | -864 | 739,277 | 5.3% | 7.77B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,049 | -9 | 749,559 | 4.1% | 119.40B | 3 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,615 | +246 | 368,438 | 7.2% | 24.01B | 2 |
| 21 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 27,479 | -1,306 | 3,011,406 | 0.9% | 24.01B | 1 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,456 | -54 | 946,321 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,801 | +83 | 801,323 | 1.9% | 11.25B | 10 |
| 24 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,413 | +266 | 748,353 | 1.9% | 8.90B | 5 |
| 25 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,016 | -158 | 1,122,100 | 1.3% | 127.70B | 2 |
| 26 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 15,714 | -528 | 34,709 | 11.7% | 78.10B | 2 |
| 27 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,543 | +543 | 15,588 | 13.4% | — | 2 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,983 | +165 | 4,945,529 | 0.3% | 122.61B | 1 |
| 29 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,831 | +51 | 697,560 | 1.9% | 7.29B | 1 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,753 | +15 | 5,047,434 | 0.2% | 122.61B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,611 | -82 | 651,410 | 1.7% | 23.57B | 2 |
| 32 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,145 | +84 | 498,685 | 1.9% | 9.15B | 1 |
| 33 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,887 | -80 | 524,877 | 1.7% | 7.24B | 8 |
| 34 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,811 | +130 | 247,243 | 3.1% | — | 1 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,520 | +219 | 22,883 | 8.6% | 27.43B | 3 |
| 36 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 9,400 | -527 | 551,484 | 1.4% | 70.60B | 2 |
| 37 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,227 | +66 | 5,391,321 | 0.2% | 22.25B | 1 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,467 | -152 | 36,287 | 6.2% | 72.01B | 4 |
| 39 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,327 | +65 | 119,891 | 3.8% | 8.42B | 7 |
| 40 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,278 | -210 | 88,025 | 4.4% | — | 5 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,627 | -1 | 17,190 | 6.5% | 1.51B | 6 |
| 42 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,165 | -181 | 160,934 | 2.7% | 9.15B | 1 |
| 43 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,067 | +157 | 22,878 | 5.8% | 3.83B | 5 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,947 | +124 | 358,892 | 1.5% | 125.03B | 1 |
| 45 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 6,943 | +632 | 261,699 | 1.9% | 4.76B | 5 |
| 46 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,637 | -280 | 604,782 | 0.9% | 22.64B | 1 |
| 47 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,318 | +46 | 23,905 | 5.1% | 572.6M | 5 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,021 | +239 | 56,850 | 3.8% | 8.03B | 7 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,891 | -47 | 153,311 | 2.3% | 2.25B | 7 |
| 50 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,847 | -47 | 138,039 | 2.5% | 2.89B | 1 |
| 51 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,646 | +14 | 82,079 | 3.1% | 7.04B | 4 |
| 52 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,584 | +4 | 158,954 | 2.2% | 351.6M | 1 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,554 | +99 | 64,914 | 3.4% | 1.60B | 5 |
| 54 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,759 | +57 | 39,111 | 3.4% | 56.7M | 1 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,673 | -27 | 910,761 | 0.5% | 23.57B | 2 |
| 56 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,487 | -3 | 155,046 | 1.8% | 7.24B | 4 |
| 57 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,356 | -1 | 140,804 | 1.8% | 7.40B | 3 |
| 58 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,254 | -38 | 124,868 | 1.9% | 8.54B | 2 |
| 59 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,191 | +41 | 41,283 | 3.0% | 2.61B | 3 |
| 60 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,168 | -14 | 378,516 | 0.9% | 7.24B | 8 |
| 61 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,035 | -19 | 141,332 | 1.7% | 7.48B | 5 |
| 62 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,960 | -4 | 5,165,774 | 0.1% | 22.25B | 1 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,804 | +11 | 28,708 | 3.0% | 22.64B | 1 |
| 64 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,768 | +1,140 | 3,768 | 3.6% | 11.17B | 14 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,628 | +4 | 44,814 | 2.5% | 13.29B | 3 |
| 66 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,268 | +15 | 96,560 | 1.7% | 2.89B | 1 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,254 | -69 | 54,822 | 2.1% | 7.77B | 3 |
| 68 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,206 | -124 | 170,130 | 1.2% | 11.17B | 16 |
| 69 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 2,999 | +173 | 3,012 | 2.9% | 3.93B | 2 |
| 70 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,983 | -33 | 13,116 | 2.6% | 9.15B | 1 |
| 71 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,705 | -54 | 5,304,055 | 0.1% | 7.25B | 1 |
| 72 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,534 | -6 | 157,325 | 1.0% | 23.57B | 2 |
| 73 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,465 | +9 | 20,983 | 2.0% | 12.19B | 2 |
| 74 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,392 | +53 | 23,261 | 1.9% | 4.30B | 2 |
| 75 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,373 | -28 | 230,987 | 0.7% | 35.13B | 4 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,198 | +55 | 102,707 | 1.1% | 30.68B | 1 |
| 77 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,188 | +23 | 86,648 | 1.2% | 9.15B | 1 |
| 78 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,184 | -40 | 34,706 | 1.6% | 14.03B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,086 | +8 | 358,740 | 0.5% | — | 3 |
| 80 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,076 | +15 | 81,106 | 1.1% | 7.45B | 1 |
| 81 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,060 | +11 | 52,122 | 1.4% | 9.24B | 4 |
| 82 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,059 | +22 | 454,843 | 0.4% | 40.43B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,020 | +20 | 160,364 | 0.8% | 1.10B | 1 |
| 84 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,980 | +13 | 108,637 | 0.9% | 7.45B | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,916 | +18 | 303,757 | 0.5% | 6.74B | 2 |
| 86 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,910 | +10 | 35,314 | 1.4% | 22.64B | 1 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,901 | +17 | 187,092 | 0.7% | 6.74B | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,837 | +20 | 147,808 | 0.7% | 13.02B | 1 |
| 89 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,799 | -7 | 180,043 | 0.6% | 12.25B | 6 |
| 90 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,684 | -42 | 41,102 | 1.2% | 70.55B | 3 |
| 91 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,627 | -41 | 44,868 | 1.1% | 12.25B | 3 |
| 92 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,554 | -7 | 54,939 | 1.0% | 7.24B | 5 |
| 93 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,548 | +20 | 20,898 | 1.3% | 1.20B | 2 |
| 94 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,545 | -242 | 9,946 | 1.4% | 9.82B | 1 |
| 95 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,536 | +8 | 802,429 | 0.2% | — | 3 |
| 96 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,496 | 0 | 53,702 | 1.0% | 7.24B | 1 |
| 97 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,447 | +30 | 1,447 | 1.4% | 3.93B | 1 |
| 98 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,437 | +107 | 416,533 | 0.3% | 1.20B | 1 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,402 | -3 | 9,744 | 1.3% | 4.30B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,343 | +9 | 16,141 | 1.2% | 353.4M | 2 |
| 101 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,335 | +106 | 419,925 | 0.3% | 353.4M | 1 |
| 102 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,329 | 0 | 9,573 | 1.2% | 28.84B | 3 |
| 103 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,278 | -366 | 9,702 | 1.2% | 40.43B | 2 |
| 104 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,252 | -29 | 175,293 | 0.5% | 11.51B | 7 |
| 105 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,171 | +109 | 401,313 | 0.2% | 3.21B | 1 |
| 106 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,148 | +17 | 56,916 | 0.7% | 7.55B | 1 |
| 107 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,104 | -2 | 219,218 | 0.3% | 12.19B | 3 |
| 108 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,088 | +13 | 45,270 | 0.7% | 12.19B | 2 |
| 109 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,070 | +13 | 58,826 | 0.7% | 1.35B | 3 |
| 110 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,056 | -156 | 31,888 | 0.8% | 33.12B | 1 |
| 111 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 929 | +8 | 671,418 | 0.1% | 7.45B | 2 |
| 112 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 888 | -10 | 24,108 | 0.7% | 11.17B | 5 |
| 113 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 862 | +12 | 2,889 | 0.8% | 40.43B | 2 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 861 | +9 | 233,688 | 0.3% | — | 2 |
| 115 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 836 | -17 | 14,858 | 0.7% | 4.33B | 3 |
| 116 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 807 | +11 | 1,729 | 0.8% | 608.3M | 1 |
| 117 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 792 | +9 | 96,713 | 0.4% | 1.35B | 8 |
| 118 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 765 | +15 | 112,575 | 0.4% | 7.29B | 2 |
| 119 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 760 | -16 | 800 | 0.8% | 437.8M | 2 |
| 120 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 753 | -31 | 31,874 | 0.6% | 11.17B | 5 |
| 121 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 697 | +10 | 17,093 | 0.6% | 1.54B | 4 |
| 122 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 691 | +3 | 82,324 | 0.4% | 8.03B | 3 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 678 | 0 | 2,115 | 0.7% | 27.23B | 3 |
| 124 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 620 | +10 | 20,909 | 0.5% | 3.20B | 2 |
| 125 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 608 | +1 | 28,043 | 0.5% | 9.24B | 2 |
| 126 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 605 | -6 | 22,224 | 0.5% | 9.24B | 2 |
| 127 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 583 | +11 | 3,769 | 0.6% | 30.68B | 1 |
| 128 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 560 | +2 | 560 | 0.6% | 3.93B | 1 |
| 129 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 560 | +1 | 560 | 0.6% | 3.93B | 1 |
| 130 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 554 | +1 | 554 | 0.6% | 3.93B | 1 |
| 131 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 553 | +3 | 553 | 0.5% | 3.93B | 1 |
| 132 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 439 | -3 | 4,478 | 0.4% | 8.03B | 3 |
| 133 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 432 | +4 | 12,465 | 0.4% | 31.59B | 6 |
| 134 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 425 | +3 | 1,731 | 0.4% | — | 1 |
| 135 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 420 | -3 | 12,268 | 0.4% | 27.23B | 2 |
| 136 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 403 | +25 | 5,735 | 0.4% | 11.51B | 5 |
| 137 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 400 | +1 | 1,152 | 0.4% | 437.8M | 1 |
| 138 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 381 | +10 | 3,453 | 0.4% | 560.9M | 2 |
| 139 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 308 | -12 | 22,235 | 0.3% | 2.61B | 2 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 307 | 0 | 2,879 | 0.3% | 4.02B | 2 |
| 141 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 301 | +1 | 32,961 | 0.2% | 40.43B | 2 |
| 142 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 276 | -7 | 37,929 | 0.2% | 27.23B | 3 |
| 143 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 266 | -8 | 107,324 | 0.1% | — | 3 |
| 144 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 266 | 0 | 70,629 | 0.2% | 8.03B | 3 |
| 145 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 216 | +18 | 1,081 | 0.2% | 9.15B | 1 |
| 146 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 208 | +5 | 41,978 | 0.1% | 11.17B | 1 |
| 147 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 205 | -2 | 16,701 | 0.2% | 7.29B | 2 |
| 148 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 204 | -28 | 39,467 | 0.1% | 7.48B | 2 |
| 149 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 200 | -5 | 322,333 | 0.0% | 7.24B | 2 |
| 150 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | +2 | 3,006 | 0.2% | 31.59B | 6 |
| 151 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 186 | -3 | 19,729 | 0.2% | 68.98B | 2 |
| 152 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 186 | -1 | 29,837 | 0.1% | 1.01B | 1 |
| 153 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | 0 | 170 | 0.2% | 7.77B | 1 |
| 154 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 162 | -2 | 44,703 | 0.1% | 7.70B | 5 |
| 155 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 157 | +1 | 1,208 | 0.2% | — | 1 |
| 156 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 142 | -3 | 2,930 | 0.1% | 40.43B | 2 |
| 157 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 141 | +14 | 7,511 | 0.1% | 31.59B | 6 |
| 158 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 140 | +2 | 28,473 | 0.1% | 46.70B | 6 |
| 159 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 138 | -4 | 5,543 | 0.1% | 353.4M | 2 |
| 160 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 133 | -45 | 12,759 | 0.1% | 70.55B | 2 |
| 161 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 132 | -6 | 2,586 | 0.1% | — | 1 |
| 162 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 107 | +4 | 5,097 | 0.1% | 70.55B | 3 |
| 163 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 99 | 0 | 5,199 | 0.1% | 437.8M | 1 |
| 164 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 81 | +5 | 38,746 | 0.1% | 70.55B | 3 |
| 165 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 68 | -5 | 971 | 0.1% | 40.43B | 2 |
| 166 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 64 | +1 | 1,325 | 0.1% | 560.9M | 1 |
| 167 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 60 | 0 | 7,275 | 0.1% | 1.20B | 2 |
| 168 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 53 | -5 | 617 | 0.1% | 6.25B | 2 |
| 169 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 50 | -2 | 230 | 0.0% | 40.43B | 2 |
| 170 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 48 | +1 | 419 | 0.0% | 437.8M | 1 |
| 171 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 48 | -2 | 456 | 0.0% | 321.0M | 1 |
| 172 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 48 | -2 | 385 | 0.0% | 7.77B | 2 |
| 173 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 46 | +1 | 251 | 0.0% | 437.8M | 1 |
| 174 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 45 | -1 | 220 | 0.0% | 8.16B | 3 |
| 175 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 42 | -1 | 274 | 0.0% | 15.17B | 3 |
| 176 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 37 | +1 | 1,457 | 0.0% | 8.03B | 1 |
| 177 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 181 | 0.0% | 437.8M | 1 |
| 178 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -4 | 152 | 0.0% | 7.24B | 1 |
| 179 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | 0 | 291 | 0.0% | 437.8M | 1 |
| 180 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 14 | 0 | 375 | 0.0% | 12.25B | 1 |
| 181 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 182 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 183 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 184 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 0 | 0 | 0 | 0.0% | — | 0 |
| 185 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 186 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,235,702 | 309,575,833 | 32 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 296,686 | 6,093,872 | 7 | 4.8% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 216,380 | 460,445 | 6 | 38.6% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 155,947 | 6,514,694 | 13 | 2.4% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 70,638 | 2,666,701 | 12 | 2.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 58,587 | 1,453,108 | 13 | 3.8% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 22,645 | 570,092 | 13 | 3.4% |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 21,360 | 116,788 | 2 | 9.9% |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,227 | 592,502 | 5 | 2.9% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,965 | 1,456,062 | 12 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,466 | 452,449 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,996 | 376,357 | 16 | 2.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,693 | 204,061 | 3 | 2.9% |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,218 | 16,632 | 7 | 7.0% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,049 | 402,840 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,758 | 495,264 | 3 | 1.0% |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,985 | 861,161 | 3 | 0.5% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,368 | 700,849 | 2 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 4,002 | 662,497 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,868 | 106,970 | 4 | 1.4% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,849 | 1,163,170 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,862 | 155,539 | 2 | 0.7% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 768 | 24,491 | 4 | 0.6% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,993,525 | 60,610,126 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 241,394 | 4,693,775 | 7 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 212,049 | 330,277 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 101,249 | 4,267,663 | 14 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 44,411 | 739,277 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,456 | 946,321 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 15,714 | 34,709 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,520 | 22,883 | 35 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,327 | 119,891 | 39 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,021 | 56,850 | 48 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,847 | 138,039 | 50 |
| 12 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,759 | 39,111 | 54 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,487 | 155,046 | 56 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,168 | 378,516 | 60 |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 2,999 | 3,012 | 69 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,198 | 102,707 | 76 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,086 | 358,740 | 79 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,076 | 81,106 | 80 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,020 | 160,364 | 83 |
| 20 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,799 | 180,043 | 89 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,536 | 802,429 | 95 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,070 | 58,826 | 109 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 432 | 12,465 | 133 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 185 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 184 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.6% | 216,380 | 460,445 | 3 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 9.9% | 21,360 | 116,788 | 8 |
| 3 | [domyn](https://huggingface.co/domyn) | 7.0% | 8,218 | 16,632 | 14 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 4.8% | 296,686 | 6,093,872 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.8% | 58,587 | 1,453,108 | 6 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.4% | 22,645 | 570,092 | 7 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,227 | 592,502 | 9 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,693 | 204,061 | 13 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,996 | 376,357 | 12 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,466 | 452,449 | 11 |
| 11 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 70,638 | 2,666,701 | 5 |
| 12 | [speakleash](https://huggingface.co/speakleash) | 2.4% | 155,947 | 6,514,694 | 4 |
| 13 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,235,702 | 309,575,833 | 1 |
| 14 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,868 | 106,970 | 20 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 6,049 | 402,840 | 15 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,965 | 1,456,062 | 10 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,758 | 495,264 | 16 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,862 | 155,539 | 22 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 768 | 24,491 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,368 | 700,849 | 18 |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 4,002 | 662,497 | 19 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,985 | 861,161 | 17 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,849 | 1,163,170 | 21 |
| 24 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 24 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
