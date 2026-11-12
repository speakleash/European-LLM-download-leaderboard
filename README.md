# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-12
- **Generated at:** 2026-11-12T14:56:12Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 186

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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,979,539 | +10,969 | 60,533,535 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,345,332 | -45,353 | 66,837,365 | 2.0% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 671,415 | +9,433 | 4,506,177 | 14.6% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 549,783 | +3,423 | 46,511,829 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 361,215 | +6,756 | 32,809,355 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 257,223 | +1,323 | 2,548,401 | 9.7% | 8.92B | 6 |
| 7 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 255,616 | -13,566 | 4,693,079 | 5.3% | 8.05B | 2 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 205,318 | -772 | 5,901,673 | 3.4% | 3.85B | 7 |
| 9 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 203,457 | -7,647 | 321,368 | 48.3% | 12.77B | 5 |
| 10 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 158,840 | +27 | 16,672,615 | 0.9% | 12.25B | 3 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 157,114 | -3,154 | 5,023,104 | 3.1% | 24.01B | 2 |
| 12 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,904 | +95 | 7,723,301 | 1.4% | 23.57B | 2 |
| 13 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 104,478 | -182 | 5,627,303 | 1.8% | 24.01B | 1 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 89,352 | +12,380 | 4,254,926 | 2.1% | 11.34B | 9 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 64,010 | +515 | 8,608,137 | 0.7% | 8.02B | 1 |
| 16 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 47,618 | -2,262 | 807,292 | 5.2% | 23.57B | 2 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 46,468 | -578 | 11,291,077 | 0.4% | 140.63B | 2 |
| 18 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 45,275 | -4 | 738,766 | 5.4% | 7.77B | 8 |
| 19 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,058 | +542 | 748,603 | 4.1% | 119.40B | 3 |
| 20 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,369 | +239 | 367,866 | 7.1% | 24.01B | 2 |
| 21 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 28,785 | -1,548 | 3,010,795 | 0.9% | 24.01B | 1 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,510 | +116 | 946,026 | 1.9% | 1.66B | 1 |
| 23 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 16,718 | +246 | 800,739 | 1.9% | 11.25B | 10 |
| 24 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 16,242 | — | 34,394 | 12.1% | 78.10B | 2 |
| 25 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,174 | -733 | 1,121,536 | 1.3% | 127.70B | 2 |
| 26 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 16,147 | +3,501 | 746,653 | 1.9% | 8.90B | 5 |
| 27 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,000 | — | 15,035 | 13.0% | — | 2 |
| 28 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,818 | +240 | 4,945,018 | 0.3% | 122.61B | 1 |
| 29 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,780 | — | 696,816 | 1.9% | 7.29B | 1 |
| 30 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,738 | -5 | 5,047,315 | 0.2% | 122.61B | 1 |
| 31 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,693 | +28 | 651,112 | 1.7% | 23.57B | 2 |
| 32 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,061 | -95 | 498,437 | 1.8% | 9.15B | 1 |
| 33 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,967 | -42 | 524,481 | 1.8% | 7.24B | 8 |
| 34 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,681 | -13,317 | 246,892 | 3.1% | — | 1 |
| 35 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 10,301 | -9 | 22,627 | 8.4% | 27.43B | 3 |
| 36 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 9,927 | -487 | 551,266 | 1.5% | 70.60B | 2 |
| 37 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,161 | +89 | 5,391,021 | 0.2% | 22.25B | 1 |
| 38 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,619 | +389 | 36,169 | 6.3% | 72.01B | 4 |
| 39 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,488 | -85 | 87,533 | 4.5% | — | 5 |
| 40 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,262 | -104 | 119,734 | 3.8% | 8.42B | 7 |
| 41 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,628 | +277 | 17,110 | 6.5% | 1.51B | 6 |
| 42 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 7,346 | -1,147 | 160,424 | 2.8% | 9.15B | 1 |
| 43 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,917 | -60 | 604,515 | 1.0% | 22.64B | 1 |
| 44 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,910 | +920 | 22,663 | 5.6% | 3.83B | 5 |
| 45 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,823 | +91 | 358,602 | 1.5% | 125.03B | 1 |
| 46 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 6,311 | +83 | 260,829 | 1.7% | 4.76B | 5 |
| 47 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,272 | +86 | 23,764 | 5.1% | 572.6M | 5 |
| 48 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,938 | +44 | 153,177 | 2.3% | 2.25B | 7 |
| 49 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,894 | — | 137,850 | 2.5% | 2.89B | 1 |
| 50 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,782 | +244 | 56,493 | 3.7% | 8.03B | 7 |
| 51 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 5,632 | +8 | 82,046 | 3.1% | 7.04B | 4 |
| 52 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,580 | — | 158,763 | 2.2% | 351.6M | 1 |
| 53 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,455 | +120 | 64,724 | 3.3% | 1.60B | 5 |
| 54 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,702 | +301 | 38,908 | 3.4% | 56.7M | 1 |
| 55 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,700 | -1 | 910,682 | 0.5% | 23.57B | 2 |
| 56 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,490 | -3 | 154,895 | 1.8% | 7.24B | 4 |
| 57 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,357 | -61 | 140,656 | 1.8% | 7.40B | 3 |
| 58 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,292 | — | 124,736 | 1.9% | 8.54B | 2 |
| 59 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,182 | +3 | 378,376 | 0.9% | 7.24B | 8 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,150 | -38 | 41,141 | 2.9% | 2.61B | 3 |
| 61 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,054 | +3 | 141,231 | 1.7% | 7.48B | 5 |
| 62 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,964 | +13 | 5,165,644 | 0.1% | 22.25B | 1 |
| 63 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,793 | +10 | 28,614 | 2.9% | 22.64B | 1 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,624 | +38 | 44,747 | 2.5% | 13.29B | 3 |
| 65 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,330 | +9 | 170,065 | 1.2% | 11.17B | 16 |
| 66 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,323 | +394 | 54,747 | 2.1% | 7.77B | 3 |
| 67 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,253 | +9 | 96,448 | 1.7% | 2.89B | 1 |
| 68 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,016 | +43 | 13,075 | 2.7% | 9.15B | 1 |
| 69 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 2,826 | — | 2,826 | 2.7% | 3.93B | 2 |
| 70 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,759 | +23 | 5,303,978 | 0.1% | 7.25B | 1 |
| 71 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 2,628 | — | 2,628 | 2.6% | 11.17B | 14 |
| 72 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,540 | -10 | 157,287 | 1.0% | 23.57B | 2 |
| 73 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,456 | +164 | 20,931 | 2.0% | 12.19B | 2 |
| 74 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,401 | +8 | 230,943 | 0.7% | 35.13B | 4 |
| 75 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,339 | +16 | 23,182 | 1.9% | 4.30B | 2 |
| 76 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,224 | -10 | 34,681 | 1.7% | 14.03B | 1 |
| 77 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,165 | -5 | 86,621 | 1.2% | 9.15B | 1 |
| 78 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,143 | +44 | 102,591 | 1.1% | 30.68B | 1 |
| 79 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,078 | +21 | 358,666 | 0.5% | — | 3 |
| 80 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,061 | +26 | 81,033 | 1.1% | 7.45B | 1 |
| 81 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,049 | +28 | 52,049 | 1.3% | 9.24B | 4 |
| 82 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,037 | +393 | 454,794 | 0.4% | 40.43B | 1 |
| 83 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,000 | +22 | 160,295 | 0.8% | 1.10B | 1 |
| 84 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,967 | +28 | 108,566 | 0.9% | 7.45B | 1 |
| 85 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,900 | +29 | 35,248 | 1.4% | 22.64B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,898 | +28 | 303,685 | 0.5% | 6.74B | 2 |
| 87 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,884 | +24 | 187,023 | 0.7% | 6.74B | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,817 | +23 | 147,739 | 0.7% | 13.02B | 1 |
| 89 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,806 | -696 | 179,989 | 0.6% | 12.25B | 6 |
| 90 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,787 | +81 | 9,878 | 1.6% | 9.82B | 1 |
| 91 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,726 | -16 | 41,074 | 1.2% | 70.55B | 3 |
| 92 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,668 | -644 | 44,831 | 1.2% | 12.25B | 3 |
| 93 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,644 | — | 9,667 | 1.5% | 40.43B | 2 |
| 94 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,561 | -4 | 54,890 | 1.0% | 7.24B | 5 |
| 95 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,528 | +11 | 802,391 | 0.2% | — | 3 |
| 96 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,528 | +22 | 20,868 | 1.3% | 1.20B | 2 |
| 97 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,496 | -3 | 53,653 | 1.0% | 7.24B | 1 |
| 98 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,417 | — | 1,417 | 1.4% | 3.93B | 1 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,405 | -15 | 9,725 | 1.3% | 4.30B | 3 |
| 100 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,334 | +18 | 16,104 | 1.1% | 353.4M | 2 |
| 101 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,330 | +113 | 416,409 | 0.3% | 1.20B | 1 |
| 102 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,329 | +14 | 9,565 | 1.2% | 28.84B | 3 |
| 103 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,281 | +19 | 175,212 | 0.5% | 11.51B | 7 |
| 104 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,229 | +129 | 419,807 | 0.2% | 353.4M | 1 |
| 105 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,212 | -11 | 31,868 | 0.9% | 33.12B | 1 |
| 106 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,131 | +25 | 56,883 | 0.7% | 7.55B | 1 |
| 107 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,106 | -8 | 219,206 | 0.3% | 12.19B | 3 |
| 108 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,075 | +42 | 45,237 | 0.7% | 12.19B | 2 |
| 109 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,062 | +116 | 401,191 | 0.2% | 3.21B | 1 |
| 110 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,057 | +22 | 58,793 | 0.7% | 1.35B | 3 |
| 111 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 921 | +1 | 671,381 | 0.1% | 7.45B | 2 |
| 112 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 898 | -13 | 24,079 | 0.7% | 11.17B | 5 |
| 113 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 853 | +53 | 14,847 | 0.7% | 4.33B | 3 |
| 114 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 852 | +20 | 233,669 | 0.3% | — | 2 |
| 115 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 850 | — | 2,873 | 0.8% | 40.43B | 2 |
| 116 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 796 | — | 1,706 | 0.8% | 608.3M | 1 |
| 117 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 784 | -17 | 31,858 | 0.6% | 11.17B | 5 |
| 118 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 783 | +28 | 96,692 | 0.4% | 1.35B | 8 |
| 119 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 776 | — | 796 | 0.8% | 437.8M | 2 |
| 120 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 750 | +8 | 112,533 | 0.4% | 7.29B | 2 |
| 121 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 688 | +1 | 82,304 | 0.4% | 8.03B | 3 |
| 122 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 687 | +1 | 17,072 | 0.6% | 1.54B | 4 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 678 | -14 | 2,114 | 0.7% | 27.23B | 3 |
| 124 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 611 | +5 | 22,214 | 0.5% | 9.24B | 2 |
| 125 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 610 | +16 | 20,895 | 0.5% | 3.20B | 2 |
| 126 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 607 | +7 | 28,035 | 0.5% | 9.24B | 2 |
| 127 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 572 | +17 | 3,751 | 0.6% | 30.68B | 1 |
| 128 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 559 | — | 559 | 0.6% | 3.93B | 1 |
| 129 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 558 | — | 558 | 0.6% | 3.93B | 1 |
| 130 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 553 | — | 553 | 0.5% | 3.93B | 1 |
| 131 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 550 | — | 550 | 0.5% | 3.93B | 1 |
| 132 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 442 | -24 | 4,476 | 0.4% | 8.03B | 3 |
| 133 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 428 | 0 | 12,461 | 0.4% | 31.59B | 6 |
| 134 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 423 | +1 | 12,256 | 0.4% | 27.23B | 2 |
| 135 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 422 | -4 | 1,719 | 0.4% | — | 1 |
| 136 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 399 | — | 1,150 | 0.4% | 437.8M | 1 |
| 137 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 378 | +20 | 5,697 | 0.4% | 11.51B | 5 |
| 138 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 371 | +11 | 3,440 | 0.4% | 560.9M | 2 |
| 139 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 320 | -22 | 22,220 | 0.3% | 2.61B | 2 |
| 140 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 307 | +10 | 2,873 | 0.3% | 4.02B | 2 |
| 141 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 300 | +21 | 32,952 | 0.2% | 40.43B | 2 |
| 142 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 283 | +3 | 37,924 | 0.2% | 27.23B | 3 |
| 143 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 274 | -2 | 107,321 | 0.1% | — | 3 |
| 144 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 266 | +5 | 70,617 | 0.2% | 8.03B | 3 |
| 145 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 232 | -5 | 39,465 | 0.2% | 7.48B | 2 |
| 146 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 207 | 0 | 16,699 | 0.2% | 7.29B | 2 |
| 147 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 205 | +7 | 322,330 | 0.0% | 7.24B | 2 |
| 148 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 203 | -1 | 41,968 | 0.1% | 11.17B | 1 |
| 149 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 198 | — | 1,061 | 0.2% | 9.15B | 1 |
| 150 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 189 | -5 | 19,728 | 0.2% | 68.98B | 2 |
| 151 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 187 | — | 29,834 | 0.1% | 1.01B | 1 |
| 152 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 185 | 0 | 3,002 | 0.2% | 31.59B | 6 |
| 153 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 178 | -8 | 12,758 | 0.2% | 70.55B | 2 |
| 154 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | — | 170 | 0.2% | 7.77B | 1 |
| 155 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 164 | -3 | 44,697 | 0.1% | 7.70B | 5 |
| 156 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 156 | 0 | 1,202 | 0.2% | — | 1 |
| 157 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 145 | — | 2,925 | 0.1% | 40.43B | 2 |
| 158 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | +2 | 5,541 | 0.1% | 353.4M | 2 |
| 159 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 138 | -6 | 2,584 | 0.1% | — | 1 |
| 160 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 138 | -22 | 28,469 | 0.1% | 46.70B | 6 |
| 161 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 127 | +3 | 7,497 | 0.1% | 31.59B | 6 |
| 162 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 103 | 0 | 5,091 | 0.1% | 70.55B | 3 |
| 163 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 99 | -1 | 5,197 | 0.1% | 437.8M | 1 |
| 164 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 76 | -7 | 38,737 | 0.1% | 70.55B | 3 |
| 165 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 73 | — | 971 | 0.1% | 40.43B | 2 |
| 166 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 63 | -1 | 1,324 | 0.1% | 560.9M | 1 |
| 167 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 60 | +1 | 7,273 | 0.1% | 1.20B | 2 |
| 168 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 58 | — | 616 | 0.1% | 6.25B | 2 |
| 169 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 52 | — | 230 | 0.1% | 40.43B | 2 |
| 170 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 50 | 0 | 456 | 0.0% | 321.0M | 1 |
| 171 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 50 | — | 385 | 0.0% | 7.77B | 2 |
| 172 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 47 | +3 | 418 | 0.0% | 437.8M | 1 |
| 173 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 46 | +3 | 220 | 0.0% | 8.16B | 3 |
| 174 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 45 | +2 | 250 | 0.0% | 437.8M | 1 |
| 175 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 43 | +3 | 274 | 0.0% | 15.17B | 3 |
| 176 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 36 | — | 1,455 | 0.0% | 8.03B | 1 |
| 177 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 32 | 0 | 151 | 0.0% | 7.24B | 1 |
| 178 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +1 | 181 | 0.0% | 437.8M | 1 |
| 179 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | +1 | 291 | 0.0% | 437.8M | 1 |
| 180 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 14 | — | 374 | 0.0% | 12.25B | 1 |
| 181 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 182 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 183 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 184 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 0 | 0 | 0 | 0.0% | — | 0 |
| 185 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |
| 186 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 0 | 0 | 0 | 0.0% | — | 0 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,276,685 | 309,382,928 | 32 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 311,119 | 6,090,704 | 7 | 5.0% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 207,764 | 451,422 | 6 | 37.7% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 142,359 | 6,498,437 | 13 | 2.2% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 70,875 | 2,664,638 | 12 | 2.6% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 59,915 | 1,452,273 | 13 | 3.9% |
| 7 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 22,377 | 569,552 | 13 | 3.3% |
| 8 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 21,874 | 116,440 | 2 | 10.1% |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,310 | 591,839 | 5 | 2.9% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,545 | 1,455,314 | 12 | 1.1% |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,476 | 451,942 | 6 | 2.6% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,997 | 375,965 | 16 | 2.7% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 8,658 | 203,896 | 3 | 2.8% |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,250 | 16,341 | 7 | 7.1% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 6,136 | 402,693 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,701 | 495,057 | 3 | 1.0% |
| 17 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 4,949 | 860,980 | 3 | 0.5% |
| 18 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,387 | 700,706 | 2 | 0.5% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,976 | 662,351 | 2 | 0.5% |
| 20 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,843 | 1,163,109 | 4 | 0.2% |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,804 | 106,836 | 4 | 1.4% |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,840 | 155,485 | 2 | 0.7% |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 748 | 24,469 | 4 | 0.6% |
| 24 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 0 | 0 | 2 | 0.0% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 0 | 0 | 1 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 1,979,539 | 60,533,535 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 255,616 | 4,693,079 | 7 |
| 3 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 203,457 | 321,368 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 89,352 | 4,254,926 | 14 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 45,275 | 738,766 | 18 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,510 | 946,026 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 16,242 | 34,394 | 24 |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 10,301 | 22,627 | 35 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,262 | 119,734 | 40 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,894 | 137,850 | 49 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,782 | 56,493 | 50 |
| 12 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,702 | 38,908 | 54 |
| 13 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,490 | 154,895 | 56 |
| 14 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,182 | 378,376 | 59 |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 2,826 | 2,826 | 69 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,143 | 102,591 | 78 |
| 17 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,078 | 358,666 | 79 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,061 | 81,033 | 80 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,000 | 160,295 | 83 |
| 20 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,806 | 179,989 | 89 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,528 | 802,391 | 95 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,057 | 58,793 | 110 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 428 | 12,461 | 133 |
| 24 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 0 | 0 | 185 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 0 | 0 | 184 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 37.7% | 207,764 | 451,422 | 3 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 10.1% | 21,874 | 116,440 | 8 |
| 3 | [domyn](https://huggingface.co/domyn) | 7.1% | 8,250 | 16,341 | 14 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 5.0% | 311,119 | 6,090,704 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.9% | 59,915 | 1,452,273 | 6 |
| 6 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3.3% | 22,377 | 569,552 | 7 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,310 | 591,839 | 9 |
| 8 | [ilsp](https://huggingface.co/ilsp) | 2.8% | 8,658 | 203,896 | 13 |
| 9 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,997 | 375,965 | 12 |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,476 | 451,942 | 11 |
| 11 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 70,875 | 2,664,638 | 5 |
| 12 | [speakleash](https://huggingface.co/speakleash) | 2.2% | 142,359 | 6,498,437 | 4 |
| 13 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,276,685 | 309,382,928 | 1 |
| 14 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,804 | 106,836 | 21 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 6,136 | 402,693 | 15 |
| 16 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,545 | 1,455,314 | 10 |
| 17 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,701 | 495,057 | 16 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,840 | 155,485 | 22 |
| 19 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.6% | 748 | 24,469 | 23 |
| 20 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,387 | 700,706 | 18 |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,976 | 662,351 | 19 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 4,949 | 860,980 | 17 |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,843 | 1,163,109 | 20 |
| 24 | [Almawave](https://huggingface.co/Almawave) | 0.0% | 0 | 0 | 24 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | 0.0% | 0 | 0 | 25 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
