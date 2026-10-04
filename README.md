# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-04
- **Generated at:** 2026-10-04T12:02:44Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,377,064 | -15,127 | 57,859,886 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,715,257 | +2,234 | 64,814,956 | 2.6% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 650,718 | +32,328 | 670,010 | 84.5% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 564,363 | -272 | 45,747,551 | 1.2% | 7.24B | 2 |
| 5 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 541,800 | -4,126 | 4,787,939 | 11.1% | 24.01B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 494,343 | -1,520 | 4,280,126 | 11.3% | 8.05B | 2 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 493,971 | -9,676 | 16,446,951 | 3.0% | 12.25B | 3 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 449,903 | -16,848 | 3,730,064 | 11.7% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 355,242 | -13,873 | 594,008 | 51.2% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 323,414 | +54 | 2,866,953 | 10.9% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 266,048 | -4,030 | 32,374,060 | 0.8% | 46.70B | 2 |
| 12 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 257,494 | -4,552 | 5,626,037 | 4.5% | 4.25B | 7 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 255,950 | -30 | 5,479,009 | 4.6% | 24.01B | 1 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 225,144 | -4,164 | 2,232,801 | 9.7% | 8.92B | 6 |
| 15 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 216,808 | +159,205 | 907,240 | 21.5% | 1.66B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 148,779 | -1,698 | 8,528,378 | 1.7% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 110,569 | -7,732 | 1,089,784 | 9.3% | 127.70B | 2 |
| 18 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 105,636 | -9,085 | 4,148,477 | 2.5% | 11.34B | 8 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,255 | +756 | 737,136 | 8.8% | 23.57B | 2 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 67,358 | -11,103 | 533,912 | 10.6% | 70.60B | 2 |
| 21 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,248 | -3 | 68,176 | 39.4% | — | 1 |
| 22 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,291 | +786 | 7,589,312 | 0.8% | 23.57B | 2 |
| 23 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 61,183 | +5,053 | 679,606 | 7.8% | 119.40B | 3 |
| 24 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,539 | -752 | 11,218,690 | 0.4% | 140.63B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 27,795 | -1,387 | 681,693 | 3.6% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 26,237 | -690 | 146,683 | 10.6% | 9.15B | 1 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,122 | -122 | 5,159,606 | 0.4% | 22.25B | 1 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,347 | -7,837 | 632,777 | 2.5% | 23.57B | 2 |
| 29 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 16,636 | +1,185 | 215,519 | 5.3% | — | 1 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,438 | -146 | 483,079 | 2.6% | 9.15B | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,997 | -96 | 779,710 | 1.7% | 11.25B | 10 |
| 32 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 14,102 | -1,337 | 26,272 | 11.2% | 72.01B | 1 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,473 | -301 | 75,005 | 7.7% | — | 5 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,057 | +13 | 509,532 | 1.8% | 7.24B | 8 |
| 35 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 10,800 | -1 | 134,570 | 4.6% | 7.48B | 5 |
| 36 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,147 | +146 | 327,567 | 2.1% | 24.01B | 2 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,168 | -38 | 4,927,235 | 0.2% | 122.61B | 1 |
| 38 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,671 | -533 | 349,987 | 1.7% | 125.03B | 1 |
| 39 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,051 | -146 | 49,405 | 4.1% | 8.03B | 7 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,942 | -49 | 109,567 | 2.8% | 8.42B | 7 |
| 41 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,730 | +175 | 5,379,149 | 0.1% | 22.25B | 1 |
| 42 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,551 | +1 | 30,179 | 4.3% | 33.12B | 1 |
| 43 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 5,338 | +2,004 | 23,896 | 4.3% | 12.25B | 3 |
| 44 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,014 | +90 | 144,995 | 2.0% | 2.25B | 7 |
| 45 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,962 | -38 | 165,035 | 1.9% | 11.17B | 16 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,933 | +25 | 134,543 | 2.1% | 7.40B | 3 |
| 47 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,889 | +5 | 154,329 | 1.9% | 23.57B | 2 |
| 48 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,821 | -57 | 111,380 | 2.3% | 7.29B | 2 |
| 49 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,639 | +182 | 15,259 | 4.0% | 572.6M | 5 |
| 50 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,627 | -3 | 67,158 | 2.8% | 12.77B | 5 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,395 | +87 | 372,535 | 0.9% | 7.24B | 8 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,238 | -62 | 253,203 | 1.2% | 4.76B | 5 |
| 53 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,121 | +2,596 | 11,586 | 3.7% | 27.43B | 3 |
| 54 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,093 | -109 | 669,788 | 0.5% | 7.45B | 2 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,060 | -26 | 905,064 | 0.4% | 23.57B | 2 |
| 56 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,890 | +93 | 66,582 | 2.3% | 14.08B | 1 |
| 57 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,867 | +42 | 5,033,504 | 0.1% | 122.61B | 1 |
| 58 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,851 | -60 | 92,090 | 2.0% | 2.89B | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,721 | +92 | 148,859 | 1.5% | 7.24B | 4 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,383 | +81 | 35,811 | 2.5% | 2.61B | 3 |
| 61 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,260 | -97 | 413,846 | 0.6% | 1.20B | 1 |
| 62 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,113 | -103 | 417,360 | 0.6% | 353.4M | 1 |
| 63 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,074 | -103 | 398,905 | 0.6% | 3.21B | 1 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,956 | +59 | 58,087 | 1.9% | 1.60B | 5 |
| 65 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,531 | -1,311 | 55,348 | 1.6% | 7.55B | 1 |
| 66 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,499 | -8 | 84,297 | 1.4% | 9.15B | 1 |
| 67 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,375 | +16 | 40,038 | 1.7% | 321.0M | 2 |
| 68 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,286 | +97 | 85,509 | 1.2% | 2.22B | 1 |
| 69 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,169 | -3 | 18,021 | 1.8% | 12.19B | 2 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,164 | -56 | 49,284 | 1.4% | 9.24B | 4 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,153 | -2 | 32,766 | 1.6% | 22.64B | 1 |
| 72 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,037 | -5 | 23,613 | 1.6% | 22.64B | 1 |
| 73 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,017 | +18 | 8,379 | 1.9% | 1.51B | 6 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,876 | -84 | 78,302 | 1.1% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,804 | -10 | 105,957 | 0.9% | 7.45B | 1 |
| 76 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,803 | +7 | 452,455 | 0.3% | 40.43B | 1 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,795 | -5 | 99,781 | 0.9% | 30.68B | 1 |
| 78 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,732 | +8 | 49,686 | 1.2% | 7.77B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,724 | +5 | 355,949 | 0.4% | — | 3 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,710 | 0 | 14,993 | 1.5% | 3.83B | 5 |
| 81 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,689 | -1,766 | 31,723 | 1.3% | 14.03B | 1 |
| 82 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,626 | +4 | 176,818 | 0.6% | 12.25B | 6 |
| 83 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,615 | +84 | 22,647 | 1.3% | 11.17B | 5 |
| 84 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,605 | +25 | 32,931 | 1.2% | 56.7M | 1 |
| 85 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,603 | -14 | 5,300,738 | 0.0% | 7.25B | 1 |
| 86 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,597 | +5 | 157,715 | 0.6% | 1.10B | 1 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,557 | 0 | 301,218 | 0.4% | 6.74B | 2 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,497 | +3 | 145,365 | 0.6% | 13.02B | 1 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,493 | +2 | 184,567 | 0.5% | 6.74B | 1 |
| 90 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,436 | -4 | 7,759 | 1.3% | 9.82B | 1 |
| 91 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,352 | +9 | 30,653 | 1.0% | 11.17B | 5 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,307 | -86 | 173,410 | 0.5% | 11.51B | 7 |
| 93 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,285 | -2 | 12,013 | 1.1% | 31.59B | 6 |
| 94 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,219 | -82 | 20,083 | 1.0% | 4.30B | 2 |
| 95 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,207 | +48 | 52,777 | 0.8% | 7.24B | 5 |
| 96 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,171 | -185 | 57,402 | 0.7% | 1.35B | 3 |
| 97 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,117 | +19 | 800,500 | 0.1% | — | 3 |
| 98 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,114 | +45 | 51,627 | 0.7% | 7.24B | 1 |
| 99 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,086 | -8 | 228,009 | 0.3% | 35.13B | 4 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,066 | +141 | 7,690 | 1.0% | 4.30B | 3 |
| 101 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,040 | -56 | 9,447 | 1.0% | 9.15B | 1 |
| 102 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,003 | +2 | 18,789 | 0.8% | 1.20B | 2 |
| 103 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 987 | -9 | 8,061 | 0.9% | 28.84B | 3 |
| 104 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 893 | -10 | 38,879 | 0.6% | 70.55B | 3 |
| 105 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 882 | -4 | 14,295 | 0.8% | 353.4M | 2 |
| 106 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 869 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 792 | -16 | 16,170 | 0.7% | 1.54B | 4 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 744 | -95 | 95,683 | 0.4% | 1.35B | 8 |
| 109 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 697 | -33 | 20,085 | 0.6% | 3.20B | 2 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 669 | +25 | 44,065 | 0.5% | 12.19B | 2 |
| 111 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 624 | 0 | 81,369 | 0.3% | 8.03B | 3 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 561 | -19 | 217,863 | 0.2% | 12.19B | 3 |
| 113 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 536 | +4 | 3,812 | 0.5% | 8.03B | 3 |
| 114 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 513 | 0 | 2,992 | 0.5% | 560.9M | 2 |
| 115 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 506 | +7 | 76,161 | 0.3% | 7.04B | 4 |
| 116 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 481 | -31 | 1,497 | 0.5% | 31.58B | 2 |
| 117 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 480 | -19 | 232,651 | 0.1% | — | 2 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 468 | -3 | 32,519 | 0.4% | 40.43B | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 462 | +47 | 21,807 | 0.4% | 2.61B | 2 |
| 120 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 455 | +23 | 13,874 | 0.4% | 4.33B | 3 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 442 | +10 | 27,282 | 0.3% | 9.24B | 2 |
| 122 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 418 | -15 | 12,496 | 0.4% | 70.55B | 2 |
| 123 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 418 | -2 | 321,967 | 0.1% | 7.24B | 2 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 402 | +1 | 39,093 | 0.3% | 7.48B | 2 |
| 125 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 391 | -11 | 3,028 | 0.4% | 30.68B | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 375 | +8 | 11,769 | 0.3% | 27.23B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 363 | -18 | 7,339 | 0.3% | 31.59B | 6 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 349 | -2 | 37,532 | 0.3% | 27.23B | 3 |
| 129 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 341 | -1 | 44,442 | 0.2% | 7.70B | 5 |
| 130 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 322 | -55 | 70,287 | 0.2% | 8.03B | 3 |
| 131 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 315 | -13 | 41,661 | 0.2% | 11.17B | 1 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 313 | +7 | 1,154 | 0.3% | — | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 299 | +7 | 106,937 | 0.1% | — | 3 |
| 134 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 275 | 0 | 21,466 | 0.2% | 9.24B | 2 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 264 | +2 | 19,465 | 0.2% | 68.98B | 2 |
| 136 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 258 | -2 | 2,482 | 0.3% | 4.02B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 247 | -11 | 16,418 | 0.2% | 7.29B | 2 |
| 138 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 230 | +1 | 1,239 | 0.2% | 27.23B | 3 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 210 | -3 | 5,220 | 0.2% | 11.51B | 5 |
| 140 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 209 | +6 | 2,374 | 0.2% | — | 1 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 200 | -10 | 5,344 | 0.2% | 353.4M | 2 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 188 | -5 | 38,623 | 0.1% | 70.55B | 3 |
| 143 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 180 | +55 | 4,939 | 0.2% | 437.8M | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 146 | +1 | 7,164 | 0.1% | 1.20B | 2 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | 0 | 28,252 | 0.1% | 46.70B | 6 |
| 146 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 138 | +3 | 4,843 | 0.1% | 70.55B | 3 |
| 147 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 128 | +123 | 6,158 | 0.1% | 12.25B | 3 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 125 | 0 | 1,013 | 0.1% | — | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 82 | -1 | 394 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 79 | -9 | 1,240 | 0.1% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 53 | -3 | 190 | 0.1% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 28 | 0 | 223 | 0.0% | 15.17B | 3 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -2 | 145 | 0.0% | 437.8M | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -6 | 258 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 23 | -1 | 166 | 0.0% | 8.16B | 3 |
| 156 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | 0 | 356 | 0.0% | 437.8M | 1 |
| 157 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 115 | 0.0% | 7.24B | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,073,539 | 300,056,241 | 30 | 2.7% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,234,887 | 5,548,951 | 7 | 21.9% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 641,682 | 2,534,837 | 11 | 24.4% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 159,445 | 6,322,205 | 12 | 2.5% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,248 | 68,176 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 36,812 | 1,361,348 | 5 | 2.5% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,801 | 433,543 | 6 | 3.3% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 16,803 | 543,675 | 13 | 2.6% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,364 | 1,430,435 | 11 | 1.1% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,067 | 358,078 | 14 | 2.4% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 9,901 | 372,875 | 10 | 2.1% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,859 | 191,468 | 6 | 3.0% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,773 | 854,047 | 3 | 0.8% |
| 14 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,685 | 193,102 | 3 | 2.3% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,176 | 152,091 | 2 | 2.4% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,933 | 134,543 | 1 | 2.1% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,813 | 694,502 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,587 | 487,647 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,281 | 657,167 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 2,998 | 23,677 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,237 | 103,198 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,160 | 1,159,553 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,915 | 153,085 | 2 | 0.8% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,436 | 7,759 | 1 | 1.3% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 506 | 76,161 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,377,064 | 57,859,886 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 650,718 | 670,010 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 355,242 | 594,008 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 105,636 | 4,148,477 | 18 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,248 | 68,176 | 21 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 27,795 | 681,693 | 25 |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,051 | 49,405 | 39 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,942 | 109,567 | 40 |
| 9 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 5,338 | 23,896 | 43 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,933 | 134,543 | 46 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,821 | 111,380 | 48 |
| 12 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,627 | 67,158 | 50 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,395 | 372,535 | 51 |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,093 | 669,788 | 54 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,890 | 66,582 | 56 |
| 16 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,851 | 92,090 | 58 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 3,260 | 413,846 | 61 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,795 | 99,781 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,724 | 355,949 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,597 | 157,715 | 86 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,436 | 7,759 | 90 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,285 | 12,013 | 93 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,171 | 57,402 | 96 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,117 | 800,500 | 97 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 506 | 76,161 | 115 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,248 | 68,176 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 24.4% | 641,682 | 2,534,837 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.9% | 1,234,887 | 5,548,951 | 2 |
| 4 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.3% | 17,801 | 433,543 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.0% | 8,859 | 191,468 | 12 |
| 6 | [mistralai](https://huggingface.co/mistralai) | 2.7% | 8,073,539 | 300,056,241 | 1 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.6% | 16,803 | 543,675 | 8 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.5% | 36,812 | 1,361,348 | 6 |
| 9 | [speakleash](https://huggingface.co/speakleash) | 2.5% | 159,445 | 6,322,205 | 4 |
| 10 | [Almawave](https://huggingface.co/Almawave) | 2.4% | 6,176 | 152,091 | 15 |
| 11 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 2,998 | 23,677 | 20 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,067 | 358,078 | 10 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.3% | 6,685 | 193,102 | 14 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,933 | 134,543 | 16 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.1% | 9,901 | 372,875 | 11 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,436 | 7,759 | 24 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,237 | 103,198 | 21 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,364 | 1,430,435 | 9 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,773 | 854,047 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,587 | 487,647 | 18 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 1,915 | 153,085 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,813 | 694,502 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,281 | 657,167 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 506 | 76,161 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,160 | 1,159,553 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
