# Yusef Syed

**University of Toronto student intending to pursue a double major in Mathematics and Computer Science, building AI evaluation systems and reliable software products.**

I work across Python evaluation infrastructure, TypeScript/React Native products, and backend reliability. I care about reproducible evidence, failure modes, and honest limits—not just demo paths.

[Product portfolio](https://yusef-product-demos.yoosefseed.chatgpt.site) · [Résumé (PDF)](resume/Yusef_Syed_Resume.pdf) · [Email](mailto:yusefmsyed@gmail.com)

## Internship availability

| Term | Availability |
| --- | --- |
| **Summer 2027** | Available full-time from May through August for software engineering, AI product, evaluation/reliability, backend/platform, or mobile roles |
| **Fall / Winter** | Open to selective AI/software internships that are compatible with University of Toronto coursework |
| **Location** | Canada or the United States; open to relocation and remote work |
| **Work authorization** | U.S.–Canadian dual citizen; no sponsorship required in either country |

Expected graduation: **May 2030**.

## Selected work

### [Agent Eval Mutation Lab](https://github.com/YusefSyed/agent-eval-mutation-lab) · Python, Inspect, Docker, SQLite

A typed, deterministic engine for testing execution-semantic robustness in tool-agent scorers. It runs 104 canonical tasks with resumable SQLite state, content-addressed evidence, explicit unknown/abstain handling, and clean-checkout artifact reproduction. Its public reports retain failed model-study gates and unfavorable outcomes instead of promoting unsupported conclusions.

### Shipped products

| Project | What I built | Evidence |
| --- | --- | --- |
| **Aesthetics AI** | Released iOS fitness product using React Native, Expo, Supabase/Postgres, structured model outputs, and RevenueCat. Documented reliability work covers persist-before-sync workout completion, atomic writes, restart recovery, and account isolation. | [App Store](https://apps.apple.com/us/app/aesthetics-ai-physique-coach/id6773502055) · [Case study](case-studies/AESTHETICS_AI.md) |
| **Tiraz** | Released privacy-first iOS wardrobe app plus a public PyTorch garment-completion study. Three seeded models reached 58.5–59.0% held-out top-1 accuracy versus a 52.7% co-occurrence baseline; the missing-context coverage failure remains visible. | [App Store](https://apps.apple.com/us/app/tiraz/id6789730283) · [ML study](https://github.com/YusefSyed/tiraz-garment-completion) · [Case study](case-studies/TIRAZ.md) |
| **CallReclaim** | Private missed-call recovery MVP with consent-aware SMS, validated AI lead extraction, signed provider webhooks, owner-scoped data, and PostgreSQL reconciliation for uncertain send outcomes. No production traffic or revenue is claimed. | [Sample-data demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim) · [Case study](case-studies/CALLRECLAIM.md) |

### Developer tools and open source

- **[Agent Proof](https://github.com/YusefSyed/agent-proof):** TypeScript CLI that runs reviewer-selected checks without shell interpolation and writes redacted JSON/Markdown verification reports.
- **Microsoft Agent Lightning:** merged fixes for [shutdown rollout races](https://github.com/microsoft/agent-lightning/pull/580) and [local-worker agent URL handling](https://github.com/microsoft/agent-lightning/pull/582).
- **Meridian Labs Inspect Scout:** merged [per-item model-usage accounting fix](https://github.com/meridianlabs-ai/inspect_scout/pull/586) with regression coverage.

## Technical toolkit

- **Languages:** Python, TypeScript, JavaScript, SQL
- **AI and evaluation:** PyTorch, NumPy, Inspect, structured LLM APIs, deterministic evaluation pipelines
- **Web and mobile:** React, React Native, Expo, Next.js, Node.js
- **Data and reliability:** PostgreSQL, Supabase, SQLite, Docker, pytest, mypy, GitHub Actions
- **Product integrations:** Twilio Voice/SMS, RevenueCat, Vercel

## How I build

- Turn ambiguous product requirements into tested systems with explicit failure behavior.
- Treat dependencies, logs, provider callbacks, and external inputs as untrusted evidence.
- Separate local or synthetic verification from production, user, revenue, and impact claims.

If you are hiring for a Summer 2027 or selective Fall/Winter AI/software internship, [email me](mailto:yusefmsyed@gmail.com).
