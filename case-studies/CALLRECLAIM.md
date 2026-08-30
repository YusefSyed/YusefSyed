# CallReclaim

CallReclaim is a missed-call recovery MVP connecting signed telephony webhooks, consent-aware messaging, validated lead extraction and a Next.js owner dashboard. Its backend uses Supabase/Postgres, with provider configuration and consent gates around live sending.

[![CallReclaim product demo poster](../assets/callreclaim.png)](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

[Watch the sample-data demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

## Engineering upgrade: reproducible reconciliation failures

Provider callbacks can arrive twice, out of order, or before the application has persisted the matching message. I built an offline replay tool that checks those sequences against the actual Twilio JavaScript correlation function and Telnyx PostgreSQL reconciliation functions, executing the committed SQL in PGlite.

Seeded symbolic schedules exercise duplicates, late arrivals, conflicting identities and ambiguous outcomes. A separate finite reference contract checks every event prefix: finalized delivery evidence cannot regress to `sent`; conflicts and stale callbacks cannot change message or reservation rows; missing evidence remains unknown. The tool never issues or retries a provider send.

When a contract fails, deletion minimization removes irrelevant events while preserving the same invariant failure. A completed result is **1-minimal**: no single remaining event can be removed without losing that failure. Exhausting the check budget produces an explicit incomplete result.

## A failure small enough to inspect

Removing the finalized-rank guard from a test-only, in-memory copy of the SQL produces this counterexample:

| Arrival | Evidence |
| --- | --- |
| 1 | `delivered`, provider time 1 |
| 2 | `sent`, provider time 7 |

The altered function incorrectly selects `sent`; unchanged production SQL preserves `delivered`. The tool reduced seven events to these two in 18 checks, and removing either event eliminates the failure. See the [symbolic counterexample and verification summary](evidence/2026-08-30/callreclaim-replay.json).

Two runs of a 256-sequence campaign produced byte-identical reports across 3,708 synthetic arrivals. The replay suite, existing reconciliation/outbox checks, TypeScript check and focused lint passed. GitHub Actions passed on August 30, 2026.

Application source remains private. This work adds debugging and regression detection without changing production behavior. Evidence covers sequential local replay; it does not establish distributed concurrency safety, live provider behavior, exactly-once delivery or customer outcomes. The audit does not determine current carrier-launch readiness.
