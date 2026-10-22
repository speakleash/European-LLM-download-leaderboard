# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-22
- **Generated at:** 2026-10-22T11:27:33Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,989,866 | -49,591 | 58,970,980 | 3.4% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,745,610 | +26 | 66,017,031 | 2.6% | 7.24B | 1 |
| 3 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 465,417 | -6,969 | 4,546,281 | 10.0% | 8.05B | 2 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 432,102 | -3,974 | 46,049,688 | 0.9% | 7.24B | 2 |
| 5 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 425,476 | -33,689 | 733,730 | 51.0% | 8.90B | 1 |
| 6 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 373,336 | -9,452 | 3,995,191 | 9.1% | 13.95B | 6 |
| 7 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 313,570 | -7,352 | 16,572,620 | 1.9% | 12.25B | 3 |
| 8 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 267,188 | +208 | 32,547,646 | 0.8% | 46.70B | 2 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 261,919 | -13,630 | 4,915,582 | 5.2% | 24.01B | 2 |
| 10 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 219,816 | -18,170 | 2,990,943 | 7.1% | 24.01B | 1 |
| 11 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 218,003 | -4,807 | 5,747,627 | 3.7% | 4.25B | 7 |
| 12 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 210,857 | -14,716 | 2,345,174 | 8.6% | 8.92B | 6 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 193,909 | -6,235 | 5,567,105 | 3.4% | 24.01B | 1 |
| 14 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 185,167 | -293 | 929,289 | 18.0% | 1.66B | 1 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 107,292 | -13,706 | 599,664 | 15.3% | 22.64B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 80,847 | +1,660 | 7,644,722 | 1.0% | 23.57B | 2 |
| 17 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 74,061 | +9 | 76,049 | 42.1% | — | 1 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,506 | -1,647 | 1,110,394 | 6.1% | 127.70B | 2 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 72,844 | -1,011 | 719,782 | 8.9% | 119.40B | 3 |
| 20 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,770 | -2,652 | 8,555,350 | 0.8% | 8.02B | 1 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,470 | -2,336 | 777,810 | 7.8% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,623 | -389 | 11,261,226 | 0.6% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,347 | -6 | 119,808 | 24.7% | 12.77B | 5 |
| 24 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 37,161 | -195 | 711,123 | 4.6% | 7.77B | 8 |
| 25 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,934 | +1,852 | 357,286 | 7.2% | 24.01B | 2 |
| 26 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 30,464 | -312 | 237,824 | 9.0% | — | 1 |
| 27 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,456 | +14 | 43,773 | 17.0% | 12.25B | 3 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,116 | -533 | 547,192 | 3.3% | 70.60B | 2 |
| 29 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 20,574 | -317 | 4,160,059 | 0.5% | 11.34B | 8 |
| 30 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 16,480 | -531 | 156,037 | 6.4% | 9.15B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,545 | -79 | 643,056 | 2.0% | 23.57B | 2 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,814 | -237 | 787,670 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,186 | -431 | 81,840 | 6.7% | — | 5 |
| 34 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 11,479 | +54 | 19,762 | 9.6% | 27.43B | 3 |
| 35 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,339 | -174 | 516,600 | 1.8% | 7.24B | 8 |
| 36 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,799 | -190 | 489,778 | 1.8% | 9.15B | 1 |
| 37 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,777 | +3,106 | 5,042,183 | 0.2% | 122.61B | 1 |
| 38 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,216 | -188 | 4,933,316 | 0.2% | 122.61B | 1 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,695 | -49 | 5,383,779 | 0.1% | 22.25B | 1 |
| 40 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,683 | -48 | 138,203 | 3.2% | 7.48B | 5 |
| 41 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,154 | +57 | 18,667 | 6.0% | 572.6M | 5 |
| 42 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,712 | -334 | 114,514 | 3.1% | 8.42B | 7 |
| 43 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,552 | -129 | 148,345 | 2.2% | 2.25B | 7 |
| 44 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,494 | +8 | 81,412 | 3.0% | 7.04B | 4 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,338 | -125 | 353,366 | 1.2% | 125.03B | 1 |
| 46 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,129 | -123 | 137,512 | 2.2% | 7.40B | 3 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,785 | -119 | 167,862 | 1.8% | 11.17B | 16 |
| 48 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,693 | -57 | 5,162,634 | 0.1% | 22.25B | 1 |
| 49 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,664 | -440 | 51,580 | 3.1% | 8.03B | 7 |
| 50 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,526 | -38 | 29,109 | 3.5% | 72.01B | 1 |
| 51 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,495 | +117 | 155,835 | 1.8% | 23.57B | 2 |
| 52 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,459 | -39 | 375,260 | 0.9% | 7.24B | 8 |
| 53 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,406 | -48 | 151,596 | 1.8% | 7.24B | 4 |
| 54 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,776 | +14 | 38,392 | 2.7% | 2.61B | 3 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,757 | +4 | 906,956 | 0.4% | 23.57B | 2 |
| 56 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,701 | -11 | 60,532 | 2.3% | 1.60B | 5 |
| 57 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,569 | -128 | 255,318 | 1.0% | 4.76B | 5 |
| 58 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,441 | +58 | 10,770 | 3.1% | 1.51B | 6 |
| 59 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,073 | -109 | 93,996 | 1.6% | 2.89B | 1 |
| 60 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,896 | -48 | 415,420 | 0.6% | 1.20B | 1 |
| 61 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,741 | -12 | 25,422 | 2.2% | 22.64B | 1 |
| 62 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,740 | -39 | 400,267 | 0.5% | 3.21B | 1 |
| 63 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,703 | -39 | 418,725 | 0.5% | 353.4M | 1 |
| 64 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,699 | -18 | 34,942 | 2.0% | 56.7M | 1 |
| 65 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,589 | -97 | 41,786 | 1.8% | 13.29B | 3 |
| 66 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,486 | -30 | 178,676 | 0.9% | 12.25B | 6 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,383 | -291 | 51,068 | 1.6% | 7.77B | 1 |
| 68 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,369 | +10 | 33,400 | 1.8% | 14.03B | 1 |
| 69 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,271 | -126 | 670,686 | 0.3% | 7.45B | 2 |
| 70 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,265 | +7 | 30,987 | 1.7% | 33.12B | 1 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,080 | -30 | 18,871 | 1.7% | 12.19B | 2 |
| 72 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,977 | +6 | 16,446 | 1.7% | 3.83B | 5 |
| 73 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,864 | -9 | 50,489 | 1.2% | 9.24B | 4 |
| 74 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,859 | -20 | 100,967 | 0.9% | 30.68B | 1 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,837 | -24 | 79,461 | 1.0% | 7.45B | 1 |
| 76 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,826 | -14 | 357,116 | 0.4% | — | 3 |
| 77 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,807 | +4 | 21,418 | 1.5% | 4.30B | 2 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,771 | -49 | 107,080 | 0.9% | 7.45B | 1 |
| 79 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,663 | -5 | 5,301,856 | 0.0% | 7.25B | 1 |
| 80 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,661 | -10 | 33,815 | 1.2% | 22.64B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,641 | -12 | 158,743 | 0.6% | 1.10B | 1 |
| 82 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,637 | -9 | 302,250 | 0.4% | 6.74B | 2 |
| 83 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,591 | -3 | 185,580 | 0.6% | 6.74B | 1 |
| 84 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,571 | -10 | 146,355 | 0.6% | 13.02B | 1 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,554 | -21 | 8,830 | 1.4% | 9.82B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,553 | -14 | 53,751 | 1.0% | 7.24B | 5 |
| 87 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,547 | -86 | 55,937 | 1.0% | 7.55B | 1 |
| 88 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,544 | -17 | 8,758 | 1.4% | 4.30B | 3 |
| 89 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,543 | -415 | 453,012 | 0.3% | 40.43B | 1 |
| 90 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,474 | -16 | 52,551 | 1.0% | 7.24B | 1 |
| 91 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,469 | -43 | 174,399 | 0.5% | 11.51B | 7 |
| 92 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,469 | +34 | 229,067 | 0.4% | 35.13B | 4 |
| 93 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,409 | -19 | 23,456 | 1.1% | 11.17B | 5 |
| 94 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,358 | +2 | 19,654 | 1.1% | 1.20B | 2 |
| 95 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,256 | +22 | 58,067 | 0.8% | 1.35B | 3 |
| 96 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,248 | +20 | 39,749 | 0.9% | 70.55B | 3 |
| 97 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,206 | -39 | 31,341 | 0.9% | 11.17B | 5 |
| 98 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,145 | +6 | 10,339 | 1.0% | 9.15B | 1 |
| 99 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,098 | +3 | 801,201 | 0.1% | — | 3 |
| 100 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,041 | -15 | 111,932 | 0.5% | 7.29B | 2 |
| 101 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,016 | +5 | 14,926 | 0.9% | 353.4M | 2 |
| 102 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 892 | +24 | 16,539 | 0.8% | 1.54B | 4 |
| 103 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 847 | -1,638 | 84,490 | 0.5% | 9.15B | 1 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 767 | -28 | 8,618 | 0.7% | 28.84B | 3 |
| 105 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 708 | -36 | 218,458 | 0.2% | 12.19B | 3 |
| 106 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 694 | +4 | 81,790 | 0.4% | 8.03B | 3 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 649 | -4 | 96,066 | 0.3% | 1.35B | 8 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 640 | -8 | 14,316 | 0.6% | 4.33B | 3 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 608 | +8 | 4,155 | 0.6% | 8.03B | 3 |
| 110 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 590 | -18 | 44,437 | 0.4% | 12.19B | 2 |
| 111 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 493 | -4 | 21,832 | 0.4% | 9.24B | 2 |
| 112 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 458 | -7 | 3,299 | 0.4% | 30.68B | 1 |
| 113 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 443 | -3 | 20,343 | 0.4% | 3.20B | 2 |
| 114 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 408 | -7 | 32,771 | 0.3% | 40.43B | 2 |
| 115 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 356 | -6 | 232,873 | 0.1% | — | 2 |
| 116 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | 0 | 11,985 | 0.3% | 27.23B | 2 |
| 117 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 349 | -8 | 27,510 | 0.3% | 9.24B | 2 |
| 118 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 339 | 0 | 21,982 | 0.3% | 2.61B | 2 |
| 119 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 336 | +16 | 1,398 | 0.3% | — | 1 |
| 120 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 333 | -3 | 322,184 | 0.1% | 7.24B | 2 |
| 121 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 312 | -4 | 1,490 | 0.3% | 27.23B | 3 |
| 122 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 302 | +3 | 41,819 | 0.2% | 11.17B | 1 |
| 123 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 298 | -6 | 37,704 | 0.2% | 27.23B | 3 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 292 | -7 | 107,119 | 0.1% | — | 3 |
| 125 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 276 | +8 | 5,380 | 0.3% | 11.51B | 5 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 271 | -32 | 39,318 | 0.2% | 7.48B | 2 |
| 127 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 269 | -14 | 3,088 | 0.3% | 560.9M | 2 |
| 128 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 260 | -2 | 12,662 | 0.2% | 70.55B | 2 |
| 129 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 260 | -20 | 7,446 | 0.2% | 31.59B | 6 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 254 | +2 | 5,115 | 0.2% | 437.8M | 1 |
| 131 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 250 | +5 | 2,651 | 0.2% | 4.02B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 239 | +2 | 70,395 | 0.1% | 8.03B | 3 |
| 133 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 236 | +1 | 19,606 | 0.2% | 68.98B | 2 |
| 134 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 230 | -14 | 44,579 | 0.2% | 7.70B | 5 |
| 135 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 213 | -1 | 5,015 | 0.2% | 70.55B | 3 |
| 136 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 211 | -15 | 1,501 | 0.2% | 31.58B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 209 | -2 | 2,499 | 0.2% | — | 1 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 198 | +7 | 16,552 | 0.2% | 7.29B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 156 | -3 | 5,439 | 0.1% | 353.4M | 2 |
| 140 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 153 | -1 | 28,359 | 0.1% | 46.70B | 6 |
| 141 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 141 | -4 | 38,691 | 0.1% | 70.55B | 3 |
| 142 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 143 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 118 | +6 | 1,082 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 113 | -1 | 7,236 | 0.1% | 1.20B | 2 |
| 145 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 80 | -2 | 416 | 0.1% | 321.0M | 1 |
| 146 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 49 | +2 | 1,278 | 0.0% | 560.9M | 1 |
| 147 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 43 | 0 | 2,836 | 0.0% | 31.59B | 6 |
| 148 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 35 | +3 | 385 | 0.0% | 437.8M | 1 |
| 149 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 34 | -3 | 245 | 0.0% | 15.17B | 3 |
| 150 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 30 | -2 | 185 | 0.0% | 8.16B | 3 |
| 151 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | -2 | 213 | 0.0% | 437.8M | 1 |
| 152 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 28 | 0 | 12,034 | 0.0% | 31.59B | 6 |
| 153 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | -1 | 126 | 0.0% | 7.24B | 1 |
| 154 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 16 | +1 | 267 | 0.0% | 437.8M | 1 |
| 155 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 13 | 0 | 153 | 0.0% | 437.8M | 1 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,765,989 | 304,113,458 | 30 | 2.2% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 929,107 | 5,902,195 | 7 | 15.5% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 360,581 | 2,607,549 | 11 | 13.3% |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 74,061 | 76,049 | 1 | 42.1% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 70,127 | 6,362,639 | 12 | 1.1% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,156 | 246,373 | 6 | 16.8% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 47,047 | 1,396,319 | 5 | 3.1% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 30,232 | 396,651 | 10 | 6.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 20,840 | 557,673 | 13 | 3.2% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,044 | 1,440,601 | 11 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,562 | 440,720 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,441 | 365,178 | 14 | 2.5% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,213 | 198,411 | 3 | 2.4% |
| 14 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,879 | 857,227 | 3 | 0.6% |
| 15 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,494 | 81,412 | 1 | 3.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,129 | 137,512 | 1 | 2.2% |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,803 | 490,678 | 3 | 0.8% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,792 | 697,444 | 2 | 0.6% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,463 | 659,366 | 2 | 0.5% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,381 | 104,696 | 4 | 1.2% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,982 | 1,160,799 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,905 | 154,133 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,554 | 8,830 | 1 | 1.4% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 542 | 23,817 | 4 | 0.4% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,989,866 | 58,970,980 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 465,417 | 4,546,281 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 185,167 | 929,289 | 14 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 74,061 | 76,049 | 17 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,347 | 119,808 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 37,161 | 711,123 | 24 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,456 | 43,773 | 27 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 20,574 | 4,160,059 | 29 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 11,479 | 19,762 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,712 | 114,514 | 42 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,494 | 81,412 | 44 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,129 | 137,512 | 46 |
| 13 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,664 | 51,580 | 49 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,459 | 375,260 | 52 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,406 | 151,596 | 53 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 1.2B Preview | 2,896 | 415,420 | 60 |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 2,271 | 670,686 | 69 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,859 | 100,967 | 74 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,826 | 357,116 | 76 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,641 | 158,743 | 81 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,554 | 8,830 | 85 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,256 | 58,067 | 95 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,098 | 801,201 | 99 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 260 | 7,446 | 129 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 42.1% | 74,061 | 76,049 | 4 |
| 2 | [cjvt](https://huggingface.co/cjvt) | 16.8% | 58,156 | 246,373 | 6 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | 15.5% | 929,107 | 5,902,195 | 2 |
| 4 | [utter-project](https://huggingface.co/utter-project) | 13.3% | 360,581 | 2,607,549 | 3 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.1% | 30,232 | 396,651 | 8 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.2% | 20,840 | 557,673 | 9 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.1% | 47,047 | 1,396,319 | 7 |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.0% | 5,494 | 81,412 | 15 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,562 | 440,720 | 11 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,441 | 365,178 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,213 | 198,411 | 13 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.2% | 6,765,989 | 304,113,458 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,129 | 137,512 | 16 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.4% | 1,554 | 8,830 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.2% | 2,381 | 104,696 | 20 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,044 | 1,440,601 | 10 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 70,127 | 6,362,639 | 5 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,803 | 490,678 | 17 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,905 | 154,133 | 22 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.6% | 5,879 | 857,227 | 14 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,792 | 697,444 | 18 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,463 | 659,366 | 19 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.4% | 542 | 23,817 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,982 | 1,160,799 | 21 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
