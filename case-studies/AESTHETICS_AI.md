# Aesthetics AI

Aesthetics AI is an iOS fitness product with structured photo reports, training plans, meal tools and progress tracking. Its stack combines Expo/React Native, TypeScript, Supabase/Postgres, validated model outputs and RevenueCat subscriptions.

[![Aesthetics AI product demo poster](../assets/aesthetics-ai-v5-atlas.jpg)](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

[App Store](https://apps.apple.com/us/app/aesthetics-ai-physique-coach/id6773502055) · [Product demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#aesthetics-ai)

## Engineering upgrade: durable workout completion

The previous save path wrote a completed workout header before writing its exercise sets. A failure between those operations could leave an empty completed workout in cloud history and advance the training program. Production-mode saves also depended on the network before the workout received a durable local record.

I implemented an account-scoped completion journal. Finishing a workout first stores its stable session/set IDs and sealed payload locally, then syncs through one PostgreSQL transaction for the header and exact set collection. Identical retries are idempotent; reusing an ID with different data produces an explicit conflict. Set IDs cannot be silently moved between workouts. Pending and synced copies merge by session ID rather than appearing as two completed workouts.

The interface distinguishes a device-saved completion from a cloud-synced one. Telemetry does not block completion navigation. A remembered drain request prevents a second save from being stranded while the first sync is in flight. Invalid numeric inputs are rejected while the form is still editable, before creating an immutable pending record.

Account transitions invalidate the old generation before clearing storage, so interrupted physical cleanup cannot make old pending records eligible for replay. Late responses cannot transfer a workout to a new account. Failed server verification cannot grant backend entitlements or automatically sign out and erase pending work; existing store-purchase access rules remain unchanged. A revoked session requires explicit reauthentication. The account-deletion request is tied to its captured identity rather than whichever session exists later.

### Failure and recovery evidence

The actual modules pass **47 behavioral tests**, the full existing test suite and TypeScript checking. A separate PostgreSQL harness runs the real migrations under authenticated row-level security and forces transaction contention rather than merely launching two processes. Both the new recovery workflow and the unchanged measurement workflow passed in GitHub Actions on August 30, 2026.

| Failure or race | Verified behavior |
| --- | --- |
| Set write fails after header insertion | Entire completion rolls back; no empty completion remains |
| Same completion is retried or submitted concurrently | One persisted workout; identical retry replays safely |
| Two accounts compete for one set ID | One complete winner; the losing transaction rolls back; no set re-parenting |
| Restart before sync or after server commit but before local acknowledgement | Pending record resumes and converges without duplicate history |
| Another workout is saved during a stalled sync | The second completion receives a later drain automatically |
| Logout interrupts physical storage cleanup | Persisted generation invalidation prevents old work from replaying |
| Account A is deleted while B signs in | Captured A request remains bound to A; late cleanup does not sign out B or purge B's journal |
| Fractional repetitions or invalid negative values | Rejected before a saved acknowledgement, completion-entry write, or RPC |

The database deletion test also preserves a valid owner-B workout while removing owner A, and rejects later insertion for the deleted account. The [sanitized evidence summary](evidence/2026-08-30/aesthetics-workout-recovery.json) records the tested boundaries.

This work is isolated on a feature branch. The new migration has not been applied to production and the App Store binary has not been replaced. Its contract concerns acknowledged local storage operations and the application's tested recovery logic, not a guarantee against device power loss or an assertion that every app screen supports offline cold start. Pre-existing unscoped caches are not imported into another user's workout history. Legacy global-cache cleanup is not claimed to be atomically isolated across every app feature.

## Earlier upgrade: trustworthy measurement

The instrumentation's `d1_return` and `d7_return` events record crossed milestones: a first return on day 10 emits both markers with `day_offset: 10`. Counting those markers as exact-day returns would misstate the measurement.

I built a behavioral harness that executes the actual TypeScript initialization module with controlled clocks, storage, app metadata and transport. A separate audit reconciles its traces against a predeclared test roster and separately defined app-open schedule. Units with no return remain in the denominator; incomplete observation or delivery evidence withholds the metric.

The validator checks identity, timing, source version and event consistency. Missing, duplicate, late and conflicting events, immature windows and app-version mismatches all prevent metric calculation. Diagnostic results remain stable when packet rows are reordered.

## Falsification and verification

A predeclared four-unit fixture establishes the expected elapsed-day app-open rate:

| Controlled case | Expected result | Observed result |
| --- | --- | --- |
| Day 1 window | 1 of 4 units | 1 of 4 |
| Day 7 window | 2 of 4 units | 2 of 4 |
| Six injected evidence faults | Withhold the metric | Withheld in every case |

The measurement suite passes **37 tests**, TypeScript checking and focused lint. GitHub Actions passed on August 30, 2026. The [sanitized evidence summary](evidence/2026-08-30/aesthetics-measurement.json) records the controlled cases and scope; application source remains private.

The compiled instrumentation runtime is unchanged. This upgrade adds executable measurement contracts and failure diagnosis. Its results concern controlled tests only and establish no production retention, real-user cohort completeness or product impact. The linked product demo uses labeled illustrative examples.
