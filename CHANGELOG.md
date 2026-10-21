# Changelog

## Unreleased — 2026-10-21

- Clarify that required design approval precedes implementation, while reuse of an accepted
  stack and an earlier approval of the same design do not require duplicate permission.
- Reject nonportable absolute local Markdown paths and linked resources reached through
  skipped metadata directories; add regression coverage for the checker.
- Record this repair's test counts, fail-first controls and behavioral limits in
  [test-evedince.md](test-evedince.md), preserving earlier test evidence.

## Unreleased — 2026-10-19

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
