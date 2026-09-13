# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-13
- **Generated at:** 2026-09-13T11:25:11Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,500,355 | -4,675 | 56,118,739 | 4.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,552,326 | +43,088 | 63,703,195 | 2.4% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 614,607 | +2,791 | 3,500,285 | 17.1% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 518,443 | +4,889 | 45,410,105 | 1.1% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 514,553 | -11,479 | 16,126,998 | 3.2% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 503,622 | -2,900 | 3,918,833 | 12.5% | 8.05B | 2 |
| 7 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 408,881 | -22,279 | 5,451,548 | 7.4% | 4.25B | 7 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 392,506 | +20,723 | 4,518,136 | 8.5% | 24.01B | 2 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,378 | -216 | 415,056 | 68.6% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,030 | -212 | 411,590 | 68.6% | 1.20B | 1 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,699 | -217 | 396,638 | 68.6% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303,529 | -4,490 | 32,183,653 | 0.9% | 46.70B | 2 |
| 13 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 255,589 | +2,459 | 4,124,166 | 6.1% | 11.34B | 8 |
| 14 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,039 | +284 | 2,643,380 | 9.2% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 206,671 | +3,603 | 8,419,662 | 2.4% | 8.02B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 204,009 | +1,804 | 2,063,942 | 9.4% | 8.92B | 6 |
| 17 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 159,749 | +13,216 | 355,044 | 35.1% | 22.64B | 1 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140,940 | -3,722 | 1,030,166 | 12.5% | 127.70B | 2 |
| 19 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 127,807 | -2,796 | 5,262,090 | 2.4% | 24.01B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 99,987 | -200 | 518,375 | 16.2% | 70.60B | 2 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 75,780 | -625 | 683,770 | 9.7% | 23.57B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,470 | +469 | 621,054 | 9.8% | 23.57B | 2 |
| 23 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,372 | -281 | 7,543,104 | 0.9% | 23.57B | 2 |
| 24 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,259 | -97 | 631,816 | 7.8% | 119.40B | 3 |
| 25 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 37,309 | -2,131 | 11,182,715 | 0.3% | 140.63B | 2 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 29,615 | -2,067 | 131,197 | 12.8% | 9.15B | 1 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 29,568 | -615 | 662,967 | 3.9% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,255 | +369 | 473,565 | 3.5% | 9.15B | 1 |
| 29 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,104 | +770 | 322,471 | 4.0% | 24.01B | 2 |
| 30 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,074 | -586 | 345,574 | 3.8% | 125.03B | 1 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,985 | +55 | 769,426 | 1.8% | 11.25B | 10 |
| 32 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,539 | +79 | 27,352 | 12.2% | 8.90B | 1 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,318 | +251 | 20,909 | 12.7% | 72.01B | 1 |
| 34 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,372 | -243 | 694,788 | 1.8% | 1.66B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,781 | -2 | 5,299,413 | 0.3% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,217 | -2 | 64,856 | 7.4% | — | 5 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,763 | +170 | 204,299 | 3.5% | — | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,342 | -159 | 501,587 | 1.6% | 7.24B | 8 |
| 39 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,170 | -635 | 4,920,398 | 0.2% | 122.61B | 1 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,268 | -2,706 | 105,488 | 3.1% | 8.42B | 5 |
| 41 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,440 | +3,093 | 127,491 | 2.4% | 7.48B | 5 |
| 42 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,849 | -82 | 5,141,454 | 0.1% | 22.25B | 1 |
| 43 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,846 | -90 | 161,623 | 1.9% | 11.17B | 16 |
| 44 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,467 | +37 | 63,306 | 2.7% | 11.77B | 4 |
| 45 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,397 | +21 | 45,164 | 3.0% | 8.03B | 7 |
| 46 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,327 | -138 | 28,522 | 3.4% | 33.12B | 1 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,268 | -163 | 141,225 | 1.8% | 2.25B | 7 |
| 48 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,185 | +8 | 89,826 | 2.2% | 2.89B | 1 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,053 | -109 | 666,662 | 0.5% | 7.45B | 2 |
| 50 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,986 | -1,158 | 30,827 | 3.0% | 14.03B | 1 |
| 51 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,836 | +281 | 901,911 | 0.4% | 23.57B | 2 |
| 52 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,594 | -15 | 5,374,414 | 0.1% | 22.25B | 1 |
| 53 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,572 | +29 | 54,052 | 2.3% | 7.55B | 1 |
| 54 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,567 | -38 | 55,887 | 2.3% | 1.60B | 5 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,507 | +83 | 250,499 | 1.0% | 4.76B | 5 |
| 56 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,274 | -207 | 130,587 | 1.4% | 7.40B | 3 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,252 | +44 | 369,142 | 0.7% | 7.24B | 8 |
| 58 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,010 | +3 | 11,043 | 2.7% | 572.6M | 5 |
| 59 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,544 | -128 | 5,030,263 | 0.0% | 122.61B | 1 |
| 60 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,427 | -7 | 22,099 | 2.0% | 22.64B | 1 |
| 61 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,419 | -5 | 38,593 | 1.7% | 321.0M | 2 |
| 62 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,293 | -5 | 107,414 | 1.1% | 7.29B | 2 |
| 63 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,244 | +11 | 145,769 | 0.9% | 7.24B | 4 |
| 64 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,193 | +32 | 19,334 | 1.8% | 4.30B | 2 |
| 65 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,998 | +9 | 33,286 | 1.5% | 2.61B | 3 |
| 66 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,882 | -12 | 13,755 | 1.7% | 3.83B | 5 |
| 67 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,854 | +81 | 16,246 | 1.6% | 12.19B | 2 |
| 68 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,854 | -51 | 6,901 | 1.7% | 4.30B | 3 |
| 69 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,822 | -7 | 63,547 | 1.1% | 14.08B | 1 |
| 70 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,679 | -111 | 8,818 | 1.5% | 9.15B | 1 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,624 | +27 | 31,597 | 1.2% | 22.64B | 1 |
| 72 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,595 | +22 | 6,660 | 1.5% | 1.51B | 6 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,558 | -3 | 76,975 | 0.9% | 7.45B | 1 |
| 74 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,479 | -14 | 172,528 | 0.5% | 11.51B | 7 |
| 75 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,471 | +25 | 7,354 | 1.4% | 28.84B | 3 |
| 76 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,405 | -104 | 18,853 | 1.2% | 12.25B | 3 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,369 | +1 | 175,642 | 0.5% | 12.25B | 6 |
| 78 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,308 | -13 | 21,520 | 1.1% | 11.17B | 5 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,257 | +3 | 98,498 | 0.6% | 30.68B | 1 |
| 80 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,211 | -13 | 47,616 | 0.8% | 9.24B | 4 |
| 81 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,198 | -47 | 29,738 | 0.9% | 11.17B | 5 |
| 82 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,192 | +75 | 43,628 | 0.8% | 12.19B | 2 |
| 83 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,185 | -5 | 104,640 | 0.6% | 7.45B | 1 |
| 84 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,139 | +9 | 31,908 | 0.9% | 56.7M | 1 |
| 85 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,124 | +8 | 354,712 | 0.2% | — | 3 |
| 86 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,098 | -25 | 95,175 | 0.6% | 1.35B | 8 |
| 87 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,040 | +4 | 300,106 | 0.3% | 6.74B | 2 |
| 88 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,035 | -1 | 156,547 | 0.4% | 1.10B | 1 |
| 89 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,031 | +7 | 80,908 | 0.6% | 8.03B | 3 |
| 90 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,009 | -15 | 7,812 | 0.9% | 27.43B | 3 |
| 91 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,002 | +9 | 217,528 | 0.3% | 12.19B | 3 |
| 92 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,002 | +17 | 56,558 | 0.6% | 1.35B | 3 |
| 93 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,002 | +36 | 12,299 | 0.9% | 70.55B | 2 |
| 94 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 973 | +6 | 799,671 | 0.1% | — | 3 |
| 95 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 969 | 0 | 144,296 | 0.4% | 13.02B | 1 |
| 96 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 962 | +1 | 183,498 | 0.3% | 6.74B | 1 |
| 97 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 938 | -113 | 37,312 | 0.7% | 27.23B | 3 |
| 98 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 927 | -1 | 48,175 | 0.6% | 7.77B | 1 |
| 99 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 926 | -15 | 38,245 | 0.7% | 70.55B | 3 |
| 100 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 900 | +46 | 83,518 | 0.5% | 2.22B | 1 |
| 101 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 839 | -54 | 81,891 | 0.5% | 9.15B | 1 |
| 102 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 807 | -192 | 2,747 | 0.8% | 30.68B | 1 |
| 103 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 789 | +10 | 227,196 | 0.2% | 35.13B | 4 |
| 104 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 767 | +7 | 1,071 | 0.8% | 27.23B | 3 |
| 105 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 710 | -17 | 70,045 | 0.4% | 8.03B | 3 |
| 106 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 690 | +24 | 6,617 | 0.6% | 9.82B | 1 |
| 107 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 650 | +4 | 450,882 | 0.1% | 40.43B | 1 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 616 | -11 | 13,515 | 0.5% | 4.33B | 3 |
| 109 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 608 | +18 | 149,620 | 0.2% | 23.57B | 2 |
| 110 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 594 | -12 | 321,679 | 0.1% | 7.24B | 2 |
| 111 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 581 | +7 | 3,389 | 0.6% | 8.03B | 3 |
| 112 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 574 | -1 | 17,955 | 0.5% | 1.20B | 2 |
| 113 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 536 | -20 | 11,100 | 0.5% | 31.59B | 6 |
| 114 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 524 | +9 | 13,586 | 0.5% | 353.4M | 2 |
| 115 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 519 | 0 | 1,249 | 0.5% | 31.58B | 2 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 512 | -2 | 32,194 | 0.4% | 40.43B | 2 |
| 117 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 453 | +10 | 51,701 | 0.3% | 7.24B | 5 |
| 118 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 432 | +27 | 19,532 | 0.4% | 3.20B | 2 |
| 119 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 422 | 0 | 44,228 | 0.3% | 7.70B | 5 |
| 120 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 405 | -10 | 1,981 | 0.4% | 31.59B | 6 |
| 121 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 404 | 0 | 232,277 | 0.1% | — | 2 |
| 122 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | +7 | 50,623 | 0.3% | 7.24B | 1 |
| 123 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 393 | -28 | 7,018 | 0.4% | 31.59B | 6 |
| 124 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 392 | -3 | 2,634 | 0.4% | 560.9M | 2 |
| 125 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 391 | -1 | 106,721 | 0.2% | — | 3 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 388 | +3 | 38,799 | 0.3% | 7.48B | 2 |
| 127 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 378 | +10 | 15,522 | 0.3% | 1.54B | 4 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 353 | +7 | 75,754 | 0.2% | 7.04B | 4 |
| 129 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 351 | -3 | 2,325 | 0.3% | 4.02B | 2 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 306 | -4 | 4,850 | 0.3% | 437.8M | 1 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 275 | +2 | 26,898 | 0.2% | 9.24B | 2 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 271 | +5 | 41,444 | 0.2% | 11.17B | 1 |
| 133 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 222 | +3 | 21,243 | 0.2% | 9.24B | 2 |
| 134 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 197 | +6 | 21,418 | 0.2% | 2.61B | 2 |
| 135 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 191 | -2 | 894 | 0.2% | — | 1 |
| 136 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 183 | -4 | 5,218 | 0.2% | 353.4M | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 182 | +19 | 16,258 | 0.2% | 7.29B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 163 | +6 | 19,289 | 0.1% | 68.98B | 2 |
| 139 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 159 | +5 | 11,441 | 0.1% | 27.23B | 2 |
| 140 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 159 | -32 | 1,938 | 0.2% | — | 1 |
| 141 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 155 | -3 | 5,043 | 0.1% | 11.51B | 5 |
| 142 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | +5 | 38,493 | 0.1% | 70.55B | 3 |
| 143 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 132 | 0 | 7,081 | 0.1% | 1.20B | 2 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 127 | 0 | 1,220 | 0.1% | 560.9M | 1 |
| 145 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 123 | +7 | 2,216 | 0.1% | — | 1 |
| 146 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 102 | +12 | 4,751 | 0.1% | 70.55B | 3 |
| 147 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 95 | +1 | 175 | 0.1% | 437.8M | 1 |
| 148 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 90 | +4 | 28,150 | 0.1% | 46.70B | 6 |
| 149 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | +4 | 6,035 | 0.1% | 12.25B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62 | +1 | 901 | 0.1% | — | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | +3 | 248 | 0.1% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 44 | +1 | 319 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | +1 | 132 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 16 | 0 | 346 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 12 | +2 | 103 | 0.0% | 7.24B | 1 |
| 156 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 12 | -1 | 145 | 0.0% | 8.16B | 3 |
| 157 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 9 | 0 | 196 | 0.0% | 15.17B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,127,886 | 294,646,527 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,051,153 | 1,418,852 | 11 | 69.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 640,953 | 4,516,927 | 7 | 13.9% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 302,687 | 6,260,952 | 12 | 4.8% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 243,444 | 2,038,800 | 11 | 11.4% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 35,925 | 1,335,443 | 5 | 2.5% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,997 | 424,006 | 6 | 3.4% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,665 | 530,089 | 13 | 2.0% |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,652 | 349,960 | 14 | 1.9% |
| 10 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,193 | 184,359 | 6 | 2.9% |
| 11 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,325 | 364,558 | 10 | 1.6% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,078 | 188,515 | 3 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,796 | 848,277 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,846 | 690,821 | 2 | 0.5% |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,274 | 130,587 | 1 | 1.4% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,966 | 484,341 | 3 | 0.5% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,722 | 147,065 | 2 | 1.1% |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,164 | 654,818 | 2 | 0.3% |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,100 | 151,733 | 2 | 0.8% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,085 | 101,586 | 4 | 1.0% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,931 | 1,157,958 | 4 | 0.2% |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 1,853 | 21,348 | 4 | 1.5% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 690 | 6,617 | 1 | 0.6% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 353 | 75,754 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 159 | 1,938 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,500,355 | 56,118,739 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 503,622 | 3,918,833 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,378 | 415,056 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 255,589 | 4,124,166 | 13 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 159,749 | 355,044 | 17 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 29,568 | 662,967 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,268 | 105,488 | 40 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,467 | 63,306 | 44 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,397 | 45,164 | 45 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,185 | 89,826 | 48 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,053 | 666,662 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,274 | 130,587 | 56 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,252 | 369,142 | 57 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 2,293 | 107,414 | 62 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 4B (2512) | 1,854 | 6,901 | 68 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 1,822 | 63,547 | 69 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,257 | 98,498 | 79 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,124 | 354,712 | 85 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,098 | 95,175 | 86 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,035 | 156,547 | 88 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 973 | 799,671 | 94 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 690 | 6,617 | 106 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 536 | 11,100 | 113 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 353 | 75,754 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 159 | 1,938 | 140 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.2% | 1,051,153 | 1,418,852 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 13.9% | 640,953 | 4,516,927 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 11.4% | 243,444 | 2,038,800 | 5 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.8% | 302,687 | 6,260,952 | 4 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.4% | 17,997 | 424,006 | 7 |
| 6 | [cjvt](https://huggingface.co/cjvt) | 2.9% | 8,193 | 184,359 | 10 |
| 7 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,127,886 | 294,646,527 | 1 |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.5% | 35,925 | 1,335,443 | 6 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,078 | 188,515 | 12 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,665 | 530,089 | 8 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,652 | 349,960 | 9 |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.6% | 7,325 | 364,558 | 11 |
| 13 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1.5% | 1,853 | 21,348 | 22 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.4% | 3,274 | 130,587 | 15 |
| 15 | [Almawave](https://huggingface.co/Almawave) | 1.1% | 2,722 | 147,065 | 17 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.0% | 2,085 | 101,586 | 20 |
| 17 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,100 | 151,733 | 19 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,796 | 848,277 | 13 |
| 19 | [domyn](https://huggingface.co/domyn) | 0.6% | 690 | 6,617 | 23 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,966 | 484,341 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,846 | 690,821 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,164 | 654,818 | 18 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 353 | 75,754 | 24 |
| 24 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 159 | 1,938 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,931 | 1,157,958 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
