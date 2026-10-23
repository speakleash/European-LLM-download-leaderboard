# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-23
- **Generated at:** 2026-10-23T11:17:22Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,931,376 | -58,490 | 59,001,290 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,746,964 | +1,354 | 66,055,268 | 2.6% | 7.24B | 1 |
| 3 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 458,426 | -6,991 | 4,554,861 | 9.8% | 8.05B | 2 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 427,704 | -4,398 | 46,063,050 | 0.9% | 7.24B | 2 |
| 5 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 392,239 | -33,237 | 733,799 | 47.0% | 8.90B | 1 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 373,735 | +399 | 4,008,899 | 9.1% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 303,198 | -10,372 | 16,574,110 | 1.8% | 12.25B | 3 |
| 8 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 265,571 | -1,617 | 32,556,813 | 0.8% | 46.70B | 2 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 247,297 | -14,622 | 4,917,824 | 4.9% | 24.01B | 2 |
| 10 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 215,283 | -2,720 | 5,751,735 | 3.7% | 4.25B | 7 |
| 11 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 207,995 | -11,821 | 2,991,787 | 6.7% | 24.01B | 1 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 199,905 | -10,952 | 2,348,797 | 8.2% | 8.92B | 6 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 187,946 | -5,963 | 5,568,704 | 3.3% | 24.01B | 1 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 185,034 | -133 | 929,441 | 18.0% | 1.66B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 93,813 | -13,479 | 599,769 | 13.4% | 22.64B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 82,236 | +1,389 | 7,648,691 | 1.1% | 23.57B | 2 |
| 17 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 74,027 | -34 | 76,051 | 42.0% | — | 1 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,014 | -830 | 720,219 | 8.8% | 119.40B | 3 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,949 | -1,521 | 779,157 | 7.6% | 23.57B | 2 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 66,665 | -4,105 | 8,556,031 | 0.8% | 8.02B | 1 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,203 | -8,303 | 1,110,653 | 5.4% | 127.70B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,078 | -545 | 11,262,536 | 0.6% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 59,664 | +5,317 | 125,508 | 26.5% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 36,764 | -397 | 711,819 | 4.5% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,240 | -694 | 357,559 | 7.0% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 29,351 | -1,113 | 237,901 | 8.7% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,435 | -21 | 43,786 | 17.0% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 20,435 | -681 | 547,282 | 3.2% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,203 | -371 | 4,160,303 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 15,913 | -567 | 156,243 | 6.2% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,611 | -934 | 643,472 | 1.8% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,490 | -324 | 787,919 | 1.5% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,751 | -435 | 82,058 | 6.5% | — | 5 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,488 | +9 | 19,791 | 9.6% | 27.43B | 3 |
| 35 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,110 | -229 | 516,778 | 1.8% | 7.24B | 8 |
| 36 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,749 | -28 | 5,042,258 | 0.2% | 122.61B | 1 |
| 37 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,564 | -235 | 489,890 | 1.8% | 9.15B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,079 | -137 | 4,933,592 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,643 | -52 | 5,383,951 | 0.1% | 22.25B | 1 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,524 | -159 | 138,248 | 3.2% | 7.48B | 5 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,361 | +207 | 19,047 | 6.2% | 572.6M | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,671 | -41 | 114,635 | 3.1% | 8.42B | 7 |
| 43 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,439 | -55 | 81,427 | 3.0% | 7.04B | 4 |
| 44 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,315 | -23 | 353,485 | 1.2% | 125.03B | 1 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,240 | -312 | 148,391 | 2.1% | 2.25B | 7 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,960 | -169 | 137,579 | 2.1% | 7.40B | 3 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,671 | -114 | 167,922 | 1.7% | 11.17B | 16 |
| 48 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,643 | -50 | 5,162,706 | 0.1% | 22.25B | 1 |
| 49 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,500 | +5 | 155,896 | 1.8% | 23.57B | 2 |
| 50 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,405 | -259 | 51,622 | 2.9% | 8.03B | 7 |
| 51 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,324 | -135 | 375,317 | 0.9% | 7.24B | 8 |
| 52 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,321 | -85 | 151,683 | 1.7% | 7.24B | 4 |
| 53 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,267 | -259 | 29,185 | 3.3% | 72.01B | 1 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,713 | -63 | 38,470 | 2.7% | 2.61B | 3 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,649 | +80 | 255,459 | 1.0% | 4.76B | 5 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,637 | -64 | 60,616 | 2.3% | 1.60B | 5 |
| 57 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,385 | -56 | 10,868 | 3.1% | 1.51B | 6 |
| 58 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,006 | -67 | 94,050 | 1.5% | 2.89B | 1 |
| 59 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,929 | -828 | 907,043 | 0.3% | 23.57B | 2 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,853 | -43 | 415,433 | 0.6% | 1.20B | 1 |
| 61 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,731 | +32 | 35,012 | 2.0% | 56.7M | 1 |
| 62 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,695 | -45 | 400,277 | 0.5% | 3.21B | 1 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,689 | -52 | 25,459 | 2.1% | 22.64B | 1 |
| 64 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,657 | -46 | 418,740 | 0.5% | 353.4M | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,543 | -46 | 41,821 | 1.8% | 13.29B | 3 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,450 | -36 | 178,709 | 0.9% | 12.25B | 6 |
| 67 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,376 | +7 | 33,437 | 1.8% | 14.03B | 1 |
| 68 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,269 | +4 | 31,018 | 1.7% | 33.12B | 1 |
| 69 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,172 | -211 | 51,089 | 1.4% | 7.77B | 1 |
| 70 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,088 | -183 | 670,704 | 0.3% | 7.45B | 2 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,001 | -79 | 18,893 | 1.7% | 12.19B | 2 |
| 72 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,960 | -17 | 16,492 | 1.7% | 3.83B | 5 |
| 73 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,839 | -25 | 50,533 | 1.2% | 9.24B | 4 |
| 74 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,831 | -28 | 101,010 | 0.9% | 30.68B | 1 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,819 | -18 | 79,504 | 1.0% | 7.45B | 1 |
| 76 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,798 | -28 | 357,161 | 0.4% | — | 3 |
| 77 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,741 | +78 | 5,301,990 | 0.0% | 7.25B | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,741 | -30 | 107,124 | 0.8% | 7.45B | 1 |
| 79 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,735 | -72 | 21,432 | 1.4% | 4.30B | 2 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,641 | -20 | 33,855 | 1.2% | 22.64B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,622 | -19 | 158,786 | 0.6% | 1.10B | 1 |
| 82 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,614 | -23 | 302,292 | 0.4% | 6.74B | 2 |
| 83 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,582 | +38 | 8,818 | 1.5% | 4.30B | 3 |
| 84 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,564 | -27 | 185,618 | 0.5% | 6.74B | 1 |
| 85 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,552 | -19 | 146,396 | 0.6% | 13.02B | 1 |
| 86 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,527 | -20 | 55,954 | 1.0% | 7.55B | 1 |
| 87 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,520 | -33 | 53,781 | 1.0% | 7.24B | 5 |
| 88 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,479 | -75 | 8,853 | 1.4% | 9.82B | 1 |
| 89 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,463 | -6 | 229,123 | 0.4% | 35.13B | 4 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,437 | -32 | 174,419 | 0.5% | 11.51B | 7 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,433 | -41 | 52,571 | 0.9% | 7.24B | 1 |
| 92 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,392 | -17 | 23,471 | 1.1% | 11.17B | 5 |
| 93 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,275 | -268 | 453,038 | 0.2% | 40.43B | 1 |
| 94 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,270 | +22 | 39,789 | 0.9% | 70.55B | 3 |
| 95 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,190 | -168 | 19,673 | 1.0% | 1.20B | 2 |
| 96 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,186 | -70 | 58,089 | 0.8% | 1.35B | 3 |
| 97 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,180 | -26 | 31,362 | 0.9% | 11.17B | 5 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,133 | -12 | 10,355 | 1.0% | 9.15B | 1 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,117 | +19 | 801,249 | 0.1% | — | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 923 | -93 | 14,942 | 0.8% | 353.4M | 2 |
| 101 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 903 | -138 | 111,935 | 0.4% | 7.29B | 2 |
| 102 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 882 | -10 | 16,552 | 0.8% | 1.54B | 4 |
| 103 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 842 | -5 | 84,493 | 0.5% | 9.15B | 1 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 748 | -19 | 8,622 | 0.7% | 28.84B | 3 |
| 105 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 708 | 0 | 218,463 | 0.2% | 12.19B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 673 | -21 | 81,805 | 0.4% | 8.03B | 3 |
| 107 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 647 | +7 | 14,332 | 0.6% | 4.33B | 3 |
| 108 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 629 | -20 | 96,088 | 0.3% | 1.35B | 8 |
| 109 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 597 | +7 | 44,457 | 0.4% | 12.19B | 2 |
| 110 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 578 | -30 | 4,168 | 0.6% | 8.03B | 3 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 495 | +2 | 21,838 | 0.4% | 9.24B | 2 |
| 112 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 461 | +3 | 3,321 | 0.4% | 30.68B | 1 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 423 | -20 | 20,348 | 0.4% | 3.20B | 2 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 400 | -8 | 32,775 | 0.3% | 40.43B | 2 |
| 115 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 350 | +11 | 21,996 | 0.3% | 2.61B | 2 |
| 116 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | 0 | 27,522 | 0.3% | 9.24B | 2 |
| 117 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 338 | +2 | 1,411 | 0.3% | — | 1 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 336 | -13 | 11,985 | 0.3% | 27.23B | 2 |
| 119 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 334 | -22 | 232,879 | 0.1% | — | 2 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 323 | -10 | 322,186 | 0.1% | 7.24B | 2 |
| 121 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 311 | -1 | 1,490 | 0.3% | 27.23B | 3 |
| 122 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 290 | -8 | 37,713 | 0.2% | 27.23B | 3 |
| 123 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 287 | -5 | 107,127 | 0.1% | — | 3 |
| 124 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 279 | -23 | 41,821 | 0.2% | 11.17B | 1 |
| 125 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 275 | -1 | 5,389 | 0.3% | 11.51B | 5 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 268 | -3 | 39,321 | 0.2% | 7.48B | 2 |
| 127 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 259 | +9 | 2,665 | 0.3% | 4.02B | 2 |
| 128 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 255 | +1 | 5,119 | 0.2% | 437.8M | 1 |
| 129 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 253 | -7 | 12,665 | 0.2% | 70.55B | 2 |
| 130 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 244 | -16 | 7,450 | 0.2% | 31.59B | 6 |
| 131 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 240 | +1 | 70,397 | 0.1% | 8.03B | 3 |
| 132 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 231 | -5 | 19,611 | 0.2% | 68.98B | 2 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 218 | -12 | 44,581 | 0.2% | 7.70B | 5 |
| 134 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 211 | -2 | 5,016 | 0.2% | 70.55B | 3 |
| 135 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 204 | -5 | 2,501 | 0.2% | — | 1 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 184 | -14 | 16,555 | 0.2% | 7.29B | 2 |
| 137 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 184 | -85 | 3,088 | 0.2% | 560.9M | 2 |
| 138 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 177 | -34 | 1,501 | 0.2% | 31.58B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 158 | +2 | 5,445 | 0.1% | 353.4M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 152 | -1 | 28,361 | 0.1% | 46.70B | 6 |
| 141 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 121 | +3 | 1,088 | 0.1% | — | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 111 | -30 | 38,693 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 107 | -6 | 7,236 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 80 | 0 | 420 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 48 | -1 | 1,278 | 0.0% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 36 | +1 | 386 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 35 | +1 | 246 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 31 | +1 | 186 | 0.0% | 8.16B | 3 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 213 | 0.0% | 437.8M | 1 |
| 152 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 28 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 126 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 17 | +1 | 268 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | 0 | 153 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,629,779 | 304,242,073 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 888,073 | 5,911,534 | 7 | 14.8% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 344,897 | 2,608,377 | 11 | 12.7% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 74,027 | 76,051 | 1 | 42.0% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 68,847 | 6,363,707 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 63,409 | 252,144 | 6 | 18.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 45,851 | 1,397,112 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,144 | 396,780 | 10 | 6.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,541 | 557,821 | 13 | 3.1% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,610 | 1,440,804 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,310 | 440,943 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,141 | 365,389 | 14 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,157 | 198,537 | 3 | 2.4% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,648 | 857,332 | 3 | 0.6% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,439 | 81,427 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,960 | 137,579 | 1 | 2.1% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,738 | 490,800 | 3 | 0.8% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,647 | 697,503 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,412 | 659,453 | 2 | 0.4% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,358 | 104,763 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,969 | 1,160,866 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,815 | 154,177 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,479 | 8,853 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 492 | 23,821 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,931,376 | 59,001,290 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 458,426 | 4,554,861 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 185,034 | 929,441 | 14 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 74,027 | 76,051 | 17 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 59,664 | 125,508 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 36,764 | 711,819 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,435 | 43,786 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,203 | 4,160,303 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,488 | 19,791 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,671 | 114,635 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,439 | 81,427 | 43 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,960 | 137,579 | 46 |
| 13 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,405 | 51,622 | 50 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,324 | 375,317 | 51 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,321 | 151,683 | 52 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 2,853 | 415,433 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,088 | 670,704 | 70 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,831 | 101,010 | 74 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,798 | 357,161 | 76 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,622 | 158,786 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,479 | 8,853 | 88 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,186 | 58,089 | 96 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,117 | 801,249 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 244 | 7,450 | 130 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 42.0% | 74,027 | 76,051 | 4 |
| 2 | [cjvt](https://huggingface.co/cjvt) | 18.0% | 63,409 | 252,144 | 6 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 14.8% | 888,073 | 5,911,534 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 12.7% | 344,897 | 2,608,377 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,144 | 396,780 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.1% | 20,541 | 557,821 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 45,851 | 1,397,112 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,439 | 81,427 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,310 | 440,943 | 11 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,157 | 198,537 | 13 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,141 | 365,389 | 12 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,629,779 | 304,242,073 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.1% | 4,960 | 137,579 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,479 | 8,853 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,358 | 104,763 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,610 | 1,440,804 | 10 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 68,847 | 6,363,707 | 5 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,738 | 490,800 | 17 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,815 | 154,177 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,648 | 857,332 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,647 | 697,503 | 18 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,412 | 659,453 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 492 | 23,821 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,969 | 1,160,866 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
