# Tiraz

Tiraz is a mobile wardrobe coach combining outfit analysis, a digital closet, look composition and opt-in sharing. The existing Expo/React Native product uses a Supabase backend, structured model outputs, image processing and subscription workflows.

[![Tiraz concept demo poster](../assets/tiraz.png)](https://yusef-product-demos.yoosefseed.chatgpt.site/#tiraz)

[Concept demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#tiraz) · [Reproducible research companion](https://github.com/YusefSyed/tiraz-garment-completion)

The demo is a concept visualization. The companion repository contains a new experiment for Tiraz; it is not a separate consumer app and contains no private application code or images.

## Research upgrade: garment-category completion

I built a PyTorch experiment that hides one apparel category from an annotated image's unordered category set and predicts it from the remaining categories. Three seeded Deep Sets-style encoders are compared with training-frequency and smoothed co-occurrence baselines on the same task.

The pipeline streams Fashionpedia annotations without downloading images, groups normalized source URLs and removes overlap between the training source and final test. It creates one deterministic masked target per eligible group. Only category IDs enter the model; the target category, source identity, pixels and URLs are excluded from its inputs.

Training uses **27,683 source-grouped examples**, with separate tuning, temperature-calibration and conformal-calibration partitions. Checkpoints are selected by tuning loss. Final evaluation uses **962 held-out official-validation groups**; all three seeds and both original and missing-context conditions are reported.

## Measured results

| Model | Original top-1 accuracy | Macro F1, all 27 classes | Missing-context top-1 |
| --- | ---: | ---: | ---: |
| Frequency | 37.8% | 0.042 | 35.3% |
| Co-occurrence | 52.7% | 0.125 | 37.9% |
| Set encoder, three seeds | **58.5–59.0%** | **0.165–0.171** | 36.7–37.3% |

On the original condition, the neural models' nominal 90% conformal prediction sets achieved **91.1–91.2% measured coverage**, averaging about 4.7 candidate categories versus 8.3 for co-occurrence. With additional visible context removed, neural coverage fell to **55.6–57.9%**, and co-occurrence performed better on top-1 accuracy. This exposes a limitation under missing context despite the neural advantage on the original task.

[Complete results](https://github.com/YusefSyed/tiraz-garment-completion/blob/main/artifacts/v1/report.md) · [Metrics and intervals](https://github.com/YusefSyed/tiraz-garment-completion/blob/main/artifacts/v1/metrics.json) · [Frozen protocol](https://github.com/YusefSyed/tiraz-garment-completion/blob/main/protocol.json)

## Reproducibility and task boundaries

Two complete CPU runs reproduced all **11 artifacts byte-for-byte**, including trained checkpoints. The package passes 24 Python tests, Ruff and strict mypy checks, with [GitHub Actions verification](https://github.com/YusefSyed/tiraz-garment-completion/actions/runs/33293667518). Input hashes, source, configuration, predictions and weights are recorded with the experiment; unsupported inputs and attempts to overwrite prior runs are rejected.

These results measure **category-set completion**. The historical extraction result (F1 0.333) and the separate 50-crop classification result (47/50) remain different tasks and are unchanged. Neither is a result from this experiment. The existing app ranker is unchanged. No image-recognition, human-taste or production recommendation accuracy is established.

Nominal conformal coverage requires exchangeability; the reported stress result demonstrates why it cannot be assumed for changed inputs. Source-group bootstrap intervals are descriptive, and exact-URL grouping does not prove visual or semantic deduplication. Fashionpedia annotations and ontology are used under CC BY 4.0; attribution, method references and reproduction commands are in the public companion.
