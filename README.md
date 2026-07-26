# Yusef Syed

### AI-native product engineer · mobile, web and applied AI

Toronto / San Francisco / Remote · US and Canadian citizen · Incoming University of Toronto student

I turn ambiguous product problems into tested TypeScript systems. My strongest work spans React and Next.js, React Native and Expo, Supabase and Postgres, OpenAI APIs, Twilio Voice/SMS, subscriptions, privacy controls and release verification.

I use coding agents heavily, but I stay responsible for the engineering result: architecture, data boundaries, failure modes, security, tests and evidence that the product actually works.

## Featured work

### [Agent Proof](https://github.com/YusefSyed/agent-proof) — public verification tool

A TypeScript CLI for running an approved verification plan and producing reviewable JSON and Markdown evidence. It uses `execFile` with `shell: false`, exact command allowlists, timeouts, output redaction and truncation. Five automated tests cover success, failure, timeout, disallowed commands and secret-safe output.

### [CallReclaim](case-studies/CALLRECLAIM.md) — missed-call recovery

A Next.js and Supabase MVP that connects Twilio Voice/SMS with consent-aware reply handling and OpenAI structured outputs. The production build compiles 32 pages and includes 25 route handlers and 8 SQL migrations. It defaults to demo/fail-closed behavior while live messaging prerequisites are incomplete.

### [Tiraz](case-studies/TIRAZ.md) — privacy-first wardrobe coach

An Expo/React Native application backed by Supabase and 19 Deno Edge Functions. The repository contains 110 top-level test files plus automated type, privacy, security and release-readiness checks. Current status: private product and launch preparation, not a public App Store release.

### [Aesthetics AI](case-studies/AESTHETICS-AI.md) — structured mobile coaching

An Expo/React Native product with Supabase, 8 Edge Functions, schema-validated OpenAI outputs and subscription infrastructure. A native build candidate and QA evidence package were prepared; it is not presented as a public launch.

## How I work with coding agents

1. Define the user outcome and the claims that must be proven.
2. Inspect the existing system and constrain the change.
3. Review generated code as untrusted input.
4. Test the happy path and the expensive negative cases.
5. Record reproducible evidence and state what remains unverified.

## Current focus

I am beginning Physical & Mathematical Sciences at the University of Toronto in September 2026. I am seeking AI product engineering, full-stack startup, forward-deployed, agent reliability/evaluation or mobile AI internships.

Available for flexible remote work during the academic year and full-time Summer 2027. Open to a structured off-cycle term or San Francisco relocation for an exceptional role.

## Stack

`TypeScript` `JavaScript` `SQL` `React` `Next.js` `React Native` `Expo` `Supabase` `PostgreSQL` `Deno` `OpenAI API` `Twilio` `RevenueCat` `GitHub Actions`

[Email](mailto:yusefmsyed@gmail.com)
