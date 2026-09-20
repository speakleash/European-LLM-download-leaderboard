# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-20
- **Generated at:** 2026-09-20T10:58:49Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,546,683 | -23,535 | 56,744,067 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,773,480 | -8,789 | 64,160,160 | 2.8% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 626,739 | +1,528 | 3,572,467 | 17.1% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 591,664 | +1,527 | 45,563,488 | 1.3% | 7.24B | 2 |
| 5 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 504,031 | -7,976 | 16,233,221 | 3.1% | 12.25B | 3 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 484,006 | -5,709 | 4,036,695 | 11.7% | 8.05B | 2 |
| 7 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 464,801 | +743 | 4,622,906 | 9.8% | 24.01B | 2 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 309,656 | -13,381 | 5,507,321 | 5.5% | 4.25B | 7 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 306,320 | -45,960 | 415,831 | 59.4% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 304,993 | -44,894 | 412,317 | 59.5% | 1.20B | 1 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 296,616 | -42,949 | 397,342 | 59.6% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 294,184 | -1,466 | 32,248,708 | 0.9% | 46.70B | 2 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 275,010 | +4,090 | 2,727,862 | 9.7% | 24.01B | 1 |
| 14 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 257,397 | +12,989 | 453,899 | 46.5% | 22.64B | 1 |
| 15 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 210,182 | -7,735 | 4,137,377 | 5.0% | 11.34B | 8 |
| 16 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 201,063 | +31,574 | 214,810 | 63.9% | 8.90B | 1 |
| 17 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 186,776 | +1,582 | 5,350,049 | 3.4% | 24.01B | 1 |
| 18 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 181,066 | -2,715 | 2,103,531 | 8.2% | 8.92B | 6 |
| 19 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 165,286 | -9,279 | 8,473,402 | 1.9% | 8.02B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 96,690 | -79 | 523,852 | 15.5% | 70.60B | 2 |
| 21 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 89,607 | -648 | 1,033,989 | 7.9% | 127.70B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 74,978 | -10 | 627,105 | 10.3% | 23.57B | 2 |
| 23 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 73,243 | -574 | 701,041 | 9.1% | 23.57B | 2 |
| 24 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 69,049 | +1,066 | 7,559,766 | 0.9% | 23.57B | 2 |
| 25 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 55,620 | -501 | 643,167 | 7.5% | 119.40B | 3 |
| 26 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 41,106 | +292 | 11,192,619 | 0.4% | 140.63B | 2 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 31,751 | -1,382 | 670,719 | 4.1% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 23,637 | +236 | 137,680 | 9.9% | 9.15B | 1 |
| 29 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 21,692 | +248 | 477,710 | 3.8% | 9.15B | 1 |
| 30 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,649 | -87 | 5,157,606 | 0.4% | 22.25B | 1 |
| 31 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 17,192 | +66 | 24,182 | 13.8% | 72.01B | 1 |
| 32 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,120 | -32 | 323,887 | 3.8% | 24.01B | 2 |
| 33 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,849 | -25 | 772,558 | 1.8% | 11.25B | 10 |
| 34 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,618 | -711 | 347,581 | 3.3% | 125.03B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,180 | -29 | 5,300,032 | 0.2% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,083 | -321 | 68,334 | 7.8% | — | 5 |
| 37 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,860 | -378 | 697,187 | 1.6% | 1.66B | 1 |
| 38 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,359 | -58 | 206,659 | 3.7% | — | 1 |
| 39 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,761 | +165 | 504,168 | 1.6% | 7.24B | 8 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,465 | -111 | 106,722 | 3.1% | 8.42B | 5 |
| 41 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,261 | -242 | 4,922,203 | 0.1% | 122.61B | 1 |
| 42 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 6,157 | +186 | 128,807 | 2.7% | 7.48B | 5 |
| 43 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 5,167 | -31 | 65,005 | 3.1% | 11.77B | 4 |
| 44 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 5,101 | -98 | 110,816 | 2.4% | 7.29B | 2 |
| 45 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,068 | -8 | 162,637 | 1.9% | 11.17B | 16 |
| 46 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,553 | -236 | 45,940 | 3.1% | 8.03B | 7 |
| 47 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,383 | +11 | 28,655 | 3.4% | 33.12B | 1 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,312 | +125 | 142,208 | 1.8% | 2.25B | 7 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,925 | +6 | 902,732 | 0.4% | 23.57B | 2 |
| 50 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,917 | -46 | 90,558 | 2.1% | 2.89B | 1 |
| 51 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 3,763 | -3 | 667,773 | 0.5% | 7.45B | 2 |
| 52 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,608 | -23 | 54,252 | 2.3% | 7.55B | 1 |
| 53 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,597 | +93 | 5,375,583 | 0.1% | 22.25B | 1 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,580 | +52 | 370,278 | 0.8% | 7.24B | 8 |
| 55 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,491 | +35 | 131,922 | 1.5% | 7.40B | 3 |
| 56 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,389 | +50 | 251,086 | 1.0% | 4.76B | 5 |
| 57 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,107 | +10 | 30,959 | 2.4% | 14.03B | 1 |
| 58 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 2,765 | -281 | 56,459 | 1.8% | 1.60B | 5 |
| 59 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 2,583 | +117 | 64,687 | 1.6% | 14.08B | 1 |
| 60 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,471 | +88 | 146,777 | 1.0% | 7.24B | 4 |
| 61 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,449 | +280 | 34,303 | 1.8% | 2.61B | 3 |
| 62 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,375 | +23 | 5,031,119 | 0.0% | 122.61B | 1 |
| 63 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,060 | -101 | 38,966 | 1.5% | 321.0M | 2 |
| 64 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,928 | -70 | 14,217 | 1.7% | 3.83B | 5 |
| 65 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,727 | +36 | 48,471 | 1.2% | 9.24B | 4 |
| 66 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,710 | +48 | 32,007 | 1.3% | 22.64B | 1 |
| 67 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,635 | +60 | 150,845 | 0.7% | 23.57B | 2 |
| 68 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,595 | +36 | 22,504 | 1.3% | 22.64B | 1 |
| 69 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,580 | -106 | 11,375 | 1.4% | 572.6M | 5 |
| 70 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,568 | +53 | 77,429 | 0.9% | 7.45B | 1 |
| 71 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,541 | -45 | 9,143 | 1.4% | 9.15B | 1 |
| 72 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,507 | -14 | 6,964 | 1.4% | 1.51B | 6 |
| 73 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,439 | +61 | 21,910 | 1.2% | 11.17B | 5 |
| 74 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,427 | -1 | 12,000 | 1.3% | 31.59B | 6 |
| 75 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,352 | +9 | 172,810 | 0.5% | 11.51B | 7 |
| 76 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,332 | -108 | 176,036 | 0.5% | 12.25B | 6 |
| 77 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,291 | +32 | 98,911 | 0.6% | 30.68B | 1 |
| 78 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,282 | +8 | 30,024 | 1.0% | 11.17B | 5 |
| 79 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,262 | -120 | 19,570 | 1.1% | 4.30B | 2 |
| 80 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,259 | +45 | 105,048 | 0.6% | 7.45B | 1 |
| 81 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,223 | +57 | 355,124 | 0.3% | — | 3 |
| 82 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,183 | -27 | 19,231 | 1.0% | 12.25B | 3 |
| 83 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1,154 | -18 | 2,810 | 1.1% | 31.59B | 6 |
| 84 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,128 | +58 | 156,932 | 0.4% | 1.10B | 1 |
| 85 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,106 | +17 | 95,348 | 0.6% | 1.35B | 8 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,102 | +48 | 300,471 | 0.3% | 6.74B | 2 |
| 87 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,101 | -51 | 7,735 | 1.0% | 28.84B | 3 |
| 88 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,057 | +51 | 84,201 | 0.6% | 2.22B | 1 |
| 89 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,041 | +10 | 800,010 | 0.1% | — | 3 |
| 90 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,036 | -96 | 16,630 | 0.9% | 12.19B | 2 |
| 91 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,035 | +46 | 144,646 | 0.4% | 13.02B | 1 |
| 92 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,027 | +46 | 183,848 | 0.4% | 6.74B | 1 |
| 93 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,025 | +34 | 7,111 | 1.0% | 4.30B | 3 |
| 94 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,018 | +15 | 8,243 | 0.9% | 27.43B | 3 |
| 95 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,018 | -31 | 81,047 | 0.6% | 8.03B | 3 |
| 96 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,014 | -139 | 32,118 | 0.8% | 56.7M | 1 |
| 97 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,008 | +37 | 56,745 | 0.6% | 1.35B | 3 |
| 98 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 997 | +5 | 7,154 | 0.9% | 9.82B | 1 |
| 99 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 992 | -12 | 38,435 | 0.7% | 70.55B | 3 |
| 100 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 946 | +2 | 227,496 | 0.3% | 35.13B | 4 |
| 101 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 937 | -43 | 217,692 | 0.3% | 12.19B | 3 |
| 102 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 865 | +6 | 37,364 | 0.6% | 27.23B | 3 |
| 103 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 862 | +4 | 1,168 | 0.9% | 27.23B | 3 |
| 104 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 827 | -4 | 12,391 | 0.7% | 70.55B | 2 |
| 105 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 816 | -14 | 48,313 | 0.6% | 7.77B | 1 |
| 106 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 791 | +9 | 18,234 | 0.7% | 1.20B | 2 |
| 107 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 714 | +14 | 70,146 | 0.4% | 8.03B | 3 |
| 108 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 708 | +4 | 19,849 | 0.6% | 3.20B | 2 |
| 109 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 665 | +4 | 13,862 | 0.6% | 353.4M | 2 |
| 110 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 656 | +38 | 81,981 | 0.4% | 9.15B | 1 |
| 111 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 616 | -24 | 13,615 | 0.5% | 4.33B | 3 |
| 112 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 598 | +17 | 232,499 | 0.2% | — | 2 |
| 113 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 590 | +7 | 450,988 | 0.1% | 40.43B | 1 |
| 114 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 578 | +52 | 52,055 | 0.4% | 7.24B | 5 |
| 115 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 568 | -126 | 43,810 | 0.4% | 12.19B | 2 |
| 116 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 557 | -17 | 2,800 | 0.5% | 30.68B | 1 |
| 117 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 554 | +1 | 321,825 | 0.1% | 7.24B | 2 |
| 118 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 534 | -23 | 32,342 | 0.4% | 40.43B | 2 |
| 119 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 510 | 0 | 1,273 | 0.5% | 31.58B | 2 |
| 120 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 501 | +26 | 3,529 | 0.5% | 8.03B | 3 |
| 121 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 500 | +46 | 50,943 | 0.3% | 7.24B | 1 |
| 122 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 468 | -5 | 2,797 | 0.5% | 560.9M | 2 |
| 123 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 446 | -1 | 44,319 | 0.3% | 7.70B | 5 |
| 124 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 414 | +72 | 27,085 | 0.3% | 9.24B | 2 |
| 125 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 414 | +7 | 38,935 | 0.3% | 7.48B | 2 |
| 126 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 407 | -91 | 7,190 | 0.4% | 31.59B | 6 |
| 127 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 401 | +13 | 106,802 | 0.2% | — | 3 |
| 128 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 392 | +6 | 75,885 | 0.2% | 7.04B | 4 |
| 129 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 369 | -2 | 2,398 | 0.4% | 4.02B | 2 |
| 130 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 366 | -71 | 15,633 | 0.3% | 1.54B | 4 |
| 131 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 362 | 0 | 21,625 | 0.3% | 2.61B | 2 |
| 132 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 282 | -2 | 1,037 | 0.3% | — | 1 |
| 133 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 279 | +35 | 11,583 | 0.2% | 27.23B | 2 |
| 134 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 259 | +9 | 41,495 | 0.2% | 11.17B | 1 |
| 135 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 241 | -4 | 4,860 | 0.2% | 437.8M | 1 |
| 136 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 236 | +9 | 21,316 | 0.2% | 9.24B | 2 |
| 137 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 216 | +6 | 16,331 | 0.2% | 7.29B | 2 |
| 138 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 209 | +15 | 19,356 | 0.2% | 68.98B | 2 |
| 139 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 200 | +2 | 5,271 | 0.2% | 353.4M | 2 |
| 140 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 172 | +14 | 5,096 | 0.2% | 11.51B | 5 |
| 141 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 160 | -3 | 38,542 | 0.1% | 70.55B | 3 |
| 142 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 159 | +11 | 2,271 | 0.2% | — | 1 |
| 143 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 145 | -18 | 1,986 | 0.1% | — | 1 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | +2 | 7,112 | 0.1% | 1.20B | 2 |
| 145 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 127 | -9 | 4,798 | 0.1% | 70.55B | 3 |
| 146 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 120 | +1 | 28,193 | 0.1% | 46.70B | 6 |
| 147 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 109 | -1 | 1,228 | 0.1% | 560.9M | 1 |
| 148 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104 | -1 | 958 | 0.1% | — | 1 |
| 149 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 84 | +2 | 179 | 0.1% | 437.8M | 1 |
| 150 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 6,035 | 0.1% | 12.25B | 3 |
| 151 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 42 | 0 | 330 | 0.0% | 321.0M | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 42 | 0 | 251 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 25 | 0 | 138 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 349 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 16 | +2 | 206 | 0.0% | 15.17B | 3 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 15 | 0 | 106 | 0.0% | 7.24B | 1 |
| 157 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 15 | +2 | 153 | 0.0% | 8.16B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,417,808 | 296,646,786 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 913,861 | 1,422,430 | 11 | 60.0% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 803,966 | 4,832,095 | 7 | 16.3% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 335,055 | 2,155,344 | 11 | 14.9% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 257,675 | 6,284,427 | 12 | 4.0% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 38,003 | 1,344,570 | 5 | 2.6% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 17,589 | 425,737 | 6 | 3.3% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 13,146 | 536,051 | 13 | 2.1% |
| 9 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 9,695 | 187,490 | 6 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,838 | 352,647 | 14 | 2.0% |
| 11 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,325 | 189,976 | 3 | 2.5% |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,590 | 850,250 | 3 | 0.7% |
| 13 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,069 | 366,012 | 10 | 1.3% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,134 | 692,103 | 2 | 0.5% |
| 15 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 3,640 | 148,888 | 2 | 1.5% |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 3,498 | 23,273 | 4 | 2.8% |
| 17 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,491 | 131,922 | 1 | 1.5% |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 3,190 | 485,426 | 3 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,325 | 655,595 | 2 | 0.3% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,249 | 1,158,667 | 4 | 0.2% |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,114 | 152,093 | 2 | 0.8% |
| 22 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 1,879 | 102,070 | 4 | 0.9% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 997 | 7,154 | 1 | 0.9% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 392 | 75,885 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 145 | 1,986 | 1 | 0.1% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,546,683 | 56,744,067 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 484,006 | 4,036,695 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 306,320 | 415,831 | 9 |
| 4 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 257,397 | 453,899 | 14 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 210,182 | 4,137,377 | 15 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 31,751 | 670,719 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,465 | 106,722 | 40 |
| 8 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 5,167 | 65,005 | 43 |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 5,101 | 110,816 | 44 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,553 | 45,940 | 46 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 3,917 | 90,558 | 50 |
| 12 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 3,763 | 667,773 | 51 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,580 | 370,278 | 54 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,491 | 131,922 | 55 |
| 15 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 2,583 | 64,687 | 59 |
| 16 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 1,427 | 12,000 | 74 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,332 | 176,036 | 76 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,291 | 98,911 | 77 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,223 | 355,124 | 81 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,128 | 156,932 | 84 |
| 21 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,106 | 95,348 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,041 | 800,010 | 89 |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 997 | 7,154 | 98 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 392 | 75,885 | 128 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 145 | 1,986 | 143 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 60.0% | 913,861 | 1,422,430 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 16.3% | 803,966 | 4,832,095 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 14.9% | 335,055 | 2,155,344 | 4 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.0% | 257,675 | 6,284,427 | 5 |
| 5 | [cjvt](https://huggingface.co/cjvt) | 3.4% | 9,695 | 187,490 | 9 |
| 6 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.3% | 17,589 | 425,737 | 7 |
| 7 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 2.8% | 3,498 | 23,273 | 16 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,417,808 | 296,646,786 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 38,003 | 1,344,570 | 6 |
| 10 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,325 | 189,976 | 11 |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.1% | 13,146 | 536,051 | 8 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.0% | 8,838 | 352,647 | 10 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,491 | 131,922 | 17 |
| 14 | [Almawave](https://huggingface.co/Almawave) | 1.5% | 3,640 | 148,888 | 15 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.3% | 6,069 | 366,012 | 13 |
| 16 | [domyn](https://huggingface.co/domyn) | 0.9% | 997 | 7,154 | 23 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | 0.9% | 1,879 | 102,070 | 22 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,114 | 152,093 | 21 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,590 | 850,250 | 12 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 3,190 | 485,426 | 18 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,134 | 692,103 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,325 | 655,595 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 392 | 75,885 | 24 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,249 | 1,158,667 | 20 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.1% | 145 | 1,986 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
