# 0001 — Record the existing instruction-package layout

Status: existing convention documented; no replacement architecture proposed.
Recorded: 2026-10-19. The original adoption date is not asserted.

## Context

The repository already ships one Agent Skill under skills/software-engineering-build-standard/.
Tests and CI read that folder directly, and install commands copy it as one self-contained package.

## Decision recorded

Keep instructions in the skill package, tests at the repository root and contributor documentation
outside the installed folder. An empty application src/ would own no code and would confuse the
actual source boundary. This is a record of the existing layout, not a new owner approval or migration.

## Consequences

New bundled guidance stays inside the package and is linked by its router. New checks remain under
tests/. Framework source-root examples in the standard do not require this documentation product to
pretend it is an executable application.
