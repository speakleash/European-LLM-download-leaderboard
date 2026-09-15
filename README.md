# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-15
- **Generated at:** 2026-09-15T11:26:47Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,536,442 | +28,271 | 56,274,519 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,659,791 | +56,078 | 63,866,337 | 2.6% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 623,646 | +7,260 | 3,524,687 | 17.2% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 534,447 | +10,572 | 45,445,030 | 1.2% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 527,393 | -369 | 16,173,796 | 3.2% | 12.25B | 3 |
| 6 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 430,416 | +22,195 | 4,566,622 | 9.2% | 24.01B | 2 |
| 7 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 374,829 | -14,869 | 5,464,002 | 6.7% | 4.25B | 7 |
| 8 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,702 | +67 | 415,400 | 68.6% | 353.4M | 1 |
| 9 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,302 | +75 | 411,888 | 68.6% | 1.20B | 1 |
| 10 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,971 | +65 | 396,923 | 68.6% | 3.21B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 305,704 | +2,208 | 32,200,921 | 0.9% | 46.70B | 2 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 256,822 | +3,329 | 2,661,982 | 9.3% | 24.01B | 1 |
| 13 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 203,423 | +1,809 | 2,072,339 | 9.4% | 8.92B | 6 |
| 14 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 202,423 | -8,884 | 8,435,720 | 2.4% | 8.02B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 188,020 | +14,548 | 383,463 | 38.9% | 22.64B | 1 |
| 16 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 133,319 | +3,756 | 5,271,940 | 2.5% | 24.01B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 126,314 | -6,883 | 1,030,879 | 11.2% | 127.70B | 2 |
| 18 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,216 | -269 | 688,529 | 9.5% | 23.57B | 2 |
| 19 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,750 | +94 | 621,664 | 9.8% | 23.57B | 2 |
| 20 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,823 | -878 | 7,545,529 | 0.8% | 23.57B | 2 |
| 21 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,764 | +1,049 | 635,812 | 8.0% | 119.40B | 3 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,208 | +729 | 11,185,050 | 0.3% | 140.63B | 2 |
| 23 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 36,520 | +20,596 | 48,404 | 24.6% | 8.90B | 1 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 31,170 | +1,271 | 664,971 | 4.1% | 7.77B | 8 |
| 25 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,261 | +713 | 133,418 | 13.0% | 9.15B | 1 |
| 26 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,260 | +286 | 474,723 | 3.5% | 9.15B | 1 |
| 27 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,968 | +1,673 | 23,559 | 14.5% | 72.01B | 1 |
| 28 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,999 | +60 | 346,407 | 3.8% | 125.03B | 1 |
| 29 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,064 | -601 | 322,794 | 3.8% | 24.01B | 2 |
| 30 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,743 | -188 | 770,287 | 1.8% | 11.25B | 10 |
| 31 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,146 | -118 | 695,261 | 1.8% | 1.66B | 1 |
| 32 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,082 | +246 | 5,299,770 | 0.3% | 7.25B | 1 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,759 | +383 | 65,775 | 7.7% | — | 5 |
| 34 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,676 | -155 | 204,731 | 3.5% | — | 1 |
| 35 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,177 | -389 | 4,920,839 | 0.1% | 122.61B | 1 |
| 36 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,196 | -12 | 105,719 | 3.0% | 8.42B | 5 |
| 37 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,970 | +57 | 161,927 | 1.9% | 11.17B | 16 |
| 38 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,962 | +41 | 5,141,707 | 0.1% | 22.25B | 1 |
| 39 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,574 | +11 | 63,649 | 2.8% | 11.77B | 4 |
| 40 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,503 | +118 | 45,358 | 3.1% | 8.03B | 7 |
| 41 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,348 | +19 | 28,574 | 3.4% | 33.12B | 1 |
| 42 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,170 | -7 | 90,014 | 2.2% | 2.89B | 1 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,138 | -78 | 141,394 | 1.7% | 2.25B | 7 |
| 44 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,097 | +167 | 666,975 | 0.5% | 7.45B | 2 |
| 45 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,929 | +84 | 902,166 | 0.4% | 23.57B | 2 |
| 46 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,570 | -16 | 54,094 | 2.3% | 7.55B | 1 |
| 47 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,550 | +24 | 56,077 | 2.3% | 1.60B | 5 |
| 48 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,453 | -14 | 30,844 | 2.6% | 14.03B | 1 |
| 49 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,443 | +97 | 130,986 | 1.5% | 7.40B | 3 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,420 | -117 | 5,374,670 | 0.1% | 22.25B | 1 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,252 | -30 | 369,436 | 0.7% | 7.24B | 8 |
| 52 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,476 | +9 | 38,706 | 1.8% | 321.0M | 2 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,448 | +21 | 5,030,580 | 0.0% | 122.61B | 1 |
| 54 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,274 | +43 | 19,456 | 1.9% | 4.30B | 2 |
| 55 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,221 | -18 | 146,054 | 0.9% | 7.24B | 4 |
| 56 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,219 | -54 | 107,456 | 1.1% | 7.29B | 2 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,094 | +17 | 33,523 | 1.6% | 2.61B | 3 |
| 58 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,072 | +195 | 14,034 | 1.8% | 3.83B | 5 |
| 59 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,045 | +103 | 16,466 | 1.8% | 12.19B | 2 |
| 60 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,889 | +67 | 63,795 | 1.2% | 14.08B | 1 |
| 61 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,760 | +23 | 8,930 | 1.6% | 9.15B | 1 |
| 62 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,638 | -11 | 31,733 | 1.2% | 22.64B | 1 |
| 63 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,563 | +1 | 77,101 | 0.9% | 7.45B | 1 |
| 64 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,540 | -254 | 6,961 | 1.4% | 4.30B | 3 |
| 65 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,537 | +5 | 22,216 | 1.3% | 22.64B | 1 |
| 66 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,515 | +3 | 7,416 | 1.4% | 28.84B | 3 |
| 67 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,431 | +895 | 11,995 | 1.3% | 31.59B | 6 |
| 68 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,413 | +26 | 18,947 | 1.2% | 12.25B | 3 |
| 69 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,374 | +2 | 175,758 | 0.5% | 12.25B | 6 |
| 70 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,338 | +25 | 21,605 | 1.1% | 11.17B | 5 |
| 71 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,318 | +115 | 47,841 | 0.9% | 9.24B | 4 |
| 72 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,289 | +11 | 43,737 | 0.9% | 12.19B | 2 |
| 73 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,239 | +21 | 29,825 | 1.0% | 11.17B | 5 |
| 74 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,226 | -26 | 98,613 | 0.6% | 30.68B | 1 |
| 75 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,224 | +819 | 2,804 | 1.2% | 31.59B | 6 |
| 76 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,185 | -3 | 104,757 | 0.6% | 7.45B | 1 |
| 77 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,127 | -10 | 31,934 | 0.9% | 56.7M | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,123 | -7 | 354,833 | 0.2% | — | 3 |
| 79 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,087 | -24 | 95,221 | 0.6% | 1.35B | 8 |
| 80 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,055 | +11 | 80,951 | 0.6% | 8.03B | 3 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,029 | -9 | 156,651 | 0.4% | 1.10B | 1 |
| 82 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,029 | -13 | 300,212 | 0.3% | 6.74B | 2 |
| 83 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,008 | -14 | 56,616 | 0.6% | 1.35B | 3 |
| 84 | Apertus v1.1 1.5B \* | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,005 | -581 | 3,448 | 1.0% | 1.51B | 6 |
| 85 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 992 | -2 | 12,344 | 0.9% | 70.55B | 2 |
| 86 | Bielik-11B v2.6 \* | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 989 | -396 | 159,403 | 0.4% | 11.17B | 7 |
| 87 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 988 | -45 | 217,575 | 0.3% | 12.19B | 3 |
| 88 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 979 | -10 | 799,744 | 0.1% | — | 3 |
| 89 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 968 | +45 | 38,319 | 0.7% | 70.55B | 3 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 958 | -13 | 144,402 | 0.4% | 13.02B | 1 |
| 91 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 956 | +15 | 37,337 | 0.7% | 27.23B | 3 |
| 92 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 946 | -15 | 183,599 | 0.3% | 6.74B | 1 |
| 93 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 936 | +26 | 7,895 | 0.9% | 27.43B | 3 |
| 94 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 923 | +23 | 83,718 | 0.5% | 2.22B | 1 |
| 95 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 913 | +348 | 6,998 | 0.9% | 9.82B | 1 |
| 96 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 909 | +10 | 48,223 | 0.6% | 7.77B | 1 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 874 | +52 | 227,320 | 0.3% | 35.13B | 4 |
| 98 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 782 | +7 | 1,086 | 0.8% | 27.23B | 3 |
| 99 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 732 | +18 | 70,075 | 0.4% | 8.03B | 3 |
| 100 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 727 | +14 | 149,784 | 0.3% | 23.57B | 2 |
| 101 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 727 | +142 | 18,116 | 0.6% | 1.20B | 2 |
| 102 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 686 | -74 | 81,896 | 0.4% | 9.15B | 1 |
| 103 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 650 | +15 | 13,573 | 0.6% | 4.33B | 3 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 647 | +121 | 13,736 | 0.6% | 353.4M | 2 |
| 105 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 641 | -4 | 450,921 | 0.1% | 40.43B | 1 |
| 106 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 593 | -31 | 2,766 | 0.6% | 30.68B | 1 |
| 107 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 566 | -18 | 3,422 | 0.5% | 8.03B | 3 |
| 108 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 563 | -19 | 321,706 | 0.1% | 7.24B | 2 |
| 109 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 521 | +2 | 1,251 | 0.5% | 31.58B | 2 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 516 | +82 | 19,622 | 0.4% | 3.20B | 2 |
| 111 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 500 | -13 | 32,230 | 0.4% | 40.43B | 2 |
| 112 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 446 | +12 | 51,805 | 0.3% | 7.24B | 5 |
| 113 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 435 | -11 | 44,271 | 0.3% | 7.70B | 5 |
| 114 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 413 | +20 | 7,038 | 0.4% | 31.59B | 6 |
| 115 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 412 | +3 | 232,293 | 0.1% | — | 2 |
| 116 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 409 | +6 | 106,746 | 0.2% | — | 3 |
| 117 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 399 | +12 | 15,546 | 0.3% | 1.54B | 4 |
| 118 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 397 | +16 | 75,812 | 0.2% | 7.04B | 4 |
| 119 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 384 | -12 | 2,667 | 0.4% | 560.9M | 2 |
| 120 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 378 | +1 | 50,712 | 0.3% | 7.24B | 1 |
| 121 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 375 | -19 | 38,823 | 0.3% | 7.48B | 2 |
| 122 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 361 | +57 | 21,598 | 0.3% | 2.61B | 2 |
| 123 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 359 | -4 | 27,000 | 0.3% | 9.24B | 2 |
| 124 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 358 | -25 | 2,366 | 0.3% | 4.02B | 2 |
| 125 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 285 | -14 | 4,854 | 0.3% | 437.8M | 1 |
| 126 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 278 | 0 | 41,472 | 0.2% | 11.17B | 1 |
| 127 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 257 | +4 | 21,287 | 0.2% | 9.24B | 2 |
| 128 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 249 | +4 | 11,536 | 0.2% | 27.23B | 2 |
| 129 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 216 | +4 | 16,297 | 0.2% | 7.29B | 2 |
| 130 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190 | +5 | 909 | 0.2% | — | 1 |
| 131 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 181 | -4 | 5,231 | 0.2% | 353.4M | 2 |
| 132 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 174 | 0 | 19,310 | 0.1% | 68.98B | 2 |
| 133 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 156 | -2 | 1,938 | 0.2% | — | 1 |
| 134 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 152 | -2 | 5,057 | 0.1% | 11.51B | 5 |
| 135 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 152 | +16 | 38,519 | 0.1% | 70.55B | 3 |
| 136 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 143 | +5 | 7,095 | 0.1% | 1.20B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 131 | +7 | 2,231 | 0.1% | — | 1 |
| 138 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 127 | +25 | 4,784 | 0.1% | 70.55B | 3 |
| 139 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 110 | -12 | 1,222 | 0.1% | 560.9M | 1 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 110 | +13 | 28,173 | 0.1% | 46.70B | 6 |
| 141 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 95 | -1 | 176 | 0.1% | 437.8M | 1 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 143 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63 | +2 | 905 | 0.1% | — | 1 |
| 144 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | 0 | 249 | 0.1% | 437.8M | 1 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 43 | -2 | 324 | 0.0% | 321.0M | 1 |
| 146 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 24 | +2 | 135 | 0.0% | 437.8M | 1 |
| 147 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 18 | +3 | 151 | 0.0% | 8.16B | 3 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 347 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 17 | +4 | 204 | 0.0% | 15.17B | 3 |
| 150 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | 0 | 105 | 0.0% | 7.24B | 1 |
| 151 | Apertus 70B (2509) \* | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 0 | -98,063 | 0 | 0.0% | — | 2 |
| 152 | Apertus 8B (2509) \* | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 0 | -496,590 | 0 | 0.0% | — | 2 |
| 153 | Apertus v1.1 0.5B \* | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 0 | -3,010 | 0 | 0.0% | — | 5 |
| 154 | Bielik-11B v3.0 \* | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 0 | -252,092 | 0 | 0.0% | — | 8 |
| 155 | Bielik-4.5B v3.0 \* | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 0 | -3,394 | 0 | 0.0% | — | 5 |
| 156 | Bielik-7B v0.1 \* | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 0 | -9,313 | 0 | 0.0% | — | 8 |
| 157 | Bielik-Minitron 7B v3.0 \* | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 0 | -5,924 | 0 | 0.0% | — | 5 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

\* Row marked incomplete: one or more member repos failed during the last fetch.

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,304,550 | 295,221,664 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,052,374 | 1,420,304 | 11 | 69.2% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 271,209 | 2,072,125 | 11 | 12.5% |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) \* | swiss-ai | CH | 57,565 | 89,445 | 7 | 30.4% |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 37,358 | 1,337,739 | 5 | 2.6% |
| 6 | [speakleash](https://huggingface.co/speakleash) \* | SpeakLeash / ACK Cyfronet AGH | PL | 28,259 | 1,245,653 | 12 | 2.1% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,716 | 424,509 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | UA | 13,358 | 531,292 | 13 | 2.1% |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,559 | 350,714 | 14 | 1.9% |
| 10 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,545 | 185,081 | 6 | 3.0% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,086 | 365,018 | 10 | 1.5% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,006 | 188,813 | 3 | 2.4% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,845 | 848,833 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,815 | 691,142 | 2 | 0.5% |
| 15 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,589 | 23,088 | 4 | 2.9% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,443 | 130,986 | 1 | 1.5% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,933 | 484,652 | 3 | 0.5% |
| 18 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,812 | 147,513 | 2 | 1.1% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,152 | 655,045 | 2 | 0.3% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,095 | 151,837 | 2 | 0.8% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,974 | 1,158,093 | 4 | 0.2% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,854 | 101,734 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 913 | 6,998 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 397 | 75,812 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 156 | 1,938 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,536,442 | 56,274,519 | 1 |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,702 | 415,400 | 8 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 188,020 | 383,463 | 15 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 36,520 | 48,404 | 23 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 31,170 | 664,971 | 24 |
| 6 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v2.3 | 15,743 | 770,287 | 30 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,196 | 105,719 | 36 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,574 | 63,649 | 39 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,503 | 45,358 | 40 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,170 | 90,014 | 42 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,097 | 666,975 | 44 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,443 | 130,986 | 49 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,252 | 369,436 | 51 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | MamayLM Gemma 3 4B v1.0 | 2,274 | 19,456 | 54 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 1,889 | 63,795 | 60 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 4B (2512) | 1,540 | 6,961 | 64 |
| 17 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,431 | 11,995 | 67 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,226 | 98,613 | 74 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,123 | 354,833 | 78 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,087 | 95,221 | 79 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,029 | 156,651 | 81 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 979 | 799,744 | 88 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 913 | 6,998 | 95 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 397 | 75,812 | 118 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 156 | 1,938 | 133 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.2% | 1,052,374 | 1,420,304 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 30.4% | 57,565 | 89,445 | 4 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 12.5% | 271,209 | 2,072,125 | 3 |
| 4 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,716 | 424,509 | 7 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.0% | 8,545 | 185,081 | 10 |
| 6 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.9% | 3,589 | 23,088 | 15 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,304,550 | 295,221,664 | 1 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 37,358 | 1,337,739 | 5 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,006 | 188,813 | 12 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,358 | 531,292 | 8 |
| 11 | [speakleash](https://huggingface.co/speakleash) | 2.1% | 28,259 | 1,245,653 | 6 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,559 | 350,714 | 9 |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.5% | 7,086 | 365,018 | 11 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,443 | 130,986 | 16 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.1% | 2,812 | 147,513 | 18 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,854 | 101,734 | 22 |
| 17 | [domyn](https://huggingface.co/domyn) | 0.9% | 913 | 6,998 | 23 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,095 | 151,837 | 20 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,845 | 848,833 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,933 | 484,652 | 17 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,815 | 691,142 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,152 | 655,045 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 397 | 75,812 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,974 | 1,158,093 | 21 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 156 | 1,938 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
