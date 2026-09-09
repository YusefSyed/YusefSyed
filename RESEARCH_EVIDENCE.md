# Research evidence

Updated September 9, 2026. I am a first-year University of Toronto student, intending Mathematics and Computer Science. My focus is AI-safety evaluation, agent oversight and reliable research software. These are personal projects with AI-assisted implementation, not research appointments or proof of unaided programming proficiency.

[Research resume](resume/Yusef_Syed_Resume.pdf) · [Email](mailto:yusef.syed@mail.utoronto.ca)

## Agent Eval Mutation Lab

[Repository](https://github.com/YusefSyed/agent-eval-mutation-lab) · [Pinned evidence](https://github.com/YusefSyed/agent-eval-mutation-lab/tree/c8422f03524aefef4b3fd99ea3a8314616a48ec6)

The deterministic engine evaluates 13 synthetic scenarios under four evidence conditions with two scorers: 104 scorer configurations. It separates proposed actions, executed effects and unknown outcomes. Independent state checks cover state changes before an error and publication followed by revocation.

A separate constrained integration contains 24 local-Qwen tool-use samples, not a general safety-rate estimate. A frozen 624-trial two-model study used a pre-specified, version-controlled protocol. Invalid-output rates differed between prompting conditions, so claims of improvement were withheld; descriptive results and missing-output sensitivity were retained. This was a protocol in the public Git history, not an external registration service. See the [results](https://github.com/YusefSyed/agent-eval-mutation-lab/blob/c8422f03524aefef4b3fd99ea3a8314616a48ec6/artifacts/engine/latest/results.jsonl), [local-model report](https://github.com/YusefSyed/agent-eval-mutation-lab/blob/c8422f03524aefef4b3fd99ea3a8314616a48ec6/artifacts/inspect-tool-execution/local-v1/REPORT.md), and [ownership limits](https://github.com/YusefSyed/agent-eval-mutation-lab/blob/c8422f03524aefef4b3fd99ea3a8314616a48ec6/OWNERSHIP.md).

Dated milestone receipts describe their pre-publication state as “not yet pushed.” The pinned public tree contains those receipts and completed engine evidence; the historical wording is not its current visibility status. In-progress work beyond that evidence is excluded here.

## Tiraz garment completion

[Repository](https://github.com/YusefSyed/tiraz-garment-completion) · [Pinned report](https://github.com/YusefSyed/tiraz-garment-completion/blob/aa11b97accd40219529c7b0c3bcd036078598b77/artifacts/v1/report.md)

Three seeded set encoders trained on 27,683 Fashionpedia annotation groups achieved 58.5-59.0% top-1 versus a 52.7% co-occurrence baseline on 962 held-out source groups. Training, tuning and calibration were separated. Under removed context, nominal 90% prediction-set coverage fell to 55.6-57.9%. This is a fixed annotation-only experiment, not image recognition, user-preference modelling or production-quality evidence.

## ShiftProof

[Repository and evaluation](https://github.com/YusefSyed/shiftproof) · [Submission](https://devpost.com/software/shiftproof-dftlh5)

A local scheduling prototype separates model suggestions from an independent constraint verifier and coordinator-only apply, approve and export operations. Its recorded workflow uses synthetic data; four inspected model requests excluded raw names, titles and instruction-like notes. The contest entry was submitted; no prize or selection is claimed.

## External open source

Nine PRs were verified merged in external upstream repositories on September 9, 2026:

- W&B RAI Toolkit: [30](https://github.com/wandb/rai-toolkit/pull/30), [31](https://github.com/wandb/rai-toolkit/pull/31), [51](https://github.com/wandb/rai-toolkit/pull/51), [52](https://github.com/wandb/rai-toolkit/pull/52).
- Microsoft Agent Lightning: [580](https://github.com/microsoft/agent-lightning/pull/580), [582](https://github.com/microsoft/agent-lightning/pull/582).
- Microsoft PyRIT: [2537](https://github.com/microsoft/PyRIT/pull/2537).
- Meridian Labs Inspect Scout: [586](https://github.com/meridianlabs-ai/inspect_scout/pull/586).
- Kornia: [4185](https://github.com/kornia/kornia/pull/4185).

These are contributions, not employment or maintainership. Locally written code, a passing test or an open PR does not establish upstream acceptance.

## Open PyTorch contribution

[PR 196390](https://github.com/pytorch/pytorch/pull/196390) · [Validation supplement](case-studies/pytorch-igamma-shape-gradients/README.md)

The CPU/CUDA incomplete-gamma shape-gradient PR is AI-assisted and open, separate from the nine merges. Local source-build validation compared 1,162 derivative outputs each on macOS CPU, Linux CPU and RTX A4000 CUDA: 3,486 comparisons, with no recorded corpus failures. The supplement contains the runner, numeric input/reference corpus, sanitized outputs and source-hash mapping. This is author-run sampled evidence, not upstream CI or an all-domain correctness theorem.
