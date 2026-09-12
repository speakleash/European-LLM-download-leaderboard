# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-09-12
- **Generated at:** 2026-09-12T10:23:29Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,505,030 | -24,245 | 56,033,093 | 4.5% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,509,238 | +21,614 | 63,629,956 | 2.4% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 611,816 | +1,483 | 3,487,070 | 17.1% | 13.95B | 6 |
| 4 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 526,032 | +1,606 | 16,107,785 | 3.2% | 12.25B | 3 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 513,554 | +65,717 | 45,392,488 | 1.1% | 7.24B | 2 |
| 6 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 506,522 | -5,523 | 3,903,193 | 12.7% | 8.05B | 2 |
| 7 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 431,160 | -21,342 | 5,445,624 | 7.8% | 4.25B | 7 |
| 8 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 371,783 | +26,134 | 4,493,302 | 8.1% | 24.01B | 2 |
| 9 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 353,594 | +145 | 415,037 | 68.7% | 353.4M | 1 |
| 10 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 351,242 | +176 | 411,570 | 68.7% | 1.20B | 1 |
| 11 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 340,916 | +146 | 396,620 | 68.6% | 3.21B | 1 |
| 12 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 308,019 | +9,662 | 32,175,769 | 1.0% | 46.70B | 2 |
| 13 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 253,130 | -309 | 4,111,952 | 6.0% | 11.34B | 8 |
| 14 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 252,755 | +1,427 | 2,634,497 | 9.2% | 24.01B | 1 |
| 15 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 203,068 | -1,905 | 8,410,183 | 2.4% | 8.02B | 1 |
| 16 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 202,205 | -10,444 | 2,051,716 | 9.4% | 8.92B | 6 |
| 17 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 146,533 | +13,833 | 341,596 | 33.2% | 22.64B | 1 |
| 18 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 144,662 | -758 | 1,029,822 | 12.8% | 127.70B | 2 |
| 19 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 130,603 | -111 | 5,258,548 | 2.4% | 24.01B | 1 |
| 20 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 100,187 | +1,160 | 516,733 | 16.2% | 70.60B | 2 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 76,405 | -365 | 681,401 | 9.8% | 23.57B | 2 |
| 22 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 70,001 | +801 | 620,258 | 9.7% | 23.57B | 2 |
| 23 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 65,653 | -707 | 7,541,456 | 0.9% | 23.57B | 2 |
| 24 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 57,356 | -163 | 630,284 | 7.9% | 119.40B | 3 |
| 25 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 39,440 | -24 | 11,181,872 | 0.3% | 140.63B | 2 |
| 26 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 31,682 | -3,224 | 131,144 | 13.7% | 9.15B | 1 |
| 27 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 30,183 | +183 | 662,611 | 4.0% | 7.77B | 8 |
| 28 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,886 | +220 | 472,924 | 3.5% | 9.15B | 1 |
| 29 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 17,660 | -325 | 345,242 | 4.0% | 125.03B | 1 |
| 30 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,334 | -162 | 321,507 | 3.9% | 24.01B | 2 |
| 31 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 15,930 | +48 | 768,877 | 1.8% | 11.25B | 10 |
| 32 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,460 | +1,095 | 27,067 | 12.2% | 8.90B | 1 |
| 33 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,067 | +1,617 | 20,610 | 12.5% | 72.01B | 1 |
| 34 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 14,615 | +2 | 694,627 | 1.8% | 1.66B | 1 |
| 35 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 13,783 | -74 | 5,299,374 | 0.3% | 7.25B | 1 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,219 | -105 | 64,501 | 7.4% | — | 5 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,593 | +698 | 203,509 | 3.5% | — | 1 |
| 38 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 9,501 | +69 | 501,258 | 1.6% | 7.24B | 8 |
| 39 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 8,974 | -87 | 105,218 | 4.4% | 8.42B | 5 |
| 40 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,805 | -153 | 4,920,247 | 0.2% | 122.61B | 1 |
| 41 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,144 | +7 | 30,817 | 3.9% | 14.03B | 1 |
| 42 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 4,936 | +89 | 161,505 | 1.9% | 11.17B | 16 |
| 43 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,931 | -185 | 5,141,396 | 0.1% | 22.25B | 1 |
| 44 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,465 | +5 | 28,513 | 3.5% | 33.12B | 1 |
| 45 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,431 | -500 | 141,185 | 1.8% | 2.25B | 7 |
| 46 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 4,430 | +2 | 63,201 | 2.7% | 11.77B | 4 |
| 47 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 4,376 | -248 | 45,094 | 3.0% | 8.03B | 7 |
| 48 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,177 | +19 | 89,730 | 2.2% | 2.89B | 1 |
| 49 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 4,162 | -26 | 666,603 | 0.5% | 7.45B | 2 |
| 50 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,609 | -69 | 5,374,218 | 0.1% | 22.25B | 1 |
| 51 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,605 | +105 | 55,835 | 2.3% | 1.60B | 5 |
| 52 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,555 | -107 | 901,579 | 0.4% | 23.57B | 2 |
| 53 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 3,543 | +116 | 54,019 | 2.3% | 7.55B | 1 |
| 54 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 3,481 | -133 | 130,434 | 1.5% | 7.40B | 3 |
| 55 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 3,424 | +23 | 250,390 | 1.0% | 4.76B | 5 |
| 56 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 3,208 | +27 | 368,975 | 0.7% | 7.24B | 8 |
| 57 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 3,007 | -94 | 11,012 | 2.7% | 572.6M | 5 |
| 58 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,672 | -56 | 5,030,087 | 0.1% | 122.61B | 1 |
| 59 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,434 | -4 | 22,043 | 2.0% | 22.64B | 1 |
| 60 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 2,424 | +79 | 38,568 | 1.7% | 321.0M | 2 |
| 61 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 2,347 | -4 | 124,301 | 1.0% | 7.48B | 5 |
| 62 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,298 | +89 | 107,370 | 1.1% | 7.29B | 2 |
| 63 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 2,233 | -30 | 145,619 | 0.9% | 7.24B | 4 |
| 64 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,161 | +110 | 19,254 | 1.8% | 4.30B | 2 |
| 65 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,989 | +89 | 33,205 | 1.5% | 2.61B | 3 |
| 66 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,905 | +43 | 6,871 | 1.8% | 4.30B | 3 |
| 67 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,894 | -229 | 13,723 | 1.7% | 3.83B | 5 |
| 68 | Velvet 14B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 1,829 | +133 | 63,464 | 1.1% | 14.08B | 1 |
| 69 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,790 | -23 | 8,802 | 1.6% | 9.15B | 1 |
| 70 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,773 | +29 | 16,157 | 1.5% | 12.19B | 2 |
| 71 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,597 | 0 | 31,521 | 1.2% | 22.64B | 1 |
| 72 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 1,573 | -236 | 6,629 | 1.5% | 1.51B | 6 |
| 73 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,561 | -139 | 76,917 | 0.9% | 7.45B | 1 |
| 74 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,509 | -91 | 18,841 | 1.3% | 12.25B | 3 |
| 75 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,493 | +25 | 172,484 | 0.5% | 11.51B | 7 |
| 76 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,446 | +32 | 7,315 | 1.3% | 28.84B | 3 |
| 77 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,368 | -21 | 175,593 | 0.5% | 12.25B | 6 |
| 78 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,321 | +50 | 21,438 | 1.1% | 11.17B | 5 |
| 79 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 1,254 | +3 | 98,446 | 0.6% | 30.68B | 1 |
| 80 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,245 | +11 | 29,706 | 1.0% | 11.17B | 5 |
| 81 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,224 | +3 | 47,567 | 0.8% | 9.24B | 4 |
| 82 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,190 | +5 | 104,587 | 0.6% | 7.45B | 1 |
| 83 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,130 | +34 | 31,893 | 0.9% | 56.7M | 1 |
| 84 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,123 | -82 | 95,162 | 0.6% | 1.35B | 8 |
| 85 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,117 | -1 | 43,547 | 0.8% | 12.19B | 2 |
| 86 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,116 | +5 | 354,653 | 0.2% | — | 3 |
| 87 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 1,051 | +37 | 37,303 | 0.8% | 27.23B | 3 |
| 88 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,036 | -1 | 156,497 | 0.4% | 1.10B | 1 |
| 89 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,036 | -3 | 300,052 | 0.3% | 6.74B | 2 |
| 90 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,024 | -37 | 7,798 | 0.9% | 27.43B | 3 |
| 91 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,024 | +11 | 80,890 | 0.6% | 8.03B | 3 |
| 92 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 999 | +11 | 2,741 | 1.0% | 30.68B | 1 |
| 93 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 993 | +31 | 217,511 | 0.3% | 12.19B | 3 |
| 94 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 985 | +31 | 56,532 | 0.6% | 1.35B | 3 |
| 95 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 969 | +6 | 144,247 | 0.4% | 13.02B | 1 |
| 96 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 967 | -8 | 799,644 | 0.1% | — | 3 |
| 97 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 966 | +24 | 12,259 | 0.9% | 70.55B | 2 |
| 98 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 961 | 0 | 183,449 | 0.3% | 6.74B | 1 |
| 99 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 941 | +2 | 38,232 | 0.7% | 70.55B | 3 |
| 100 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 928 | -166 | 48,164 | 0.6% | 7.77B | 1 |
| 101 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 893 | -161 | 81,887 | 0.5% | 9.15B | 1 |
| 102 | Velvet 2B | IT | Almawave | [Almawave](https://huggingface.co/Almawave) | 854 | +4 | 83,380 | 0.5% | 2.22B | 1 |
| 103 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 779 | +13 | 227,170 | 0.2% | 35.13B | 4 |
| 104 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 760 | +1 | 1,064 | 0.8% | 27.23B | 3 |
| 105 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 727 | -24 | 70,042 | 0.4% | 8.03B | 3 |
| 106 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 666 | +11 | 6,590 | 0.6% | 9.82B | 1 |
| 107 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 646 | +33 | 450,870 | 0.1% | 40.43B | 1 |
| 108 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 627 | -3 | 13,508 | 0.6% | 4.33B | 3 |
| 109 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 606 | +7 | 321,663 | 0.1% | 7.24B | 2 |
| 110 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 590 | +5 | 149,597 | 0.2% | 23.57B | 2 |
| 111 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 575 | +23 | 17,947 | 0.5% | 1.20B | 2 |
| 112 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 574 | +4 | 3,368 | 0.6% | 8.03B | 3 |
| 113 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 556 | +48 | 11,100 | 0.5% | 31.59B | 6 |
| 114 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 519 | +197 | 1,249 | 0.5% | 31.58B | 2 |
| 115 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 515 | +10 | 13,571 | 0.5% | 353.4M | 2 |
| 116 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 514 | +13 | 32,184 | 0.4% | 40.43B | 2 |
| 117 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 443 | -17 | 51,645 | 0.3% | 7.24B | 5 |
| 118 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 422 | +9 | 44,215 | 0.3% | 7.70B | 5 |
| 119 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 421 | -24 | 7,018 | 0.4% | 31.59B | 6 |
| 120 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 415 | -18 | 1,981 | 0.4% | 31.59B | 6 |
| 121 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 405 | -2 | 19,504 | 0.3% | 3.20B | 2 |
| 122 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 404 | -69 | 232,274 | 0.1% | — | 2 |
| 123 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 395 | +6 | 2,630 | 0.4% | 560.9M | 2 |
| 124 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 392 | -15 | 106,712 | 0.2% | — | 3 |
| 125 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 387 | -17 | 50,571 | 0.3% | 7.24B | 1 |
| 126 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 385 | -7 | 38,794 | 0.3% | 7.48B | 2 |
| 127 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 368 | +23 | 15,511 | 0.3% | 1.54B | 4 |
| 128 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 354 | -8 | 2,324 | 0.3% | 4.02B | 2 |
| 129 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 346 | +12 | 75,742 | 0.2% | 7.04B | 4 |
| 130 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 310 | -23 | 4,847 | 0.3% | 437.8M | 1 |
| 131 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 273 | -9 | 26,889 | 0.2% | 9.24B | 2 |
| 132 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 266 | -12 | 41,439 | 0.2% | 11.17B | 1 |
| 133 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 219 | -5 | 21,235 | 0.2% | 9.24B | 2 |
| 134 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 193 | +2 | 887 | 0.2% | — | 1 |
| 135 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 191 | +16 | 21,410 | 0.2% | 2.61B | 2 |
| 136 | OpenEuroLLM Prelude | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 191 | +1 | 1,938 | 0.2% | — | 1 |
| 137 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 187 | +4 | 5,216 | 0.2% | 353.4M | 2 |
| 138 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 163 | -1 | 16,239 | 0.1% | 7.29B | 2 |
| 139 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 158 | -3 | 5,043 | 0.2% | 11.51B | 5 |
| 140 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 157 | +5 | 19,283 | 0.1% | 68.98B | 2 |
| 141 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 154 | +1 | 11,434 | 0.1% | 27.23B | 2 |
| 142 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 132 | +3 | 7,079 | 0.1% | 1.20B | 2 |
| 143 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 127 | +7 | 38,486 | 0.1% | 70.55B | 3 |
| 144 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 127 | -13 | 1,220 | 0.1% | 560.9M | 1 |
| 145 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 116 | +5 | 2,207 | 0.1% | — | 1 |
| 146 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 94 | 0 | 174 | 0.1% | 437.8M | 1 |
| 147 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 90 | +19 | 4,739 | 0.1% | 70.55B | 3 |
| 148 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 86 | -1 | 28,145 | 0.1% | 46.70B | 6 |
| 149 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 76 | +1 | 6,031 | 0.1% | 12.25B | 3 |
| 150 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 61 | -2 | 899 | 0.1% | — | 1 |
| 151 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 53 | +2 | 245 | 0.1% | 437.8M | 1 |
| 152 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 43 | -19 | 318 | 0.0% | 321.0M | 1 |
| 153 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 20 | +1 | 130 | 0.0% | 437.8M | 1 |
| 154 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 16 | -15 | 346 | 0.0% | 437.8M | 1 |
| 155 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 13 | 0 | 145 | 0.0% | 8.16B | 3 |
| 156 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 10 | +1 | 101 | 0.0% | 7.24B | 1 |
| 157 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 9 | 0 | 196 | 0.0% | 15.17B | 3 |
| 158 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 8,103,192 | 294,354,658 | 30 | 2.8% |
| 2 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 1,051,782 | 1,418,709 | 11 | 69.3% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 643,710 | 4,498,967 | 7 | 14.0% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 297,356 | 6,244,228 | 12 | 4.7% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 232,128 | 2,023,465 | 11 | 10.9% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 36,702 | 1,335,014 | 5 | 2.6% |
| 7 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 19,248 | 423,845 | 6 | 3.7% |
| 8 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 12,439 | 529,667 | 13 | 2.0% |
| 9 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 9,781 | 188,227 | 3 | 3.4% |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 8,619 | 349,590 | 14 | 1.9% |
| 11 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 8,238 | 184,150 | 6 | 2.9% |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 7,428 | 364,375 | 10 | 1.6% |
| 13 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 6,913 | 848,107 | 3 | 0.7% |
| 14 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 3,814 | 690,638 | 2 | 0.5% |
| 15 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 3,481 | 130,434 | 1 | 1.5% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 2,966 | 484,193 | 3 | 0.5% |
| 17 | [Almawave](https://huggingface.co/Almawave) | Almawave | IT | 2,683 | 146,844 | 2 | 1.1% |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,275 | 101,528 | 4 | 1.1% |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 2,152 | 654,705 | 2 | 0.3% |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,108 | 151,694 | 2 | 0.8% |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 1,920 | 1,157,913 | 4 | 0.2% |
| 22 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 1,911 | 21,348 | 4 | 1.6% |
| 23 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 666 | 6,590 | 1 | 0.6% |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 346 | 75,742 | 1 | 0.2% |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 191 | 1,938 | 1 | 0.2% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,505,030 | 56,033,093 | 1 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 506,522 | 3,903,193 | 6 |
| 3 | [PleIAs](https://huggingface.co/PleIAs) | Pleias 350M Preview | 353,594 | 415,037 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 253,130 | 4,111,952 | 13 |
| 5 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-22B-Instruct (2512) | 146,533 | 341,596 | 17 |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 30,183 | 662,611 | 27 |
| 7 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 8,974 | 105,218 | 39 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Viking 13B | 5,144 | 30,817 | 41 |
| 9 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 4,430 | 63,201 | 46 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | Minerva Chat v0.1 | 4,177 | 89,730 | 48 |
| 11 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.6 | 4,162 | 666,603 | 49 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 7B v1.0 | 3,481 | 130,434 | 54 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 3,208 | 368,975 | 56 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT 7B v0.2 | 2,298 | 107,370 | 62 |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 4B (2512) | 1,905 | 6,871 | 66 |
| 16 | [Almawave](https://huggingface.co/Almawave) | Velvet 14B | 1,829 | 63,464 | 68 |
| 17 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 1,254 | 98,446 | 79 |
| 18 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Chat v0.1 | 1,123 | 95,162 | 84 |
| 19 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 1,116 | 354,653 | 86 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 1,036 | 156,497 | 88 |
| 21 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 967 | 799,644 | 96 |
| 22 | [domyn](https://huggingface.co/domyn) | Domyn Small v1.0 | 666 | 6,590 | 106 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 556 | 11,100 | 113 |
| 24 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Pharia-1-LLM-7B-control | 346 | 75,742 | 129 |
| 25 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude | 191 | 1,938 | 136 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [PleIAs](https://huggingface.co/PleIAs) | 69.3% | 1,051,782 | 1,418,709 | 2 |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | 14.0% | 643,710 | 4,498,967 | 3 |
| 3 | [utter-project](https://huggingface.co/utter-project) | 10.9% | 232,128 | 2,023,465 | 5 |
| 4 | [speakleash](https://huggingface.co/speakleash) | 4.7% | 297,356 | 6,244,228 | 4 |
| 5 | [LumiOpen](https://huggingface.co/LumiOpen) | 3.7% | 19,248 | 423,845 | 7 |
| 6 | [ilsp](https://huggingface.co/ilsp) | 3.4% | 9,781 | 188,227 | 9 |
| 7 | [cjvt](https://huggingface.co/cjvt) | 2.9% | 8,238 | 184,150 | 11 |
| 8 | [mistralai](https://huggingface.co/mistralai) | 2.8% | 8,103,192 | 294,354,658 | 1 |
| 9 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 36,702 | 1,335,014 | 6 |
| 10 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.0% | 12,439 | 529,667 | 8 |
| 11 | [mii-llm](https://huggingface.co/mii-llm) | 1.9% | 8,619 | 349,590 | 10 |
| 12 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.6% | 7,428 | 364,375 | 12 |
| 13 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 1.6% | 1,911 | 21,348 | 22 |
| 14 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 1.5% | 3,481 | 130,434 | 15 |
| 15 | [TildeAI](https://huggingface.co/TildeAI) | 1.1% | 2,275 | 101,528 | 18 |
| 16 | [Almawave](https://huggingface.co/Almawave) | 1.1% | 2,683 | 146,844 | 17 |
| 17 | [croissantllm](https://huggingface.co/croissantllm) | 0.8% | 2,108 | 151,694 | 20 |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.7% | 6,913 | 848,107 | 13 |
| 19 | [domyn](https://huggingface.co/domyn) | 0.6% | 666 | 6,590 | 23 |
| 20 | [OPI-PG](https://huggingface.co/OPI-PG) | 0.5% | 2,966 | 484,193 | 16 |
| 21 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 3,814 | 690,638 | 14 |
| 22 | [Voicelab](https://huggingface.co/Voicelab) | 0.3% | 2,152 | 654,705 | 19 |
| 23 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 0.2% | 346 | 75,742 | 24 |
| 24 | [openeurollm](https://huggingface.co/openeurollm) | 0.2% | 191 | 1,938 | 25 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 1,920 | 1,157,913 | 21 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
