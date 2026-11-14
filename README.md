# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-14
- **Generated at:** 2026-11-14T13:15:12Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,003,998 | +10,473 | 60,678,213 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,240,207 | -56,429 | 66,902,660 | 1.9% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 677,585 | +1,198 | 4,550,183 | 14.6% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 552,740 | +5,052 | 46,535,538 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 361,437 | -1,634 | 32,833,502 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,357 | +3,293 | 2,566,438 | 9.7% | 8.92B | 6 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 228,078 | -13,316 | 4,694,690 | 4.8% | 8.05B | 2 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213,269 | +1,220 | 331,862 | 49.4% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,176 | -460 | 5,915,006 | 3.4% | 3.85B | 7 |
| 10 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 150,556 | -6,328 | 16,680,872 | 0.9% | 12.25B | 3 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 148,671 | -2,259 | 5,035,976 | 2.9% | 24.01B | 2 |
| 12 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 113,074 | +11,825 | 4,280,083 | 2.6% | 11.34B | 9 |
| 13 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,960 | -1,001 | 7,728,997 | 1.3% | 23.57B | 2 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 97,487 | -9,274 | 5,641,258 | 1.7% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,769 | -445 | 8,610,662 | 0.7% | 8.02B | 1 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 44,467 | -1,423 | 11,294,929 | 0.4% | 140.63B | 2 |
| 17 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 44,356 | -55 | 740,477 | 5.3% | 7.77B | 8 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 42,987 | -2,282 | 807,537 | 4.7% | 23.57B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,307 | +258 | 750,736 | 4.2% | 119.40B | 3 |
| 20 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,683 | -796 | 3,011,949 | 0.9% | 24.01B | 1 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,380 | -13,235 | 369,053 | 4.3% | 24.01B | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,875 | +419 | 947,100 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,978 | +177 | 801,931 | 1.9% | 11.25B | 10 |
| 24 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,142 | +599 | 16,190 | 13.9% | — | 2 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,861 | -552 | 749,178 | 1.9% | 8.90B | 5 |
| 26 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,502 | -514 | 1,122,636 | 1.3% | 127.70B | 2 |
| 27 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,073 | +242 | 698,326 | 1.9% | 7.29B | 1 |
| 28 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 15,039 | -675 | 35,218 | 11.1% | 78.10B | 2 |
| 29 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,937 | -46 | 4,945,927 | 0.3% | 122.61B | 1 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,803 | +50 | 5,047,582 | 0.2% | 122.61B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,463 | -148 | 651,651 | 1.7% | 23.57B | 2 |
| 32 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,109 | -36 | 498,937 | 1.9% | 9.15B | 1 |
| 33 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,968 | +157 | 247,622 | 3.2% | — | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,768 | -119 | 525,247 | 1.7% | 7.24B | 8 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,267 | -253 | 22,897 | 8.4% | 27.43B | 3 |
| 36 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,178 | -49 | 5,391,617 | 0.2% | 22.25B | 1 |
| 37 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,684 | -716 | 551,775 | 1.3% | 70.60B | 2 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,599 | +132 | 36,673 | 6.3% | 72.01B | 4 |
| 39 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,535 | +208 | 120,238 | 3.9% | 8.42B | 7 |
| 40 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,110 | -168 | 88,388 | 4.3% | — | 5 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,553 | -74 | 17,292 | 6.4% | 1.51B | 6 |
| 42 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,443 | +376 | 23,310 | 6.0% | 3.83B | 5 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,088 | +141 | 359,249 | 1.5% | 125.03B | 1 |
| 44 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 7,059 | +116 | 261,864 | 2.0% | 4.76B | 5 |
| 45 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,739 | +102 | 605,267 | 1.0% | 22.64B | 1 |
| 46 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,661 | -504 | 161,447 | 2.5% | 9.15B | 1 |
| 47 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,286 | -32 | 23,995 | 5.1% | 572.6M | 5 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,004 | -17 | 56,981 | 3.8% | 8.03B | 7 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,941 | +50 | 153,460 | 2.3% | 2.25B | 7 |
| 50 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,845 | -2 | 138,228 | 2.5% | 2.89B | 1 |
| 51 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,583 | -1 | 159,145 | 2.2% | 351.6M | 1 |
| 52 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,501 | -53 | 64,994 | 3.3% | 1.60B | 5 |
| 53 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,727 | -32 | 39,215 | 3.4% | 56.7M | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,636 | -37 | 910,853 | 0.5% | 23.57B | 2 |
| 55 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,564 | +796 | 4,564 | 4.4% | 11.17B | 14 |
| 56 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,485 | -2 | 155,200 | 1.8% | 7.24B | 4 |
| 57 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,315 | -41 | 140,936 | 1.8% | 7.40B | 3 |
| 58 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,238 | -16 | 125,017 | 1.9% | 8.54B | 2 |
| 59 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,230 | +39 | 41,442 | 3.0% | 2.61B | 3 |
| 60 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,162 | -6 | 378,640 | 0.9% | 7.24B | 8 |
| 61 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,983 | -52 | 141,431 | 1.6% | 7.48B | 5 |
| 62 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,960 | 0 | 5,165,928 | 0.1% | 22.25B | 1 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,908 | +104 | 28,887 | 3.0% | 22.64B | 1 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,560 | -68 | 44,889 | 2.5% | 13.29B | 3 |
| 65 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,427 | +173 | 55,038 | 2.2% | 7.77B | 3 |
| 66 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,271 | +3 | 96,670 | 1.7% | 2.89B | 1 |
| 67 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,225 | +19 | 170,280 | 1.2% | 11.17B | 16 |
| 68 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,148 | +149 | 3,161 | 3.1% | 3.93B | 2 |
| 69 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,038 | +55 | 13,206 | 2.7% | 9.15B | 1 |
| 70 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,725 | +20 | 5,304,136 | 0.1% | 7.25B | 1 |
| 71 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,568 | +34 | 157,395 | 1.0% | 23.57B | 2 |
| 72 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,539 | +74 | 21,120 | 2.1% | 12.19B | 2 |
| 73 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,414 | +22 | 23,315 | 2.0% | 4.30B | 2 |
| 74 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,371 | -2 | 231,046 | 0.7% | 35.13B | 4 |
| 75 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,305 | +117 | 86,772 | 1.2% | 9.15B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,220 | +22 | 102,791 | 1.1% | 30.68B | 1 |
| 77 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,141 | -43 | 34,726 | 1.6% | 14.03B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,109 | +23 | 358,833 | 0.5% | — | 3 |
| 79 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,092 | +16 | 81,179 | 1.2% | 7.45B | 1 |
| 80 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,084 | +24 | 52,202 | 1.4% | 9.24B | 4 |
| 81 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,072 | +13 | 454,889 | 0.4% | 40.43B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,030 | +10 | 160,428 | 0.8% | 1.10B | 1 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,987 | +7 | 108,703 | 1.0% | 7.45B | 1 |
| 84 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,913 | -3 | 303,817 | 0.5% | 6.74B | 2 |
| 85 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,912 | +2 | 35,373 | 1.4% | 22.64B | 1 |
| 86 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,909 | +8 | 187,153 | 0.7% | 6.74B | 1 |
| 87 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,846 | +9 | 147,869 | 0.7% | 13.02B | 1 |
| 88 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,797 | -2 | 180,103 | 0.6% | 12.25B | 6 |
| 89 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,650 | -34 | 41,122 | 1.2% | 70.55B | 3 |
| 90 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,634 | +98 | 802,557 | 0.2% | — | 3 |
| 91 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,601 | -26 | 44,882 | 1.1% | 12.25B | 3 |
| 92 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,592 | +47 | 10,096 | 1.4% | 9.82B | 1 |
| 93 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,551 | -3 | 54,990 | 1.0% | 7.24B | 5 |
| 94 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,526 | +89 | 416,635 | 0.3% | 1.20B | 1 |
| 95 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,499 | +3 | 53,751 | 1.0% | 7.24B | 1 |
| 96 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,480 | +33 | 1,480 | 1.5% | 3.93B | 1 |
| 97 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,421 | +86 | 420,025 | 0.3% | 353.4M | 1 |
| 98 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,394 | -154 | 20,918 | 1.2% | 1.20B | 2 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,369 | -33 | 9,759 | 1.2% | 4.30B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,361 | +18 | 16,177 | 1.2% | 353.4M | 2 |
| 101 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,312 | -17 | 9,578 | 1.2% | 28.84B | 3 |
| 102 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,278 | +107 | 401,438 | 0.3% | 3.21B | 1 |
| 103 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,275 | -3 | 9,751 | 1.2% | 40.43B | 2 |
| 104 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,208 | -44 | 175,324 | 0.4% | 11.51B | 7 |
| 105 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,155 | +7 | 56,948 | 0.7% | 7.55B | 1 |
| 106 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,101 | +13 | 45,297 | 0.8% | 12.19B | 2 |
| 107 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,077 | +7 | 58,864 | 0.7% | 1.35B | 3 |
| 108 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,060 | +4 | 31,904 | 0.8% | 33.12B | 1 |
| 109 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,031 | -73 | 219,243 | 0.3% | 12.19B | 3 |
| 110 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 940 | +11 | 671,450 | 0.1% | 7.45B | 2 |
| 111 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 879 | +18 | 233,710 | 0.3% | — | 2 |
| 112 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 878 | -4,768 | 82,112 | 0.5% | 7.04B | 4 |
| 113 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 875 | +13 | 2,908 | 0.9% | 40.43B | 2 |
| 114 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 854 | -34 | 24,127 | 0.7% | 11.17B | 5 |
| 115 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 837 | +1 | 14,868 | 0.7% | 4.33B | 3 |
| 116 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 814 | +7 | 1,752 | 0.8% | 608.3M | 1 |
| 117 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 802 | +10 | 96,736 | 0.4% | 1.35B | 8 |
| 118 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 748 | -5 | 31,894 | 0.6% | 11.17B | 5 |
| 119 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 744 | -21 | 112,587 | 0.4% | 7.29B | 2 |
| 120 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 704 | +7 | 17,113 | 0.6% | 1.54B | 4 |
| 121 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 689 | -71 | 803 | 0.7% | 437.8M | 2 |
| 122 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 677 | -14 | 82,337 | 0.4% | 8.03B | 3 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 671 | -7 | 2,116 | 0.7% | 27.23B | 3 |
| 124 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 634 | +14 | 20,927 | 0.5% | 3.20B | 2 |
| 125 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 616 | +11 | 22,243 | 0.5% | 9.24B | 2 |
| 126 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 596 | -12 | 28,059 | 0.5% | 9.24B | 2 |
| 127 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 595 | +12 | 3,787 | 0.6% | 30.68B | 1 |
| 128 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 562 | +2 | 562 | 0.6% | 3.93B | 1 |
| 129 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 562 | +2 | 562 | 0.6% | 3.93B | 1 |
| 130 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 561 | +7 | 561 | 0.6% | 3.93B | 1 |
| 131 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 558 | +5 | 558 | 0.6% | 3.93B | 1 |
| 132 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | +122 | 12,588 | 0.5% | 31.59B | 6 |
| 133 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 432 | +7 | 1,749 | 0.4% | — | 1 |
| 134 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 424 | -15 | 4,491 | 0.4% | 8.03B | 3 |
| 135 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 419 | +16 | 5,756 | 0.4% | 11.51B | 5 |
| 136 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 398 | -2 | 1,155 | 0.4% | 437.8M | 1 |
| 137 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 379 | -2 | 3,454 | 0.4% | 560.9M | 2 |
| 138 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 375 | -45 | 12,272 | 0.3% | 27.23B | 2 |
| 139 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 314 | +6 | 22,244 | 0.3% | 2.61B | 2 |
| 140 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 305 | +4 | 32,974 | 0.2% | 40.43B | 2 |
| 141 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 303 | -4 | 2,881 | 0.3% | 4.02B | 2 |
| 142 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 289 | +23 | 107,359 | 0.1% | — | 3 |
| 143 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 275 | +9 | 70,641 | 0.2% | 8.03B | 3 |
| 144 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 265 | -11 | 37,945 | 0.2% | 27.23B | 3 |
| 145 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 230 | +14 | 1,095 | 0.2% | 9.15B | 1 |
| 146 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 212 | +4 | 41,988 | 0.1% | 11.17B | 1 |
| 147 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 209 | +23 | 19,761 | 0.2% | 68.98B | 2 |
| 148 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 206 | +2 | 39,472 | 0.1% | 7.48B | 2 |
| 149 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 200 | 0 | 322,347 | 0.0% | 7.24B | 2 |
| 150 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 194 | -11 | 16,708 | 0.2% | 7.29B | 2 |
| 151 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 191 | +5 | 29,846 | 0.1% | 1.01B | 1 |
| 152 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | 0 | 3,006 | 0.2% | 31.59B | 6 |
| 153 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | 0 | 170 | 0.2% | 7.77B | 1 |
| 154 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 168 | +11 | 1,221 | 0.2% | — | 1 |
| 155 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 160 | -2 | 44,709 | 0.1% | 7.70B | 5 |
| 156 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 155 | +15 | 28,489 | 0.1% | 46.70B | 6 |
| 157 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 147 | +5 | 2,940 | 0.1% | 40.43B | 2 |
| 158 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | +6 | 12,767 | 0.1% | 70.55B | 2 |
| 159 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 135 | -3 | 5,546 | 0.1% | 353.4M | 2 |
| 160 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 128 | -4 | 2,588 | 0.1% | — | 1 |
| 161 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 113 | -28 | 7,511 | 0.1% | 31.59B | 6 |
| 162 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 112 | +5 | 5,103 | 0.1% | 70.55B | 3 |
| 163 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 110 | +11 | 5,210 | 0.1% | 437.8M | 1 |
| 164 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 89 | +8 | 38,756 | 0.1% | 70.55B | 3 |
| 165 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 68 | 0 | 973 | 0.1% | 40.43B | 2 |
| 166 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 60 | -4 | 1,325 | 0.1% | 560.9M | 1 |
| 167 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 59 | -1 | 7,277 | 0.1% | 1.20B | 2 |
| 168 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 55 | +9 | 262 | 0.1% | 437.8M | 1 |
| 169 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 53 | +5 | 390 | 0.1% | 7.77B | 2 |
| 170 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 49 | +1 | 457 | 0.0% | 321.0M | 1 |
| 171 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 48 | -5 | 618 | 0.0% | 6.25B | 2 |
| 172 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 48 | 0 | 422 | 0.0% | 437.8M | 1 |
| 173 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 45 | 0 | 220 | 0.0% | 8.16B | 3 |
| 174 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | +14 | 195 | 0.0% | 437.8M | 1 |
| 175 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | +16 | 308 | 0.0% | 437.8M | 1 |
| 176 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 42 | 0 | 275 | 0.0% | 15.17B | 3 |
| 177 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 40 | -10 | 230 | 0.0% | 40.43B | 2 |
| 178 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 40 | +3 | 1,461 | 0.0% | 8.03B | 1 |
| 179 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | +1 | 153 | 0.0% | 7.24B | 1 |
| 180 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 15 | +1 | 377 | 0.0% | 12.25B | 1 |
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
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,160,552 | 309,776,357 | 32 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 282,504 | 6,096,913 | 7 | 4.6% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 217,627 | 462,165 | 6 | 38.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 168,593 | 6,529,483 | 13 | 2.5% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 71,103 | 2,669,736 | 12 | 2.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 58,777 | 1,454,818 | 13 | 3.8% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 22,340 | 570,431 | 13 | 3.3% |
| 8 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,172 | 593,172 | 5 | 2.9% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,001 | 1,456,666 | 12 | 1.1% |
| 10 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 15,917 | 117,330 | 2 | 7.3% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,381 | 452,727 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,965 | 376,787 | 16 | 2.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,901 | 204,419 | 3 | 2.9% |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,463 | 16,980 | 7 | 7.2% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,020 | 403,000 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,785 | 495,450 | 3 | 1.0% |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,019 | 861,332 | 3 | 0.5% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,362 | 700,987 | 2 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 4,022 | 662,650 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 3,011 | 1,163,387 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,902 | 107,073 | 4 | 1.4% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,879 | 155,600 | 2 | 0.7% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 862 | 24,614 | 4 | 0.7% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,003,998 | 60,678,213 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 228,078 | 4,694,690 | 7 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 213,269 | 331,862 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 113,074 | 4,280,083 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 44,356 | 740,477 | 17 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,875 | 947,100 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 15,039 | 35,218 | 28 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,267 | 22,897 | 35 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,535 | 120,238 | 39 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,004 | 56,981 | 48 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,845 | 138,228 | 50 |
| 12 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,727 | 39,215 | 53 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,485 | 155,200 | 56 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,162 | 378,640 | 60 |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,148 | 3,161 | 68 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,220 | 102,791 | 76 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,109 | 358,833 | 78 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,092 | 81,179 | 79 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,030 | 160,428 | 82 |
| 20 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,797 | 180,103 | 88 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,634 | 802,557 | 90 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,077 | 58,864 | 107 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 132 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 185 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 184 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.7% | 217,627 | 462,165 | 3 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 7.3% | 15,917 | 117,330 | 10 |
| 3 | [domyn](https://huggingface.co/domyn) | 7.2% | 8,463 | 16,980 | 14 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 4.6% | 282,504 | 6,096,913 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.8% | 58,777 | 1,454,818 | 6 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 22,340 | 570,431 | 7 |
| 7 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,901 | 204,419 | 13 |
| 8 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,172 | 593,172 | 8 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,965 | 376,787 | 12 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,381 | 452,727 | 11 |
| 11 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 71,103 | 2,669,736 | 5 |
| 12 | [speakleash](https://huggingface.co/speakleash) | 2.5% | 168,593 | 6,529,483 | 4 |
| 13 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,160,552 | 309,776,357 | 1 |
| 14 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,902 | 107,073 | 21 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 6,020 | 403,000 | 15 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,001 | 1,456,666 | 9 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,785 | 495,450 | 16 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,879 | 155,600 | 22 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 862 | 24,614 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,362 | 700,987 | 18 |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 4,022 | 662,650 | 19 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,019 | 861,332 | 17 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 3,011 | 1,163,387 | 20 |
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
