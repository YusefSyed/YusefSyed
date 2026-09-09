# Yusef Syed

**First-year University of Toronto student, intending Mathematics and Computer Science, focused on AI-safety evaluation and reliable research software.**

I build Python evaluation tools and software products with AI-assisted implementation. My interests are evaluation validity, oversight of tool-using agents, and reproducible experiments with explicit limits.

[Research evidence](RESEARCH_EVIDENCE.md) · [Product portfolio](https://yusef-product-demos.yoosefseed.chatgpt.site) · [Résumé (PDF)](resume/Yusef_Syed_Resume.pdf) · [Email](mailto:yusefmsyed@gmail.com)

## Research and internship availability

| Term | Availability |
| --- | --- |
| **Summer 2027** | Available full-time from May through August for software engineering, AI product, evaluation/reliability, backend/platform, or mobile roles |
| **Fall / Winter** | Seeking supervised research or selective AI/software work compatible with University of Toronto coursework |
| **Location** | Canada or the United States; open to relocation and remote work |
| **Work authorization** | U.S.–Canadian dual citizen; no sponsorship required in either country |

Expected graduation: **May 2030**.

## Selected work

### [Agent Eval Mutation Lab](https://github.com/YusefSyed/agent-eval-mutation-lab) · Python, Inspect, Docker, SQLite

A typed, deterministic engine for testing execution-semantic robustness in tool-agent scorers. It runs 104 canonical tasks with resumable SQLite state, content-addressed evidence, explicit unknown/abstain handling, and clean-checkout artifact reproduction. Its public reports retain failed model-study gates and unfavorable outcomes instead of promoting unsupported conclusions.

### [Tiraz garment-completion experiment](https://github.com/YusefSyed/tiraz-garment-completion)

Three seeded annotation-only models achieved 58.5-59.0% top-1 against a 52.7% baseline on 962 held-out groups; a context-removal audit exposed coverage degradation. [Methods and limits](RESEARCH_EVIDENCE.md).

### [ShiftProof](https://github.com/YusefSyed/shiftproof)

Local scheduling prototype with independent constraint checks and coordinator-only apply, approve and export actions. Validation uses synthetic data.

### Product engineering

| Project | What I built | Evidence |
| --- | --- | --- |
| **Aesthetics AI** | Released iOS fitness product using React Native, Expo, Supabase/Postgres, structured model outputs, and RevenueCat. Documented reliability work covers persist-before-sync workout completion, atomic writes, restart recovery, and account isolation. | [App Store](https://apps.apple.com/us/app/aesthetics-ai-physique-coach/id6773502055) · [Case study](case-studies/AESTHETICS_AI.md) |
| **Tiraz** | Released privacy-first iOS wardrobe app plus a public PyTorch garment-completion study. Three seeded models reached 58.5–59.0% held-out top-1 accuracy versus a 52.7% co-occurrence baseline; the missing-context coverage failure remains visible. | [App Store](https://apps.apple.com/us/app/tiraz/id6789730283) · [ML study](https://github.com/YusefSyed/tiraz-garment-completion) · [Case study](case-studies/TIRAZ.md) |
| **CallReclaim** | Private missed-call recovery MVP with consent-aware SMS, validated AI lead extraction, signed provider webhooks, owner-scoped data, and PostgreSQL reconciliation for uncertain send outcomes. No production traffic or revenue is claimed. | [Sample-data demo](https://yusef-product-demos.yoosefseed.chatgpt.site/#callreclaim) · [Case study](case-studies/CALLRECLAIM.md) |

### Developer tools and open source

**9 external upstream PRs verified merged on September 8, 2026.** [Evidence](RESEARCH_EVIDENCE.md#external-open-source). The [open PyTorch CPU/CUDA contribution](https://github.com/pytorch/pytorch/pull/196390) is separate; its [3,486-output local validation supplement](case-studies/pytorch-igamma-shape-gradients/README.md) is publicly inspectable.

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

If you are considering supervised Fall/Winter research or a Summer 2027 research/AI/software role, [email me](mailto:yusefmsyed@gmail.com).
