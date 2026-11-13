# Yusef Syed

Software engineer working on AI agent security and evals. Looking to join a startup team from January 2027, as a paid intern or full-time, anywhere in the U.S. (happy to relocate, or remote), as a security engineer, evals engineer, AI red team engineer or AI safety research engineer. Also interested in RL environment and agent infrastructure roles. U.S. and Canadian citizen, no sponsorship needed.

**[Résumé (PDF)](resume/Yusef_Syed_Resume.pdf)** · [Email](mailto:yusefmsyed@gmail.com) · [LinkedIn](https://www.linkedin.com/in/yusef-syed-4b811a289/)

## Merged upstream

21 merged PRs: [20 in this search](https://github.com/search?q=author%3AYusefSyed+is%3Apr+is%3Amerged+-user%3AYusefSyed+-repo%3Ahni-z%2FProvidence+NOT+ScopeHaven+in%3Atitle&type=pullrequests), plus Google ADK, which Google merged through its internal import (so GitHub lists that PR as closed). AI-assisted under my direction; each was merged by that project's maintainers.

- **[Google ADK](https://github.com/google/adk-python/pull/8074)** (Agent Development Kit): fixed an eval that scored a matching no-argument tool call as a miss.
- **[Hugging Face transformers](https://github.com/huggingface/transformers/pull/50606)**: fixed tool-schema generation (`get_json_schema`) cutting multi-line argument descriptions short, with tests.
- **[A2A Python SDK](https://github.com/a2aproject/a2a-python/pull/1442)** (Agent2Agent protocol): made the v0.3 REST compatibility layer serve DELETE for push-notification configs.
- **[Microsoft PyRIT](https://github.com/microsoft/PyRIT/pull/2537)** (AI red teaming): extended the package-hallucination scenario to Dart, Perl and Raku, with tests.
- **[Microsoft Agent Lightning](https://github.com/microsoft/agent-lightning/pull/584)** (agent training, reinforcement learning): landed four reliability fixes, e.g. case-insensitive auth-header replacement.
- **[W&B RAI Toolkit](https://github.com/wandb/rai-toolkit/pull/106)**: landed five evaluation fixes, including keeping a failed prediction's error text from scoring as a pass.
- **[Apache Arrow](https://github.com/apache/arrow/pull/51160)**: extended four PyArrow slice APIs to accept Arrow integer scalars, with regression tests.
- **[Inspect Scout](https://github.com/meridianlabs-ai/inspect_scout/pull/586)**, **[Kornia](https://github.com/kornia/kornia/pull/4185)** and **[Sentience Governor](https://github.com/crescerelabs/sentience-governor/pull/28)**: seven more fixes.

## Papers

- **[ToolEffectBench: Scoring Prompt Injection on Tool-Using Agents from Persisted State](https://doi.org/10.5281/zenodo.23966727)**. Sole author, Zenodo, 2026. doi:10.5281/zenodo.23966727. Code, logs and paper: [tool-effect-bench](https://github.com/YusefSyed/tool-effect-bench).
- **[Checks for Checkers: Sealed Paired Comparisons of AI Agent Verification Tools](https://doi.org/10.5281/zenodo.23966747)**. Sole author, Zenodo, 2026. doi:10.5281/zenodo.23966747. A sealed, blind comparison of my startup's tool and an open-source framework: no lead (83 vs 88 of 96, p = 0.30).

## Projects

I build with AI coding agents that I direct and review.

- **[ToolEffectBench](https://github.com/YusefSyed/tool-effect-bench)** (Python, Inspect, Docker): an Inspect benchmark scoring prompt injection from a sandbox's database state, not transcripts (188 samples, 17 models, 5,628 scored runs). On one synthetic task, agents' final reports denied at least 13 of 232 recorded forbidden publications.
- **[effect-tracer](https://github.com/YusefSyed/effect-tracer)** (Rust, Linux ptrace/seccomp, Ed25519): a tracer that signs a process tree's file writes, connects, DNS and execs into a hash chain. 19 of 20 seeded bypasses caught at 1.1-1.9x overhead in seccomp mode (20 of 20 at 5-298x in full mode).
- **[Scopehaven open edition](https://github.com/YusefSyed/scopehaven-oss)** (Node.js, Apache-2.0; solo project): a CLI and GitHub Action that tests whether an AI agent touched the wrong account, tenant or refund, decided from the app's own records rather than the agent's report.
- **[Agent Eval Mutation Lab](https://github.com/YusefSyed/agent-eval-mutation-lab)** (Python): a 624-trial study across two local models on a version-controlled protocol. Five of six validity gates failed, so I withheld improvement claims.

## Security research

Filed 22 private security advisories and 2 HackerOne reports (authorization, code-execution, credential and data-exposure flaws) with 15 open-source projects, each reproduced 3 of 3 by an automated harness; three triaged, others awaiting triage, as of November 13, 2026.

## Also

[Providence](https://devpost.com/software/providence-tn6m4h) (Swift): 1st Place, Aramco Americas Challenge (Best Beginner Hack), Hack the North. [Evidence and more detail](RESEARCH_EVIDENCE.md).

First year at the University of Toronto, intended Math + CS.
