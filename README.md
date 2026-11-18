# European LLM Hugging Face download leaderboard

- **Snapshot date:** 2026-11-18
- **Generated at:** 2026-11-18T15:28:32Z
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
| 1 | Mistral 7B v0.3 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 2,037,287 | +2,113 | 60,922,075 | 3.3% | 7.25B | 2 |
| 2 | Mistral 7B v0.2 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,099,117 | -32,911 | 67,025,404 | 1.6% | 7.24B | 1 |
| 3 | Ministral 3 14B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 644,369 | +1,942 | 4,605,597 | 13.7% | 13.95B | 6 |
| 4 | Mistral 7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 551,783 | -249 | 46,575,202 | 1.2% | 7.24B | 2 |
| 5 | Mixtral 8x7B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 359,244 | -344 | 32,881,368 | 1.1% | 46.70B | 2 |
| 6 | Ministral 3 8B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 260,613 | -3,755 | 2,594,771 | 9.7% | 8.92B | 6 |
| 7 | GaMS3 12B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 213,285 | +85 | 332,415 | 49.3% | 12.77B | 4 |
| 8 | Ministral 3 3B (2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 208,814 | -2,344 | 5,945,849 | 3.5% | 3.85B | 7 |
| 9 | Apertus 8B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 176,914 | -12,315 | 4,700,450 | 3.7% | 8.05B | 2 |
| 10 | Mistral Small 3.1 (24B, 2503) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 147,385 | +2,711 | 5,055,645 | 2.9% | 24.01B | 2 |
| 11 | Bielik-11B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 134,240 | +3,908 | 4,301,723 | 3.0% | 11.34B | 10 |
| 12 | Voxtral Mini 3B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 133,006 | +26,526 | 6,630,832 | 2.0% | 4.68B | 1 |
| 13 | Mistral NeMo (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 126,692 | -3,484 | 16,693,498 | 0.8% | 12.25B | 3 |
| 14 | Mistral Small 3.2 (24B, 2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 109,929 | +3,410 | 5,671,945 | 1.9% | 24.01B | 1 |
| 15 | Mistral Small 24B (2501) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 100,928 | -981 | 7,738,488 | 1.3% | 23.57B | 2 |
| 16 | Ministral 8B Instruct (2410) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 63,115 | -192 | 8,615,226 | 0.7% | 8.02B | 1 |
| 17 | Mixtral 8x22B v0.1 | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 45,048 | +325 | 11,301,794 | 0.4% | 140.63B | 2 |
| 18 | Mistral Small 4 (119B, 2603) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 36,263 | +234 | 754,644 | 4.2% | 119.40B | 3 |
| 19 | Salamandra 7B Instruct | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 35,767 | -362 | 738,255 | 4.3% | 7.77B | 5 |
| 20 | Magistral Small (2506) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 33,962 | -2,183 | 808,044 | 3.7% | 23.57B | 2 |
| 21 | Mistral Large 4 (1T-A52B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 20,409 | +778 | 20,473 | 16.9% | — | 2 |
| 22 | EuroLLM-1.7B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 19,694 | -92 | 948,630 | 1.9% | 1.66B | 1 |
| 23 | Magistral Small (2509) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 18,154 | +861 | 372,903 | 3.8% | 24.01B | 2 |
| 24 | Bielik-11B v2.3 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 17,578 | +56 | 804,532 | 1.9% | 11.25B | 10 |
| 25 | Apertus v1.5 8B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 15,547 | +318 | 751,026 | 1.8% | 8.90B | 5 |
| 26 | Mistral Large Instruct (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,818 | +7 | 4,947,412 | 0.3% | 122.61B | 1 |
| 27 | Mistral Medium 3.5 (128B) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 14,687 | -76 | 1,124,303 | 1.2% | 127.70B | 2 |
| 28 | EuroLLM-1.7B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 13,292 | +131 | 250,839 | 3.8% | — | 1 |
| 29 | Kolibri-1 | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 12,876 | -528 | 36,305 | 9.4% | 78.10B | 2 |
| 30 | EuroLLM-9B-Instruct | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 11,245 | +440 | 500,430 | 1.9% | 9.15B | 1 |
| 31 | Mistral Large Instruct (2407) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 10,655 | -2,165 | 5,048,103 | 0.2% | 122.61B | 1 |
| 32 | Bielik-7B v0.1 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 10,452 | -26 | 526,576 | 1.7% | 7.24B | 8 |
| 33 | Mistral Small Instruct (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 9,467 | +29 | 5,392,802 | 0.2% | 22.25B | 1 |
| 34 | Bielik-4.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 8,544 | +431 | 263,649 | 2.3% | 4.76B | 8 |
| 35 | Apertus v1.1 4B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 8,194 | +296 | 24,460 | 6.6% | 3.83B | 5 |
| 36 | Mistral Large 3 (675B, 2512) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 8,048 | +110 | 89,480 | 4.2% | — | 5 |
| 37 | Apertus v1.5 70B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,894 | -29 | 37,222 | 5.8% | 72.01B | 4 |
| 38 | Bielik-11B v3.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 7,808 | +854 | 7,808 | 7.2% | 11.17B | 8 |
| 39 | Pixtral 12B (2409) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 7,535 | +159 | 144,139 | 3.1% | — | 2 |
| 40 | Apertus v1.1 1.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 7,485 | +173 | 17,870 | 6.4% | 1.51B | 6 |
| 41 | Llama-Krikri 8B | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 7,104 | -255 | 120,903 | 3.2% | 8.42B | 7 |
| 42 | Llama-Poro 2 8B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 6,922 | +50 | 58,302 | 4.4% | 8.03B | 7 |
| 43 | Voxtral Small 24B (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 6,890 | +37 | 998,922 | 0.6% | 24.26B | 1 |
| 44 | EuroLLM-22B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,547 | +2 | 605,935 | 0.9% | 22.64B | 1 |
| 45 | EuroLLM-9B-Instruct (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 6,512 | -77 | 162,316 | 2.5% | 9.15B | 1 |
| 46 | Apertus v1.1 0.5B | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,444 | -82 | 24,773 | 5.2% | 572.6M | 5 |
| 47 | Apertus 70B (2509) | CH | swiss-ai | [swiss-ai](https://huggingface.co/swiss-ai) | 6,391 | -532 | 552,593 | 1.0% | 70.60B | 2 |
| 48 | Minerva 3B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,839 | -6 | 138,963 | 2.4% | 2.89B | 1 |
| 49 | Salamandra 2B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 5,738 | +106 | 153,899 | 2.3% | 2.25B | 7 |
| 50 | Minerva 350M v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 5,600 | +1 | 159,924 | 2.2% | 351.6M | 1 |
| 51 | Bielik-1.5B v3.0 | PL | SpeakLeash | [speakleash](https://huggingface.co/speakleash) | 5,356 | -60 | 65,694 | 3.2% | 1.60B | 9 |
| 52 | Monad | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 4,970 | +116 | 39,757 | 3.6% | 56.7M | 1 |
| 53 | EuroLLM-22B (2512 base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 4,483 | +170 | 29,775 | 3.5% | 22.64B | 1 |
| 54 | Maestrale Chat v0.4 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 4,402 | -15 | 155,772 | 1.7% | 7.24B | 4 |
| 55 | Modello Italia 9B | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,195 | -8 | 125,502 | 1.9% | 8.54B | 2 |
| 56 | Minerva 7B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 4,100 | -36 | 141,422 | 1.7% | 7.40B | 3 |
| 57 | Occiglot 7B (bilingual) | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 4,044 | -7 | 379,107 | 0.8% | 7.24B | 8 |
| 58 | ALIA 40B Instruct (2606) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,963 | +28 | 12,660 | 3.5% | 40.43B | 2 |
| 59 | Bielik-Minitron 7B v3.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 3,759 | +155 | 131,860 | 1.6% | 7.48B | 9 |
| 60 | EuroMoE 2.6B-A0.6B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,751 | -29 | 41,889 | 2.6% | 2.61B | 3 |
| 61 | Salamandra 7B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 3,726 | +4 | 55,589 | 2.4% | 7.77B | 3 |
| 62 | OpenEuroLLM Prelude-base 9B | EU | openeurollm | [openeurollm](https://huggingface.co/openeurollm) | 3,694 | +89 | 79,248 | 2.1% | 9.09B | 1 |
| 63 | Domyn Edge | IT | Domyn | [domyn](https://huggingface.co/domyn) | 3,639 | +104 | 3,684 | 3.5% | 3.93B | 2 |
| 64 | Baguettotron | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 3,513 | -10 | 45,200 | 2.4% | 13.29B | 3 |
| 65 | BgGPT Gemma 3 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 3,344 | -52 | 22,987 | 2.7% | 27.43B | 3 |
| 66 | EuroLLM-9B (2512) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 3,342 | +56 | 13,639 | 2.9% | 9.15B | 1 |
| 67 | Minerva Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 3,219 | -6 | 97,060 | 1.6% | 2.89B | 1 |
| 68 | AI Sweden Llama 3 8B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3,001 | +54 | 96,196 | 1.5% | 8.03B | 10 |
| 69 | Bielik-11B v2.2 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 2,988 | -8 | 170,634 | 1.1% | 11.17B | 16 |
| 70 | Velvet 14B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,804 | -4 | 70,753 | 1.6% | 14.08B | 1 |
| 71 | MamayLM Gemma 3 12B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,792 | +12 | 21,569 | 2.3% | 12.19B | 2 |
| 72 | Velvet 2B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2,748 | -4 | 89,619 | 1.4% | 2.22B | 1 |
| 73 | EuroLLM-9B (base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 2,685 | +18 | 87,172 | 1.4% | 9.15B | 1 |
| 74 | Poro 34B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 2,294 | -56 | 231,219 | 0.7% | 35.13B | 4 |
| 75 | TildeOpen 30B | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 2,255 | -12 | 103,112 | 1.1% | 30.68B | 1 |
| 76 | MamayLM Gemma 3 4B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2,239 | +87 | 23,595 | 1.8% | 4.30B | 2 |
| 77 | Teuken 7B v0.4 (research) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 2,097 | -2 | 81,452 | 1.2% | 7.45B | 1 |
| 78 | TRURL 2 13B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 2,097 | -8 | 359,097 | 0.5% | — | 3 |
| 79 | GaMS 9B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 2,073 | +2 | 52,453 | 1.4% | 9.24B | 4 |
| 80 | ALIA 40B (base) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 2,060 | +4 | 455,019 | 0.4% | 40.43B | 1 |
| 81 | Qra 1B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 2,025 | -4 | 160,671 | 0.8% | 1.10B | 1 |
| 82 | Teuken 7B v0.4 (commercial) | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 1,990 | -6 | 108,968 | 1.0% | 7.45B | 1 |
| 83 | Magistral Small (2507) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 1,938 | -114 | 157,559 | 0.8% | 23.57B | 2 |
| 84 | Qra 7B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,907 | -4 | 187,389 | 0.7% | 6.74B | 1 |
| 85 | TRURL 2 7B | PL | Voicelab | [Voicelab](https://huggingface.co/Voicelab) | 1,907 | -6 | 304,059 | 0.5% | 6.74B | 2 |
| 86 | EuroLLM-22B-Instruct (Preview) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 1,905 | -4 | 35,620 | 1.4% | 22.64B | 1 |
| 87 | Domyn Small v1.0 | IT | Domyn | [domyn](https://huggingface.co/domyn) | 1,872 | +111 | 10,505 | 1.7% | 9.82B | 1 |
| 88 | Pleias 350M Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,871 | +88 | 420,559 | 0.4% | 353.4M | 1 |
| 89 | Qra 13B | PL | OPI-PG | [OPI-PG](https://huggingface.co/OPI-PG) | 1,843 | -2 | 148,107 | 0.7% | 13.02B | 1 |
| 90 | Pleias 1.2B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,780 | +76 | 417,134 | 0.3% | 1.20B | 1 |
| 91 | PLLuM 12B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,769 | +15 | 180,347 | 0.6% | 12.25B | 6 |
| 92 | Pleias 3B Preview | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 1,761 | +89 | 401,989 | 0.4% | 3.21B | 1 |
| 93 | LeoLM HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 1,634 | 0 | 802,719 | 0.2% | — | 3 |
| 94 | Llama-Poro 2 70B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,554 | -62 | 41,208 | 1.1% | 70.55B | 3 |
| 95 | Maestrale Chat v0.3 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,527 | -3 | 55,195 | 1.0% | 7.24B | 5 |
| 96 | Maestrale Chat v0.2 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 1,463 | -7 | 53,941 | 1.0% | 7.24B | 1 |
| 97 | Viking 13B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,445 | -5 | 34,799 | 1.1% | 14.03B | 1 |
| 98 | PLLuM 12B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,400 | -47 | 45,010 | 1.0% | 12.25B | 3 |
| 99 | PLLuM 4B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1,346 | -11 | 9,851 | 1.2% | 4.30B | 3 |
| 100 | Bielik-11B v2.6 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 1,183 | +13 | 175,494 | 0.4% | 11.51B | 9 |
| 101 | Viking 7B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,158 | +5 | 57,060 | 0.7% | 7.55B | 1 |
| 102 | CroissantLLM Base | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 1,055 | -25 | 59,024 | 0.7% | 1.35B | 3 |
| 103 | Viking 33B | FI | LumiOpen | [LumiOpen](https://huggingface.co/LumiOpen) | 1,039 | -13 | 31,982 | 0.8% | 33.12B | 1 |
| 104 | MamayLM Gemma 3 27B v2.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,026 | -250 | 9,622 | 0.9% | 28.84B | 3 |
| 105 | MamayLM Gemma 3 12B v1.0 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 1,002 | +15 | 45,387 | 0.7% | 12.19B | 2 |
| 106 | Teuken 7B v0.6 | DE | openGPT-X | [openGPT-X](https://huggingface.co/openGPT-X) | 993 | -5 | 671,640 | 0.1% | 7.45B | 2 |
| 107 | BgGPT Gemma 3 12B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 927 | -47 | 219,368 | 0.3% | 12.19B | 3 |
| 108 | LeoLM Mistral HessianAI 7B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 880 | +2 | 233,735 | 0.3% | — | 2 |
| 109 | EuroVLM 9B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 876 | +1 | 8,610 | 0.8% | 9.57B | 1 |
| 110 | Baguettotron 600M | FR | PleIAs | [PleIAs](https://huggingface.co/PleIAs) | 840 | -1 | 1,863 | 0.8% | 608.3M | 1 |
| 111 | Bielik-11B v2.0 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 837 | +30 | 24,260 | 0.7% | 11.17B | 5 |
| 112 | CroissantLLM Chat v0.1 | FR | croissantllm | [croissantllm](https://huggingface.co/croissantllm) | 834 | +22 | 96,866 | 0.4% | 1.35B | 8 |
| 113 | Pharia-1-LLM-7B-control | DE | Aleph Alpha | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 786 | -12 | 82,161 | 0.4% | 7.04B | 4 |
| 114 | BgGPT Gemma 3 4B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 762 | -4 | 15,044 | 0.7% | 4.33B | 3 |
| 115 | Bielik-11B v2.1 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 702 | +8 | 32,004 | 0.5% | 11.17B | 5 |
| 116 | BgGPT 7B v0.2 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 699 | -11 | 112,610 | 0.3% | 7.29B | 2 |
| 117 | GaMS 1B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 698 | -7 | 17,188 | 0.6% | 1.54B | 4 |
| 118 | EuroLLM 1.5 9B | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 656 | +223 | 1,535 | 0.6% | 9.15B | 2 |
| 119 | GaMS 2B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 654 | +12 | 20,987 | 0.5% | 3.20B | 2 |
| 120 | TildeOpen 30B (64k) | LV | Tilde | [TildeAI](https://huggingface.co/TildeAI) | 586 | +1 | 3,851 | 0.6% | 30.68B | 1 |
| 121 | BgGPT Gemma 2 9B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 584 | 0 | 28,082 | 0.5% | 9.24B | 2 |
| 122 | Soofi S Isar Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 554 | 0 | 12,588 | 0.5% | 31.59B | 6 |
| 123 | GaMS2 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 534 | -3 | 1,799 | 0.5% | 852,480 | 2 |
| 124 | MamayLM Gemma 2 9B v0.1 | UA | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 486 | -14 | 22,275 | 0.4% | 9.24B | 2 |
| 125 | Bielik-11B v2.5 | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 467 | +22 | 5,821 | 0.4% | 11.51B | 5 |
| 126 | Llama-PLLuM 8B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 462 | +12 | 4,579 | 0.4% | 8.03B | 3 |
| 127 | GaMS 27B | SI | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | [cjvt](https://huggingface.co/cjvt) | 351 | +16 | 38,047 | 0.3% | 27.23B | 3 |
| 128 | BgGPT Gemma 2 27B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 347 | -19 | 12,309 | 0.3% | 27.23B | 2 |
| 129 | OpenEuroLLM Prelude-long 9B | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 338 | +113 | 338 | 0.3% | 9.09B | 1 |
| 130 | BgGPT Gemma 2 2.6B | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 317 | +30 | 22,291 | 0.3% | 2.61B | 2 |
| 131 | Llama-PLLuM 8B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 313 | +13 | 70,694 | 0.2% | 8.03B | 3 |
| 132 | OpenEuroLLM Prelude SFT Excellent v0.2 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 310 | +2 | 310 | 0.3% | 9.09B | 1 |
| 133 | LeoLM HessianAI 13B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 289 | +3 | 107,386 | 0.1% | — | 3 |
| 134 | Nesso 4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 251 | -7 | 2,883 | 0.2% | 4.02B | 2 |
| 135 | Mambaoutai 1.6B | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 249 | -27 | 1,397 | 0.2% | 1.62B | 1 |
| 136 | ALIA 40B Instruct (2601) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 243 | +6 | 32,997 | 0.2% | 40.43B | 2 |
| 137 | Minerva 1B v1.0 | IT | SapienzaNLP | [sapienzanlp](https://huggingface.co/sapienzanlp) | 229 | +27 | 29,890 | 0.2% | 1.01B | 1 |
| 138 | Bielik-11B v2 (base) | PL | SpeakLeash / ACK Cyfronet AGH | [speakleash](https://huggingface.co/speakleash) | 217 | +7 | 42,022 | 0.2% | 11.17B | 1 |
| 139 | LeoLM HessianAI 70B | DE | LeoLM | [LeoLM](https://huggingface.co/LeoLM) | 196 | -2 | 19,778 | 0.2% | 68.98B | 2 |
| 140 | Soofi S Rhine Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 187 | 0 | 3,006 | 0.2% | 31.59B | 6 |
| 141 | BgGPT 7B v0.1 | BG | INSAIT | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 184 | -3 | 16,719 | 0.2% | 7.29B | 2 |
| 142 | PAGnol xl | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 179 | +1 | 1,639 | 0.2% | 1.64B | 1 |
| 143 | Occiglot 7B EU5 | EU | occiglot | [occiglot](https://huggingface.co/occiglot) | 177 | -4 | 322,358 | 0.0% | 7.24B | 2 |
| 144 | Alfred 40B (1023) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 170 | 0 | 78,647 | 0.1% | — | 1 |
| 145 | Meltemi 7B v1.5 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 169 | 0 | 39,483 | 0.1% | 7.48B | 2 |
| 146 | Pixtral Large (2411) | FR | Mistral AI | [mistralai](https://huggingface.co/mistralai) | 169 | -15 | 4,492 | 0.2% | — | 1 |
| 147 | Velvet2 3B Speech | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 169 | -6 | 204 | 0.2% | 4.55B | 1 |
| 148 | TowerVision 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 165 | -3 | 2,785 | 0.2% | 3.02B | 1 |
| 149 | PLLuM 8x7B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 163 | +7 | 28,518 | 0.1% | 46.70B | 6 |
| 150 | Meltemi 7B v1 | GR | ILSP | [ilsp](https://huggingface.co/ilsp) | 151 | -10 | 44,721 | 0.1% | 7.70B | 5 |
| 151 | Llama-PLLuM 70B (2512) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 139 | -2 | 12,784 | 0.1% | 70.55B | 2 |
| 152 | ALIA 40B Instruct (2605) | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 137 | +7 | 2,966 | 0.1% | 40.43B | 2 |
| 153 | GPT-SW3 1.3B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 129 | 0 | 306,785 | 0.0% | 1.47B | 4 |
| 154 | Zagreus 0.4B (ITA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 126 | +2 | 5,238 | 0.1% | 437.8M | 1 |
| 155 | Salamandra VL 7B (2512) | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 123 | 0 | 2,101 | 0.1% | 8.90B | 1 |
| 156 | EuroLLM-22B (Preview base) | EU | utter-project | [utter-project](https://huggingface.co/utter-project) | 120 | -1 | 2,609 | 0.1% | — | 1 |
| 157 | Velvet2 3B | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 113 | +15 | 130 | 0.1% | 3.89B | 1 |
| 158 | PAGnol medium | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 106 | +1 | 1,164 | 0.1% | 380.0M | 1 |
| 159 | Soofi S Instruct Preview | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 105 | -8 | 7,511 | 0.1% | 31.59B | 6 |
| 160 | Llama-PLLuM 70B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 104 | -11 | 5,114 | 0.1% | 70.55B | 3 |
| 161 | Alfred 40B (0723) | FR | LightOn | [lightonai](https://huggingface.co/lightonai) | 97 | -1 | 5,545 | 0.1% | — | 1 |
| 162 | EuroVLM 1.7B Preview | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 95 | -3 | 3,043 | 0.1% | 2.06B | 1 |
| 163 | Llama-PLLuM 70B (2412) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 93 | +11 | 38,777 | 0.1% | 70.55B | 3 |
| 164 | Open Zagreus 0.4B | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 93 | 0 | 474 | 0.1% | 437.8M | 1 |
| 165 | TowerVision 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 86 | -20 | 1,384 | 0.1% | 9.66B | 1 |
| 166 | CroissantCool v0.2 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 85 | 0 | 14,810 | 0.1% | 1.35B | 1 |
| 167 | PAGnol small | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 68 | 0 | 4,664 | 0.1% | — | 1 |
| 168 | PAGnol large | FR | LightOn / Inria | [lightonai](https://huggingface.co/lightonai) | 66 | +1 | 889 | 0.1% | — | 1 |
| 169 | Zagreus 0.4B (FRA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 65 | +1 | 217 | 0.1% | 437.8M | 1 |
| 170 | Zagreus 0.4B (SPA) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 65 | 0 | 275 | 0.1% | 437.8M | 1 |
| 171 | Velvet2 3B Vision | IT | Almawave | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 63 | 0 | 78 | 0.1% | 4.33B | 1 |
| 172 | Nesso 0.4B Instruct | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 61 | +1 | 1,334 | 0.1% | 560.9M | 1 |
| 173 | OpenEuroLLM Prelude SFT Excellent v0.1 | EU | OpenEuroLLM | [openeurollm](https://huggingface.co/openeurollm) | 55 | 0 | 58 | 0.1% | 9.10B | 1 |
| 174 | TowerVideo 2B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 55 | -6 | 1,132 | 0.1% | 3.02B | 1 |
| 175 | Zagreus 0.4B (POR) | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 55 | +1 | 321 | 0.1% | 437.8M | 1 |
| 176 | TowerVideo 9B | EU | UTTER consortium | [utter-project](https://huggingface.co/utter-project) | 47 | -5 | 484 | 0.0% | 9.66B | 1 |
| 177 | Salamandra 7B Vision | ES | Barcelona Supercomputing Center | [BSC-LT](https://huggingface.co/BSC-LT) | 43 | 0 | 3,721 | 0.0% | 8.19B | 1 |
| 178 | Llama-PLLuM 8B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 37 | -7 | 1,465 | 0.0% | 8.03B | 1 |
| 179 | Flor 6.3B | ES | BSC-LT | [BSC-LT](https://huggingface.co/BSC-LT) | 36 | -1 | 624 | 0.0% | 6.25B | 2 |
| 180 | NorwAI Magistral 24B reasoning | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 31 | 0 | 547,892 | 0.0% | 23.85B | 1 |
| 181 | Maestrale Chat v0.1 | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 30 | 0 | 154 | 0.0% | 7.24B | 1 |
| 182 | CroissantCool v0.1 | FR | CroissantLLM consortium | [croissantllm](https://huggingface.co/croissantllm) | 27 | -1 | 606 | 0.0% | 1.35B | 1 |
| 183 | NorwAI Mistral-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 25 | 0 | 111,668 | 0.0% | 7.54B | 3 |
| 184 | GPT-SW3 20B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 22 | 0 | 141,983 | 0.0% | 20.92B | 5 |
| 185 | Tyr 7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 21 | -1 | 913 | 0.0% | 7.24B | 1 |
| 186 | PLLuM 12B (2508) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 19 | 0 | 381 | 0.0% | 12.25B | 1 |
| 187 | GPT-sl Base | SI | CJVT UL | [cjvt](https://huggingface.co/cjvt) | 16 | 0 | 1,762 | 0.0% | — | 1 |
| 188 | GPT-SW3 126M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 10 | 0 | 893,762 | 0.0% | 186.1M | 4 |
| 189 | Soofi S Base | DE | Soofi Project | [Soofi-Project](https://huggingface.co/Soofi-Project) | 8 | 0 | 1,509 | 0.0% | 31.58B | 2 |
| 190 | GPT-SW3 6.7B v2 | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 7 | 0 | 262,851 | 0.0% | 7.11B | 5 |
| 191 | PLLuM 12B nc (2507) | PL | CYFRAGOVPL / PLLuM consortium | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 4 | 0 | 6,171 | 0.0% | 12.25B | 3 |
| 192 | GPT-SW3 40B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 3 | 0 | 59,796 | 0.0% | 39.93B | 2 |
| 193 | Emma 5 Boost | IT | mii-llm | [mii-llm](https://huggingface.co/mii-llm) | 0 | 0 | 8 | 0.0% | 1.39B | 1 |
| 194 | GPT-SW3 356M | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 334,511 | 0.0% | 470.6M | 4 |
| 195 | GPT-SW3 6.7B | SE | AI Sweden | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0 | 0 | 68,906 | 0.0% | 7.11B | 1 |
| 196 | NorwAI Llama2-7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | 0 | 65,548 | 0.0% | 7.03B | 1 |
| 197 | NorwAI Mixtral-8x7B | NO | NorwAI / NTNU | [NorwAI](https://huggingface.co/NorwAI) | 0 | 0 | 2,172 | 0.0% | 47.00B | 2 |

## Organizations

Same downloads, aggregated across every model version an organization publishes.

| Rank | Organization | Developer | Country | Downloads (30d) | All-time | Models | Momentum |
| ---: | --- | --- | :---: | ---: | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral AI | FR | 6,070,325 | 302,120,970 | 27 | 2.0% |
| 2 | [swiss-ai](https://huggingface.co/swiss-ai) | swiss-ai | CH | 228,869 | 6,108,394 | 7 | 3.7% |
| 3 | [cjvt](https://huggingface.co/cjvt) | CJVT UL (Center za jezikovne vire in tehnologije, University of Ljubljana) | SI | 217,611 | 464,651 | 7 | 38.5% |
| 4 | [speakleash](https://huggingface.co/speakleash) | SpeakLeash / ACK Cyfronet AGH | PL | 194,131 | 6,552,077 | 13 | 2.9% |
| 5 | [utter-project](https://huggingface.co/utter-project) | utter-project | EU | 75,556 | 2,697,827 | 18 | 2.7% |
| 6 | [BSC-LT](https://huggingface.co/BSC-LT) | BSC-LT | ES | 51,836 | 1,457,831 | 10 | 3.3% |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | SapienzaNLP | IT | 19,963 | 595,701 | 5 | 2.9% |
| 8 | [PleIAs](https://huggingface.co/PleIAs) | PleIAs | FR | 14,735 | 1,326,502 | 6 | 1.0% |
| 9 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | INSAIT | BG | 14,709 | 571,858 | 13 | 2.2% |
| 10 | [LumiOpen](https://huggingface.co/LumiOpen) | LumiOpen | FI | 14,412 | 454,570 | 6 | 2.6% |
| 11 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Aleph Alpha | DE | 13,662 | 118,466 | 2 | 6.3% |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | mii-llm | IT | 11,357 | 372,872 | 13 | 2.4% |
| 13 | [ilsp](https://huggingface.co/ilsp) | ILSP | GR | 7,424 | 205,107 | 3 | 2.4% |
| 14 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Almawave | IT | 5,897 | 160,784 | 5 | 2.3% |
| 15 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | CYFRAGOVPL / PLLuM consortium | PL | 5,849 | 403,691 | 12 | 1.2% |
| 16 | [OPI-PG](https://huggingface.co/OPI-PG) | OPI-PG | PL | 5,775 | 496,167 | 3 | 1.0% |
| 17 | [domyn](https://huggingface.co/domyn) | Domyn | IT | 5,511 | 14,189 | 2 | 4.8% |
| 18 | [openGPT-X](https://huggingface.co/openGPT-X) | openGPT-X | DE | 5,080 | 862,060 | 3 | 0.5% |
| 19 | [openeurollm](https://huggingface.co/openeurollm) | openeurollm | EU | 4,397 | 79,954 | 4 | 2.4% |
| 20 | [occiglot](https://huggingface.co/occiglot) | occiglot | EU | 4,221 | 701,465 | 2 | 0.5% |
| 21 | [Voicelab](https://huggingface.co/Voicelab) | Voicelab | PL | 4,004 | 663,156 | 2 | 0.5% |
| 22 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden | SE | 3,193 | 2,165,703 | 9 | 0.1% |
| 23 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM | DE | 2,999 | 1,163,618 | 4 | 0.2% |
| 24 | [TildeAI](https://huggingface.co/TildeAI) | Tilde | LV | 2,841 | 106,963 | 2 | 1.4% |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | croissantllm | FR | 2,001 | 171,306 | 4 | 0.7% |
| 26 | [lightonai](https://huggingface.co/lightonai) | LightOn | FR | 935 | 93,945 | 7 | 0.5% |
| 27 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi Project | DE | 854 | 24,614 | 4 | 0.7% |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI / NTNU | NO | 56 | 727,280 | 4 | 0.0% |

### By best single model

Ranked by each organization's single highest-downloading model (no summing across versions) — who has the biggest individual hit.

| Rank | Organization | Best model | Downloads (30d) | All-time | Overall model rank |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | [mistralai](https://huggingface.co/mistralai) | Mistral 7B v0.3 | 2,037,287 | 60,922,075 | 1 |
| 2 | [cjvt](https://huggingface.co/cjvt) | GaMS3 12B | 213,285 | 332,415 | 7 |
| 3 | [swiss-ai](https://huggingface.co/swiss-ai) | Apertus 8B (2509) | 176,914 | 4,700,450 | 9 |
| 4 | [speakleash](https://huggingface.co/speakleash) | Bielik-11B v3.0 | 134,240 | 4,301,723 | 11 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | Salamandra 7B Instruct | 35,767 | 738,255 | 19 |
| 6 | [utter-project](https://huggingface.co/utter-project) | EuroLLM-1.7B-Instruct | 19,694 | 948,630 | 22 |
| 7 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | Kolibri-1 | 12,876 | 36,305 | 29 |
| 8 | [ilsp](https://huggingface.co/ilsp) | Llama-Krikri 8B | 7,104 | 120,903 | 41 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | Llama-Poro 2 8B | 6,922 | 58,302 | 42 |
| 10 | [sapienzanlp](https://huggingface.co/sapienzanlp) | Minerva 3B v1.0 | 5,839 | 138,963 | 48 |
| 11 | [PleIAs](https://huggingface.co/PleIAs) | Monad | 4,970 | 39,757 | 52 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | Maestrale Chat v0.4 | 4,402 | 155,772 | 54 |
| 13 | [occiglot](https://huggingface.co/occiglot) | Occiglot 7B (bilingual) | 4,044 | 379,107 | 57 |
| 14 | [openeurollm](https://huggingface.co/openeurollm) | OpenEuroLLM Prelude-base 9B | 3,694 | 79,248 | 62 |
| 15 | [domyn](https://huggingface.co/domyn) | Domyn Edge | 3,639 | 3,684 | 63 |
| 16 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | BgGPT Gemma 3 27B | 3,344 | 22,987 | 65 |
| 17 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | AI Sweden Llama 3 8B | 3,001 | 96,196 | 68 |
| 18 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | Velvet 14B | 2,804 | 70,753 | 70 |
| 19 | [TildeAI](https://huggingface.co/TildeAI) | TildeOpen 30B | 2,255 | 103,112 | 75 |
| 20 | [Voicelab](https://huggingface.co/Voicelab) | TRURL 2 13B | 2,097 | 359,097 | 78 |
| 21 | [openGPT-X](https://huggingface.co/openGPT-X) | Teuken 7B v0.4 (research) | 2,097 | 81,452 | 77 |
| 22 | [OPI-PG](https://huggingface.co/OPI-PG) | Qra 1B | 2,025 | 160,671 | 81 |
| 23 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | PLLuM 12B (2412) | 1,769 | 180,347 | 91 |
| 24 | [LeoLM](https://huggingface.co/LeoLM) | LeoLM HessianAI 7B | 1,634 | 802,719 | 93 |
| 25 | [croissantllm](https://huggingface.co/croissantllm) | CroissantLLM Base | 1,055 | 59,024 | 102 |
| 26 | [Soofi-Project](https://huggingface.co/Soofi-Project) | Soofi S Isar Preview | 554 | 12,588 | 122 |
| 27 | [lightonai](https://huggingface.co/lightonai) | Mambaoutai 1.6B | 249 | 1,397 | 135 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | NorwAI Magistral 24B reasoning | 31 | 547,892 | 180 |

### By momentum

Sorted by momentum (highest first). Momentum highlights orgs whose recent downloads are large *relative to their lifetime total* — i.e. accelerating adoption, not legacy long-tail traffic from an old release.

| Momentum rank | Organization | Momentum | Downloads (30d) | All-time | Downloads rank |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | [cjvt](https://huggingface.co/cjvt) | 38.5% | 217,611 | 464,651 | 3 |
| 2 | [Aleph-Alpha](https://huggingface.co/Aleph-Alpha) | 6.3% | 13,662 | 118,466 | 11 |
| 3 | [domyn](https://huggingface.co/domyn) | 4.8% | 5,511 | 14,189 | 17 |
| 4 | [swiss-ai](https://huggingface.co/swiss-ai) | 3.7% | 228,869 | 6,108,394 | 2 |
| 5 | [BSC-LT](https://huggingface.co/BSC-LT) | 3.3% | 51,836 | 1,457,831 | 6 |
| 6 | [speakleash](https://huggingface.co/speakleash) | 2.9% | 194,131 | 6,552,077 | 4 |
| 7 | [sapienzanlp](https://huggingface.co/sapienzanlp) | 2.9% | 19,963 | 595,701 | 7 |
| 8 | [utter-project](https://huggingface.co/utter-project) | 2.7% | 75,556 | 2,697,827 | 5 |
| 9 | [LumiOpen](https://huggingface.co/LumiOpen) | 2.6% | 14,412 | 454,570 | 10 |
| 10 | [openeurollm](https://huggingface.co/openeurollm) | 2.4% | 4,397 | 79,954 | 19 |
| 11 | [ilsp](https://huggingface.co/ilsp) | 2.4% | 7,424 | 205,107 | 13 |
| 12 | [mii-llm](https://huggingface.co/mii-llm) | 2.4% | 11,357 | 372,872 | 12 |
| 13 | [AlmawaveLabs](https://huggingface.co/AlmawaveLabs) | 2.3% | 5,897 | 160,784 | 14 |
| 14 | [INSAIT-Institute](https://huggingface.co/INSAIT-Institute) | 2.2% | 14,709 | 571,858 | 9 |
| 15 | [mistralai](https://huggingface.co/mistralai) | 2.0% | 6,070,325 | 302,120,970 | 1 |
| 16 | [TildeAI](https://huggingface.co/TildeAI) | 1.4% | 2,841 | 106,963 | 24 |
| 17 | [CYFRAGOVPL](https://huggingface.co/CYFRAGOVPL) | 1.2% | 5,849 | 403,691 | 15 |
| 18 | [PleIAs](https://huggingface.co/PleIAs) | 1.0% | 14,735 | 1,326,502 | 8 |
| 19 | [OPI-PG](https://huggingface.co/OPI-PG) | 1.0% | 5,775 | 496,167 | 16 |
| 20 | [croissantllm](https://huggingface.co/croissantllm) | 0.7% | 2,001 | 171,306 | 25 |
| 21 | [Soofi-Project](https://huggingface.co/Soofi-Project) | 0.7% | 854 | 24,614 | 27 |
| 22 | [openGPT-X](https://huggingface.co/openGPT-X) | 0.5% | 5,080 | 862,060 | 18 |
| 23 | [occiglot](https://huggingface.co/occiglot) | 0.5% | 4,221 | 701,465 | 20 |
| 24 | [Voicelab](https://huggingface.co/Voicelab) | 0.5% | 4,004 | 663,156 | 21 |
| 25 | [lightonai](https://huggingface.co/lightonai) | 0.5% | 935 | 93,945 | 26 |
| 26 | [LeoLM](https://huggingface.co/LeoLM) | 0.2% | 2,999 | 1,163,618 | 23 |
| 27 | [AI-Sweden-Models](https://huggingface.co/AI-Sweden-Models) | 0.1% | 3,193 | 2,165,703 | 22 |
| 28 | [NorwAI](https://huggingface.co/NorwAI) | 0.0% | 56 | 727,280 | 28 |

## Notes

- Downloads are Hugging Face Hub **rolling last-30-day** counts, aggregated over official repos matched by config regexes (GGUF / MLX / FP8 / etc. when published by the same org).
- **Params** is the max reported parameter count among member repos (`safetensors.total`, else `gguf.total`).
- **Momentum** = `downloads_30d / (downloads_all_time + 100,000)` — a recency ratio damped by a smoothing constant so low-volume/brand-new rows can't look like they have outsized momentum from a handful of downloads. Higher = more of its lifetime downloads happened in the last 30 days.
- **Trend charts** use [`data/metrics/timeseries.jsonl`](data/metrics/timeseries.jsonl). Rolling-30d lines follow HF’s sliding window; daily Δ lines use day-over-day changes in `downloads_all_time` (approximate new downloads, not unique users).
- Machine-readable data: [`output/leaderboard.json`](output/leaderboard.json), [`output/leaderboard.csv`](output/leaderboard.csv), [`output/leaderboard_orgs.json`](output/leaderboard_orgs.json), [`output/leaderboard_orgs.csv`](output/leaderboard_orgs.csv).
- How this is built / how to add models: [`DEVELOPMENT.md`](DEVELOPMENT.md).
- This file is regenerated by CI (`fetch` workflow) via `scripts/render_leaderboard_md.py`.
