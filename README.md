# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-06
- **Generated at:** 2026-11-06T13:58:58Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,872,047 | +10,532 | 60,036,094 | 3.1% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,590,330 | -35,954 | 66,645,277 | 2.4% | 7.24B | 1 |
| 3 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 598,444 | +17,738 | 46,409,477 | 1.3% | 7.24B | 2 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 587,409 | +9,789 | 4,372,193 | 13.1% | 13.95B | 6 |
| 5 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 345,163 | -14,866 | 4,687,321 | 7.2% | 8.05B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 327,505 | +896 | 32,741,222 | 1.0% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 241,820 | +25,791 | 2,502,241 | 9.3% | 8.92B | 6 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 201,769 | +420 | 5,856,572 | 3.4% | 3.85B | 7 |
| 9 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 200,568 | +9,430 | 268,372 | 54.4% | 12.77B | 5 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 172,004 | -5,306 | 4,993,039 | 3.4% | 24.01B | 2 |
| 11 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 163,361 | -8,760 | 16,646,814 | 1.0% | 12.25B | 3 |
| 12 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 110,264 | -1,801 | 5,611,444 | 1.9% | 24.01B | 1 |
| 13 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 109,354 | -6,942 | 3,006,709 | 3.5% | 24.01B | 1 |
| 14 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 107,071 | -645 | 7,707,789 | 1.4% | 23.57B | 2 |
| 15 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 58,873 | -2,205 | 806,073 | 6.5% | 23.57B | 2 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 56,828 | +8,146 | 8,591,526 | 0.7% | 8.02B | 1 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 50,452 | -4,826 | 11,281,747 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 46,172 | -604 | 733,426 | 5.5% | 7.77B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,785 | -507 | 741,176 | 4.0% | 119.40B | 3 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 32,514 | -3,147 | 364,774 | 7.0% | 24.01B | 2 |
| 21 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 29,637 | +3,933 | 4,180,670 | 0.7% | 11.34B | 8 |
| 22 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 24,443 | +1,151 | 243,788 | 7.1% | — | 1 |
| 23 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 20,342 | -389 | 944,417 | 1.9% | 1.66B | 1 |
| 24 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 19,675 | -3,494 | 1,118,690 | 1.6% | 127.70B | 2 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,399 | -553 | 739,685 | 2.0% | 8.90B | 1 |
| 26 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,240 | +58 | 797,714 | 1.8% | 11.25B | 10 |
| 27 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,930 | -26 | 649,471 | 2.1% | 23.57B | 2 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,687 | +214 | 4,942,113 | 0.3% | 122.61B | 1 |
| 29 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 13,289 | -494 | 550,328 | 2.0% | 70.60B | 2 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,703 | +31 | 5,046,676 | 0.2% | 122.61B | 1 |
| 31 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,531 | -64 | 159,436 | 4.4% | 9.15B | 1 |
| 32 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 11,176 | -91 | 522,382 | 1.8% | 7.24B | 8 |
| 33 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,941 | -283 | 495,903 | 1.8% | 9.15B | 1 |
| 34 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 9,171 | -2,642 | 44,558 | 6.3% | 12.25B | 3 |
| 35 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,900 | -282 | 85,711 | 4.8% | — | 5 |
| 36 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,687 | +260 | 5,389,284 | 0.2% | 22.25B | 1 |
| 37 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 8,544 | -73 | 603,524 | 1.2% | 22.64B | 1 |
| 38 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 8,501 | -29 | 20,588 | 7.0% | 27.43B | 3 |
| 39 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 8,445 | -39 | 76,704 | 4.8% | — | 1 |
| 40 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,320 | +25 | 35,043 | 6.2% | 72.01B | 1 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,110 | -12 | 118,288 | 3.7% | 8.42B | 7 |
| 42 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,653 | +201 | 15,647 | 5.8% | 1.51B | 6 |
| 43 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,520 | +106 | 357,157 | 1.4% | 125.03B | 1 |
| 44 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,701 | -31 | 259,447 | 1.6% | 4.76B | 5 |
| 45 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,577 | -40 | 81,884 | 3.1% | 7.04B | 4 |
| 46 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,537 | -137 | 20,920 | 4.6% | 3.83B | 5 |
| 47 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,256 | -164 | 151,692 | 2.1% | 2.25B | 7 |
| 48 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 4,680 | +159 | 21,716 | 3.8% | 572.6M | 5 |
| 49 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,601 | -9 | 910,073 | 0.5% | 23.57B | 2 |
| 50 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,542 | -40 | 139,803 | 1.9% | 7.40B | 3 |
| 51 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,517 | -18 | 154,000 | 1.8% | 7.24B | 4 |
| 52 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,492 | -280 | 140,337 | 1.9% | 7.48B | 5 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 4,415 | -32 | 63,002 | 2.7% | 1.60B | 5 |
| 54 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,377 | -44 | 377,633 | 0.9% | 7.24B | 8 |
| 55 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,343 | -104 | 5,165,053 | 0.1% | 22.25B | 1 |
| 56 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,170 | -15 | 37,612 | 3.0% | 56.7M | 1 |
| 57 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,116 | +3 | 40,360 | 2.9% | 2.61B | 3 |
| 58 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,056 | +17 | 53,748 | 2.6% | 8.03B | 7 |
| 59 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,795 | +37 | 44,328 | 2.6% | 13.29B | 3 |
| 60 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,647 | -200 | 169,499 | 1.4% | 11.17B | 16 |
| 61 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,301 | +25 | 95,833 | 1.7% | 2.89B | 1 |
| 62 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,044 | -51 | 27,069 | 2.4% | 22.64B | 1 |
| 63 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,749 | -4 | 34,538 | 2.0% | 14.03B | 1 |
| 64 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,692 | +2 | 5,303,647 | 0.0% | 7.25B | 1 |
| 65 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2,543 | -6 | 179,606 | 0.9% | 12.25B | 6 |
| 66 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,510 | +7 | 156,993 | 1.0% | 23.57B | 2 |
| 67 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,391 | -11 | 52,271 | 1.6% | 7.77B | 1 |
| 68 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,379 | +77 | 230,612 | 0.7% | 35.13B | 4 |
| 69 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,157 | +14 | 22,574 | 1.8% | 4.30B | 2 |
| 70 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,067 | +1 | 102,133 | 1.0% | 30.68B | 1 |
| 71 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,044 | -1 | 358,252 | 0.4% | — | 3 |
| 72 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,029 | +8 | 51,621 | 1.3% | 9.24B | 4 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,001 | -2 | 80,582 | 1.1% | 7.45B | 1 |
| 74 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,915 | -10 | 159,869 | 0.7% | 1.10B | 1 |
| 75 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,910 | -6 | 108,138 | 0.9% | 7.45B | 1 |
| 76 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,866 | +192 | 11,460 | 1.7% | 9.15B | 1 |
| 77 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,839 | -1 | 19,998 | 1.5% | 12.19B | 2 |
| 78 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,828 | +2 | 186,625 | 0.6% | 6.74B | 1 |
| 79 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,824 | -10 | 34,831 | 1.4% | 22.64B | 1 |
| 80 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,824 | -4 | 303,278 | 0.5% | 6.74B | 2 |
| 81 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,796 | -2 | 40,876 | 1.3% | 70.55B | 3 |
| 82 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,749 | -10 | 147,346 | 0.7% | 13.02B | 1 |
| 83 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,678 | -64 | 20,626 | 1.4% | 1.20B | 2 |
| 84 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,631 | -19 | 9,487 | 1.5% | 4.30B | 3 |
| 85 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,608 | +7 | 9,513 | 1.5% | 9.82B | 1 |
| 86 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,578 | -13 | 54,584 | 1.0% | 7.24B | 5 |
| 87 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,513 | -12 | 53,354 | 1.0% | 7.24B | 1 |
| 88 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,488 | +14 | 802,135 | 0.2% | — | 3 |
| 89 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,451 | -14 | 31,728 | 1.1% | 33.12B | 1 |
| 90 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,431 | +17 | 175,003 | 0.5% | 11.51B | 7 |
| 91 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,412 | -70 | 15,899 | 1.2% | 353.4M | 2 |
| 92 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,219 | +6 | 219,138 | 0.4% | 12.19B | 3 |
| 93 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,210 | +13 | 85,560 | 0.7% | 9.15B | 1 |
| 94 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,170 | -31 | 56,724 | 0.7% | 7.55B | 1 |
| 95 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,128 | -39 | 671,202 | 0.1% | 7.45B | 2 |
| 96 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,096 | -9 | 9,241 | 1.0% | 28.84B | 3 |
| 97 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,063 | +2 | 23,923 | 0.9% | 11.17B | 5 |
| 98 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,034 | +9 | 58,584 | 0.7% | 1.35B | 3 |
| 99 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 978 | -10 | 453,561 | 0.2% | 40.43B | 1 |
| 100 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 924 | -18 | 31,750 | 0.7% | 11.17B | 5 |
| 101 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 913 | +18 | 415,867 | 0.2% | 1.20B | 1 |
| 102 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 892 | +11 | 45,010 | 0.6% | 12.19B | 2 |
| 103 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 838 | -6 | 233,592 | 0.3% | — | 2 |
| 104 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 820 | -11 | 112,457 | 0.4% | 7.29B | 2 |
| 105 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 789 | +1 | 14,718 | 0.7% | 4.33B | 3 |
| 106 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 770 | +2 | 2,014 | 0.8% | 27.23B | 3 |
| 107 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 751 | +20 | 96,522 | 0.4% | 1.35B | 8 |
| 108 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 746 | +31 | 419,198 | 0.1% | 353.4M | 1 |
| 109 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 724 | +52 | 400,719 | 0.1% | 3.21B | 1 |
| 110 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 701 | -10 | 82,169 | 0.4% | 8.03B | 3 |
| 111 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 663 | -2 | 16,925 | 0.6% | 1.54B | 4 |
| 112 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 615 | +4 | 22,153 | 0.5% | 9.24B | 2 |
| 113 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 604 | -15 | 27,951 | 0.5% | 9.24B | 2 |
| 114 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 577 | -4 | 20,784 | 0.5% | 3.20B | 2 |
| 115 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 552 | +13 | 3,636 | 0.5% | 30.68B | 1 |
| 116 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 528 | +20 | 4,388 | 0.5% | 8.03B | 3 |
| 117 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 438 | +63 | 12,461 | 0.4% | 31.59B | 6 |
| 118 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 424 | +4 | 12,223 | 0.4% | 27.23B | 2 |
| 119 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 420 | -1 | 1,638 | 0.4% | — | 1 |
| 120 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | 0 | 3,407 | 0.4% | 560.9M | 2 |
| 121 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 325 | -8 | 5,583 | 0.3% | 11.51B | 5 |
| 122 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 321 | +12 | 22,155 | 0.3% | 2.61B | 2 |
| 123 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 309 | +3 | 32,886 | 0.2% | 40.43B | 2 |
| 124 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 307 | -3 | 2,842 | 0.3% | 4.02B | 2 |
| 125 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 289 | -5 | 37,891 | 0.2% | 27.23B | 3 |
| 126 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 287 | -2 | 107,273 | 0.1% | — | 3 |
| 127 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 270 | -2 | 39,443 | 0.2% | 7.48B | 2 |
| 128 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 238 | 0 | 70,544 | 0.1% | 8.03B | 3 |
| 129 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 234 | -7 | 41,919 | 0.2% | 11.17B | 1 |
| 130 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 224 | +4 | 322,275 | 0.1% | 7.24B | 2 |
| 131 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 220 | +1 | 19,716 | 0.2% | 68.98B | 2 |
| 132 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 192 | -8 | 44,665 | 0.1% | 7.70B | 5 |
| 133 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 191 | +35 | 3,002 | 0.2% | 31.59B | 6 |
| 134 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 184 | 0 | 5,071 | 0.2% | 70.55B | 3 |
| 135 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 184 | +2 | 12,718 | 0.2% | 70.55B | 2 |
| 136 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 179 | -12 | 16,646 | 0.2% | 7.29B | 2 |
| 137 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 176 | -11 | 5,180 | 0.2% | 437.8M | 1 |
| 138 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 171 | -2 | 2,572 | 0.2% | — | 1 |
| 139 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 164 | +1 | 28,433 | 0.1% | 46.70B | 6 |
| 140 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 150 | +14 | 7,490 | 0.1% | 31.59B | 6 |
| 141 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 148 | +1 | 5,509 | 0.1% | 353.4M | 2 |
| 142 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 143 | +4 | 1,170 | 0.1% | — | 1 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 88 | -3 | 38,723 | 0.1% | 70.55B | 3 |
| 144 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 79 | 0 | 7,258 | 0.1% | 1.20B | 2 |
| 145 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 70 | 0 | 1,318 | 0.1% | 560.9M | 1 |
| 146 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 44 | 0 | 404 | 0.0% | 437.8M | 1 |
| 147 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 40 | 0 | 439 | 0.0% | 321.0M | 1 |
| 148 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 36 | 0 | 263 | 0.0% | 15.17B | 3 |
| 149 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 33 | 0 | 204 | 0.0% | 8.16B | 3 |
| 150 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | +2 | 232 | 0.0% | 437.8M | 1 |
| 151 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 27 | -1 | 145 | 0.0% | 7.24B | 1 |
| 152 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | 0 | 281 | 0.0% | 437.8M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 19 | 0 | 167 | 0.0% | 437.8M | 1 |
| 154 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 10 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 155 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 156 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 157 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 158 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,414,641 | 307,441,843 | 30 | 2.1% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 400,041 | 6,070,660 | 7 | 6.5% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 204,896 | 397,607 | 6 | 41.2% |
| 4 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 88,032 | 2,648,920 | 11 | 3.2% |
| 5 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 79,285 | 6,411,229 | 12 | 1.2% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 55,106 | 1,423,836 | 5 | 3.6% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 19,456 | 564,852 | 13 | 2.9% |
| 8 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 14,735 | 399,699 | 10 | 2.9% |
| 9 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,406 | 1,449,624 | 11 | 0.9% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,601 | 448,226 | 6 | 2.5% |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,998 | 371,755 | 14 | 2.5% |
| 12 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,572 | 202,396 | 3 | 2.8% |
| 13 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 8,445 | 76,704 | 1 | 4.8% |
| 14 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 5,577 | 81,884 | 1 | 3.1% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,492 | 493,840 | 3 | 0.9% |
| 16 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,039 | 859,922 | 3 | 0.5% |
| 17 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,601 | 699,908 | 2 | 0.6% |
| 18 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 4,542 | 139,803 | 1 | 1.9% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,868 | 661,530 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,833 | 1,162,716 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,688 | 106,236 | 4 | 1.3% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,785 | 155,106 | 2 | 0.7% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 1,608 | 9,513 | 1 | 1.5% |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 789 | 24,462 | 4 | 0.6% |
| 25 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,872,047 | 60,036,094 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 345,163 | 4,687,321 | 5 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 200,568 | 268,372 | 9 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 46,172 | 733,426 | 18 |
| 5 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 29,637 | 4,180,670 | 21 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B (base) | 24,443 | 243,788 | 22 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2512) | 9,171 | 44,558 | 34 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 8,501 | 20,588 | 38 |
| 9 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 8,445 | 76,704 | 39 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,110 | 118,288 | 41 |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 5,577 | 81,884 | 45 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 4,542 | 139,803 | 50 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,517 | 154,000 | 51 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,377 | 377,633 | 54 |
| 15 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,170 | 37,612 | 56 |
| 16 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 4,056 | 53,748 | 58 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,067 | 102,133 | 70 |
| 18 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,044 | 358,252 | 71 |
| 19 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,001 | 80,582 | 73 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,915 | 159,869 | 74 |
| 21 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 1,608 | 9,513 | 85 |
| 22 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,488 | 802,135 | 88 |
| 23 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,034 | 58,584 | 98 |
| 24 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 438 | 12,461 | 117 |
| 25 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 157 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 41.2% | 204,896 | 397,607 | 3 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 6.5% | 400,041 | 6,070,660 | 2 |
| 3 | [openeurollm](https://huggingface.co/openeurollm) | 4.8% | 8,445 | 76,704 | 13 |
| 4 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.6% | 55,106 | 1,423,836 | 6 |
| 5 | [utter-project](https://huggingface.co/utter-project) | 3.2% | 88,032 | 2,648,920 | 4 |
| 6 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 3.1% | 5,577 | 81,884 | 14 |
| 7 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 2.9% | 14,735 | 399,699 | 8 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.9% | 19,456 | 564,852 | 7 |
| 9 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,572 | 202,396 | 12 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.5% | 11,998 | 371,755 | 11 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,601 | 448,226 | 10 |
| 12 | [mistralai](https://huggingface.co/mistralai) | 2.1% | 6,414,641 | 307,441,843 | 1 |
| 13 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.9% | 4,542 | 139,803 | 18 |
| 14 | [domyn](https://huggingface.co/domyn) | 1.5% | 1,608 | 9,513 | 23 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.3% | 2,688 | 106,236 | 21 |
| 16 | [speakleash](https://huggingface.co/speakleash) | 1.2% | 79,285 | 6,411,229 | 5 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 0.9% | 14,406 | 1,449,624 | 9 |
| 18 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.9% | 5,492 | 493,840 | 15 |
| 19 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,785 | 155,106 | 22 |
| 20 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 789 | 24,462 | 24 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.6% | 4,601 | 699,908 | 17 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,039 | 859,922 | 16 |
| 23 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,868 | 661,530 | 19 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,833 | 1,162,716 | 20 |
| 25 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
