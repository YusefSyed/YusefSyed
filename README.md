# Yusef Syed

### Software engineer building AI-powered mobile and web products

Incoming University of Toronto student, September 2026

Toronto / Pennsylvania · Open to relocation and remote · Canadian–U.S. dual citizen

My work focuses on typed evaluation infrastructure, product reliability, security boundaries, and reproducible evidence across Python and TypeScript systems.

## Featured work

### [Agent Eval Mutation Lab](https://github.com/YusefSyed/agent-eval-mutation-lab) · Python evaluation reliability

A typed Python evaluation system for distinguishing proposed, executed and harmful tool actions. Its resumable engine runs 104 deterministic scorer tasks through transactional SQLite and a content-addressed evidence store. Tests detect all 14 predeclared development semantic mutants, and clean-checkout reproduction verifies 17 canonical artifacts byte-for-byte.

The optional missing-output auditor adds exact-rational sensitivity bounds, explicit estimands and endpoint witnesses, checked against 8,192 exhaustive small-case oracle evaluations. It keeps valid semantic uncertainty separate from invalid responses and makes unsupported point estimates visible.

A separate preregistered 624-trial study across two pinned local models failed five of six frozen promotion gates, including output validity. Promotion was withheld; all outcomes were released without invalid-response retries or post-hoc prompt tuning. The failed differential-validity gate prevents a clean arm-effect conclusion. The later diagnostic does not override that verdict.

### [Aesthetics AI](case-studies/AESTHETICS_AI.md) · iOS fitness product

[![Aesthetics AI product demo poster](assets/aesthetics-ai-v5-atlas.jpg)](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

A publicly released iOS product that turns physique and meal photos into structured reports, training plans and progress tools. Built with React Native, Expo, Supabase, validated structured-output LLM workflows and RevenueCat. [App Store](https://apps.apple.com/us/app/aesthetics-ai-physique-coach/id6773502055) · [Demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

Executable telemetry QA now reconciles actual app-module traces against controlled test schedules and rejects incomplete, duplicated, late or mismatched evidence before computing a metric. The case study publishes a sanitized falsification summary; it does not claim real-user retention.

### [CallReclaim](case-studies/CALLRECLAIM.md) · missed-call recovery

[![CallReclaim product demo poster](assets/callreclaim.png)](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

A private Next.js and Supabase missed-call recovery MVP connecting telephony, consent-aware messaging and validated structured LLM outputs. Its adversarial replay tool checks production JavaScript and PostgreSQL reconciliation functions and reduces ordering failures to small reproducible traces. A 256-schedule campaign covered 3,708 synthetic arrivals; the case study includes a two-event injected-failure reproduction. [Sample-data demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

### [Tiraz](case-studies/TIRAZ.md) · privacy-first wardrobe coach

[![Tiraz concept demo poster](assets/tiraz.png)](https://yusef-product-demos.yoosefseed.chatgpt.site/#tiraz)

A publicly released Expo/React Native wardrobe app backed by Supabase. Version 1.0.0 was released on the U.S. iOS App Store on July 31, 2026. The current proof branch adds privacy-gated share import, private cutouts, review-before-write AI tagging and owner-bound community controls with 91 source-level deterministic checks; those checks are not device, live-provider, deployed-backend or two-account proof. [App Store](https://apps.apple.com/us/app/tiraz/id6789730283)

The linked [Demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#tiraz) is a concept visualization, not a live-product capture. Apple's public record does not establish that Build 20 or the proof-layer branch is the distributed binary.

The new [public PyTorch research companion](https://github.com/YusefSyed/tiraz-garment-completion) trains garment-category completion models on 27,683 annotation-derived examples. Three seeds reach 58.5–59.0% held-out accuracy versus a 52.7% co-occurrence baseline, while the missing-context evaluation exposes a substantial prediction-set coverage drop. All 11 artifacts, including trained weights, reproduce byte-for-byte in the pinned CPU environment. This is category-set prediction, not fashion-taste or production image accuracy.

### [Agent Proof](https://github.com/YusefSyed/agent-proof) · open-source developer tool

A TypeScript CLI that runs reviewer-approved checks and produces local JSON and Markdown reports. It uses `execFile` with `shell: false`, exact command allowlists, timeouts, output redaction and truncation. [CI is passing](https://github.com/YusefSyed/agent-proof/actions/workflows/ci.yml).

### [Inspect Scout PR #586](https://github.com/meridianlabs-ai/inspect_scout/pull/586) · open upstream bug fix

Opened a focused upstream PR correcting per-result model-usage accounting for custom loaders, with a targeted regression test. The PR remains open and has not received maintainer review or attached CI checks.

## Engineering approach

- Turn ambiguous product requirements into working systems.
- Treat dependencies, logs and external inputs as untrusted until they are understood and tested.
- Design explicitly for privacy, consent and failure modes.
- Distinguish verified results from work that still needs production evidence.

## Current focus

Seeking Summer 2027 software engineering and AI product internships, especially backend, platform, evaluation, reliability and developer-tooling work. Available in the U.S. or Canada and open to relocation.

## Technologies

`Python` `PyTorch` `NumPy` `pytest` `mypy` `uv` `SQLite` `TypeScript` `JavaScript` `SQL` `React` `Next.js` `React Native` `Expo` `Supabase` `PostgreSQL` `Deno` `Structured LLM APIs` `Twilio` `RevenueCat` `GitHub Actions`

[Email](mailto:yusefmsyed@gmail.com)
