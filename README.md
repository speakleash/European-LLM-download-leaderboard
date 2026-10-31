# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-31
- **Generated at:** 2026-10-31T11:56:32Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,822,497 | +9,641 | 59,528,435 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,772,351 | -25,684 | 66,463,144 | 2.7% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 561,627 | +4,996 | 46,276,868 | 1.2% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 525,606 | +19,672 | 4,234,424 | 12.1% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 409,774 | +3,470 | 4,656,506 | 8.6% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 317,246 | +3,078 | 32,674,999 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 218,904 | +2,331 | 2,442,371 | 8.6% | 8.92B | 6 |
| 8 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 216,979 | -28,988 | 16,630,323 | 1.3% | 12.25B | 3 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,902 | +19 | 5,815,933 | 3.5% | 3.85B | 7 |
| 10 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 194,195 | +733 | 941,248 | 18.7% | 1.66B | 1 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 190,605 | -5,980 | 4,964,333 | 3.8% | 24.01B | 2 |
| 12 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 153,339 | -6,966 | 3,003,343 | 4.9% | 24.01B | 1 |
| 13 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 144,524 | +11,947 | 211,510 | 46.4% | 12.77B | 5 |
| 14 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 140,748 | -32,082 | 738,345 | 16.8% | 8.90B | 1 |
| 15 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 126,792 | -3,516 | 5,593,762 | 2.2% | 24.01B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 96,860 | +1,334 | 7,679,882 | 1.2% | 23.57B | 2 |
| 17 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,142 | +538 | 801,061 | 7.8% | 23.57B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,008 | -2,309 | 736,114 | 7.9% | 119.40B | 3 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 59,503 | -6,019 | 11,275,260 | 0.5% | 140.63B | 2 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 49,779 | -2,085 | 8,571,632 | 0.6% | 8.02B | 1 |
| 21 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 43,890 | +905 | 724,784 | 5.3% | 7.77B | 8 |
| 22 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,095 | +441 | 361,908 | 7.6% | 24.01B | 2 |
| 23 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 27,523 | -22 | 1,115,984 | 2.3% | 127.70B | 2 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 27,351 | +69 | 240,826 | 8.0% | — | 1 |
| 25 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,555 | +1 | 44,254 | 17.0% | 12.25B | 3 |
| 26 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,369 | +92 | 4,167,645 | 0.5% | 11.34B | 8 |
| 27 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,709 | -620 | 549,183 | 2.6% | 70.60B | 2 |
| 28 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,475 | +245 | 647,677 | 2.1% | 23.57B | 2 |
| 29 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,006 | +54 | 792,678 | 1.6% | 11.25B | 10 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,707 | +39 | 5,046,008 | 0.2% | 122.61B | 1 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,891 | -202 | 157,963 | 4.6% | 9.15B | 1 |
| 32 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,510 | -187 | 20,361 | 9.6% | 27.43B | 3 |
| 33 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,492 | +190 | 4,937,853 | 0.2% | 122.61B | 1 |
| 34 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,188 | +120 | 519,959 | 1.8% | 7.24B | 8 |
| 35 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,790 | +35 | 493,045 | 1.8% | 9.15B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,041 | -61 | 84,306 | 5.4% | — | 5 |
| 37 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 9,108 | +482 | 34,398 | 6.8% | 72.01B | 1 |
| 38 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,829 | +146 | 5,387,165 | 0.2% | 22.25B | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,512 | +292 | 601,966 | 1.2% | 22.64B | 1 |
| 40 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,161 | +15 | 76,334 | 4.6% | — | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,645 | +760 | 116,962 | 3.5% | 8.42B | 7 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 6,239 | -36 | 150,646 | 2.5% | 2.25B | 7 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,123 | +33 | 355,761 | 1.3% | 125.03B | 1 |
| 44 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,104 | -337 | 20,728 | 5.1% | 572.6M | 5 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,533 | +19 | 81,665 | 3.0% | 7.04B | 4 |
| 46 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,520 | -63 | 13,732 | 4.9% | 1.51B | 6 |
| 47 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,272 | -429 | 139,426 | 2.2% | 7.48B | 5 |
| 48 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,000 | +270 | 19,928 | 4.2% | 3.83B | 5 |
| 49 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,754 | +1 | 138,827 | 2.0% | 7.40B | 3 |
| 50 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,678 | +576 | 257,644 | 1.3% | 4.76B | 5 |
| 51 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,598 | +152 | 5,163,991 | 0.1% | 22.25B | 1 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,542 | +86 | 376,752 | 1.0% | 7.24B | 8 |
| 53 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,493 | +118 | 909,379 | 0.4% | 23.57B | 2 |
| 54 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,489 | +45 | 153,037 | 1.8% | 7.24B | 4 |
| 55 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,266 | -23 | 168,972 | 1.6% | 11.17B | 16 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,033 | +66 | 61,929 | 2.5% | 1.60B | 5 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,993 | +52 | 39,525 | 2.9% | 2.61B | 3 |
| 58 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,718 | +17 | 36,513 | 2.7% | 56.7M | 1 |
| 59 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,414 | +236 | 52,724 | 2.2% | 8.03B | 7 |
| 60 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,144 | +22 | 95,022 | 1.6% | 2.89B | 1 |
| 61 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,854 | +28 | 42,807 | 2.0% | 13.29B | 3 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,797 | +90 | 26,279 | 2.2% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,710 | +18 | 34,384 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,608 | +34 | 5,303,259 | 0.0% | 7.25B | 1 |
| 65 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,593 | +24 | 156,842 | 1.0% | 23.57B | 2 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,501 | +13 | 179,210 | 0.9% | 12.25B | 6 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,285 | +23 | 51,832 | 1.5% | 7.77B | 1 |
| 68 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,177 | +25 | 22,218 | 1.8% | 4.30B | 2 |
| 69 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,170 | +91 | 230,098 | 0.7% | 35.13B | 4 |
| 70 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,015 | -27 | 51,193 | 1.3% | 9.24B | 4 |
| 71 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,000 | +54 | 101,668 | 1.0% | 30.68B | 1 |
| 72 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,986 | +29 | 357,811 | 0.4% | — | 3 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,953 | +26 | 80,138 | 1.1% | 7.45B | 1 |
| 74 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,892 | +23 | 107,734 | 0.9% | 7.45B | 1 |
| 75 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,829 | +69 | 159,435 | 0.7% | 1.10B | 1 |
| 76 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,821 | -121 | 415,599 | 0.4% | 1.20B | 1 |
| 77 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,804 | +32 | 9,228 | 1.7% | 4.30B | 3 |
| 78 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,788 | +20 | 34,436 | 1.3% | 22.64B | 1 |
| 79 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,763 | +27 | 302,873 | 0.4% | 6.74B | 2 |
| 80 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,762 | +56 | 186,222 | 0.6% | 6.74B | 1 |
| 81 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,700 | +24 | 146,959 | 0.7% | 13.02B | 1 |
| 82 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,658 | +89 | 40,471 | 1.2% | 70.55B | 3 |
| 83 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,653 | +52 | 19,590 | 1.4% | 12.19B | 2 |
| 84 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,631 | -113 | 418,927 | 0.3% | 353.4M | 1 |
| 85 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,595 | -126 | 400,438 | 0.3% | 3.21B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,570 | +16 | 54,244 | 1.0% | 7.24B | 5 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,502 | +16 | 53,032 | 1.0% | 7.24B | 1 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,460 | +14 | 9,195 | 1.3% | 9.82B | 1 |
| 89 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,385 | +32 | 174,737 | 0.5% | 11.51B | 7 |
| 90 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,373 | +41 | 801,795 | 0.2% | — | 3 |
| 91 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,354 | +19 | 31,506 | 1.0% | 33.12B | 1 |
| 92 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,349 | -16 | 671,006 | 0.2% | 7.45B | 2 |
| 93 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,248 | -42 | 23,740 | 1.0% | 11.17B | 5 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,213 | +10 | 19,956 | 1.0% | 1.20B | 2 |
| 95 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,144 | +21 | 10,568 | 1.0% | 9.15B | 1 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,091 | +11 | 9,132 | 1.0% | 28.84B | 3 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,075 | +24 | 58,366 | 0.7% | 1.35B | 3 |
| 98 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,053 | -31 | 31,616 | 0.8% | 11.17B | 5 |
| 99 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,021 | +9 | 56,325 | 0.7% | 7.55B | 1 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,019 | -8 | 15,287 | 0.9% | 353.4M | 2 |
| 101 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 943 | +23 | 453,353 | 0.2% | 40.43B | 1 |
| 102 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 902 | +47 | 218,749 | 0.3% | 12.19B | 3 |
| 103 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 838 | +8 | 44,859 | 0.6% | 12.19B | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 781 | +23 | 112,123 | 0.4% | 7.29B | 2 |
| 105 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 749 | +94 | 233,389 | 0.2% | — | 2 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 714 | +2 | 14,540 | 0.6% | 4.33B | 3 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 701 | +6 | 82,027 | 0.4% | 8.03B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 646 | +19 | 96,315 | 0.3% | 1.35B | 8 |
| 109 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 646 | +9 | 16,795 | 0.6% | 1.54B | 4 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 619 | +5 | 20,666 | 0.5% | 3.20B | 2 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 577 | +21 | 22,026 | 0.5% | 9.24B | 2 |
| 112 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 526 | +40 | 27,778 | 0.4% | 9.24B | 2 |
| 113 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 522 | +17 | 3,512 | 0.5% | 30.68B | 1 |
| 114 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 498 | +1 | 1,732 | 0.5% | 27.23B | 3 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 486 | +12 | 4,283 | 0.5% | 8.03B | 3 |
| 116 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 445 | +23 | 1,579 | 0.4% | — | 1 |
| 117 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 375 | +12 | 12,119 | 0.3% | 27.23B | 2 |
| 118 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 364 | -3 | 2,816 | 0.4% | 4.02B | 2 |
| 119 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 356 | -18 | 32,858 | 0.3% | 40.43B | 2 |
| 120 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 338 | +2 | 22,089 | 0.3% | 2.61B | 2 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 331 | -6 | 5,527 | 0.3% | 11.51B | 5 |
| 122 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 309 | +167 | 12,322 | 0.3% | 31.59B | 6 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 308 | +2 | 107,219 | 0.1% | — | 3 |
| 124 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 304 | +12 | 39,392 | 0.2% | 7.48B | 2 |
| 125 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 293 | -21 | 84,566 | 0.2% | 9.15B | 1 |
| 126 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 287 | -3 | 322,228 | 0.1% | 7.24B | 2 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 281 | -3 | 37,805 | 0.2% | 27.23B | 3 |
| 128 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 271 | 0 | 5,153 | 0.3% | 437.8M | 1 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 236 | +7 | 41,890 | 0.2% | 11.17B | 1 |
| 130 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 230 | +1 | 19,676 | 0.2% | 68.98B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 223 | -7 | 44,647 | 0.2% | 7.70B | 5 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 217 | +26 | 70,496 | 0.1% | 8.03B | 3 |
| 133 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 215 | -1 | 12,704 | 0.2% | 70.55B | 2 |
| 134 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 212 | +1 | 5,051 | 0.2% | 70.55B | 3 |
| 135 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 203 | +12 | 16,618 | 0.2% | 7.29B | 2 |
| 136 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 190 | -1 | 2,545 | 0.2% | — | 1 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 175 | +1 | 5,498 | 0.2% | 353.4M | 2 |
| 138 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 158 | +8 | 28,404 | 0.1% | 46.70B | 6 |
| 139 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 155 | 0 | 3,138 | 0.2% | 560.9M | 2 |
| 140 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 151 | -31 | 7,461 | 0.1% | 31.59B | 6 |
| 141 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 138 | +3 | 1,149 | 0.1% | — | 1 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 6,171 | 0.1% | 12.25B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 101 | 0 | 7,252 | 0.1% | 1.20B | 2 |
| 144 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 95 | +2 | 38,714 | 0.1% | 70.55B | 3 |
| 145 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 74 | -4 | 1,313 | 0.1% | 560.9M | 1 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 45 | -1 | 400 | 0.0% | 437.8M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,854 | 0.0% | 31.59B | 6 |
| 148 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 39 | -41 | 432 | 0.0% | 321.0M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | +2 | 256 | 0.0% | 15.17B | 3 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 31 | -1 | 221 | 0.0% | 437.8M | 1 |
| 151 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 29 | +1 | 194 | 0.0% | 8.16B | 3 |
| 152 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | 0 | 133 | 0.0% | 7.24B | 1 |
| 153 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | -1 | 275 | 0.0% | 437.8M | 1 |
| 154 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | -2 | 158 | 0.0% | 437.8M | 1 |
| 155 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | +2 | 1,505 | 0.0% | 31.58B | 2 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,596,300 | 306,164,745 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 592,963 | 6,032,820 | 7 | 9.7% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 262,944 | 2,632,967 | 11 | 9.6% |
| 4 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 148,583 | 339,701 | 6 | 33.8% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 68,065 | 6,385,763 | 12 | 1.0% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 53,713 | 1,413,473 | 5 | 3.5% |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,379 | 398,515 | 10 | 6.1% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 21,685 | 562,202 | 13 | 3.3% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,867 | 1,444,736 | 11 | 1.0% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 12,327 | 445,508 | 6 | 2.3% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,696 | 368,950 | 14 | 2.5% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,172 | 201,001 | 3 | 2.7% |
| 13 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,161 | 76,334 | 1 | 4.6% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,533 | 81,665 | 1 | 3.0% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,291 | 492,616 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,194 | 858,878 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,829 | 698,980 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,754 | 138,827 | 1 | 2.0% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,749 | 660,684 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,660 | 1,162,079 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,584 | 105,630 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,721 | 154,681 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,460 | 9,195 | 1 | 1.3% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 511 | 24,142 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,822,497 | 59,528,435 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 409,774 | 4,656,506 | 5 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 194,195 | 941,248 | 10 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 144,524 | 211,510 | 13 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 43,890 | 724,784 | 21 |
| 6 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,555 | 44,254 | 25 |
| 7 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,369 | 4,167,645 | 26 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,510 | 20,361 | 32 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,161 | 76,334 | 40 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,645 | 116,962 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,533 | 81,665 | 45 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,754 | 138,827 | 49 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,542 | 376,752 | 52 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,489 | 153,037 | 54 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 3,718 | 36,513 | 58 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 3,414 | 52,724 | 59 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,000 | 101,668 | 71 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,986 | 357,811 | 72 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 1,953 | 80,138 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,829 | 159,435 | 75 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,460 | 9,195 | 88 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,373 | 801,795 | 90 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,075 | 58,366 | 97 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 309 | 12,322 | 122 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 33.8% | 148,583 | 339,701 | 4 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 9.7% | 592,963 | 6,032,820 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 9.6% | 262,944 | 2,632,967 | 3 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,379 | 398,515 | 7 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | 4.6% | 8,161 | 76,334 | 13 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.5% | 53,713 | 1,413,473 | 6 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 21,685 | 562,202 | 8 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,533 | 81,665 | 14 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.7% | 8,172 | 201,001 | 12 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,696 | 368,950 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.3% | 12,327 | 445,508 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,596,300 | 306,164,745 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.0% | 4,754 | 138,827 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.3% | 1,460 | 9,195 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,584 | 105,630 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.0% | 68,065 | 6,385,763 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 14,867 | 1,444,736 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,291 | 492,616 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,721 | 154,681 | 22 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,829 | 698,980 | 17 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,194 | 858,878 | 16 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,749 | 660,684 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 511 | 24,142 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,660 | 1,162,079 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
