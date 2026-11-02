# Changelog

## 1.1.1 — 2026-11-02

- Rewrite the eleven beginner behavioral requests in a beginner's own words without hints,
  so the agent must recognize the engineering decisions the request requires.
- Add the "Where should I add the API key?" behavioral case for an existing browser-side call.
- Allow baseline runs without the skill, recording their results separately from skill runs.

## 1.1.0 — 2026-11-02

- Add §74–§83 for test levels and flaky tests, CI gates, branches and pull requests,
  ADR format/lifecycle, releases, environments and feature flags, privacy, dependency
  health, incidents and code ownership, with explicit due-at triggers and workflow precedence.
- Route the team/lifecycle guide from SKILL.md, declare standard version 1.1.0 and extend
  stable rule IDs to §1–§83 without changing existing rule meanings or numbering.
- Align the layout map and tree chooser with ADR indexes, privacy inventories, code
  ownership and PR templates; connect CI to the project's documented local commands.
- Extend heading/citation checks for §74–§83 while retaining §66–§72 and version agreement;
  add five Request/Observe behavioral contracts for team changes and lifecycle decisions.
- Document eight main guides and the expanded scope; record baseline, final package
  checks, fail-first controls and unexecuted behavioral limits while preserving earlier history.

## 1.0.0 — 2026-11-02

- Extend §69 to project keys in shipped mobile, desktop and CLI apps, with a user-supplied
  runtime-key exception and matching tree guidance and Android exercise contract.
- Add backend rules §66–§70 for API contracts and errors, pagination, reliability and
  operations, security, secret/API-key handling and containers, each with explicit due triggers.
- Add frontend rules §71–§72 for data ownership and view states, forms, accessibility,
  security, measured performance and languages, including Arabic and right-to-left layouts.
- Route both guides from SKILL.md, declare standard version 1.0.0 and fill the stable
  rule-ID range §1–§73 without renumbering existing rules.
- Align the layout map and API, webapp and AI-service trees with secret configuration,
  backend proxies and conditional Dockerfile, ignore-file and Compose responsibilities.
- Extend allowed rule IDs and add a package test for exactly one heading per new rule and
  the entrypoint/changelog version match; add five behavioral exercise contracts.
- Document semantic versions, future tag pinning, seven main reference guides and the
  expanded scope. Preserve earlier changelog entries under dated Before 1.0.0 headings.
- Consolidate the October 21 evidence verbatim into TEST-EVIDENCE.md, remove the duplicate
  evidence file and update its links; record this run's baseline, final count and limits.
- Prepare the owner-approved 1.0.0 candidate on a local release branch; no push, tag,
  GitHub Release or installation is part of this change.

## Before 1.0.0 — 2026-10-21

- Clarify that required design approval precedes implementation, while reuse of an accepted
  stack and an earlier approval of the same design do not require duplicate permission.
- Reject nonportable absolute local Markdown paths and linked resources reached through
  skipped metadata directories; add regression coverage for the checker.
- Record this repair's test counts, fail-first controls and behavioral limits in
  [TEST-EVIDENCE.md](TEST-EVIDENCE.md), preserving earlier test evidence.

## Before 1.0.0 — 2026-10-19

Deep audit and repair work is recorded here. This starts an explicit change history; it does not invent
version numbers or release dates for earlier commits. See Git history for previous changes.

- Align tree-example triggers for security, licensing, contribution documentation, substantive CLI logic,
  mobile end-to-end tests and operations documentation with the shared layout map.
- Add a staged game guide and chooser route, preserving engine conventions and conditional responsibilities.
- Add the repository's missing contributor instructions, scope, package catalog, architecture and verification
  notes. Record why the instruction package uses skills/ rather than an empty application src/ directory.
- Extend package checks with invalid-fragment and filesystem-node controls; record actual automated and
  behavioral verification in TEST-EVIDENCE.md.
- Record 33 passing checks on each of Windows, macOS and Linux, including native Windows junction fixtures.
