# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-19
- **Generated at:** 2026-11-19T15:30:13Z
- **Ranking metric:** `total_downloads_30d` (last 30 days, summed across official format variants)
- **Rows:** 197

General-purpose generative LLMs, including general-purpose multimodal models. Task-specific OCR, translation, RAG, coding, math/proof, decision and function-calling specialists are excluded, alongside auxiliary models.

Historical snapshots retain their original scope; changes across the scope correction on 2026-11-16 also reflect the removed repositories.

## Charts

![Top models by 30-day downloads](docs/charts/top-models-30d.png)

![Organizations by best single model (30-day downloads)](docs/charts/orgs-best-single-model-30d.png)

![Best single model per organization (30-day downloads, log scale)](docs/charts/orgs-best-single-model-30d-log.png)

### Trends over time

From daily snapshots in `data/metrics/timeseries.jsonl` (top 15 models / top 10 orgs by latest-day volume). Rolling-30d charts use a symlog y-axis (0 at zero, log compression above).

Rolling-30-day charts omit incomplete model observations; organization totals have a gap if any member model is incomplete. Complete zero observations remain zero.

Daily estimates omit intervals where the catalog changed, its identity is unknown, or a fetch was incomplete; they resume after two complete observations of the same catalog. This avoids counting newly added models’ lifetime downloads as daily growth.

![Top models: rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-top-models-30d.png)

![Top models: estimated daily downloads (Δ all-time)](docs/charts/timeseries-top-models-daily.png)

![Top organizations: summed rolling 30-day downloads over time (symlog scale)](docs/charts/timeseries-orgs-30d.png)

![Top organizations: estimated daily downloads (Δ all-time)](docs/charts/timeseries-orgs-daily.png)

| Rank | Model | Country | Developer | Org | Downloads (30d) | Δ 30d | All-time | Momentum | Params | Repos |
| ---: | --- | :---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,040,029 | +2,742 | 60,976,989 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,071,464 | -27,653 | 67,059,578 | 1.6% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 648,344 | +3,975 | 4,631,430 | 13.7% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 550,703 | -1,080 | 46,589,726 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 354,086 | -5,158 | 32,892,218 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 259,098 | -1,515 | 2,600,318 | 9.6% | 8.92B | 6 |
| 7 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 219,270 | +5,985 | 338,660 | 50.0% | 12.77B | 4 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 210,521 | +1,707 | 5,954,993 | 3.5% | 3.85B | 7 |
| 9 | Voxtral Mini 3B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 164,415 | +31,409 | 6,664,963 | 2.4% | 4.68B | 1 |
| 10 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 163,192 | -13,722 | 4,701,573 | 3.4% | 8.05B | 2 |
| 11 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 151,022 | +3,637 | 5,064,244 | 2.9% | 24.01B | 2 |
| 12 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 135,859 | +1,619 | 4,303,878 | 3.1% | 11.34B | 10 |
| 13 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 125,957 | -735 | 16,696,651 | 0.7% | 12.25B | 3 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 110,592 | +663 | 5,675,817 | 1.9% | 24.01B | 1 |
| 15 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 99,402 | -1,526 | 7,740,786 | 1.3% | 23.57B | 2 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 62,435 | -680 | 8,616,550 | 0.7% | 8.02B | 1 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 43,535 | -1,513 | 11,303,458 | 0.4% | 140.63B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 36,237 | -26 | 755,596 | 4.2% | 119.40B | 3 |
| 19 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 35,208 | -559 | 739,416 | 4.2% | 7.77B | 5 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 31,706 | -2,256 | 808,212 | 3.5% | 23.57B | 2 |
| 21 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 21,017 | +608 | 21,089 | 17.4% | — | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,925 | +231 | 949,086 | 1.9% | 1.66B | 1 |
| 23 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,383 | +229 | 373,615 | 3.9% | 24.01B | 2 |
| 24 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 17,538 | -40 | 804,980 | 1.9% | 11.25B | 10 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,254 | -293 | 751,251 | 1.8% | 8.90B | 5 |
| 26 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 15,068 | +381 | 1,125,165 | 1.2% | 127.70B | 2 |
| 27 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,707 | -111 | 4,947,835 | 0.3% | 122.61B | 1 |
| 28 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,463 | +171 | 251,182 | 3.8% | — | 1 |
| 29 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 12,292 | -584 | 36,631 | 9.0% | 78.10B | 2 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,097 | -148 | 500,718 | 1.8% | 9.15B | 1 |
| 31 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,475 | +23 | 526,919 | 1.7% | 7.24B | 8 |
| 32 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,440 | -27 | 5,393,079 | 0.2% | 22.25B | 1 |
| 33 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 8,789 | +245 | 264,051 | 2.4% | 4.76B | 8 |
| 34 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,689 | -1,966 | 5,048,231 | 0.2% | 122.61B | 1 |
| 35 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 8,459 | +651 | 8,459 | 7.8% | 11.17B | 8 |
| 36 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,322 | +128 | 24,677 | 6.7% | 3.83B | 5 |
| 37 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,261 | +213 | 89,948 | 4.3% | — | 5 |
| 38 | Pixtral 12B (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,732 | +197 | 144,594 | 3.2% | — | 2 |
| 39 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,635 | -259 | 37,401 | 5.6% | 72.01B | 4 |
| 40 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,318 | -167 | 17,978 | 6.2% | 1.51B | 6 |
| 41 | Voxtral Small 24B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,031 | +141 | 999,288 | 0.6% | 24.26B | 1 |
| 42 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,882 | -40 | 58,397 | 4.3% | 8.03B | 7 |
| 43 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 6,610 | -494 | 121,003 | 3.0% | 8.42B | 7 |
| 44 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,607 | +95 | 162,507 | 2.5% | 9.15B | 1 |
| 45 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,543 | -4 | 606,101 | 0.9% | 22.64B | 1 |
| 46 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,423 | -21 | 24,950 | 5.1% | 572.6M | 5 |
| 47 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 5,983 | -408 | 552,890 | 0.9% | 70.60B | 2 |
| 48 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,825 | -14 | 139,137 | 2.4% | 2.89B | 1 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,806 | +68 | 154,066 | 2.3% | 2.25B | 7 |
| 50 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,635 | +35 | 160,145 | 2.2% | 351.6M | 1 |
| 51 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,328 | -28 | 65,801 | 3.2% | 1.60B | 9 |
| 52 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 5,053 | +83 | 39,961 | 3.6% | 56.7M | 1 |
| 53 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,808 | +1,295 | 46,561 | 3.3% | 13.29B | 3 |
| 54 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,658 | +175 | 30,042 | 3.6% | 22.64B | 1 |
| 55 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,401 | -1 | 155,920 | 1.7% | 7.24B | 4 |
| 56 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,198 | +3 | 125,635 | 1.9% | 8.54B | 2 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,166 | +122 | 379,341 | 0.9% | 7.24B | 8 |
| 58 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,133 | +33 | 141,593 | 1.7% | 7.40B | 3 |
| 59 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 4,024 | +61 | 12,746 | 3.6% | 40.43B | 2 |
| 60 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,883 | +124 | 132,112 | 1.7% | 7.48B | 9 |
| 61 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,751 | +112 | 3,835 | 3.6% | 3.93B | 2 |
| 62 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,749 | +23 | 55,641 | 2.4% | 7.77B | 3 |
| 63 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,719 | -32 | 42,003 | 2.6% | 2.61B | 3 |
| 64 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,350 | +8 | 13,673 | 2.9% | 9.15B | 1 |
| 65 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,296 | -48 | 22,998 | 2.7% | 27.43B | 3 |
| 66 | OpenEuroLLM Prelude-base 9B | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 3,262 | -432 | 79,303 | 1.8% | 9.09B | 1 |
| 67 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,222 | +3 | 97,162 | 1.6% | 2.89B | 1 |
| 68 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 2,989 | +1 | 170,799 | 1.1% | 11.17B | 16 |
| 69 | AI Sweden Llama 3 8B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 2,987 | -14 | 96,246 | 1.5% | 8.03B | 10 |
| 70 | Velvet 14B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,803 | -1 | 70,849 | 1.6% | 14.08B | 1 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,754 | -38 | 21,594 | 2.3% | 12.19B | 2 |
| 72 | Velvet 2B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,749 | +1 | 89,712 | 1.4% | 2.22B | 1 |
| 73 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,684 | -1 | 87,174 | 1.4% | 9.15B | 1 |
| 74 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,300 | +61 | 23,704 | 1.9% | 4.30B | 2 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,274 | +19 | 103,201 | 1.1% | 30.68B | 1 |
| 76 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,242 | -52 | 231,256 | 0.7% | 35.13B | 4 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,101 | +4 | 81,522 | 1.2% | 7.45B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,080 | -17 | 359,160 | 0.5% | — | 3 |
| 79 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,073 | 0 | 52,523 | 1.4% | 9.24B | 4 |
| 80 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,061 | +1 | 455,049 | 0.4% | 40.43B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,024 | -1 | 160,733 | 0.8% | 1.10B | 1 |
| 82 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,994 | +4 | 109,035 | 1.0% | 7.45B | 1 |
| 83 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,912 | -26 | 157,583 | 0.7% | 23.57B | 2 |
| 84 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,910 | +5 | 35,687 | 1.4% | 22.64B | 1 |
| 85 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,910 | +3 | 187,450 | 0.7% | 6.74B | 1 |
| 86 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,908 | +1 | 304,121 | 0.5% | 6.74B | 2 |
| 87 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,878 | +7 | 420,586 | 0.4% | 353.4M | 1 |
| 88 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,846 | +3 | 148,168 | 0.7% | 13.02B | 1 |
| 89 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,786 | -86 | 10,571 | 1.6% | 9.82B | 1 |
| 90 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,758 | -3 | 402,009 | 0.4% | 3.21B | 1 |
| 91 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,757 | -23 | 417,161 | 0.3% | 1.20B | 1 |
| 92 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,753 | -16 | 180,402 | 0.6% | 12.25B | 6 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,598 | -36 | 802,761 | 0.2% | — | 3 |
| 94 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,537 | -17 | 41,238 | 1.1% | 70.55B | 3 |
| 95 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,527 | 0 | 55,246 | 1.0% | 7.24B | 5 |
| 96 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,468 | +5 | 53,993 | 1.0% | 7.24B | 1 |
| 97 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,446 | +1 | 34,816 | 1.1% | 14.03B | 1 |
| 98 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,306 | -94 | 45,035 | 0.9% | 12.25B | 3 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,173 | -173 | 9,879 | 1.1% | 4.30B | 3 |
| 100 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,171 | +13 | 57,094 | 0.7% | 7.55B | 1 |
| 101 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,160 | -23 | 175,543 | 0.4% | 11.51B | 9 |
| 102 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,032 | -7 | 31,997 | 0.8% | 33.12B | 1 |
| 103 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,023 | -32 | 59,056 | 0.6% | 1.35B | 3 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,019 | -7 | 9,635 | 0.9% | 28.84B | 3 |
| 105 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,018 | +16 | 45,427 | 0.7% | 12.19B | 2 |
| 106 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,001 | +239 | 15,294 | 0.9% | 4.33B | 3 |
| 107 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 999 | +6 | 671,667 | 0.1% | 7.45B | 2 |
| 108 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 929 | +2 | 219,386 | 0.3% | 12.19B | 3 |
| 109 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 876 | -4 | 233,742 | 0.3% | — | 2 |
| 110 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 849 | +9 | 1,888 | 0.8% | 608.3M | 1 |
| 111 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 849 | +15 | 96,897 | 0.4% | 1.35B | 8 |
| 112 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 844 | +7 | 24,288 | 0.7% | 11.17B | 5 |
| 113 | EuroVLM 9B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 825 | -51 | 8,623 | 0.8% | 9.57B | 1 |
| 114 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 775 | -11 | 82,172 | 0.4% | 7.04B | 4 |
| 115 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 708 | +6 | 32,038 | 0.5% | 11.17B | 5 |
| 116 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 708 | +52 | 1,587 | 0.7% | 9.15B | 2 |
| 117 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 692 | -7 | 112,620 | 0.3% | 7.29B | 2 |
| 118 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 691 | -7 | 17,207 | 0.6% | 1.54B | 4 |
| 119 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 661 | +7 | 21,001 | 0.5% | 3.20B | 2 |
| 120 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 589 | +3 | 3,871 | 0.6% | 30.68B | 1 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 585 | +1 | 28,088 | 0.5% | 9.24B | 2 |
| 122 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | 0 | 12,588 | 0.5% | 31.59B | 6 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 540 | +6 | 1,809 | 0.5% | 852,480 | 2 |
| 124 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 464 | -22 | 22,289 | 0.4% | 9.24B | 2 |
| 125 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 463 | -4 | 5,833 | 0.4% | 11.51B | 5 |
| 126 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 453 | -9 | 4,587 | 0.4% | 8.03B | 3 |
| 127 | OpenEuroLLM Prelude-long 9B | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 391 | +53 | 391 | 0.4% | 9.09B | 1 |
| 128 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 358 | +7 | 38,062 | 0.3% | 27.23B | 3 |
| 129 | OpenEuroLLM Prelude SFT Excellent v0.2 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 352 | +42 | 352 | 0.4% | 9.09B | 1 |
| 130 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 345 | -2 | 12,325 | 0.3% | 27.23B | 2 |
| 131 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 330 | +13 | 22,308 | 0.3% | 2.61B | 2 |
| 132 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 313 | 0 | 70,702 | 0.2% | 8.03B | 3 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 276 | -13 | 107,393 | 0.1% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 244 | -7 | 2,885 | 0.2% | 4.02B | 2 |
| 135 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 241 | -2 | 33,002 | 0.2% | 40.43B | 2 |
| 136 | Mambaoutai 1.6B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 239 | -10 | 1,399 | 0.2% | 1.62B | 1 |
| 137 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 233 | +4 | 29,897 | 0.2% | 1.01B | 1 |
| 138 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 214 | -3 | 42,030 | 0.2% | 11.17B | 1 |
| 139 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 204 | +27 | 322,388 | 0.0% | 7.24B | 2 |
| 140 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 191 | +4 | 3,010 | 0.2% | 31.59B | 6 |
| 141 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 185 | +1 | 16,731 | 0.2% | 7.29B | 2 |
| 142 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 182 | -14 | 19,781 | 0.2% | 68.98B | 2 |
| 143 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 169 | 0 | 39,487 | 0.1% | 7.48B | 2 |
| 144 | Velvet2 3B Speech | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 169 | 0 | 204 | 0.2% | 4.55B | 1 |
| 145 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 167 | +4 | 28,525 | 0.1% | 46.70B | 6 |
| 146 | Pixtral Large (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 165 | -4 | 4,494 | 0.2% | — | 1 |
| 147 | Alfred 40B (1023) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 162 | -8 | 78,650 | 0.1% | — | 1 |
| 148 | PAGnol xl | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 161 | -18 | 1,643 | 0.2% | 1.64B | 1 |
| 149 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 150 | -1 | 44,728 | 0.1% | 7.70B | 5 |
| 150 | TowerVision 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 149 | -16 | 2,788 | 0.1% | 3.02B | 1 |
| 151 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 136 | -1 | 2,971 | 0.1% | 40.43B | 2 |
| 152 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 130 | -9 | 12,787 | 0.1% | 70.55B | 2 |
| 153 | GPT-SW3 1.3B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 129 | 0 | 306,785 | 0.0% | 1.47B | 4 |
| 154 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 129 | +3 | 5,242 | 0.1% | 437.8M | 1 |
| 155 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 116 | -4 | 2,614 | 0.1% | — | 1 |
| 156 | Salamandra VL 7B (2512) | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 115 | -8 | 2,102 | 0.1% | 8.90B | 1 |
| 157 | Velvet2 3B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 115 | +2 | 134 | 0.1% | 3.89B | 1 |
| 158 | PAGnol medium | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 106 | 0 | 1,165 | 0.1% | 380.0M | 1 |
| 159 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 102 | -2 | 5,117 | 0.1% | 70.55B | 3 |
| 160 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 94 | +1 | 476 | 0.1% | 437.8M | 1 |
| 161 | GPT-sl Base | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 93 | +77 | 1,840 | 0.1% | — | 1 |
| 162 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 92 | -1 | 38,782 | 0.1% | 70.55B | 3 |
| 163 | Alfred 40B (0723) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 89 | -8 | 5,547 | 0.1% | — | 1 |
| 164 | EuroVLM 1.7B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 89 | -6 | 3,045 | 0.1% | 2.06B | 1 |
| 165 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 89 | -16 | 7,511 | 0.1% | 31.59B | 6 |
| 166 | CroissantCool v0.2 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 86 | +1 | 14,815 | 0.1% | 1.35B | 1 |
| 167 | TowerVision 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 80 | -6 | 1,386 | 0.1% | 9.66B | 1 |
| 168 | PAGnol small | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 71 | +3 | 4,669 | 0.1% | — | 1 |
| 169 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 67 | +2 | 219 | 0.1% | 437.8M | 1 |
| 170 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 65 | 0 | 276 | 0.1% | 437.8M | 1 |
| 171 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 60 | -1 | 1,336 | 0.1% | 560.9M | 1 |
| 172 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 57 | +2 | 323 | 0.1% | 437.8M | 1 |
| 173 | PAGnol large | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 51 | -15 | 892 | 0.1% | — | 1 |
| 174 | TowerVideo 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 46 | -1 | 486 | 0.0% | 9.66B | 1 |
| 175 | OpenEuroLLM Prelude SFT Excellent v0.1 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 40 | -15 | 58 | 0.0% | 9.10B | 1 |
| 176 | Salamandra 7B Vision | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 40 | -3 | 3,721 | 0.0% | 8.19B | 1 |
| 177 | TowerVideo 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 39 | -16 | 1,132 | 0.0% | 3.02B | 1 |
| 178 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 37 | +1 | 626 | 0.0% | 6.25B | 2 |
| 179 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 34 | -3 | 1,466 | 0.0% | 8.03B | 1 |
| 180 | NorwAI Magistral 24B reasoning | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 31 | 0 | 547,892 | 0.0% | 23.85B | 1 |
| 181 | CroissantCool v0.1 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 28 | +1 | 607 | 0.0% | 1.35B | 1 |
| 182 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 28 | -2 | 154 | 0.0% | 7.24B | 1 |
| 183 | NorwAI Mistral-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 25 | 0 | 111,668 | 0.0% | 7.54B | 3 |
| 184 | Velvet2 3B Vision | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 23 | -40 | 78 | 0.0% | 4.33B | 1 |
| 185 | GPT-SW3 20B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 22 | 0 | 141,983 | 0.0% | 20.92B | 5 |
| 186 | Tyr 7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 21 | 0 | 916 | 0.0% | 7.24B | 1 |
| 187 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 17 | -2 | 381 | 0.0% | 12.25B | 1 |
| 188 | GPT-SW3 126M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 10 | 0 | 893,762 | 0.0% | 186.1M | 4 |
| 189 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 190 | GPT-SW3 6.7B v2 | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 7 | 0 | 262,851 | 0.0% | 7.11B | 5 |
| 191 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 192 | GPT-SW3 40B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | 0 | 59,796 | 0.0% | 39.93B | 2 |
| 193 | NorwAI Mixtral-8x7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 3 | +3 | 2,175 | 0.0% | 47.00B | 2 |
| 194 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 195 | GPT-SW3 356M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 334,511 | 0.0% | 470.6M | 4 |
| 196 | GPT-SW3 6.7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 68,906 | 0.0% | 7.11B | 1 |
| 197 | NorwAI Llama2-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | 0 | 65,548 | 0.0% | 7.03B | 1 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,071,951 | 302,336,450 | 27 | 2.0% |
| 2 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 223,686 | 471,102 | 7 | 39.2% |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 214,127 | 6,110,720 | 7 | 3.4% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 196,709 | 6,556,731 | 13 | 3.0% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 76,008 | 2,699,834 | 18 | 2.7% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 51,417 | 1,459,340 | 10 | 3.3% |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 20,024 | 596,407 | 5 | 2.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 16,103 | 1,328,166 | 6 | 1.1% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 14,918 | 572,399 | 13 | 2.2% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,310 | 454,798 | 6 | 2.6% |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 13,067 | 118,803 | 2 | 6.0% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,362 | 373,240 | 13 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 6,929 | 205,218 | 3 | 2.3% |
| 14 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Almawave | IT | 5,859 | 160,977 | 5 | 2.2% |
| 15 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,780 | 496,351 | 3 | 1.0% |
| 16 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,544 | 403,834 | 12 | 1.1% |
| 17 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 5,537 | 14,406 | 2 | 4.8% |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,094 | 862,224 | 3 | 0.5% |
| 19 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,370 | 701,729 | 2 | 0.5% |
| 20 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 4,045 | 80,104 | 4 | 2.2% |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 3,988 | 663,281 | 2 | 0.5% |
| 22 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden | SE | 3,179 | 2,165,756 | 9 | 0.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,932 | 1,163,677 | 4 | 0.2% |
| 24 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,863 | 107,072 | 2 | 1.4% |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 1,986 | 171,375 | 4 | 0.7% |
| 26 | [lightonai](https://huggingface.co/lightonai) | LightOn | FR | 879 | 93,965 | 7 | 0.5% |
| 27 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 842 | 24,618 | 4 | 0.7% |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI / NTNU | NO | 59 | 727,283 | 4 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,040,029 | 60,976,989 | 1 |
| 2 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 219,270 | 338,660 | 7 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 163,192 | 4,701,573 | 10 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 135,859 | 4,303,878 | 12 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 35,208 | 739,416 | 19 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,925 | 949,086 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 12,292 | 36,631 | 29 |
| 8 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,882 | 58,397 | 42 |
| 9 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 6,610 | 121,003 | 43 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,825 | 139,137 | 48 |
| 11 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 5,053 | 39,961 | 52 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,401 | 155,920 | 55 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,166 | 379,341 | 57 |
| 14 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,751 | 3,835 | 61 |
| 15 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,296 | 22,998 | 65 |
| 16 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude-base 9B | 3,262 | 79,303 | 66 |
| 17 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden Llama 3 8B | 2,987 | 96,246 | 69 |
| 18 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Velvet 14B | 2,803 | 70,849 | 70 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,274 | 103,201 | 75 |
| 20 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,101 | 81,522 | 77 |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,080 | 359,160 | 78 |
| 22 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,024 | 160,733 | 81 |
| 23 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,753 | 180,402 | 92 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,598 | 802,761 | 93 |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,023 | 59,056 | 103 |
| 26 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 122 |
| 27 | [lightonai](https://huggingface.co/lightonai) | Mambaoutai 1.6B | 239 | 1,399 | 136 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI Magistral 24B reasoning | 31 | 547,892 | 180 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 39.2% | 223,686 | 471,102 | 2 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 6.0% | 13,067 | 118,803 | 11 |
| 3 | [domyn](https://huggingface.co/domyn) | 4.8% | 5,537 | 14,406 | 17 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 3.4% | 214,127 | 6,110,720 | 3 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.3% | 51,417 | 1,459,340 | 6 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 3.0% | 196,709 | 6,556,731 | 4 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 20,024 | 596,407 | 7 |
| 8 | [utter-project](https://huggingface.co/utter-project) | 2.7% | 76,008 | 2,699,834 | 5 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,310 | 454,798 | 10 |
| 10 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,362 | 373,240 | 12 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.3% | 6,929 | 205,218 | 13 |
| 12 | [openeurollm](https://huggingface.co/openeurollm) | 2.2% | 4,045 | 80,104 | 20 |
| 13 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2.2% | 5,859 | 160,977 | 14 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 14,918 | 572,399 | 9 |
| 15 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,071,951 | 302,336,450 | 1 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,863 | 107,072 | 24 |
| 17 | [PleIAs](https://huggingface.co/PleIAs) | 1.1% | 16,103 | 1,328,166 | 8 |
| 18 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.1% | 5,544 | 403,834 | 16 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,780 | 496,351 | 15 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 1,986 | 171,375 | 25 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 842 | 24,618 | 27 |
| 22 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,370 | 701,729 | 19 |
| 23 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,094 | 862,224 | 18 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 3,988 | 663,281 | 21 |
| 25 | [lightonai](https://huggingface.co/lightonai) | 0.5% | 879 | 93,965 | 26 |
| 26 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,932 | 1,163,677 | 23 |
| 27 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0.1% | 3,179 | 2,165,756 | 22 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | 0.0% | 59 | 727,283 | 28 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
