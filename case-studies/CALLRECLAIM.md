# CallReclaim

CallReclaim is a missed-call recovery MVP connecting signed telephony webhooks, consent-aware messaging, validated lead extraction and a Next.js owner dashboard. Its backend uses Supabase/Postgres, with provider configuration and consent gates around live sending.

[![CallReclaim product demo poster](../assets/callreclaim.png)](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

[Watch the sample-data demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim)

## Engineering upgrade: recover uncertain SMS outcomes

An SMS provider can accept a message while the application's response is lost. A retry can text the customer twice; treating the timeout as a delivery failure invents information the application does not have.

I implemented an authenticated callback path tied to the original send reservation. The application persists the attempt and a hashed random callback token before its single provider request. Signed callbacks enter the existing durable outbox; one PostgreSQL transaction reconciles the message and reservation. The synchronous API response uses that same transaction, so a late `queued` response cannot downgrade an already received `delivered` receipt.

The implementation separates provider acceptance from delivery. Conflicting delivered/failure receipts remain explicitly uncertain. Missing evidence never triggers an automatic resend. The owner dashboard uses the explicitly linked message receipt, and delivery failure does not accidentally clear the existing conversation debounce.

### Crash and concurrency checks

The actual modules and migration run against synthetic fixtures with a fake provider transport. Separate local PostgreSQL transactions verify:

| Experiment | Observed result |
| --- | --- |
| Callback arrives before the send response | Delivery retained; one fake provider request |
| Eight concurrent duplicate receipts | One update, seven stale results |
| Two businesses compete for one provider message ID | One binding; conflicting attempt rejected |
| Delivered and failure receipts arrive concurrently | Explicit, stable delivery conflict |
| Eight signed callbacks and three workers | One durable processed event |
| Worker killed after database commit, before queue acknowledgement | Lease recovered; reconciled rows unchanged; stale acknowledgement rejected |
| Direct mutation calls from client roles | Anonymous and authenticated roles denied |

The feature also passes 24 behavioral tests, existing regression suites, lint, TypeScript checking, and the production build. GitHub Actions passed on the feature commit on August 30, 2026.

The [sanitized PostgreSQL results](evidence/2026-08-30/callreclaim-sms-recovery.json) distinguish these local experiments from production evidence. The implementation is on an isolated feature branch: its migration has not been applied to production, and automatic web deployment is disabled for that branch. Application source remains private.

This does not establish exactly-once carrier delivery, customer conversion, or production reliability. If every callback is lost, the attempt can remain unresolved. Historical messages without the new identity are not backfilled; a call without an explicit message link retains its warning.

## Earlier upgrade: reproducible reconciliation failures

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

The earlier replay tool adds debugging and regression detection without changing the functions it evaluates. Its evidence covers sequential local replay; the separate SMS recovery experiments above add finite transaction and process-failure checks. Neither establishes live provider behavior, exactly-once delivery or customer outcomes. The audit does not determine current carrier-launch readiness.
