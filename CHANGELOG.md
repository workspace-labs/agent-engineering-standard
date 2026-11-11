# Changelog

## 1.6.0 — 2026-11-11

- Extend §92 with conditional Keycloak and LDAP guidance: explain when an identity provider
  or directory integration is earned, reuse the accepted provider, and keep ordinary sign-in small.
- Define OIDC and LDAP boundaries, secure client/token and directory configuration, approved
  write modes, account linking, access-removal delays and safe provider-outage behaviour.
- Require proportionate synthetic integration checks and settings/operator handover; distinguish
  mocked checks from verified federation. Route the addition from the entrypoint and README.
- Add behavioral exercise contracts for simple sign-in, existing LDAP with SSO, accepted
  providers and access removal; record executed verification separately in TEST-EVIDENCE.md.
- Prepare a local minor-version candidate; publication and installed-copy updates are separate steps.

## 1.5.1 — 2026-11-10

- Make README version pinning follow the newest published GitHub Release, with v1.5.0
  as an example, instead of the outdated local v1.0.0 candidate instructions.
- Shorten README package-check instructions and merge the details into the existing
  verification guide, preserving the checks, caveats and historical evidence links.
- Explain project coverage and the other technical overview bullets in plain words,
  keeping their meaning, rule IDs and bullet count.
- Teach §105 edge cases and §106 overload in two more beginner mistakes, with glossary
  entries and distinct too-big, too-fast and server-full responses.
- Show the walkthrough agent writing selection rules and deferring shared-booking
  cases until that service is planned, without expanding the practice-page scope.
- Mark the standard 1.5.1 and record local verification; wording and docs only, with
  no rule changes. Keep the existing 1.5.0 hero image for this patch.
- Fix round 1 after independent review (C1–C3): remove local tool paths from public
  evidence, have the walkthrough agent raise the same-time case without being asked,
  and distinguish oversized uploads from temporary overload in the README.

## 1.5.0 — 2026-11-10

- Add §105 Business rules and edge cases to the architecture guide: write each product
  rule in a plain sentence, walk the cases a request never mentions (nothing, the limit,
  twice, out of order, the wrong person, halfway), ask the owner about the ones that
  change money, access, kept data or a promise, and give each rule and kept case a test.
- Add §106 Overload and traffic spikes to the backend guide: bound everything that can
  grow, refuse cheaply and honestly at the bound, never drop accepted work, retry with
  backoff, let the owner decide what fails last, and measure the limit before a known
  peak; scaling follows the measurement.
- **Removed:** the game example tree (`references/trees/game.md`) and its chooser row.
  The standard serves products such as websites, apps, servers and services; a game
  still follows the layout map's due-at rule and its engine's own layout (§61). No rule
  is removed or changed, so this stays a minor version.
- Route both rules from the entrypoint and the reference table; extend the rule-ID and
  heading checks through §106; two behavioral scenarios added to
  tests/behavioral-cases.md.
- Re-render the README hero image for 106 rules and ten trees, without the 1.4.0 badge.
- Fix round 1 after independent review (R1, R4), in §106: an input over a size limit is
  refused as too big (413 over HTTP, no retry hint), apart from a rate limit (429) and a
  server that is full for now (503); and a slow request is a bottleneck to fix first,
  becoming a job only when §93's own trigger is met. The "Launch day" scenario follows.

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
