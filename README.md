# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-10-15
- **Generated at:** 2026-10-15T11:07:22Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,257,820 | -17,135 | 58,618,305 | 3.8% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,629,832 | +3,783 | 65,573,562 | 2.5% | 7.24B | 1 |
| 3 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 653,723 | -32,016 | 730,597 | 78.7% | 8.90B | 1 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 486,822 | -18,830 | 45,972,648 | 1.1% | 7.24B | 2 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 486,050 | -1,754 | 4,453,466 | 10.7% | 8.05B | 2 |
| 6 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 326,644 | -8,612 | 16,520,250 | 2.0% | 12.25B | 3 |
| 7 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 319,311 | +12,026 | 3,853,572 | 8.1% | 13.95B | 6 |
| 8 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 312,196 | -7,675 | 2,984,070 | 10.1% | 24.01B | 1 |
| 9 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 297,682 | +1,193 | 4,878,851 | 6.0% | 24.01B | 2 |
| 10 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 248,354 | -2,722 | 5,527,147 | 4.4% | 24.01B | 1 |
| 11 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 248,212 | +1,835 | 32,458,800 | 0.8% | 46.70B | 2 |
| 12 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 231,114 | -109 | 926,895 | 22.5% | 1.66B | 1 |
| 13 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 229,959 | -1,358 | 5,703,023 | 4.0% | 4.25B | 7 |
| 14 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 221,182 | +1,755 | 2,300,068 | 9.2% | 8.92B | 6 |
| 15 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 200,948 | -13,066 | 598,172 | 28.8% | 22.64B | 1 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,480 | -3,595 | 8,546,441 | 1.2% | 8.02B | 1 |
| 17 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 77,523 | -269 | 714,592 | 9.5% | 119.40B | 3 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,849 | +324 | 1,106,157 | 6.1% | 127.70B | 2 |
| 19 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 71,262 | +54 | 762,307 | 8.3% | 23.57B | 2 |
| 20 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 70,455 | +929 | 72,393 | 40.9% | — | 1 |
| 21 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 68,833 | -3,027 | 7,620,600 | 0.9% | 23.57B | 2 |
| 22 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 60,945 | +1,429 | 11,247,443 | 0.5% | 140.63B | 2 |
| 23 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 54,354 | +163 | 118,238 | 24.9% | 12.77B | 5 |
| 24 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 31,241 | -72 | 236,436 | 9.3% | — | 1 |
| 25 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 28,288 | -230 | 694,981 | 3.6% | 7.77B | 8 |
| 26 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 24,161 | +52 | 43,244 | 16.9% | 12.25B | 3 |
| 27 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 21,679 | +52 | 4,155,994 | 0.5% | 11.34B | 8 |
| 28 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 21,102 | +57 | 542,140 | 3.3% | 70.60B | 2 |
| 29 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,152 | -464 | 153,779 | 7.5% | 9.15B | 1 |
| 30 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,870 | +117 | 638,809 | 2.3% | 23.57B | 2 |
| 31 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,372 | -4,566 | 5,161,821 | 0.3% | 22.25B | 1 |
| 32 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 13,772 | +88 | 784,543 | 1.6% | 11.25B | 10 |
| 33 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,520 | +239 | 79,790 | 7.5% | — | 5 |
| 34 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,345 | -313 | 487,544 | 2.1% | 9.15B | 1 |
| 35 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,795 | +92 | 334,861 | 2.7% | 24.01B | 2 |
| 36 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,317 | +85 | 514,008 | 1.8% | 7.24B | 8 |
| 37 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,341 | -12 | 4,930,562 | 0.2% | 122.61B | 1 |
| 38 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 9,078 | +56 | 137,299 | 3.8% | 7.48B | 5 |
| 39 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,312 | +117 | 5,382,101 | 0.1% | 22.25B | 1 |
| 40 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,365 | +53 | 17,593 | 5.4% | 572.6M | 5 |
| 41 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,765 | -19 | 147,426 | 2.3% | 2.25B | 7 |
| 42 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,409 | +87 | 50,843 | 3.6% | 8.03B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 5,382 | -225 | 111,570 | 2.5% | 8.42B | 7 |
| 44 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,168 | -148 | 136,460 | 2.2% | 7.40B | 3 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 5,080 | -292 | 351,963 | 1.1% | 125.03B | 1 |
| 46 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,859 | -108 | 154,795 | 1.9% | 23.57B | 2 |
| 47 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,837 | +38 | 166,930 | 1.8% | 11.17B | 16 |
| 48 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,736 | -12 | 374,362 | 1.0% | 7.24B | 8 |
| 49 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,460 | +13 | 12,364 | 4.0% | 27.43B | 3 |
| 50 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,375 | +18 | 150,567 | 1.7% | 7.24B | 4 |
| 51 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 4,273 | +2 | 111,811 | 2.0% | 7.29B | 2 |
| 52 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,002 | +135 | 254,756 | 1.1% | 4.76B | 5 |
| 53 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,984 | -24 | 5,034,684 | 0.1% | 122.61B | 1 |
| 54 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,809 | -7 | 906,108 | 0.4% | 23.57B | 2 |
| 55 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,609 | +88 | 27,442 | 2.8% | 72.01B | 1 |
| 56 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 3,478 | -245 | 67,475 | 2.1% | 14.08B | 1 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,444 | 0 | 37,101 | 2.5% | 2.61B | 3 |
| 58 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,342 | -94 | 670,493 | 0.4% | 7.45B | 2 |
| 59 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,186 | 0 | 400,146 | 0.6% | 3.21B | 1 |
| 60 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,173 | +11 | 59,356 | 2.0% | 1.60B | 5 |
| 61 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,170 | -2 | 415,098 | 0.6% | 1.20B | 1 |
| 62 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,149 | -7 | 418,592 | 0.6% | 353.4M | 1 |
| 63 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,145 | -27 | 93,296 | 1.6% | 2.89B | 1 |
| 64 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 2,793 | +44 | 9,569 | 2.5% | 1.51B | 6 |
| 65 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,632 | +26 | 24,911 | 2.1% | 22.64B | 1 |
| 66 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,595 | -122 | 86,391 | 1.4% | 2.22B | 1 |
| 67 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,547 | -6 | 84,460 | 1.4% | 9.15B | 1 |
| 68 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,474 | +124 | 50,723 | 1.6% | 7.77B | 1 |
| 69 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,420 | -8 | 178,247 | 0.9% | 12.25B | 6 |
| 70 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,419 | +24 | 41,189 | 1.7% | 13.29B | 3 |
| 71 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,369 | +111 | 34,356 | 1.8% | 56.7M | 1 |
| 72 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,240 | +158 | 30,830 | 1.7% | 33.12B | 1 |
| 73 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,178 | +12 | 50,068 | 1.5% | 9.24B | 4 |
| 74 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,007 | -1 | 18,527 | 1.7% | 12.19B | 2 |
| 75 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,870 | -2 | 79,036 | 1.0% | 7.45B | 1 |
| 76 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,843 | +5 | 100,513 | 0.9% | 30.68B | 1 |
| 77 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,842 | +11 | 452,785 | 0.3% | 40.43B | 1 |
| 78 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,840 | -2 | 106,663 | 0.9% | 7.45B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,764 | +9 | 356,661 | 0.4% | — | 3 |
| 80 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,742 | +28 | 15,816 | 1.5% | 3.83B | 5 |
| 81 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,668 | +62 | 32,530 | 1.3% | 14.03B | 1 |
| 82 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,646 | +3 | 158,349 | 0.6% | 1.10B | 1 |
| 83 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,622 | +6 | 33,409 | 1.2% | 22.64B | 1 |
| 84 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,617 | -15 | 55,771 | 1.0% | 7.55B | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,577 | +2 | 301,845 | 0.4% | 6.74B | 2 |
| 86 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,564 | -4 | 23,224 | 1.3% | 11.17B | 5 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,545 | +5 | 185,195 | 0.5% | 6.74B | 1 |
| 88 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,533 | +6 | 53,386 | 1.0% | 7.24B | 5 |
| 89 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,523 | +92 | 5,301,343 | 0.0% | 7.25B | 1 |
| 90 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,522 | +2 | 145,974 | 0.6% | 13.02B | 1 |
| 91 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,451 | +4 | 52,206 | 1.0% | 7.24B | 1 |
| 92 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,430 | +77 | 174,043 | 0.5% | 11.51B | 7 |
| 93 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,353 | -6 | 8,343 | 1.2% | 4.30B | 3 |
| 94 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,340 | -50 | 20,870 | 1.1% | 4.30B | 2 |
| 95 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,332 | +291 | 8,402 | 1.2% | 9.82B | 1 |
| 96 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,275 | +61 | 228,628 | 0.4% | 35.13B | 4 |
| 97 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,243 | +3 | 31,123 | 0.9% | 11.17B | 5 |
| 98 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,195 | -19 | 19,352 | 1.0% | 1.20B | 2 |
| 99 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,119 | +3 | 57,755 | 0.7% | 1.35B | 3 |
| 100 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,114 | +6 | 800,897 | 0.1% | — | 3 |
| 101 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,108 | -17 | 10,135 | 1.0% | 9.15B | 1 |
| 102 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,064 | +38 | 39,429 | 0.8% | 70.55B | 3 |
| 103 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,022 | -4 | 14,798 | 0.9% | 353.4M | 2 |
| 104 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 844 | +6 | 16,397 | 0.7% | 1.54B | 4 |
| 105 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 745 | -72 | 8,246 | 0.7% | 28.84B | 3 |
| 106 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 687 | +1 | 95,921 | 0.4% | 1.35B | 8 |
| 107 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 671 | +9 | 81,636 | 0.4% | 8.03B | 3 |
| 108 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 611 | +7 | 76,436 | 0.3% | 7.04B | 4 |
| 109 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 610 | -1 | 4,040 | 0.6% | 8.03B | 3 |
| 110 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 589 | -74 | 20,290 | 0.5% | 3.20B | 2 |
| 111 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 523 | 0 | 232,827 | 0.2% | — | 2 |
| 112 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 522 | -3 | 218,121 | 0.2% | 12.19B | 3 |
| 113 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 438 | +14 | 14,022 | 0.4% | 4.33B | 3 |
| 114 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 435 | +7 | 27,439 | 0.3% | 9.24B | 2 |
| 115 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 420 | +4 | 322,136 | 0.1% | 7.24B | 2 |
| 116 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 419 | -9 | 44,176 | 0.3% | 12.19B | 2 |
| 117 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 410 | -1 | 3,187 | 0.4% | 30.68B | 1 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 408 | -8 | 32,660 | 0.3% | 40.43B | 2 |
| 119 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 391 | +2 | 1,307 | 0.4% | — | 1 |
| 120 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 379 | -30 | 39,261 | 0.3% | 7.48B | 2 |
| 121 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 355 | -25 | 7,394 | 0.3% | 31.59B | 6 |
| 122 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 349 | -3 | 1,437 | 0.3% | 27.23B | 3 |
| 123 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 332 | +16 | 21,619 | 0.3% | 9.24B | 2 |
| 124 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 319 | +16 | 21,928 | 0.3% | 2.61B | 2 |
| 125 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 313 | +6 | 37,654 | 0.2% | 27.23B | 3 |
| 126 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 307 | +10 | 11,849 | 0.3% | 27.23B | 2 |
| 127 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 300 | -116 | 3,072 | 0.3% | 560.9M | 2 |
| 128 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 296 | -4 | 107,058 | 0.1% | — | 3 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 294 | +1 | 41,770 | 0.2% | 11.17B | 1 |
| 130 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 276 | +1 | 70,364 | 0.2% | 8.03B | 3 |
| 131 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 271 | +28 | 12,625 | 0.2% | 70.55B | 2 |
| 132 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 268 | +7 | 5,332 | 0.3% | 11.51B | 5 |
| 133 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 263 | +1 | 44,541 | 0.2% | 7.70B | 5 |
| 134 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 244 | -1 | 5,100 | 0.2% | 437.8M | 1 |
| 135 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 228 | 0 | 1,501 | 0.2% | 31.58B | 2 |
| 136 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 217 | -11 | 19,543 | 0.2% | 68.98B | 2 |
| 137 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 212 | 0 | 2,454 | 0.2% | — | 1 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 211 | +17 | 16,510 | 0.2% | 7.29B | 2 |
| 139 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 206 | 0 | 4,990 | 0.2% | 70.55B | 3 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 203 | +3 | 2,574 | 0.2% | 4.02B | 2 |
| 141 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 155 | -5 | 28,333 | 0.1% | 46.70B | 6 |
| 142 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 151 | +4 | 5,405 | 0.1% | 353.4M | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 143 | 0 | 38,665 | 0.1% | 70.55B | 3 |
| 144 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 138 | -2 | 1,052 | 0.1% | — | 1 |
| 145 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 132 | 0 | 6,167 | 0.1% | 12.25B | 3 |
| 146 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 118 | +1 | 7,216 | 0.1% | 1.20B | 2 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 81 | -1 | 408 | 0.1% | 321.0M | 1 |
| 148 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 49 | +2 | 2,836 | 0.0% | 31.59B | 6 |
| 149 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 38 | 0 | 12,033 | 0.0% | 31.59B | 6 |
| 150 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 36 | -1 | 1,261 | 0.0% | 560.9M | 1 |
| 151 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 28 | +1 | 232 | 0.0% | 15.17B | 3 |
| 152 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -1 | 205 | 0.0% | 437.8M | 1 |
| 153 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 24 | +1 | 175 | 0.0% | 8.16B | 3 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 23 | -1 | 371 | 0.0% | 437.8M | 1 |
| 155 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 18 | +4 | 124 | 0.0% | 7.24B | 1 |
| 156 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | -2 | 151 | 0.0% | 437.8M | 1 |
| 157 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 14 | 0 | 264 | 0.0% | 437.8M | 1 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 7,128,900 | 302,667,032 | 30 | 2.4% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 1,175,384 | 5,796,623 | 7 | 19.9% |
| 3 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 506,365 | 2,595,296 | 11 | 18.8% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 72,657 | 6,348,378 | 12 | 1.1% |
| 5 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 70,455 | 72,393 | 1 | 40.9% |
| 6 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 58,627 | 244,084 | 6 | 17.0% |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,777 | 1,378,575 | 5 | 2.6% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 29,727 | 395,018 | 10 | 6.0% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,531 | 1,438,196 | 11 | 1.1% |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,808 | 547,482 | 13 | 2.4% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,273 | 438,031 | 6 | 2.5% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,385 | 362,585 | 14 | 2.5% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 7,052 | 856,192 | 3 | 0.7% |
| 14 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 6,073 | 153,866 | 2 | 2.4% |
| 15 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,024 | 195,372 | 3 | 2.0% |
| 16 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 5,168 | 136,460 | 1 | 2.2% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 5,156 | 696,498 | 2 | 0.6% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 4,713 | 489,518 | 3 | 0.8% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,341 | 658,506 | 2 | 0.4% |
| 20 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,305 | 104,107 | 4 | 1.1% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,150 | 1,160,325 | 4 | 0.2% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,806 | 153,676 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,332 | 8,402 | 1 | 1.2% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 670 | 23,764 | 4 | 0.5% |
| 25 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 611 | 76,436 | 1 | 0.3% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,257,820 | 58,618,305 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus v1.5 8B | 653,723 | 730,597 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 231,114 | 926,895 | 12 |
| 4 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 70,455 | 72,393 | 20 |
| 5 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 54,354 | 118,238 | 23 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 28,288 | 694,981 | 25 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 24,161 | 43,244 | 26 |
| 8 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 21,679 | 4,155,994 | 27 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,409 | 50,843 | 42 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 5,382 | 111,570 | 43 |
| 11 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 5,168 | 136,460 | 44 |
| 12 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,736 | 374,362 | 48 |
| 13 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 4,460 | 12,364 | 49 |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,375 | 150,567 | 50 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 3,478 | 67,475 | 56 |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,342 | 670,493 | 58 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 3B Preview | 3,186 | 400,146 | 59 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,843 | 100,513 | 76 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,764 | 356,661 | 79 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,646 | 158,349 | 82 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,332 | 8,402 | 95 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,119 | 57,755 | 99 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,114 | 800,897 | 100 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 611 | 76,436 | 108 |
| 25 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Instruct Preview | 355 | 7,394 | 121 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [openeurollm](https://huggingface.co/openeurollm) | 40.9% | 70,455 | 72,393 | 5 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 19.9% | 1,175,384 | 5,796,623 | 2 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 18.8% | 506,365 | 2,595,296 | 3 |
| 4 | [cjvt](https://huggingface.co/cjvt) | 17.0% | 58,627 | 244,084 | 6 |
| 5 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 6.0% | 29,727 | 395,018 | 8 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,777 | 1,378,575 | 7 |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,273 | 438,031 | 11 |
| 8 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,385 | 362,585 | 12 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.4% | 15,808 | 547,482 | 10 |
| 10 | [Almawave](https://huggingface.co/Almawave) | 2.4% | 6,073 | 153,866 | 14 |
| 11 | [mistralai](https://huggingface.co/mistralai) | 2.4% | 7,128,900 | 302,667,032 | 1 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.2% | 5,168 | 136,460 | 16 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.0% | 6,024 | 195,372 | 15 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.2% | 1,332 | 8,402 | 23 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,531 | 1,438,196 | 9 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,305 | 104,107 | 20 |
| 17 | [speakleash](https://huggingface.co/speakleash) | 1.1% | 72,657 | 6,348,378 | 4 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.8% | 4,713 | 489,518 | 18 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 7,052 | 856,192 | 13 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,806 | 153,676 | 22 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 5,156 | 696,498 | 17 |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.5% | 670 | 23,764 | 24 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.4% | 3,341 | 658,506 | 19 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.3% | 611 | 76,436 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,150 | 1,160,325 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
