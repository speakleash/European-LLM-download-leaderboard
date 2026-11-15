# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-15
- **Generated at:** 2026-11-15T13:43:44Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,012,027 | +8,029 | 60,742,925 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,194,460 | -45,747 | 66,932,279 | 1.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 667,840 | -9,745 | 4,560,252 | 14.3% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 552,369 | -371 | 46,545,385 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 361,160 | -277 | 32,845,374 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 264,373 | +5,016 | 2,577,933 | 9.9% | 8.92B | 6 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 215,073 | -13,005 | 4,695,848 | 4.5% | 8.05B | 2 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213,120 | -149 | 332,031 | 49.3% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 210,956 | +5,780 | 5,927,721 | 3.5% | 3.85B | 7 |
| 10 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 146,555 | -4,001 | 16,684,202 | 0.9% | 12.25B | 3 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 144,088 | -4,583 | 5,039,166 | 2.8% | 24.01B | 2 |
| 12 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 122,675 | +9,601 | 4,290,187 | 2.8% | 11.34B | 9 |
| 13 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 102,106 | -2,854 | 7,730,627 | 1.3% | 23.57B | 2 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 101,018 | +3,531 | 5,649,123 | 1.8% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,216 | -553 | 8,611,443 | 0.7% | 8.02B | 1 |
| 16 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,786 | -681 | 11,296,098 | 0.4% | 140.63B | 2 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 40,495 | -2,492 | 807,623 | 4.5% | 23.57B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 38,673 | -5,683 | 740,821 | 4.6% | 7.77B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,162 | -145 | 751,343 | 4.1% | 119.40B | 3 |
| 20 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,373 | -310 | 3,012,289 | 0.8% | 24.01B | 1 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,727 | +347 | 369,773 | 4.4% | 24.01B | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,888 | +13 | 947,803 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,885 | -93 | 802,372 | 1.9% | 11.25B | 10 |
| 24 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,626 | +484 | 16,686 | 14.2% | — | 2 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,453 | -408 | 749,384 | 1.8% | 8.90B | 5 |
| 26 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,151 | +78 | 698,921 | 1.9% | 7.29B | 1 |
| 27 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,084 | -418 | 1,123,039 | 1.2% | 127.70B | 2 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,720 | -217 | 4,946,238 | 0.3% | 122.61B | 1 |
| 29 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 13,624 | -1,415 | 35,434 | 10.1% | 78.10B | 2 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,835 | +32 | 5,047,714 | 0.2% | 122.61B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,146 | -317 | 651,928 | 1.6% | 23.57B | 2 |
| 32 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,263 | +295 | 248,226 | 3.2% | — | 1 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,068 | -41 | 499,170 | 1.8% | 9.15B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,637 | -131 | 525,545 | 1.7% | 7.24B | 8 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,252 | +74 | 5,391,920 | 0.2% | 22.25B | 1 |
| 36 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,538 | +3 | 120,389 | 3.9% | 8.42B | 7 |
| 37 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,472 | -127 | 36,685 | 6.2% | 72.01B | 4 |
| 38 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,053 | -631 | 552,042 | 1.2% | 70.60B | 2 |
| 39 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,807 | -303 | 88,568 | 4.1% | — | 5 |
| 40 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,608 | +165 | 23,533 | 6.2% | 3.83B | 5 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,452 | -101 | 17,379 | 6.3% | 1.51B | 6 |
| 42 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 7,275 | +216 | 262,144 | 2.0% | 4.76B | 5 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,061 | -27 | 359,498 | 1.5% | 125.03B | 1 |
| 44 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,704 | -35 | 605,427 | 1.0% | 22.64B | 1 |
| 45 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,398 | -263 | 161,604 | 2.4% | 9.15B | 1 |
| 46 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,277 | -9 | 24,143 | 5.1% | 572.6M | 5 |
| 47 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,146 | +1,582 | 6,146 | 5.8% | 11.17B | 14 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,987 | -17 | 57,101 | 3.8% | 8.03B | 7 |
| 49 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,848 | +3 | 138,420 | 2.5% | 2.89B | 1 |
| 50 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,688 | -253 | 153,550 | 2.2% | 2.25B | 7 |
| 51 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,599 | +16 | 159,374 | 2.2% | 351.6M | 1 |
| 52 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,187 | -314 | 65,104 | 3.1% | 1.60B | 5 |
| 53 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,695 | -32 | 39,255 | 3.4% | 56.7M | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,629 | -7 | 910,955 | 0.5% | 23.57B | 2 |
| 55 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,487 | +2 | 155,351 | 1.8% | 7.24B | 4 |
| 56 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,263 | -52 | 141,069 | 1.8% | 7.40B | 3 |
| 57 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,242 | +4 | 125,141 | 1.9% | 8.54B | 2 |
| 58 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,135 | -27 | 378,756 | 0.9% | 7.24B | 8 |
| 59 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,082 | +174 | 29,128 | 3.2% | 22.64B | 1 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,989 | -241 | 41,552 | 2.8% | 2.61B | 3 |
| 61 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,909 | -74 | 141,496 | 1.6% | 7.48B | 5 |
| 62 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,888 | -72 | 5,166,043 | 0.1% | 22.25B | 1 |
| 63 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,575 | +148 | 55,252 | 2.3% | 7.77B | 3 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,541 | -19 | 44,956 | 2.4% | 13.29B | 3 |
| 65 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,378 | -6,889 | 22,921 | 2.7% | 27.43B | 3 |
| 66 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,264 | -7 | 96,771 | 1.7% | 2.89B | 1 |
| 67 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,186 | +38 | 3,229 | 3.1% | 3.93B | 2 |
| 68 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,137 | +99 | 13,355 | 2.8% | 9.15B | 1 |
| 69 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,130 | -95 | 170,330 | 1.2% | 11.17B | 16 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,744 | +205 | 21,394 | 2.3% | 12.19B | 2 |
| 71 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,723 | -2 | 5,304,209 | 0.1% | 7.25B | 1 |
| 72 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,512 | -56 | 157,428 | 1.0% | 23.57B | 2 |
| 73 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,380 | +9 | 231,106 | 0.7% | 35.13B | 4 |
| 74 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,331 | +26 | 86,800 | 1.2% | 9.15B | 1 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,237 | +17 | 102,866 | 1.1% | 30.68B | 1 |
| 76 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,138 | -276 | 23,401 | 1.7% | 4.30B | 2 |
| 77 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,121 | +12 | 358,910 | 0.5% | — | 3 |
| 78 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,099 | +7 | 81,248 | 1.2% | 7.45B | 1 |
| 79 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,076 | -8 | 52,262 | 1.4% | 9.24B | 4 |
| 80 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,065 | -7 | 454,922 | 0.4% | 40.43B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,032 | +2 | 160,487 | 0.8% | 1.10B | 1 |
| 82 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,002 | -139 | 34,754 | 1.5% | 14.03B | 1 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,996 | +9 | 108,768 | 1.0% | 7.45B | 1 |
| 84 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,923 | +11 | 35,440 | 1.4% | 22.64B | 1 |
| 85 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,918 | +9 | 187,214 | 0.7% | 6.74B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,917 | +4 | 303,878 | 0.5% | 6.74B | 2 |
| 87 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,853 | +7 | 147,930 | 0.7% | 13.02B | 1 |
| 88 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,769 | -28 | 180,161 | 0.6% | 12.25B | 6 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,661 | +27 | 802,613 | 0.2% | — | 3 |
| 90 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,637 | +45 | 10,167 | 1.5% | 9.82B | 1 |
| 91 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,620 | -30 | 41,141 | 1.1% | 70.55B | 3 |
| 92 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,564 | -37 | 44,931 | 1.1% | 12.25B | 3 |
| 93 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,555 | +4 | 55,047 | 1.0% | 7.24B | 5 |
| 94 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,529 | +3 | 416,652 | 0.3% | 1.20B | 1 |
| 95 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,497 | -2 | 53,802 | 1.0% | 7.24B | 1 |
| 96 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,491 | +11 | 1,491 | 1.5% | 3.93B | 1 |
| 97 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,430 | +9 | 420,055 | 0.3% | 353.4M | 1 |
| 98 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,397 | +3 | 20,939 | 1.2% | 1.20B | 2 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,376 | +7 | 9,794 | 1.3% | 4.30B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,367 | +6 | 16,200 | 1.2% | 353.4M | 2 |
| 101 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,305 | -7 | 9,585 | 1.2% | 28.84B | 3 |
| 102 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,283 | +5 | 401,457 | 0.3% | 3.21B | 1 |
| 103 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,181 | -94 | 9,784 | 1.1% | 40.43B | 2 |
| 104 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,173 | -35 | 175,348 | 0.4% | 11.51B | 7 |
| 105 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,165 | +10 | 56,989 | 0.7% | 7.55B | 1 |
| 106 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,101 | +24 | 58,933 | 0.7% | 1.35B | 3 |
| 107 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,072 | -29 | 45,314 | 0.7% | 12.19B | 2 |
| 108 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,066 | +6 | 31,925 | 0.8% | 33.12B | 1 |
| 109 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,004 | +64 | 671,537 | 0.1% | 7.45B | 2 |
| 110 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 997 | -34 | 219,257 | 0.3% | 12.19B | 3 |
| 111 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 885 | +10 | 2,925 | 0.9% | 40.43B | 2 |
| 112 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 884 | +5 | 233,716 | 0.3% | — | 2 |
| 113 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 845 | -9 | 24,154 | 0.7% | 11.17B | 5 |
| 114 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 842 | -36 | 82,121 | 0.5% | 7.04B | 4 |
| 115 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 829 | -8 | 14,898 | 0.7% | 4.33B | 3 |
| 116 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 816 | +2 | 1,768 | 0.8% | 608.3M | 1 |
| 117 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 805 | +3 | 96,752 | 0.4% | 1.35B | 8 |
| 118 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 739 | -5 | 112,590 | 0.3% | 7.29B | 2 |
| 119 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 715 | -33 | 31,902 | 0.5% | 11.17B | 5 |
| 120 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 705 | +1 | 17,130 | 0.6% | 1.54B | 4 |
| 121 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 676 | -1 | 82,352 | 0.4% | 8.03B | 3 |
| 122 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 640 | -31 | 2,117 | 0.6% | 27.23B | 3 |
| 123 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 637 | +3 | 20,940 | 0.5% | 3.20B | 2 |
| 124 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 625 | -64 | 806 | 0.6% | 437.8M | 2 |
| 125 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 599 | +3 | 28,068 | 0.5% | 9.24B | 2 |
| 126 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 599 | +4 | 3,801 | 0.6% | 30.68B | 1 |
| 127 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 564 | -52 | 22,246 | 0.5% | 9.24B | 2 |
| 128 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | +1 | 563 | 0.6% | 3.93B | 1 |
| 129 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | +1 | 563 | 0.6% | 3.93B | 1 |
| 130 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 562 | +1 | 562 | 0.6% | 3.93B | 1 |
| 131 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 561 | +3 | 561 | 0.6% | 3.93B | 1 |
| 132 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | 0 | 12,588 | 0.5% | 31.59B | 6 |
| 133 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 434 | +10 | 4,517 | 0.4% | 8.03B | 3 |
| 134 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 428 | -4 | 1,762 | 0.4% | — | 1 |
| 135 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 422 | +3 | 5,761 | 0.4% | 11.51B | 5 |
| 136 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | -4 | 1,155 | 0.4% | 437.8M | 1 |
| 137 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 389 | +10 | 3,469 | 0.4% | 560.9M | 2 |
| 138 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 374 | -1 | 12,280 | 0.3% | 27.23B | 2 |
| 139 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 317 | +3 | 22,251 | 0.3% | 2.61B | 2 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 302 | -1 | 2,883 | 0.3% | 4.02B | 2 |
| 141 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 298 | +9 | 107,371 | 0.1% | — | 3 |
| 142 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 280 | +15 | 37,967 | 0.2% | 27.23B | 3 |
| 143 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 276 | +1 | 70,648 | 0.2% | 8.03B | 3 |
| 144 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 265 | -40 | 32,977 | 0.2% | 40.43B | 2 |
| 145 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 253 | +23 | 1,121 | 0.3% | 9.15B | 1 |
| 146 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 218 | +6 | 41,997 | 0.2% | 11.17B | 1 |
| 147 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 214 | +5 | 19,771 | 0.2% | 68.98B | 2 |
| 148 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 198 | -2 | 322,353 | 0.0% | 7.24B | 2 |
| 149 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 193 | -1 | 16,711 | 0.2% | 7.29B | 2 |
| 150 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 189 | -2 | 29,848 | 0.1% | 1.01B | 1 |
| 151 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | 0 | 3,006 | 0.2% | 31.59B | 6 |
| 152 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 181 | -25 | 39,475 | 0.1% | 7.48B | 2 |
| 153 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | 0 | 170 | 0.2% | 7.77B | 1 |
| 154 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 167 | -1 | 1,223 | 0.2% | — | 1 |
| 155 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 158 | +3 | 28,496 | 0.1% | 46.70B | 6 |
| 156 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 157 | -3 | 44,711 | 0.1% | 7.70B | 5 |
| 157 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 137 | -10 | 2,947 | 0.1% | 40.43B | 2 |
| 158 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | -3 | 12,771 | 0.1% | 70.55B | 2 |
| 159 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 132 | -3 | 5,550 | 0.1% | 353.4M | 2 |
| 160 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 129 | +1 | 2,594 | 0.1% | — | 1 |
| 161 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 115 | +3 | 5,110 | 0.1% | 70.55B | 3 |
| 162 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 113 | 0 | 7,511 | 0.1% | 31.59B | 6 |
| 163 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 113 | +3 | 5,218 | 0.1% | 437.8M | 1 |
| 164 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | -9 | 38,758 | 0.1% | 70.55B | 3 |
| 165 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 62 | +14 | 438 | 0.1% | 437.8M | 1 |
| 166 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 59 | +4 | 266 | 0.1% | 437.8M | 1 |
| 167 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 58 | -1 | 7,281 | 0.1% | 1.20B | 2 |
| 168 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | -3 | 1,326 | 0.1% | 560.9M | 1 |
| 169 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | +12 | 207 | 0.1% | 437.8M | 1 |
| 170 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 51 | -2 | 390 | 0.1% | 7.77B | 2 |
| 171 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 48 | -20 | 973 | 0.0% | 40.43B | 2 |
| 172 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 47 | -2 | 457 | 0.0% | 321.0M | 1 |
| 173 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 46 | -2 | 621 | 0.0% | 6.25B | 2 |
| 174 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 44 | -1 | 221 | 0.0% | 8.16B | 3 |
| 175 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 43 | -1 | 308 | 0.0% | 437.8M | 1 |
| 176 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 42 | +2 | 1,463 | 0.0% | 8.03B | 1 |
| 177 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 41 | -1 | 277 | 0.0% | 15.17B | 3 |
| 178 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 39 | -1 | 230 | 0.0% | 40.43B | 2 |
| 179 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 29 | 0 | 153 | 0.0% | 7.24B | 1 |
| 180 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 17 | +2 | 379 | 0.0% | 12.25B | 1 |
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
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,110,740 | 309,949,688 | 32 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 268,388 | 6,099,014 | 7 | 4.3% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 217,458 | 462,447 | 6 | 38.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 179,217 | 6,542,486 | 13 | 2.7% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 71,165 | 2,672,220 | 12 | 2.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 52,823 | 1,455,562 | 13 | 3.4% |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,141 | 593,852 | 5 | 2.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,971 | 1,456,922 | 12 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,249 | 570,916 | 13 | 2.3% |
| 10 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 14,466 | 117,555 | 2 | 6.6% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,220 | 453,016 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,932 | 377,208 | 16 | 2.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,876 | 204,575 | 3 | 2.9% |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,563 | 17,136 | 7 | 7.3% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,971 | 403,199 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,803 | 495,631 | 3 | 1.0% |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,099 | 861,553 | 3 | 0.5% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,333 | 701,109 | 2 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 4,038 | 662,788 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 3,057 | 1,163,471 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,921 | 107,165 | 4 | 1.4% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,906 | 155,685 | 2 | 0.7% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 862 | 24,614 | 4 | 0.7% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,012,027 | 60,742,925 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 215,073 | 4,695,848 | 7 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 213,120 | 332,031 | 8 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 122,675 | 4,290,187 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 38,673 | 740,821 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,888 | 947,803 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 13,624 | 35,434 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,538 | 120,389 | 36 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,987 | 57,101 | 48 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,848 | 138,420 | 49 |
| 11 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,695 | 39,255 | 53 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,487 | 155,351 | 55 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,135 | 378,756 | 58 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,378 | 22,921 | 65 |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,186 | 3,229 | 67 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,237 | 102,866 | 75 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,121 | 358,910 | 77 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,099 | 81,248 | 78 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,032 | 160,487 | 81 |
| 20 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,769 | 180,161 | 88 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,661 | 802,613 | 89 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,101 | 58,933 | 106 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 132 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 185 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 184 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.7% | 217,458 | 462,447 | 3 |
| 2 | [domyn](https://huggingface.co/domyn) | 7.3% | 8,563 | 17,136 | 14 |
| 3 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 6.6% | 14,466 | 117,555 | 10 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 4.3% | 268,388 | 6,099,014 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.4% | 52,823 | 1,455,562 | 6 |
| 6 | [ilsp](https://huggingface.co/ilsp) | 2.9% | 8,876 | 204,575 | 13 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,141 | 593,852 | 7 |
| 8 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,932 | 377,208 | 12 |
| 9 | [speakleash](https://huggingface.co/speakleash) | 2.7% | 179,217 | 6,542,486 | 4 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,220 | 453,016 | 11 |
| 11 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 71,165 | 2,672,220 | 5 |
| 12 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.3% | 15,249 | 570,916 | 9 |
| 13 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,110,740 | 309,949,688 | 1 |
| 14 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,921 | 107,165 | 21 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 5,971 | 403,199 | 15 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,971 | 1,456,922 | 8 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,803 | 495,631 | 16 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,906 | 155,685 | 22 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 862 | 24,614 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,333 | 701,109 | 18 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,099 | 861,553 | 17 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 4,038 | 662,788 | 19 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 3,057 | 1,163,471 | 20 |
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
