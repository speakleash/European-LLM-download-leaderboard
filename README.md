# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-16
- **Generated at:** 2026-11-16T11:52:15Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 253

Standalone generative LLMs, including multimodal models that generate text. Auxiliary draft models and classification-only adapters are excluded.

Historical snapshots retain their original scope; changes across the scope correction on 2026-11-16 also reflect the removed repositories.

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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,021,775 | +9,748 | 60,805,659 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,159,669 | -34,791 | 66,958,424 | 1.7% | 7.24B | 1 |
| 3 | LightOnOCR 2 1B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 812,022 | — | 4,933,530 | 16.1% | 1.01B | 6 |
| 4 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 667,840 | 0 | 4,560,252 | 14.3% | 13.95B | 6 |
| 5 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 551,470 | -899 | 46,553,497 | 1.2% | 7.24B | 2 |
| 6 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 359,851 | -1,309 | 32,856,363 | 1.1% | 46.70B | 2 |
| 7 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 264,373 | 0 | 2,577,933 | 9.9% | 8.92B | 6 |
| 8 | VLT5 Base Keywords | PL | VoiceLab | [Voicelab](https://huggingface.co/Voicelab) | 219,626 | — | 1,860,898 | 11.2% | 275.1M | 1 |
| 9 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213,120 | 0 | 332,031 | 49.3% | 12.77B | 5 |
| 10 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 210,956 | 0 | 5,927,721 | 3.5% | 3.85B | 7 |
| 11 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 201,288 | -13,785 | 4,696,239 | 4.2% | 8.05B | 2 |
| 12 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 145,331 | -1,224 | 16,687,585 | 0.9% | 12.25B | 3 |
| 13 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 140,087 | -4,001 | 5,041,492 | 2.7% | 24.01B | 2 |
| 14 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 122,460 | -215 | 4,288,054 | 2.8% | 11.34B | 10 |
| 15 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 105,616 | +4,598 | 5,656,809 | 1.8% | 24.01B | 1 |
| 16 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 101,326 | -780 | 7,732,991 | 1.3% | 23.57B | 2 |
| 17 | Voxtral Mini 3B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 86,069 | — | 6,580,241 | 1.3% | 4.68B | 1 |
| 18 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,418 | +202 | 8,612,489 | 0.7% | 8.02B | 1 |
| 19 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,827 | +41 | 11,297,423 | 0.4% | 140.63B | 2 |
| 20 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 38,706 | +33 | 740,716 | 4.6% | 7.77B | 7 |
| 21 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 38,252 | -2,243 | 807,720 | 4.2% | 23.57B | 2 |
| 22 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 35,162 | 0 | 751,343 | 4.1% | 119.40B | 3 |
| 23 | Devstral Small 2 (24B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 26,373 | 0 | 3,012,289 | 0.8% | 24.01B | 1 |
| 24 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,727 | 0 | 369,773 | 4.4% | 24.01B | 2 |
| 25 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,733 | -155 | 948,064 | 1.9% | 1.66B | 1 |
| 26 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 17,522 | +637 | 803,455 | 1.9% | 11.25B | 10 |
| 27 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 16,626 | 0 | 16,686 | 14.2% | — | 2 |
| 28 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,453 | 0 | 749,384 | 1.8% | 8.90B | 5 |
| 29 | Mamba-Codestral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,332 | +181 | 699,360 | 1.9% | 7.29B | 1 |
| 30 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,084 | 0 | 1,123,039 | 1.2% | 127.70B | 2 |
| 31 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,703 | -17 | 4,946,542 | 0.3% | 122.61B | 1 |
| 32 | LightOnOCR 3 4B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 14,321 | — | 25,187 | 11.4% | 4.54B | 1 |
| 33 | LightOnOCR 3 0.8B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 14,168 | — | 18,886 | 11.9% | 853.0M | 1 |
| 34 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 13,624 | 0 | 35,434 | 10.1% | 78.10B | 2 |
| 35 | LightOnOCR 1B (1025) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 12,979 | — | 1,348,838 | 0.9% | 1.16B | 1 |
| 36 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 12,815 | -20 | 5,047,833 | 0.2% | 122.61B | 1 |
| 37 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 12,462 | +1,199 | 249,586 | 3.6% | — | 1 |
| 38 | Devstral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 11,974 | -172 | 652,172 | 1.6% | 23.57B | 2 |
| 39 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 10,967 | -101 | 499,402 | 1.8% | 9.15B | 1 |
| 40 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,571 | -66 | 525,863 | 1.7% | 7.24B | 8 |
| 41 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,374 | +122 | 5,392,215 | 0.2% | 22.25B | 1 |
| 42 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,472 | 0 | 36,685 | 6.2% | 72.01B | 4 |
| 43 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,053 | 0 | 552,042 | 1.2% | 70.60B | 2 |
| 44 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,807 | 0 | 88,568 | 4.1% | — | 5 |
| 45 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,608 | 0 | 23,533 | 6.2% | 3.83B | 5 |
| 46 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 7,485 | +210 | 262,428 | 2.1% | 4.76B | 8 |
| 47 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,452 | 0 | 17,379 | 6.3% | 1.51B | 6 |
| 48 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,265 | -1,273 | 120,481 | 3.3% | 8.42B | 7 |
| 49 | Pixtral 12B (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,063 | — | 143,291 | 2.9% | — | 2 |
| 50 | Devstral 2 (123B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,061 | 0 | 359,498 | 1.5% | 125.03B | 1 |
| 51 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,704 | 0 | 605,427 | 1.0% | 22.64B | 1 |
| 52 | Voxtral Small 24B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,691 | — | 998,363 | 0.6% | 24.26B | 1 |
| 53 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,398 | 0 | 161,604 | 2.4% | 9.15B | 1 |
| 54 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,277 | 0 | 24,143 | 5.1% | 572.6M | 5 |
| 55 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 5,948 | -39 | 57,152 | 3.8% | 8.03B | 7 |
| 56 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,847 | -1 | 138,604 | 2.5% | 2.89B | 1 |
| 57 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,648 | -40 | 153,627 | 2.2% | 2.25B | 7 |
| 58 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,601 | +2 | 159,558 | 2.2% | 351.6M | 1 |
| 59 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 5,442 | -704 | 5,442 | 5.2% | 11.17B | 8 |
| 60 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,360 | +173 | 65,382 | 3.2% | 1.60B | 9 |
| 61 | OpenEuroLLM Prelude-base 9B | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 4,773 | +4,773 | 78,823 | 2.7% | 9.09B | 1 |
| 62 | ColGrep Agent 2B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 4,741 | — | 7,812 | 4.4% | 2.52B | 2 |
| 63 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,695 | 0 | 39,255 | 3.4% | 56.7M | 1 |
| 64 | Devstral Small (2505) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 4,645 | +16 | 911,052 | 0.5% | 23.57B | 2 |
| 65 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,444 | -43 | 155,495 | 1.7% | 7.24B | 4 |
| 66 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,236 | -6 | 125,260 | 1.9% | 8.54B | 2 |
| 67 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,226 | -37 | 141,189 | 1.8% | 7.40B | 3 |
| 68 | LightOnOCR 3 1B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 4,196 | — | 7,483 | 3.9% | 1.01B | 1 |
| 69 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,088 | -47 | 378,866 | 0.9% | 7.24B | 8 |
| 70 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,082 | 0 | 29,128 | 3.2% | 22.64B | 1 |
| 71 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,979 | -10 | 41,640 | 2.8% | 2.61B | 3 |
| 72 | Codestral 22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 3,907 | +19 | 5,166,157 | 0.1% | 22.25B | 1 |
| 73 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,688 | -221 | 131,370 | 1.6% | 7.48B | 9 |
| 74 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,585 | +10 | 55,302 | 2.3% | 7.77B | 3 |
| 75 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,541 | 0 | 44,956 | 2.4% | 13.29B | 3 |
| 76 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,378 | 0 | 22,921 | 2.7% | 27.43B | 3 |
| 77 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,253 | -11 | 96,868 | 1.7% | 2.89B | 1 |
| 78 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,186 | 0 | 3,229 | 3.1% | 3.93B | 2 |
| 79 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,129 | -8 | 13,387 | 2.8% | 9.15B | 1 |
| 80 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,020 | -110 | 170,408 | 1.1% | 11.17B | 16 |
| 81 | SalamandraTA 7B | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 2,817 | — | 574,709 | 0.4% | 7.77B | 2 |
| 82 | Velvet 14B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,788 | +2,788 | 70,552 | 1.6% | 14.08B | 1 |
| 83 | Mathstral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,779 | +56 | 5,304,295 | 0.1% | 7.25B | 1 |
| 84 | Velvet 2B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,751 | +2,751 | 89,438 | 1.5% | 2.22B | 1 |
| 85 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,744 | 0 | 21,394 | 2.3% | 12.19B | 2 |
| 86 | AI Sweden Llama 3 8B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 2,496 | — | 95,570 | 1.3% | 8.03B | 10 |
| 87 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,475 | +144 | 86,948 | 1.3% | 9.15B | 1 |
| 88 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,442 | -70 | 157,479 | 0.9% | 23.57B | 2 |
| 89 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,358 | -22 | 231,141 | 0.7% | 35.13B | 4 |
| 90 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,237 | 0 | 102,866 | 1.1% | 30.68B | 1 |
| 91 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,138 | 0 | 23,401 | 1.7% | 4.30B | 2 |
| 92 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,120 | -1 | 358,974 | 0.5% | — | 3 |
| 93 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,100 | +1 | 81,313 | 1.2% | 7.45B | 1 |
| 94 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,084 | +8 | 52,323 | 1.4% | 9.24B | 4 |
| 95 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,067 | +2 | 454,954 | 0.4% | 40.43B | 1 |
| 96 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,040 | +8 | 160,550 | 0.8% | 1.10B | 1 |
| 97 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,999 | +3 | 108,834 | 1.0% | 7.45B | 1 |
| 98 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,924 | +1 | 35,502 | 1.4% | 22.64B | 1 |
| 99 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,924 | +6 | 187,273 | 0.7% | 6.74B | 1 |
| 100 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,923 | +6 | 303,941 | 0.5% | 6.74B | 2 |
| 101 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,859 | +6 | 147,991 | 0.7% | 13.02B | 1 |
| 102 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,765 | -4 | 180,214 | 0.6% | 12.25B | 6 |
| 103 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,658 | -3 | 802,645 | 0.2% | — | 3 |
| 104 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,637 | 0 | 10,167 | 1.5% | 9.82B | 1 |
| 105 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,613 | -7 | 41,160 | 1.1% | 70.55B | 3 |
| 106 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,564 | 0 | 44,931 | 1.1% | 12.25B | 3 |
| 107 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,538 | -17 | 55,098 | 1.0% | 7.24B | 5 |
| 108 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,522 | -7 | 416,679 | 0.3% | 1.20B | 1 |
| 109 | LightOnOCR 0.9B 32k (1025) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 1,521 | — | 3,436 | 1.5% | 917.2M | 1 |
| 110 | LightOnOCR 0.9B 16k (1025) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 1,519 | — | 5,746 | 1.4% | 883.6M | 1 |
| 111 | Domyn Edge Teacher IF | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,491 | 0 | 1,491 | 1.5% | 3.93B | 1 |
| 112 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,478 | -19 | 53,850 | 1.0% | 7.24B | 1 |
| 113 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,470 | -532 | 34,772 | 1.1% | 14.03B | 1 |
| 114 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,437 | +7 | 420,085 | 0.3% | 353.4M | 1 |
| 115 | Pleias RAG 1B | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,415 | +18 | 20,979 | 1.2% | 1.20B | 2 |
| 116 | Pleias RAG 350M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,385 | +18 | 16,228 | 1.2% | 353.4M | 2 |
| 117 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,376 | 0 | 9,794 | 1.3% | 4.30B | 3 |
| 118 | SalamandraTA 2B | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 1,337 | — | 30,845 | 1.0% | 2.25B | 3 |
| 119 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,305 | 0 | 9,585 | 1.2% | 28.84B | 3 |
| 120 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,298 | +15 | 401,483 | 0.3% | 3.21B | 1 |
| 121 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 1,181 | 0 | 9,784 | 1.1% | 40.43B | 2 |
| 122 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,178 | +5 | 175,385 | 0.4% | 11.51B | 9 |
| 123 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,167 | +2 | 57,017 | 0.7% | 7.55B | 1 |
| 124 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,095 | -6 | 58,968 | 0.7% | 1.35B | 3 |
| 125 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,081 | +9 | 45,328 | 0.7% | 12.19B | 2 |
| 126 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,067 | +1 | 31,946 | 0.8% | 33.12B | 1 |
| 127 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 997 | 0 | 219,257 | 0.3% | 12.19B | 3 |
| 128 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 994 | -10 | 671,566 | 0.1% | 7.45B | 2 |
| 129 | ALIA 40B Function Calling (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 885 | 0 | 2,925 | 0.9% | 40.43B | 2 |
| 130 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 884 | 0 | 233,721 | 0.3% | — | 2 |
| 131 | EuroVLM 9B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 875 | — | 8,579 | 0.8% | 9.57B | 1 |
| 132 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 829 | 0 | 14,898 | 0.7% | 4.33B | 3 |
| 133 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 829 | -16 | 24,187 | 0.7% | 11.17B | 5 |
| 134 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 823 | -19 | 82,131 | 0.5% | 7.04B | 4 |
| 135 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 816 | 0 | 1,768 | 0.8% | 608.3M | 1 |
| 136 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 801 | -4 | 96,784 | 0.4% | 1.35B | 8 |
| 137 | OCRonos | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 760 | +84 | 82,455 | 0.4% | 8.03B | 3 |
| 138 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 739 | 0 | 112,596 | 0.3% | 7.29B | 2 |
| 139 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 713 | -2 | 31,948 | 0.5% | 11.17B | 5 |
| 140 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 713 | +8 | 17,152 | 0.6% | 1.54B | 4 |
| 141 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 640 | 0 | 2,117 | 0.6% | 27.23B | 3 |
| 142 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 631 | -6 | 20,956 | 0.5% | 3.20B | 2 |
| 143 | Nesso 3 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 625 | 0 | 806 | 0.6% | 437.8M | 2 |
| 144 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 599 | 0 | 3,801 | 0.6% | 30.68B | 1 |
| 145 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 584 | -15 | 28,072 | 0.5% | 9.24B | 2 |
| 146 | Domyn Edge Teacher Math | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | 0 | 563 | 0.6% | 3.93B | 1 |
| 147 | Domyn Edge Teacher STEM | IT | Domyn | [domyn](https://huggingface.co/domyn) | 563 | 0 | 563 | 0.6% | 3.93B | 1 |
| 148 | Domyn Edge Teacher Code | IT | Domyn | [domyn](https://huggingface.co/domyn) | 562 | 0 | 562 | 0.6% | 3.93B | 1 |
| 149 | Domyn Edge Teacher Agentic | IT | Domyn | [domyn](https://huggingface.co/domyn) | 561 | 0 | 561 | 0.6% | 3.93B | 1 |
| 150 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | 0 | 12,588 | 0.5% | 31.59B | 6 |
| 151 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 528 | -36 | 22,252 | 0.4% | 9.24B | 2 |
| 152 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 437 | +15 | 5,782 | 0.4% | 11.51B | 5 |
| 153 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 434 | 0 | 4,517 | 0.4% | 8.03B | 3 |
| 154 | Leanstral 1.5 (119B-A6B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 428 | 0 | 1,762 | 0.4% | — | 1 |
| 155 | Nesso 2 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 394 | 0 | 1,155 | 0.4% | 437.8M | 1 |
| 156 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 393 | +19 | 12,301 | 0.4% | 27.23B | 2 |
| 157 | Nesso 0.4B Agentic | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 389 | 0 | 3,469 | 0.4% | 560.9M | 2 |
| 158 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 302 | -15 | 22,255 | 0.2% | 2.61B | 2 |
| 159 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 302 | 0 | 2,883 | 0.3% | 4.02B | 2 |
| 160 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 292 | -6 | 107,375 | 0.1% | — | 3 |
| 161 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 280 | 0 | 37,971 | 0.2% | 27.23B | 3 |
| 162 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 278 | +2 | 70,652 | 0.2% | 8.03B | 3 |
| 163 | Mambaoutai 1.6B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 270 | — | 1,386 | 0.3% | 1.62B | 1 |
| 164 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 265 | 0 | 32,977 | 0.2% | 40.43B | 2 |
| 165 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 265 | +12 | 1,139 | 0.3% | 9.15B | 2 |
| 166 | OpenEuroLLM Prelude SFT Excellent v0.2 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 227 | — | 227 | 0.2% | 9.09B | 1 |
| 167 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 219 | +1 | 42,002 | 0.2% | 11.17B | 1 |
| 168 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 206 | -8 | 19,774 | 0.2% | 68.98B | 2 |
| 169 | Bielik-One 4B r1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 200 | — | 200 | 0.2% | 4.66B | 1 |
| 170 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 196 | +3 | 16,714 | 0.2% | 7.29B | 2 |
| 171 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 189 | 0 | 29,848 | 0.1% | 1.01B | 1 |
| 172 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | 0 | 3,006 | 0.2% | 31.59B | 6 |
| 173 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 186 | -12 | 322,353 | 0.0% | 7.24B | 2 |
| 174 | Pixtral Large (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 185 | — | 4,485 | 0.2% | — | 1 |
| 175 | T5-sl small | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 181 | — | 3,941 | 0.2% | — | 1 |
| 176 | Velvet2 3B Speech | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 175 | — | 204 | 0.2% | 4.55B | 1 |
| 177 | Alfred 40B (1023) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 172 | — | 78,640 | 0.1% | — | 1 |
| 178 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 170 | -11 | 39,478 | 0.1% | 7.48B | 2 |
| 179 | PAGnol xl | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 170 | — | 1,624 | 0.2% | 1.64B | 1 |
| 180 | Salamandra 7B Function Calling (2610 evo) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 170 | 0 | 170 | 0.2% | 7.77B | 1 |
| 181 | TowerVision 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 170 | — | 2,755 | 0.2% | 3.02B | 1 |
| 182 | Leanstral (2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 167 | 0 | 1,223 | 0.2% | — | 1 |
| 183 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 160 | +3 | 44,717 | 0.1% | 7.70B | 5 |
| 184 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 157 | -1 | 28,499 | 0.1% | 46.70B | 6 |
| 185 | Pleias Pico | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 142 | +10 | 5,562 | 0.1% | 353.4M | 2 |
| 186 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 137 | 0 | 2,947 | 0.1% | 40.43B | 2 |
| 187 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 136 | 0 | 12,771 | 0.1% | 70.55B | 2 |
| 188 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 129 | 0 | 2,602 | 0.1% | — | 1 |
| 189 | GPT-SW3 1.3B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 127 | — | 306,783 | 0.0% | 1.47B | 4 |
| 190 | Salamandra VL 7B (2512) | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 127 | — | 2,097 | 0.1% | 8.90B | 1 |
| 191 | Bielik-One 11B v3.1 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 115 | — | 115 | 0.1% | 11.17B | 1 |
| 192 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 113 | 0 | 7,511 | 0.1% | 31.59B | 6 |
| 193 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 113 | 0 | 5,218 | 0.1% | 437.8M | 1 |
| 194 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 112 | -3 | 5,111 | 0.1% | 70.55B | 3 |
| 195 | TowerVision 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 111 | — | 1,377 | 0.1% | 9.66B | 1 |
| 196 | EuroVLM 1.7B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 101 | — | 3,039 | 0.1% | 2.06B | 1 |
| 197 | Velvet2 3B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 100 | — | 115 | 0.1% | 3.89B | 1 |
| 198 | Alfred 40B (0723) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 99 | — | 5,541 | 0.1% | — | 1 |
| 199 | T5-sl large | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 98 | — | 1,782 | 0.1% | — | 1 |
| 200 | PAGnol medium | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 97 | — | 1,153 | 0.1% | 380.0M | 1 |
| 201 | Bielik-One 7B v3.0 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 95 | — | 95 | 0.1% | 7.48B | 1 |
| 202 | OpenEuroLLM Prelude-long 9B | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 90 | — | 90 | 0.1% | 9.09B | 1 |
| 203 | CroissantCool v0.2 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 85 | — | 14,808 | 0.1% | 1.35B | 1 |
| 204 | Spire 7B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 85 | — | 5,021 | 0.1% | 6.78B | 2 |
| 205 | Bielik-One 11B v3.0 r1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 83 | — | 83 | 0.1% | 11.17B | 1 |
| 206 | Salamandra TAV 7B | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 83 | — | 759 | 0.1% | 7.78B | 1 |
| 207 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 80 | 0 | 38,759 | 0.1% | 70.55B | 3 |
| 208 | Pleias Nano | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 65 | +7 | 7,290 | 0.1% | 1.20B | 2 |
| 209 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 62 | 0 | 438 | 0.1% | 437.8M | 1 |
| 210 | PAGnol small | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 62 | — | 4,653 | 0.1% | — | 1 |
| 211 | PAGnol large | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 61 | — | 883 | 0.1% | — | 1 |
| 212 | TowerVideo 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 61 | — | 1,127 | 0.1% | 3.02B | 1 |
| 213 | Velvet2 3B Vision | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 59 | — | 74 | 0.1% | 4.33B | 1 |
| 214 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 59 | 0 | 266 | 0.1% | 437.8M | 1 |
| 215 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | 0 | 1,326 | 0.1% | 560.9M | 1 |
| 216 | OpenEuroLLM Prelude SFT Excellent v0.1 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 57 | — | 57 | 0.1% | 9.10B | 1 |
| 217 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 56 | 0 | 207 | 0.1% | 437.8M | 1 |
| 218 | TowerVideo 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 55 | — | 481 | 0.1% | 9.66B | 1 |
| 219 | Salamandra 7B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 51 | 0 | 390 | 0.1% | 7.77B | 2 |
| 220 | ALIA 40B Function Calling (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 48 | 0 | 973 | 0.0% | 40.43B | 2 |
| 221 | Pleias SLM RAG | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 47 | 0 | 457 | 0.0% | 321.0M | 1 |
| 222 | Salamandra 7B Vision | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 44 | — | 3,716 | 0.0% | 8.19B | 1 |
| 223 | TildeOpen 8B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 44 | 0 | 221 | 0.0% | 8.16B | 3 |
| 224 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 43 | 0 | 308 | 0.0% | 437.8M | 1 |
| 225 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 42 | 0 | 1,463 | 0.0% | 8.03B | 1 |
| 226 | TildeOpen 15B WMT26 (cs-de) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 41 | 0 | 277 | 0.0% | 15.17B | 3 |
| 227 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 40 | -6 | 621 | 0.0% | 6.25B | 2 |
| 228 | ALIA 40B Function Calling (2607) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 39 | 0 | 230 | 0.0% | 40.43B | 2 |
| 229 | M2M100 1.2B Ancient to Modern Greek | GR | Athena Research Center / ILSP | [ilsp](https://huggingface.co/ilsp) | 31 | — | 177 | 0.0% | 1.24B | 1 |
| 230 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | +1 | 154 | 0.0% | 7.24B | 1 |
| 231 | OriOn Qwen 32B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 29 | — | 188 | 0.0% | 33.36B | 1 |
| 232 | Cassandre RAG 8B | FR | Pleias | [PleIAs](https://huggingface.co/PleIAs) | 28 | — | 1,106 | 0.0% | 8.03B | 1 |
| 233 | NorwAI Magistral 24B reasoning | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 28 | — | 547,889 | 0.0% | 23.85B | 1 |
| 234 | CroissantCool v0.1 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 27 | — | 605 | 0.0% | 1.35B | 1 |
| 235 | NorwAI Mistral-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 25 | — | 111,668 | 0.0% | 7.54B | 3 |
| 236 | OriOn Qwen 32B SR1 | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 23 | — | 423 | 0.0% | 33.36B | 1 |
| 237 | GPT-SW3 20B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 22 | — | 141,983 | 0.0% | 20.92B | 5 |
| 238 | Tyr 7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 21 | — | 910 | 0.0% | 7.24B | 1 |
| 239 | GaMS DPO Translator | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 20 | — | 300 | 0.0% | 9.24B | 1 |
| 240 | Krikri 8B Ancient to Modern Greek | GR | Athena Research Center / ILSP | [ilsp](https://huggingface.co/ilsp) | 19 | — | 124 | 0.0% | — | 1 |
| 241 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 17 | 0 | 379 | 0.0% | 12.25B | 1 |
| 242 | OriOn Mistral 24B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 16 | — | 284 | 0.0% | 24.01B | 1 |
| 243 | GPT-sl Base | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 15 | — | 1,761 | 0.0% | — | 1 |
| 244 | GPT-SW3 126M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 10 | — | 893,762 | 0.0% | 186.1M | 4 |
| 245 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 246 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 247 | GPT-SW3 40B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | — | 59,796 | 0.0% | 39.93B | 2 |
| 248 | GPT-SW3 6.7B v2 | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | — | 276,937 | 0.0% | 7.11B | 7 |
| 249 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 250 | GPT-SW3 356M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | — | 334,511 | 0.0% | 470.6M | 4 |
| 251 | GPT-SW3 6.7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | — | 68,906 | 0.0% | 7.11B | 1 |
| 252 | NorwAI Llama2-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | — | 65,548 | 0.0% | 7.03B | 1 |
| 253 | NorwAI Mixtral-8x7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | — | 2,172 | 0.0% | 47.00B | 2 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,180,205 | 317,804,024 | 36 | 1.9% |
| 2 | [lightonai](https://huggingface.co/lightonai) | LightOn | FR | 866,466 | 6,445,693 | 18 | 13.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 254,603 | 6,099,405 | 7 | 4.1% |
| 4 | [Voicelab](https://huggingface.co/Voicelab) | VoiceLab | PL | 223,669 | 2,523,813 | 3 | 8.5% |
| 5 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 217,782 | 470,334 | 10 | 38.2% |
| 6 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 179,417 | 6,532,199 | 17 | 2.7% |
| 7 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 73,705 | 2,696,808 | 19 | 2.6% |
| 8 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 57,230 | 2,067,742 | 18 | 2.6% |
| 9 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,099 | 594,459 | 5 | 2.9% |
| 10 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 17,151 | 1,458,303 | 13 | 1.1% |
| 11 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 15,214 | 570,974 | 13 | 2.3% |
| 12 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 14,447 | 117,565 | 2 | 6.6% |
| 13 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 13,623 | 453,188 | 6 | 2.5% |
| 14 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 12,843 | 377,549 | 16 | 2.7% |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 8,563 | 17,136 | 7 | 7.3% |
| 16 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,645 | 204,977 | 5 | 2.5% |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,965 | 403,261 | 12 | 1.2% |
| 18 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Almawave | IT | 5,873 | 160,383 | 5 | 2.3% |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,823 | 495,814 | 3 | 1.0% |
| 20 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 5,147 | 79,197 | 4 | 2.9% |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,093 | 861,713 | 3 | 0.5% |
| 22 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,274 | 701,219 | 2 | 0.5% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 3,040 | 1,163,515 | 4 | 0.2% |
| 24 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,921 | 107,165 | 4 | 1.4% |
| 25 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden | SE | 2,682 | 2,179,158 | 9 | 0.1% |
| 26 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,008 | 171,165 | 4 | 0.7% |
| 27 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 862 | 24,614 | 4 | 0.7% |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI / NTNU | NO | 53 | 727,277 | 4 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,021,775 | 60,805,659 | 1 |
| 2 | [lightonai](https://huggingface.co/lightonai) | LightOnOCR 2 1B | 812,022 | 4,933,530 | 3 |
| 3 | [Voicelab](https://huggingface.co/Voicelab) | VLT5 Base Keywords | 219,626 | 1,860,898 | 8 |
| 4 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 213,120 | 332,031 | 9 |
| 5 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 201,288 | 4,696,239 | 11 |
| 6 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 122,460 | 4,288,054 | 14 |
| 7 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 38,706 | 740,716 | 20 |
| 8 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,733 | 948,064 | 25 |
| 9 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 13,624 | 35,434 | 34 |
| 10 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,265 | 120,481 | 48 |
| 11 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 5,948 | 57,152 | 55 |
| 12 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,847 | 138,604 | 56 |
| 13 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude-base 9B | 4,773 | 78,823 | 61 |
| 14 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,695 | 39,255 | 63 |
| 15 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,444 | 155,495 | 65 |
| 16 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,088 | 378,866 | 69 |
| 17 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,378 | 22,921 | 76 |
| 18 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,186 | 3,229 | 78 |
| 19 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Velvet 14B | 2,788 | 70,552 | 82 |
| 20 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden Llama 3 8B | 2,496 | 95,570 | 86 |
| 21 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,237 | 102,866 | 90 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,100 | 81,313 | 93 |
| 23 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,040 | 160,550 | 96 |
| 24 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,765 | 180,214 | 102 |
| 25 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,658 | 802,645 | 103 |
| 26 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,095 | 58,968 | 124 |
| 27 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 150 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI Magistral 24B reasoning | 28 | 547,889 | 233 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.2% | 217,782 | 470,334 | 5 |
| 2 | [lightonai](https://huggingface.co/lightonai) | 13.2% | 866,466 | 6,445,693 | 2 |
| 3 | [Voicelab](https://huggingface.co/Voicelab) | 8.5% | 223,669 | 2,523,813 | 4 |
| 4 | [domyn](https://huggingface.co/domyn) | 7.3% | 8,563 | 17,136 | 15 |
| 5 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 6.6% | 14,447 | 117,565 | 12 |
| 6 | [swiss-ai](https://huggingface.co/swiss-ai) | 4.1% | 254,603 | 6,099,405 | 3 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,099 | 594,459 | 9 |
| 8 | [openeurollm](https://huggingface.co/openeurollm) | 2.9% | 5,147 | 79,197 | 20 |
| 9 | [speakleash](https://huggingface.co/speakleash) | 2.7% | 179,417 | 6,532,199 | 6 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.7% | 12,843 | 377,549 | 14 |
| 11 | [BSC-LT](https://huggingface.co/BSC-LT) | 2.6% | 57,230 | 2,067,742 | 8 |
| 12 | [utter-project](https://huggingface.co/utter-project) | 2.6% | 73,705 | 2,696,808 | 7 |
| 13 | [ilsp](https://huggingface.co/ilsp) | 2.5% | 7,645 | 204,977 | 16 |
| 14 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.5% | 13,623 | 453,188 | 13 |
| 15 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.3% | 15,214 | 570,974 | 11 |
| 16 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2.3% | 5,873 | 160,383 | 18 |
| 17 | [mistralai](https://huggingface.co/mistralai) | 1.9% | 6,180,205 | 317,804,024 | 1 |
| 18 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,921 | 107,165 | 24 |
| 19 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 5,965 | 403,261 | 17 |
| 20 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 17,151 | 1,458,303 | 10 |
| 21 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,823 | 495,814 | 19 |
| 22 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 2,008 | 171,165 | 26 |
| 23 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 862 | 24,614 | 27 |
| 24 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,274 | 701,219 | 22 |
| 25 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,093 | 861,713 | 21 |
| 26 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 3,040 | 1,163,515 | 23 |
| 27 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0.1% | 2,682 | 2,179,158 | 25 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | 0.0% | 53 | 727,277 | 28 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
