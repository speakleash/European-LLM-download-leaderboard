# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-07
- **Generated at:** 2026-10-07T12:58:42Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,375,385 | -8,339 | 58,096,593 | 4.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,571,085 | -30,457 | 64,994,852 | 2.4% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 700,250 | +3,112 | 722,664 | 85.1% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 550,225 | -4,045 | 45,781,392 | 1.2% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 493,605 | +30 | 4,328,434 | 11.1% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 474,767 | -6,156 | 16,472,497 | 2.9% | 12.25B | 3 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 464,663 | -33,188 | 4,811,046 | 9.5% | 24.01B | 2 |
| 8 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 398,336 | -17,748 | 3,776,772 | 10.3% | 13.95B | 6 |
| 9 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 313,652 | -14,125 | 594,801 | 45.1% | 22.64B | 1 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 304,977 | -5,955 | 2,890,826 | 10.2% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 276,000 | +5,820 | 32,405,217 | 0.8% | 46.70B | 2 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,014 | +358 | 5,495,609 | 4.6% | 24.01B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 255,622 | -4,067 | 5,647,531 | 4.4% | 4.25B | 7 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 232,214 | +226 | 923,419 | 22.7% | 1.66B | 1 |
| 15 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 227,421 | +1,562 | 2,254,877 | 9.7% | 8.92B | 6 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 145,618 | -1,736 | 8,533,265 | 1.7% | 8.02B | 1 |
| 17 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 91,528 | -4,092 | 1,095,743 | 7.7% | 127.70B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 82,884 | +2,569 | 706,126 | 10.3% | 119.40B | 3 |
| 19 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 78,666 | -9,464 | 4,150,493 | 1.9% | 11.34B | 8 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,925 | -31 | 745,179 | 8.7% | 23.57B | 2 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,472 | +2,338 | 7,597,591 | 0.9% | 23.57B | 2 |
| 22 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 66,265 | +1 | 68,196 | 39.4% | — | 1 |
| 23 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 53,947 | +3,611 | 11,225,931 | 0.5% | 140.63B | 2 |
| 24 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 45,390 | -8,764 | 536,346 | 7.1% | 70.60B | 2 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,906 | +382 | 685,487 | 3.7% | 7.77B | 8 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,638 | -429 | 147,616 | 8.3% | 9.15B | 1 |
| 27 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,597 | +202 | 5,160,476 | 0.4% | 22.25B | 1 |
| 28 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,367 | +1,071 | 218,969 | 6.1% | — | 1 |
| 29 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,154 | -146 | 633,368 | 2.5% | 23.57B | 2 |
| 30 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 14,587 | -84 | 781,084 | 1.7% | 11.25B | 10 |
| 31 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,493 | -627 | 484,619 | 2.5% | 9.15B | 1 |
| 32 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,037 | +108 | 76,277 | 8.0% | — | 5 |
| 33 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 14,006 | +3,028 | 32,720 | 10.6% | 12.25B | 3 |
| 34 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 11,422 | +423 | 135,445 | 4.9% | 7.48B | 5 |
| 35 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 11,277 | -1,200 | 26,686 | 8.9% | 72.01B | 1 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,162 | +94 | 510,821 | 1.8% | 7.24B | 8 |
| 37 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,642 | +4 | 328,765 | 2.0% | 24.01B | 2 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,465 | +64 | 4,927,997 | 0.2% | 122.61B | 1 |
| 39 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,983 | -125 | 350,495 | 1.6% | 125.03B | 1 |
| 40 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,623 | +260 | 5,380,380 | 0.1% | 22.25B | 1 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,008 | +24 | 16,827 | 5.1% | 572.6M | 5 |
| 42 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,794 | +315 | 146,161 | 2.4% | 2.25B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,609 | -72 | 110,025 | 2.7% | 8.42B | 7 |
| 44 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,532 | -148 | 49,625 | 3.7% | 8.03B | 7 |
| 45 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,139 | +113 | 135,127 | 2.2% | 7.40B | 3 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,983 | +52 | 154,465 | 2.0% | 23.57B | 2 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,845 | +7 | 165,581 | 1.8% | 11.17B | 16 |
| 48 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,834 | +66 | 111,622 | 2.3% | 7.29B | 2 |
| 49 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,730 | +198 | 67,637 | 2.8% | 12.77B | 5 |
| 50 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,605 | +97 | 373,099 | 1.0% | 7.24B | 8 |
| 51 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,509 | +5 | 12,043 | 4.0% | 27.43B | 3 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,297 | -97 | 253,624 | 1.2% | 4.76B | 5 |
| 53 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,157 | +120 | 414,865 | 0.8% | 1.20B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,141 | +26 | 905,386 | 0.4% | 23.57B | 2 |
| 55 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,080 | +84 | 5,033,891 | 0.1% | 122.61B | 1 |
| 56 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 4,059 | -20 | 66,863 | 2.4% | 14.08B | 1 |
| 57 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,009 | -55 | 670,012 | 0.5% | 7.45B | 2 |
| 58 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,003 | +120 | 418,373 | 0.8% | 353.4M | 1 |
| 59 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,996 | +118 | 149,335 | 1.6% | 7.24B | 4 |
| 60 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,964 | +118 | 399,918 | 0.8% | 3.21B | 1 |
| 61 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,788 | -1,745 | 30,262 | 2.9% | 33.12B | 1 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,560 | -255 | 92,443 | 1.8% | 2.89B | 1 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,457 | +25 | 36,141 | 2.5% | 2.61B | 3 |
| 64 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,139 | +150 | 58,470 | 2.0% | 1.60B | 5 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,570 | +137 | 40,468 | 1.8% | 13.29B | 3 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,534 | +85 | 85,787 | 1.4% | 2.22B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,532 | +8 | 84,342 | 1.4% | 9.15B | 1 |
| 68 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,265 | +61 | 8,740 | 2.1% | 1.51B | 6 |
| 69 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,217 | -5 | 49,546 | 1.5% | 9.24B | 4 |
| 70 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,198 | +24 | 55,511 | 1.4% | 7.55B | 1 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,162 | +35 | 18,135 | 1.8% | 12.19B | 2 |
| 72 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,130 | +3 | 32,946 | 1.6% | 22.64B | 1 |
| 73 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,118 | +79 | 23,910 | 1.7% | 22.64B | 1 |
| 74 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,877 | +19 | 78,531 | 1.1% | 7.45B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,828 | +10 | 106,174 | 0.9% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,804 | +1 | 100,004 | 0.9% | 30.68B | 1 |
| 77 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,795 | +53 | 49,854 | 1.2% | 7.77B | 1 |
| 78 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,793 | -13 | 452,549 | 0.3% | 40.43B | 1 |
| 79 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,729 | +124 | 33,337 | 1.3% | 56.7M | 1 |
| 80 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,715 | +7 | 356,140 | 0.4% | — | 3 |
| 81 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,694 | -47 | 15,187 | 1.5% | 3.83B | 5 |
| 82 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,676 | +23 | 5,300,908 | 0.0% | 7.25B | 1 |
| 83 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,639 | +40 | 22,841 | 1.3% | 11.17B | 5 |
| 84 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,639 | +20 | 177,014 | 0.6% | 12.25B | 6 |
| 85 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,598 | +8 | 157,890 | 0.6% | 1.10B | 1 |
| 86 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,565 | -12 | 31,769 | 1.2% | 14.03B | 1 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,550 | +7 | 301,394 | 0.4% | 6.74B | 2 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,522 | +14 | 7,881 | 1.4% | 9.82B | 1 |
| 89 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,500 | +24 | 184,749 | 0.5% | 6.74B | 1 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,496 | +10 | 145,536 | 0.6% | 13.02B | 1 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,423 | -15 | 20,396 | 1.2% | 4.30B | 2 |
| 92 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,347 | +29 | 30,807 | 1.0% | 11.17B | 5 |
| 93 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,342 | +56 | 52,950 | 0.9% | 7.24B | 5 |
| 94 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,291 | +6 | 12,023 | 1.2% | 31.59B | 6 |
| 95 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,282 | -6 | 173,553 | 0.5% | 11.51B | 7 |
| 96 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,246 | +53 | 51,786 | 0.8% | 7.24B | 1 |
| 97 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,161 | +18 | 228,204 | 0.4% | 35.13B | 4 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,158 | +27 | 57,534 | 0.7% | 1.35B | 3 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,090 | +16 | 800,608 | 0.1% | — | 3 |
| 100 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,044 | +48 | 7,811 | 1.0% | 4.30B | 3 |
| 101 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 982 | -34 | 18,847 | 0.8% | 1.20B | 2 |
| 102 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 980 | +5 | 8,125 | 0.9% | 28.84B | 3 |
| 103 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 913 | -20 | 9,550 | 0.8% | 9.15B | 1 |
| 104 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 898 | -13 | 14,396 | 0.8% | 353.4M | 2 |
| 105 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 866 | +10 | 38,979 | 0.6% | 70.55B | 3 |
| 106 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 864 | 0 | 2,828 | 0.8% | 31.59B | 6 |
| 107 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 802 | +20 | 16,244 | 0.7% | 1.54B | 4 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 737 | -5 | 20,190 | 0.6% | 3.20B | 2 |
| 109 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 701 | -40 | 95,762 | 0.4% | 1.35B | 8 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 671 | +9 | 44,109 | 0.5% | 12.19B | 2 |
| 111 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 622 | +12 | 81,440 | 0.3% | 8.03B | 3 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 550 | -9 | 217,904 | 0.2% | 12.19B | 3 |
| 113 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 538 | +19 | 76,230 | 0.3% | 7.04B | 4 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 518 | -4 | 232,738 | 0.2% | — | 2 |
| 115 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 514 | -8 | 3,858 | 0.5% | 8.03B | 3 |
| 116 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 483 | +2 | 1,499 | 0.5% | 31.58B | 2 |
| 117 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 470 | -7 | 3,010 | 0.5% | 560.9M | 2 |
| 118 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 461 | +8 | 27,320 | 0.4% | 9.24B | 2 |
| 119 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | -3 | 21,832 | 0.4% | 2.61B | 2 |
| 120 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 459 | -9 | 13,921 | 0.4% | 4.33B | 3 |
| 121 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 458 | -7 | 32,575 | 0.3% | 40.43B | 2 |
| 122 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 427 | +10 | 322,047 | 0.1% | 7.24B | 2 |
| 123 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 423 | +2 | 39,169 | 0.3% | 7.48B | 2 |
| 124 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 389 | -6 | 12,532 | 0.3% | 70.55B | 2 |
| 125 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 386 | +23 | 3,083 | 0.4% | 30.68B | 1 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 377 | -2 | 11,796 | 0.3% | 27.23B | 2 |
| 127 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 372 | -6 | 7,364 | 0.3% | 31.59B | 6 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 371 | +12 | 37,595 | 0.3% | 27.23B | 3 |
| 129 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 345 | +9 | 1,205 | 0.3% | — | 1 |
| 130 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 313 | -8 | 21,531 | 0.3% | 9.24B | 2 |
| 131 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 313 | -2 | 44,465 | 0.2% | 7.70B | 5 |
| 132 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 305 | +6 | 106,978 | 0.1% | — | 3 |
| 133 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 283 | -9 | 70,300 | 0.2% | 8.03B | 3 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 274 | -35 | 41,677 | 0.2% | 11.17B | 1 |
| 135 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 255 | +3 | 19,494 | 0.2% | 68.98B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 250 | -14 | 16,454 | 0.2% | 7.29B | 2 |
| 137 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 234 | -16 | 2,526 | 0.2% | 4.02B | 2 |
| 138 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 222 | +9 | 5,250 | 0.2% | 11.51B | 5 |
| 139 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 210 | +2 | 2,397 | 0.2% | — | 1 |
| 140 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 209 | -4 | 1,242 | 0.2% | 27.23B | 3 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 182 | -6 | 5,359 | 0.2% | 353.4M | 2 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 174 | -8 | 38,632 | 0.1% | 70.55B | 3 |
| 143 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 174 | +4 | 4,886 | 0.2% | 70.55B | 3 |
| 144 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 173 | -20 | 4,991 | 0.2% | 437.8M | 1 |
| 145 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 137 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | -3 | 28,266 | 0.1% | 46.70B | 6 |
| 147 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 130 | -5 | 7,177 | 0.1% | 1.20B | 2 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 129 | +2 | 1,026 | 0.1% | — | 1 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 87 | +2 | 399 | 0.1% | 321.0M | 1 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 66 | -6 | 1,247 | 0.1% | 560.9M | 1 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 45 | -14 | 200 | 0.0% | 437.8M | 1 |
| 152 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | +1 | 227 | 0.0% | 15.17B | 3 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | +1 | 148 | 0.0% | 437.8M | 1 |
| 154 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 26 | +2 | 171 | 0.0% | 8.16B | 3 |
| 155 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 22 | -1 | 261 | 0.0% | 437.8M | 1 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 117 | 0.0% | 7.24B | 1 |
| 157 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | 0 | 359 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,769,724 | 300,785,686 | 30 | 2.6% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,260,489 | 5,654,884 | 7 | 21.9% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 611,724 | 2,558,710 | 11 | 23.0% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 132,882 | 6,329,646 | 12 | 2.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 66,265 | 68,196 | 1 | 39.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,746 | 1,366,626 | 5 | 2.6% |
| 7 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 19,324 | 1,434,579 | 11 | 1.3% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 18,496 | 382,186 | 10 | 3.8% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 17,448 | 545,188 | 13 | 2.7% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 15,110 | 434,350 | 6 | 2.8% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,215 | 359,381 | 14 | 2.4% |
| 12 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,066 | 192,454 | 6 | 3.1% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,714 | 854,717 | 3 | 0.8% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,593 | 152,650 | 2 | 2.6% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,345 | 193,659 | 3 | 2.2% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,139 | 135,127 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,032 | 695,146 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,594 | 488,175 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,265 | 657,534 | 2 | 0.4% |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,010 | 23,714 | 4 | 2.4% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,247 | 103,485 | 4 | 1.1% |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,168 | 1,159,818 | 4 | 0.2% |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,859 | 153,296 | 2 | 0.7% |
| 24 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,522 | 7,881 | 1 | 1.4% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 538 | 76,230 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,375,385 | 58,096,593 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 700,250 | 722,664 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 313,652 | 594,801 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 78,666 | 4,150,493 | 19 |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 66,265 | 68,196 | 22 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,906 | 685,487 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 14,006 | 32,720 | 33 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,609 | 110,025 | 43 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,532 | 49,625 | 44 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,139 | 135,127 | 45 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 4,834 | 111,622 | 48 |
| 12 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,730 | 67,637 | 49 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,605 | 373,099 | 50 |
| 14 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 4,157 | 414,865 | 53 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 4,059 | 66,863 | 56 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,009 | 670,012 | 57 |
| 17 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 3,996 | 149,335 | 59 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,804 | 100,004 | 76 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,715 | 356,140 | 80 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,598 | 157,890 | 85 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,522 | 7,881 | 88 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,291 | 12,023 | 94 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,158 | 57,534 | 98 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,090 | 800,608 | 99 |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 538 | 76,230 | 113 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 39.4% | 66,265 | 68,196 | 5 |
| 2 | [utter-project](https://huggingface.co/utter-project) | 23.0% | 611,724 | 2,558,710 | 3 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 21.9% | 1,260,489 | 5,654,884 | 2 |
| 4 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 3.8% | 18,496 | 382,186 | 8 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.1% | 9,066 | 192,454 | 12 |
| 6 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.8% | 15,110 | 434,350 | 10 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.7% | 17,448 | 545,188 | 9 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,746 | 1,366,626 | 6 |
| 9 | [Almawave](https://huggingface.co/Almawave) | 2.6% | 6,593 | 152,650 | 14 |
| 10 | [mistralai](https://huggingface.co/mistralai) | 2.6% | 7,769,724 | 300,785,686 | 1 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,215 | 359,381 | 11 |
| 12 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.4% | 3,010 | 23,714 | 20 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,139 | 135,127 | 16 |
| 14 | [ilsp](https://huggingface.co/ilsp) | 2.2% | 6,345 | 193,659 | 15 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 2.1% | 132,882 | 6,329,646 | 4 |
| 16 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,522 | 7,881 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.3% | 19,324 | 1,434,579 | 7 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,247 | 103,485 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.8% | 7,714 | 854,717 | 13 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,594 | 488,175 | 18 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,859 | 153,296 | 23 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,032 | 695,146 | 17 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,265 | 657,534 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 538 | 76,230 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,168 | 1,159,818 | 22 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
