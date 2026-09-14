# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-14
- **Generated at:** 2026-09-14T12:17:57Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,508,171 | +7,816 | 56,193,452 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,603,713 | +51,387 | 63,784,659 | 2.5% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 616,386 | +1,779 | 3,510,193 | 17.1% | 13.95B | 6 |
| 4 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 527,762 | +13,209 | 16,155,834 | 3.2% | 12.25B | 3 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 523,875 | +5,432 | 45,425,512 | 1.2% | 7.24B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 496,590 | -7,032 | 3,933,553 | 12.3% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 408,221 | +15,715 | 4,541,422 | 8.8% | 24.01B | 2 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 389,698 | -19,183 | 5,455,840 | 7.0% | 4.25B | 7 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,635 | +257 | 415,327 | 68.6% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,227 | +197 | 411,809 | 68.6% | 1.20B | 1 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,906 | +207 | 396,852 | 68.6% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303,496 | -33 | 32,190,650 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,493 | +454 | 2,651,690 | 9.2% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 252,092 | -3,497 | 4,130,399 | 6.0% | 11.34B | 8 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 211,307 | +4,636 | 8,429,008 | 2.5% | 8.02B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,614 | -2,395 | 2,067,546 | 9.3% | 8.92B | 6 |
| 17 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 173,472 | +13,723 | 368,845 | 37.0% | 22.64B | 1 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 133,197 | -7,743 | 1,030,505 | 11.8% | 127.70B | 2 |
| 19 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 129,563 | +1,756 | 5,266,127 | 2.4% | 24.01B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 98,063 | -1,924 | 518,977 | 15.8% | 70.60B | 2 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,485 | -295 | 686,106 | 9.6% | 23.57B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,656 | +186 | 621,351 | 9.8% | 23.57B | 2 |
| 23 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,701 | -671 | 7,544,157 | 0.8% | 23.57B | 2 |
| 24 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,715 | +456 | 633,421 | 7.9% | 119.40B | 3 |
| 25 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 37,479 | +170 | 11,183,600 | 0.3% | 140.63B | 2 |
| 26 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 29,899 | +331 | 663,449 | 3.9% | 7.77B | 8 |
| 27 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 29,548 | -67 | 132,404 | 12.7% | 9.15B | 1 |
| 28 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,974 | -281 | 473,997 | 3.5% | 9.15B | 1 |
| 29 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,939 | -135 | 345,841 | 3.8% | 125.03B | 1 |
| 30 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,665 | -439 | 322,690 | 3.9% | 24.01B | 2 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,295 | +977 | 21,886 | 13.4% | 72.01B | 1 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,931 | -54 | 769,885 | 1.8% | 11.25B | 10 |
| 33 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,924 | +385 | 27,760 | 12.5% | 8.90B | 1 |
| 34 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,264 | -108 | 694,968 | 1.8% | 1.66B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,836 | +55 | 5,299,490 | 0.3% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,376 | +159 | 65,186 | 7.5% | — | 5 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,831 | +68 | 204,530 | 3.6% | — | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,313 | -29 | 501,918 | 1.5% | 7.24B | 8 |
| 39 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,566 | -604 | 4,920,571 | 0.2% | 122.61B | 1 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,208 | -60 | 105,599 | 3.0% | 8.42B | 5 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,924 | +484 | 128,058 | 2.6% | 7.48B | 5 |
| 42 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,921 | +72 | 5,141,574 | 0.1% | 22.25B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,913 | +67 | 161,771 | 1.9% | 11.17B | 16 |
| 44 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,563 | +96 | 63,520 | 2.8% | 11.77B | 4 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,385 | -12 | 45,202 | 3.0% | 8.03B | 7 |
| 46 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,329 | +2 | 28,532 | 3.4% | 33.12B | 1 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,216 | -52 | 141,303 | 1.7% | 2.25B | 7 |
| 48 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,177 | -8 | 89,919 | 2.2% | 2.89B | 1 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,930 | -123 | 666,740 | 0.5% | 7.45B | 2 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,845 | +9 | 902,018 | 0.4% | 23.57B | 2 |
| 51 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,586 | +14 | 54,080 | 2.3% | 7.55B | 1 |
| 52 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,537 | -57 | 5,374,540 | 0.1% | 22.25B | 1 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,526 | -41 | 55,959 | 2.3% | 1.60B | 5 |
| 54 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,467 | -519 | 30,835 | 2.6% | 14.03B | 1 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,394 | -113 | 250,558 | 1.0% | 4.76B | 5 |
| 56 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,346 | +72 | 130,766 | 1.5% | 7.40B | 3 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,282 | +30 | 369,310 | 0.7% | 7.24B | 8 |
| 58 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,010 | 0 | 11,088 | 2.7% | 572.6M | 5 |
| 59 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,467 | +48 | 38,656 | 1.8% | 321.0M | 2 |
| 60 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,427 | -117 | 5,030,414 | 0.0% | 122.61B | 1 |
| 61 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,273 | -20 | 107,444 | 1.1% | 7.29B | 2 |
| 62 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,239 | -5 | 145,907 | 0.9% | 7.24B | 4 |
| 63 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,231 | +38 | 19,385 | 1.9% | 4.30B | 2 |
| 64 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,077 | +79 | 33,444 | 1.6% | 2.61B | 3 |
| 65 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,942 | +88 | 16,339 | 1.7% | 12.19B | 2 |
| 66 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,877 | -5 | 13,811 | 1.6% | 3.83B | 5 |
| 67 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,822 | 0 | 63,635 | 1.1% | 14.08B | 1 |
| 68 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,794 | -60 | 6,914 | 1.7% | 4.30B | 3 |
| 69 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,737 | +58 | 8,885 | 1.6% | 9.15B | 1 |
| 70 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,649 | +25 | 31,679 | 1.3% | 22.64B | 1 |
| 71 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,586 | -9 | 6,686 | 1.5% | 1.51B | 6 |
| 72 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,562 | +4 | 77,037 | 0.9% | 7.45B | 1 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,532 | -895 | 22,147 | 1.3% | 22.64B | 1 |
| 74 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,512 | +41 | 7,403 | 1.4% | 28.84B | 3 |
| 75 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,387 | -18 | 18,867 | 1.2% | 12.25B | 3 |
| 76 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,385 | -94 | 172,546 | 0.5% | 11.51B | 7 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,372 | +3 | 175,698 | 0.5% | 12.25B | 6 |
| 78 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,313 | +5 | 21,556 | 1.1% | 11.17B | 5 |
| 79 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,278 | +86 | 43,718 | 0.9% | 12.19B | 2 |
| 80 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,252 | -5 | 98,552 | 0.6% | 30.68B | 1 |
| 81 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,218 | +20 | 29,779 | 0.9% | 11.17B | 5 |
| 82 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,203 | -8 | 47,670 | 0.8% | 9.24B | 4 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,188 | +3 | 104,699 | 0.6% | 7.45B | 1 |
| 84 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,137 | -2 | 31,923 | 0.9% | 56.7M | 1 |
| 85 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,130 | +6 | 354,772 | 0.2% | — | 3 |
| 86 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,111 | +13 | 95,200 | 0.6% | 1.35B | 8 |
| 87 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,044 | +13 | 80,927 | 0.6% | 8.03B | 3 |
| 88 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,042 | +2 | 300,160 | 0.3% | 6.74B | 2 |
| 89 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,038 | +3 | 156,600 | 0.4% | 1.10B | 1 |
| 90 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,033 | +31 | 217,564 | 0.3% | 12.19B | 3 |
| 91 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,022 | +20 | 56,593 | 0.7% | 1.35B | 3 |
| 92 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 994 | -8 | 12,306 | 0.9% | 70.55B | 2 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 989 | +16 | 799,711 | 0.1% | — | 3 |
| 94 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 971 | +2 | 144,352 | 0.4% | 13.02B | 1 |
| 95 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 961 | -1 | 183,549 | 0.3% | 6.74B | 1 |
| 96 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 941 | +3 | 37,319 | 0.7% | 27.23B | 3 |
| 97 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 923 | -3 | 38,260 | 0.7% | 70.55B | 3 |
| 98 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 910 | -99 | 7,857 | 0.8% | 27.43B | 3 |
| 99 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 900 | 0 | 83,607 | 0.5% | 2.22B | 1 |
| 100 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 899 | -28 | 48,187 | 0.6% | 7.77B | 1 |
| 101 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 822 | +33 | 227,243 | 0.3% | 35.13B | 4 |
| 102 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 775 | +8 | 1,079 | 0.8% | 27.23B | 3 |
| 103 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 760 | -79 | 81,896 | 0.4% | 9.15B | 1 |
| 104 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 714 | +4 | 70,052 | 0.4% | 8.03B | 3 |
| 105 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 713 | +105 | 149,763 | 0.3% | 23.57B | 2 |
| 106 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 645 | -5 | 450,895 | 0.1% | 40.43B | 1 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 635 | +19 | 13,549 | 0.6% | 4.33B | 3 |
| 108 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 624 | -183 | 2,750 | 0.6% | 30.68B | 1 |
| 109 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 585 | +11 | 17,970 | 0.5% | 1.20B | 2 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 584 | +3 | 3,407 | 0.6% | 8.03B | 3 |
| 111 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 582 | -12 | 321,694 | 0.1% | 7.24B | 2 |
| 112 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 565 | -125 | 6,629 | 0.5% | 9.82B | 1 |
| 113 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 536 | 0 | 11,100 | 0.5% | 31.59B | 6 |
| 114 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 526 | +2 | 13,600 | 0.5% | 353.4M | 2 |
| 115 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 519 | 0 | 1,249 | 0.5% | 31.58B | 2 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 513 | +1 | 32,211 | 0.4% | 40.43B | 2 |
| 117 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 446 | +24 | 44,263 | 0.3% | 7.70B | 5 |
| 118 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 434 | +2 | 19,534 | 0.4% | 3.20B | 2 |
| 119 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 434 | -19 | 51,749 | 0.3% | 7.24B | 5 |
| 120 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 409 | +5 | 232,287 | 0.1% | — | 2 |
| 121 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 405 | 0 | 1,981 | 0.4% | 31.59B | 6 |
| 122 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 403 | +12 | 106,736 | 0.2% | — | 3 |
| 123 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 396 | +4 | 2,646 | 0.4% | 560.9M | 2 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 394 | +6 | 38,810 | 0.3% | 7.48B | 2 |
| 125 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 393 | 0 | 7,018 | 0.4% | 31.59B | 6 |
| 126 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 387 | +9 | 15,534 | 0.3% | 1.54B | 4 |
| 127 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 383 | +32 | 2,364 | 0.4% | 4.02B | 2 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 381 | +28 | 75,788 | 0.2% | 7.04B | 4 |
| 129 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 377 | -17 | 50,666 | 0.3% | 7.24B | 1 |
| 130 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 363 | +88 | 26,994 | 0.3% | 9.24B | 2 |
| 131 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 304 | +107 | 21,535 | 0.3% | 2.61B | 2 |
| 132 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 299 | -7 | 4,851 | 0.3% | 437.8M | 1 |
| 133 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 278 | +7 | 41,454 | 0.2% | 11.17B | 1 |
| 134 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 253 | +31 | 21,278 | 0.2% | 9.24B | 2 |
| 135 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 245 | +86 | 11,529 | 0.2% | 27.23B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 212 | +30 | 16,288 | 0.2% | 7.29B | 2 |
| 137 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 185 | -6 | 899 | 0.2% | — | 1 |
| 138 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 185 | +2 | 5,227 | 0.2% | 353.4M | 2 |
| 139 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 174 | +11 | 19,302 | 0.1% | 68.98B | 2 |
| 140 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 158 | -1 | 1,938 | 0.2% | — | 1 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 154 | -1 | 5,047 | 0.1% | 11.51B | 5 |
| 142 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 138 | +6 | 7,088 | 0.1% | 1.20B | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | +4 | 38,500 | 0.1% | 70.55B | 3 |
| 144 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 124 | +1 | 2,222 | 0.1% | — | 1 |
| 145 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 122 | -5 | 1,221 | 0.1% | 560.9M | 1 |
| 146 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 102 | 0 | 4,756 | 0.1% | 70.55B | 3 |
| 147 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 97 | +7 | 28,158 | 0.1% | 46.70B | 6 |
| 148 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 96 | +1 | 176 | 0.1% | 437.8M | 1 |
| 149 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 61 | -1 | 902 | 0.1% | — | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | +1 | 249 | 0.1% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 45 | +1 | 324 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 22 | +1 | 133 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | +1 | 347 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | +3 | 148 | 0.0% | 8.16B | 3 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | +2 | 105 | 0.0% | 7.24B | 1 |
| 157 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | +4 | 200 | 0.0% | 15.17B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,199,603 | 294,924,961 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,051,895 | 1,419,703 | 11 | 69.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 633,345 | 4,533,761 | 7 | 13.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 299,441 | 6,268,930 | 12 | 4.7% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 255,968 | 2,055,017 | 11 | 11.9% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 36,172 | 1,336,045 | 5 | 2.5% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,512 | 424,152 | 6 | 3.3% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,191 | 530,883 | 13 | 2.1% |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,633 | 350,341 | 14 | 1.9% |
| 10 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,303 | 184,656 | 6 | 2.9% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,260 | 364,693 | 10 | 1.6% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,048 | 188,672 | 3 | 2.4% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,680 | 848,476 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,864 | 691,004 | 2 | 0.5% |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,346 | 130,766 | 1 | 1.5% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,970 | 484,501 | 3 | 0.5% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,722 | 147,242 | 2 | 1.1% |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,172 | 654,932 | 2 | 0.3% |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,133 | 151,793 | 2 | 0.8% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,975 | 1,158,036 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,904 | 101,650 | 4 | 0.9% |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 1,853 | 21,348 | 4 | 1.5% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 565 | 6,629 | 1 | 0.5% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 381 | 75,788 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 158 | 1,938 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,508,171 | 56,193,452 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 496,590 | 3,933,553 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,635 | 415,327 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 252,092 | 4,130,399 | 14 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 173,472 | 368,845 | 17 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 29,899 | 663,449 | 26 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,208 | 105,599 | 40 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,563 | 63,520 | 44 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,385 | 45,202 | 45 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,177 | 89,919 | 48 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,930 | 666,740 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,346 | 130,766 | 56 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,282 | 369,310 | 57 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 2,273 | 107,444 | 61 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 1,822 | 63,635 | 67 |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 4B (2512) | 1,794 | 6,914 | 68 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,252 | 98,552 | 80 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,130 | 354,772 | 85 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,111 | 95,200 | 86 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,038 | 156,600 | 89 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 989 | 799,711 | 93 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 565 | 6,629 | 112 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 536 | 11,100 | 113 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 381 | 75,788 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 158 | 1,938 | 140 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.2% | 1,051,895 | 1,419,703 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 13.7% | 633,345 | 4,533,761 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 11.9% | 255,968 | 2,055,017 | 5 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.7% | 299,441 | 6,268,930 | 4 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.3% | 17,512 | 424,152 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 2.9% | 8,303 | 184,656 | 10 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,199,603 | 294,924,961 | 1 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.5% | 36,172 | 1,336,045 | 6 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,048 | 188,672 | 12 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,191 | 530,883 | 8 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,633 | 350,341 | 9 |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.6% | 7,260 | 364,693 | 11 |
| 13 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1.5% | 1,853 | 21,348 | 22 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,346 | 130,766 | 15 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.1% | 2,722 | 147,242 | 17 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,904 | 101,650 | 21 |
| 17 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,133 | 151,793 | 19 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,680 | 848,476 | 13 |
| 19 | [domyn](https://huggingface.co/domyn) | 0.5% | 565 | 6,629 | 23 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,970 | 484,501 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,864 | 691,004 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,172 | 654,932 | 18 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 381 | 75,788 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,975 | 1,158,036 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 158 | 1,938 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
