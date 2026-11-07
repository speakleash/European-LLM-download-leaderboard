# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-07
- **Generated at:** 2026-11-07T12:43:06Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,912,262 | +40,215 | 60,128,124 | 3.2% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,560,501 | -29,829 | 66,682,019 | 2.3% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 602,667 | +15,258 | 4,393,839 | 13.4% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 519,660 | -78,784 | 46,419,684 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 335,297 | -9,866 | 4,688,201 | 7.0% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 333,025 | +5,520 | 32,752,443 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 253,420 | +11,600 | 2,517,876 | 9.7% | 8.92B | 6 |
| 8 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 209,868 | +9,300 | 277,786 | 55.6% | 12.77B | 5 |
| 9 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 207,176 | +5,407 | 5,866,788 | 3.5% | 3.85B | 7 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 170,524 | -1,480 | 4,999,412 | 3.3% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 160,508 | -2,853 | 16,649,705 | 1.0% | 12.25B | 3 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 109,246 | -1,018 | 5,613,973 | 1.9% | 24.01B | 1 |
| 13 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 108,467 | +1,396 | 7,711,682 | 1.4% | 23.57B | 2 |
| 14 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,537 | -4,817 | 3,007,592 | 3.4% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 60,937 | +4,109 | 8,596,980 | 0.7% | 8.02B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,422 | -1,451 | 806,288 | 6.3% | 23.57B | 2 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,255 | -197 | 11,283,701 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,560 | -612 | 734,145 | 5.5% | 7.77B | 8 |
| 19 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 36,580 | +6,943 | 4,187,954 | 0.9% | 11.34B | 8 |
| 20 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,768 | -17 | 742,093 | 4.0% | 119.40B | 3 |
| 21 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,649 | +135 | 365,139 | 7.0% | 24.01B | 2 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 25,137 | +694 | 244,859 | 7.3% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,184 | -158 | 944,676 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,507 | -2,168 | 1,119,120 | 1.4% | 127.70B | 2 |
| 25 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,388 | +148 | 798,179 | 1.8% | 11.25B | 10 |
| 26 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,011 | +81 | 649,703 | 2.1% | 23.57B | 2 |
| 27 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,685 | -714 | 739,799 | 1.9% | 8.90B | 1 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,999 | +312 | 4,942,782 | 0.3% | 122.61B | 1 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 12,804 | -485 | 550,493 | 2.0% | 70.60B | 2 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,765 | +62 | 5,046,802 | 0.2% | 122.61B | 1 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,531 | 0 | 159,647 | 4.4% | 9.15B | 1 |
| 32 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,238 | +62 | 522,721 | 1.8% | 7.24B | 8 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,883 | -58 | 496,106 | 1.8% | 9.15B | 1 |
| 34 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,829 | -71 | 86,006 | 4.7% | — | 5 |
| 35 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,785 | +98 | 5,389,608 | 0.2% | 22.25B | 1 |
| 36 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,495 | +50 | 76,755 | 4.8% | — | 1 |
| 37 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,452 | -49 | 20,607 | 7.0% | 27.43B | 3 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,263 | -57 | 35,078 | 6.1% | 72.01B | 1 |
| 39 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,178 | -366 | 603,663 | 1.2% | 22.64B | 1 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,060 | -50 | 118,406 | 3.7% | 8.42B | 7 |
| 41 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 7,214 | -1,957 | 44,624 | 5.0% | 12.25B | 3 |
| 42 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,684 | +31 | 15,862 | 5.8% | 1.51B | 6 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,575 | +55 | 357,433 | 1.4% | 125.03B | 1 |
| 44 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,751 | +50 | 259,600 | 1.6% | 4.76B | 5 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,595 | +18 | 81,914 | 3.1% | 7.04B | 4 |
| 46 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,567 | +30 | 20,995 | 4.6% | 3.83B | 5 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,145 | -111 | 151,779 | 2.0% | 2.25B | 7 |
| 48 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,042 | +986 | 54,830 | 3.3% | 8.03B | 7 |
| 49 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,781 | +101 | 21,865 | 3.9% | 572.6M | 5 |
| 50 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,657 | +56 | 910,197 | 0.5% | 23.57B | 2 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,551 | +34 | 154,150 | 1.8% | 7.24B | 4 |
| 52 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,542 | 0 | 139,917 | 1.9% | 7.40B | 3 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,409 | -6 | 63,105 | 2.7% | 1.60B | 5 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,407 | +30 | 377,769 | 0.9% | 7.24B | 8 |
| 55 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,385 | -107 | 140,515 | 1.8% | 7.48B | 5 |
| 56 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,229 | -114 | 5,165,143 | 0.1% | 22.25B | 1 |
| 57 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,226 | +56 | 37,740 | 3.1% | 56.7M | 1 |
| 58 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,176 | +60 | 40,483 | 3.0% | 2.61B | 3 |
| 59 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,796 | +1 | 44,379 | 2.6% | 13.29B | 3 |
| 60 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,548 | -99 | 169,529 | 1.3% | 11.17B | 16 |
| 61 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,397 | +353 | 27,479 | 2.7% | 22.64B | 1 |
| 62 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,327 | +26 | 95,933 | 1.7% | 2.89B | 1 |
| 63 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,780 | +914 | 12,381 | 2.5% | 9.15B | 1 |
| 64 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,758 | +9 | 34,555 | 2.0% | 14.03B | 1 |
| 65 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,687 | -5 | 5,303,681 | 0.0% | 7.25B | 1 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,581 | +38 | 179,683 | 0.9% | 12.25B | 6 |
| 67 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,537 | +27 | 157,060 | 1.0% | 23.57B | 2 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,388 | +9 | 230,659 | 0.7% | 35.13B | 4 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,340 | -51 | 52,315 | 1.5% | 7.77B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,215 | +376 | 20,432 | 1.8% | 12.19B | 2 |
| 71 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,195 | +38 | 22,633 | 1.8% | 4.30B | 2 |
| 72 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,086 | +19 | 102,200 | 1.0% | 30.68B | 1 |
| 73 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,064 | +20 | 358,316 | 0.5% | — | 3 |
| 74 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,028 | -1 | 51,688 | 1.3% | 9.24B | 4 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,015 | +14 | 80,660 | 1.1% | 7.45B | 1 |
| 76 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,945 | +30 | 159,949 | 0.7% | 1.10B | 1 |
| 77 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,930 | +20 | 108,201 | 0.9% | 7.45B | 1 |
| 78 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,853 | +29 | 303,344 | 0.5% | 6.74B | 2 |
| 79 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,848 | +24 | 34,895 | 1.4% | 22.64B | 1 |
| 80 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,842 | +14 | 186,689 | 0.6% | 6.74B | 1 |
| 81 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,802 | +6 | 40,905 | 1.3% | 70.55B | 3 |
| 82 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,775 | +26 | 147,408 | 0.7% | 13.02B | 1 |
| 83 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,773 | +563 | 86,167 | 1.0% | 9.15B | 1 |
| 84 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,646 | +15 | 9,522 | 1.5% | 4.30B | 3 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,645 | +37 | 9,580 | 1.5% | 9.82B | 1 |
| 86 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,636 | -42 | 20,673 | 1.4% | 1.20B | 2 |
| 87 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,589 | +11 | 54,633 | 1.0% | 7.24B | 5 |
| 88 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,522 | +9 | 53,401 | 1.0% | 7.24B | 1 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,509 | +21 | 802,181 | 0.2% | — | 3 |
| 90 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,450 | -1 | 31,743 | 1.1% | 33.12B | 1 |
| 91 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,433 | +21 | 15,925 | 1.2% | 353.4M | 2 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,301 | -130 | 175,039 | 0.5% | 11.51B | 7 |
| 93 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,218 | -1 | 219,150 | 0.4% | 12.19B | 3 |
| 94 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,175 | +5 | 56,742 | 0.7% | 7.55B | 1 |
| 95 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,115 | +19 | 9,266 | 1.0% | 28.84B | 3 |
| 96 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,104 | -24 | 671,231 | 0.1% | 7.45B | 2 |
| 97 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,053 | -10 | 23,948 | 0.8% | 11.17B | 5 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,027 | -7 | 58,605 | 0.6% | 1.35B | 3 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 993 | +15 | 453,596 | 0.2% | 40.43B | 1 |
| 100 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 944 | +31 | 415,956 | 0.2% | 1.20B | 1 |
| 101 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 906 | +14 | 45,029 | 0.6% | 12.19B | 2 |
| 102 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 902 | -22 | 31,760 | 0.7% | 11.17B | 5 |
| 103 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 854 | +108 | 419,360 | 0.2% | 353.4M | 1 |
| 104 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 833 | -5 | 233,598 | 0.2% | — | 2 |
| 105 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 825 | +5 | 112,470 | 0.4% | 7.29B | 2 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 820 | +50 | 2,064 | 0.8% | 27.23B | 3 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 788 | -1 | 14,721 | 0.7% | 4.33B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 776 | +25 | 96,552 | 0.4% | 1.35B | 8 |
| 109 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 755 | +31 | 400,812 | 0.2% | 3.21B | 1 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 702 | +1 | 82,184 | 0.4% | 8.03B | 3 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 679 | +16 | 16,950 | 0.6% | 1.54B | 4 |
| 112 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 624 | +9 | 22,165 | 0.5% | 9.24B | 2 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 600 | -4 | 27,976 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 575 | -2 | 20,801 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 550 | -2 | 3,654 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 536 | +8 | 4,416 | 0.5% | 8.03B | 3 |
| 117 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 438 | 0 | 12,461 | 0.4% | 31.59B | 6 |
| 118 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 437 | +17 | 1,665 | 0.4% | — | 1 |
| 119 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 429 | +5 | 12,231 | 0.4% | 27.23B | 2 |
| 120 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 375 | -19 | 3,407 | 0.4% | 560.9M | 2 |
| 121 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 332 | +11 | 22,172 | 0.3% | 2.61B | 2 |
| 122 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 326 | +1 | 5,589 | 0.3% | 11.51B | 5 |
| 123 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 303 | -4 | 2,849 | 0.3% | 4.02B | 2 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 301 | +14 | 107,301 | 0.1% | — | 3 |
| 125 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 293 | -16 | 32,889 | 0.2% | 40.43B | 2 |
| 126 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 287 | -2 | 37,891 | 0.2% | 27.23B | 3 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 271 | +1 | 39,445 | 0.2% | 7.48B | 2 |
| 128 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 250 | +12 | 70,572 | 0.1% | 8.03B | 3 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 233 | -1 | 41,936 | 0.2% | 11.17B | 1 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 223 | -1 | 322,280 | 0.1% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 214 | -6 | 19,717 | 0.2% | 68.98B | 2 |
| 132 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 192 | +13 | 16,659 | 0.2% | 7.29B | 2 |
| 133 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 191 | 0 | 3,002 | 0.2% | 31.59B | 6 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 189 | -3 | 44,668 | 0.1% | 7.70B | 5 |
| 135 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 184 | 0 | 12,721 | 0.2% | 70.55B | 2 |
| 136 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 180 | -4 | 5,075 | 0.2% | 70.55B | 3 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 168 | -3 | 2,575 | 0.2% | — | 1 |
| 138 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | -1 | 28,438 | 0.1% | 46.70B | 6 |
| 139 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 154 | +11 | 1,181 | 0.2% | — | 1 |
| 140 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 152 | -24 | 5,183 | 0.1% | 437.8M | 1 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 150 | +2 | 5,514 | 0.1% | 353.4M | 2 |
| 142 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 125 | -25 | 7,490 | 0.1% | 31.59B | 6 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 84 | -4 | 38,724 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 75 | -4 | 7,260 | 0.1% | 1.20B | 2 |
| 145 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 72 | +2 | 1,321 | 0.1% | 560.9M | 1 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | 0 | 407 | 0.0% | 437.8M | 1 |
| 147 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | +2 | 265 | 0.0% | 15.17B | 3 |
| 148 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 38 | +5 | 209 | 0.0% | 8.16B | 3 |
| 149 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 37 | -3 | 440 | 0.0% | 321.0M | 1 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 34 | +2 | 235 | 0.0% | 437.8M | 1 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | 0 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 21 | +1 | 282 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +1 | 168 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,376,196 | 307,667,719 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 389,081 | 6,072,293 | 7 | 6.3% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 214,257 | 407,180 | 6 | 42.2% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 90,055 | 2,652,931 | 11 | 3.3% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 86,114 | 6,419,875 | 12 | 1.3% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 54,331 | 1,424,724 | 5 | 3.6% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,891 | 565,511 | 13 | 3.0% |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,615 | 449,434 | 6 | 2.7% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,608 | 1,450,243 | 11 | 0.9% |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 12,842 | 399,946 | 10 | 2.6% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,037 | 372,122 | 14 | 2.5% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,520 | 202,519 | 3 | 2.8% |
| 13 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,495 | 76,755 | 1 | 4.8% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,595 | 81,914 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,562 | 494,046 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,049 | 860,092 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,630 | 700,049 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,542 | 139,917 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,917 | 661,660 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,857 | 1,162,797 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,712 | 106,328 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,803 | 155,157 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,645 | 9,580 | 1 | 1.5% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 764 | 24,462 | 4 | 0.6% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,912,262 | 60,128,124 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 335,297 | 4,688,201 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 209,868 | 277,786 | 8 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,560 | 734,145 | 18 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 36,580 | 4,187,954 | 19 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 25,137 | 244,859 | 22 |
| 7 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,495 | 76,755 | 36 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,452 | 20,607 | 37 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,060 | 118,406 | 40 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 7,214 | 44,624 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,595 | 81,914 | 45 |
| 12 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,042 | 54,830 | 48 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,551 | 154,150 | 51 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,542 | 139,917 | 52 |
| 15 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,407 | 377,769 | 54 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,226 | 37,740 | 57 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,086 | 102,200 | 72 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,064 | 358,316 | 73 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,015 | 80,660 | 75 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,945 | 159,949 | 76 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,645 | 9,580 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,509 | 802,181 | 89 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,027 | 58,605 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 438 | 12,461 | 117 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 42.2% | 214,257 | 407,180 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 6.3% | 389,081 | 6,072,293 | 2 |
| 3 | [openeurollm](https://huggingface.co/openeurollm) | 4.8% | 8,495 | 76,755 | 13 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.6% | 54,331 | 1,424,724 | 6 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.3% | 90,055 | 2,652,931 | 4 |
| 6 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,595 | 81,914 | 14 |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.0% | 19,891 | 565,511 | 7 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,520 | 202,519 | 12 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.7% | 14,615 | 449,434 | 8 |
| 10 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.6% | 12,842 | 399,946 | 10 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 12,037 | 372,122 | 11 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,376,196 | 307,667,719 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,542 | 139,917 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,645 | 9,580 | 23 |
| 15 | [speakleash](https://huggingface.co/speakleash) | 1.3% | 86,114 | 6,419,875 | 5 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,712 | 106,328 | 21 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,608 | 1,450,243 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,562 | 494,046 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,803 | 155,157 | 22 |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 764 | 24,462 | 24 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,630 | 700,049 | 17 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,049 | 860,092 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,917 | 661,660 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,857 | 1,162,797 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
