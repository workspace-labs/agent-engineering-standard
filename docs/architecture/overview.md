# Package architecture

This repository distributes instructions. It has no application process, database, server or runtime
provider. The existing source location is retained, rather than adding an unused application src/.

```text
README.md                         usage and installation
AGENTS.md                         contributor instructions
CHANGELOG.md                      dated changes
TEST-EVIDENCE.md                   observed verification and limits
skills/README.md                  package catalog
skills/software-engineering-build-standard/
  SKILL.md                        entrypoint and reference router
  agents/openai.yaml              optional Codex display metadata
  references/                     focused guidance
    trees/                        chooser and staged examples
tests/                           offline package checks and behavior exercise contracts
docs/                            repository scope, boundaries, decisions and operations
.github/workflows/                cross-platform package validation
```

Exact paths and checks are described in
[boundaries](boundaries.md). [The recorded layout](../adr/0001-instruction-package-layout.md) preserves
this package's existing convention; it does not propose a code migration.
