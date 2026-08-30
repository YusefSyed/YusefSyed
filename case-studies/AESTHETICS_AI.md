# Aesthetics AI

Aesthetics AI is an iOS fitness product with structured photo reports, training plans, meal tools and progress tracking. Its stack combines Expo/React Native, TypeScript, Supabase/Postgres, validated model outputs and RevenueCat subscriptions.

[![Aesthetics AI product demo poster](../assets/aesthetics-ai-v5-atlas.jpg)](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

[App Store](https://apps.apple.com/us/app/aesthetics-ai-physique-coach/id6773502055) · [Product demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

## Engineering upgrade: trustworthy measurement

The instrumentation's `d1_return` and `d7_return` events record crossed milestones: a first return on day 10 emits both markers with `day_offset: 10`. Counting those markers as exact-day returns would misstate the measurement.

I built a behavioral harness that executes the actual TypeScript initialization module with controlled clocks, storage, app metadata and transport. A separate audit reconciles its traces against a predeclared test roster and independently authored app-open schedule. Units with no return remain in the denominator; incomplete observation or delivery evidence withholds the metric.

The validator checks identity, timing, source version and event consistency. Missing, duplicate, late and conflicting events, immature windows and app-version mismatches all prevent metric calculation. Diagnostic results remain stable when packet rows are reordered.

## Falsification and verification

An independently specified four-unit fixture establishes the expected elapsed-day app-open rate:

| Controlled case | Expected result | Observed result |
| --- | --- | --- |
| Day 1 window | 1 of 4 units | 1 of 4 |
| Day 7 window | 2 of 4 units | 2 of 4 |
| Six injected evidence faults | Withhold the metric | Withheld in every case |

The measurement suite passes **37 tests**, TypeScript checking and focused lint. GitHub Actions passed on August 30, 2026. The [sanitized evidence summary](evidence/2026-08-30/aesthetics-measurement.json) records the controlled cases and scope; application source remains private.

The compiled instrumentation runtime is unchanged. This upgrade adds executable measurement contracts and failure diagnosis. Its results concern controlled tests only and establish no production retention, real-user cohort completeness or product impact. The linked product demo uses labeled illustrative examples.
