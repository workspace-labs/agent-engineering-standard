# Changelog

## 1.4.0 — 2026-11-09

- Add the platform services guide, §91–§104: HTTPS, domains and certificates; sessions and
  multi-tenancy; background jobs, queues and scheduled tasks; realtime connections; files,
  uploads and object storage; email and notifications; payments and billing; webhooks and
  integrations; search; audit log; caching, CDN and running more than one copy;
  infrastructure as code; public pages and SEO; product analytics and error tracking. Each
  rule applies only at its due-at trigger, and the stack's existing mechanism comes before
  a new service.
- Add the homes these services earn to the layout map (`jobs/`, `realtime/`,
  `infrastructure/storage/`, `email/`, `payments/`, `search/`, `api/webhooks/`, `audit/`,
  `locales/`, `apps/worker/`, root `infra/`), to the API backend and monorepo example trees
  and to the mature-project table; `docs/deployment/` now also records domain, DNS and
  certificate ownership.
- Route the guide from the entrypoint's always-on rules and reference table; extend the
  rule-ID and heading checks through §104.
- Fix round 1 after independent review (F01–F05): webhooks read bounded raw bytes, verify
  the provider's way, record durably, then acknowledge; localization is earned by the
  second language while a right-to-left first language earns the §72 layout checks;
  the payments home also covers tracked subscriptions; one mapped sender home for email
  or notifications; basic search guidance applies at the first search and the separate
  engine only on measurement; sitemap and robots are proportional. Four behavioral
  scenarios added to tests/behavioral-cases.md.
- Fix round 2 (F06): the hero image's due labels name each guide's real trigger — the
  lifecycle guide applies rule by rule, to solo projects too, not from a second person;
  platform services at each service's first use; data at the first stored row, contract or
  failure; backend at the first endpoint or outside call.
- Replace the README hero image with the whole-map picture (`media/the-whole-map.png`):
  the entrypoint, the ten guides with their rule ranges and due moments, the eleven trees
  and the three promises. The previous board-specific picture is removed.

## 1.3.0 — 2026-11-05

- Add triggered project coverage and evidence rules §87–§90, reusing approved PRD/TRD/Plan decisions and their human checks instead of parallel planning.
- Require proportionate threat assessment, meaningful failure evidence, engine-aware recovery, and conditional distribution/assurance verification.
- Distinguish repeatable builds from byte-identical claims and verify actual published artifacts and workflow controls. Tiny changes retain the narrow workflow.
- Add routing/integrity protection and isolated agent exercise contracts; observed results are recorded separately in TEST-EVIDENCE.md.
- Record owner acceptance, verified installation across six logical skill paths, and installed-copy checks; remove one extra EOF blank line found during staging without changing instruction meaning.

## 1.2.1 — 2026-11-02

- Route configuration changes explicitly to §85 from the entrypoint and completion
  checklist after an executed email exercise omitted setting purposes and value sources.
  Clarify that names and defaults alone do not satisfy the existing handover rule.
- Reject incorrect filename or directory capitalization in local Markdown links on
  case-insensitive filesystems, so Windows checks catch links that would break on Linux.
  Add a fail-first regression with a correctly spelled positive control.
- Clarify the Windows command fallback when `py` exists but cannot find Python, and
  record native PowerShell package, installation and behavioral verification.

## 1.2.0 — 2026-11-02

- Add §84, Teach while building: explain project structure and important decisions in plain
  words when needed, keep unsafe requests safe, and keep tiny tasks free of lessons.
- Add §85, The ten-year handover, with triggered README sections and same-change settings
  documentation; add §86, Taking over a project, to map actual code without guessing secrets
  or history or rebuilding an unfamiliar tree.
- Add a new developer guide and an illustrative first-project conversation, grounded in the
  existing layout map and webapp tree, and link the guide from README.md.
- Extend rule-ID and heading checks through §86; add first-project, tiny-typo, takeover and
  new-settings behavioral contracts and record fail-first package proof separately from
  unexecuted exercises. Update the layout map's README description without adding starter pieces.

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
