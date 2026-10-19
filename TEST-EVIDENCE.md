# Test evidence

## Deep audit and repair — 19 October 2026

**Automated result: PASS — 33/33 checks on Windows, macOS and Linux (99 CI test executions),
plus local checks and native macOS installation/refusal tests.** Eleven isolated behavioral
scenarios were evaluated, with replay and self-review limits recorded below.

### Current cross-platform CI

Tested repair: [`4ce941ffc78a4fb3589bcfcf42f0012df5f0a382`](https://github.com/workspace-labs/agent-engineering-standard/commit/4ce941ffc78a4fb3589bcfcf42f0012df5f0a382).
[Run 39182011334](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/39182011334)
completed successfully on 19 October 2026, 00:42:57–00:43:12 UTC. All three jobs reported
33 tests and OK, without failures, errors or skips. This evidence entry was added afterward;
the instruction bundle and test source are unchanged by the evidence update.

| Platform | Environment from job logs | Python | Observed result | Evidence |
|---|---|---|---|---|
| Linux | Ubuntu 24.04.5 LTS | 3.12.15 | 33/33; 0.080s | [Linux job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/39182011334/job/117836572402) |
| Windows | Windows Server 2025, 10.0.26100 | 3.12.10 | 33/33; 0.267s | [Windows job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/39182011334/job/117836572663) |
| macOS | macOS 26.6.2, ARM64 | 3.12.10 | 33/33; 0.053s | [macOS job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/39182011334/job/117836572692) |

The native Windows junction fixtures executed successfully in the Windows job, including
linked-entrypoint refusal and external-target preservation. Native FIFO read-order probes were
also independently checked on the local Mac. The historical manual Windows installation
procedure below was not repeated; it remains evidence for its October 8 revision only.

The repair started from [`24f35d88cf085b3de7fe3867a4e06fcbbd0383db`](https://github.com/workspace-labs/agent-engineering-standard/commit/24f35d88cf085b3de7fe3867a4e06fcbbd0383db).
The checked candidate has 19 skill files and eleven staged project-type guides. Its static
auditor bundle digest is `1c7b81ed9c3d3dcb80c22ab10724deb02ec4c86fe7ff33b466a9d70d72455237`.
This identifies the installable instructions independently of subsequent evidence-only edits.

### Findings repaired

- Aligned website, CLI and library licensing/contribution triggers with the shared layout map.
- Aligned the webapp, API, desktop, mobile, AI-service and pipeline security-document triggers
  with the shared stored-data, sign-in, network-call or secret rule.
- Corrected operations captions that deferred instructions until a signed build, deployment,
  incident, scheduled run or multiple-app release; operations are documented when first needed.
- Made mobile end-to-end tests due with the first complete flow, including simulator flows;
  physical-device checks follow the actual interaction/performance requirement.
- Allowed substantial logic in a single CLI command to earn a separate owner.
- Added a staged game guide and chooser route, with engine-layout precedence, authored/generated
  asset ownership and conditional save, testing and release responsibilities.
- Added the repository's missing contributor instructions, package catalog, scope, architecture,
  boundary record, verification procedure and findings/limits documentation. No unused application
  source tree or dependency manifest was added to this instruction package.
- Repaired validator gaps for local heading fragments, directory READMEs, links outside the root
  README, nonportable local URLs, special nodes, symlinks and Windows reparse points. The resource
  inventory now checks node metadata before descent, and every package test guards reads with it.

### Automated checks and fault controls

The original 10 checks passed before repair. The repaired suite adds 23 adversarial fixture
checks, for **33/33 passing tests**, with no failures, errors or skips on local Python 3.9.6/macOS.
The same 33 checks passed against a disposable installed copy using `ENGINEERING_SKILL_ROOT`.
Run from the repository root:

```text
python3 -B -m unittest discover -s tests -v
```

Fail-first runs reproduced eight link/resource failures, then a missed local-file URL, then
three traversal/read-order failures before their corrections. Independent review then exposed
a repository link reaching a later unsafe node before lazy inventory completed; a further fail-first
round reproduced two read-order failures. The repair inventories the repository before link reads
and checks source/target regular-file metadata, including fragment targets in skipped Git metadata.
Fixtures cover missing paths and fragments, directory READMEs, encoded paths, Unicode/duplicate
headings, code examples, boundary
escapes, repository docs beyond README, Windows junction metadata, special nodes and linked
external children. Native macOS directory links were refused; read/enumeration traps confirmed
refusal before following unsafe children. The Windows-specific native junction branch also
passed in the current Windows CI job; simulated metadata checks provide separate portable controls.

The available Codex skill validator reported `Skill is valid!`. The read-only skill audit found
zero structural errors and twelve `deep-reference` review warnings. All twelve refer to the
intentional chooser plus guides under `references/trees/`; their discovery links and reachability
were reviewed. They are retained as layout observations, rather than hidden or reported as a
warning-free audit. Safety, portability, triggers, Claude and Codex profiles passed static checks.

### Fresh-context behavioral exercises

Each row used a separate agent context, an explicit frozen copy of the candidate skill, the raw
request and a disposable synthetic project. Executing agents did not receive the evaluator's
expected outcomes. The evaluator then inspected files, command results and before/after hashes,
and independently reran generated suites and direct controls where applicable.

The initial eleven contexts used bundle digest
`c37d3cfba573ccee26a687c7fd413c5c54ef2699d0f5ddae433ec908fc6802ee`.
After the final operations/security-caption changes in six guides, the CSV and two-deployable
scenarios were replayed in two new contexts against the final digest above, for thirteen fresh
contexts in total. Earlier artifacts were retained. The final planning replay initially delayed
several documentation/tooling triggers; one explicitly requested self-review corrected these,
including operations at the first build. This is evidence for a reviewed workflow, not reliable
first-pass compliance.

| Scenario | Observed outcome |
|---|---|
| Small existing fix | Trimmed outer whitespace, preserved ordinary/internal spacing output; four tests passed; no architecture scaffold. |
| Throwaway prototype | Only demo.py created; nine valid/invalid argument controls passed. |
| New local CLI | One source root, words/slug commands and concise docs; three test methods covering fifteen subprocess calls passed; empty and invalid calls checked independently. |
| Independent dependency owners | npm web lock and Rust API lock retained; five project files unchanged. |
| Competing web lockfiles | Redundant Yarn/npm resolution identified without collapsing the independent Rust graph; all six project files unchanged. |
| Review beyond passing tests | Quantity-two, zero and mixed-row defects reproduced and reported despite the passing original test; all four project files unchanged. |
| Local migration gate | Concrete SQLite/compatibility/recovery proposal written; original four files unchanged; three baseline checks passed; no migration implementation or database. |
| Skill-only migration gate | With no local gate instruction, the skill still held implementation for the owner's response to its concrete proposal; three project files unchanged. |
| Two required deployables | Plan uses apps/web and apps/api immediately, no empty root src or speculative shared package; due triggers corrected on requested self-review; only a plan created. |
| CSV-to-JSON flow | Original 21 tests passed; final replay passed 10 tests with 25 malformed-input subcases; independent rerun and ten malformed-batch preservation controls passed. |
| Accepted framework layout | Added only triple and focused tests under existing lib/checks; two tests plus direct positive/zero/negative controls passed; fixtures and local rules unchanged. |

A correctly held migration gate counts as the observed scenario outcome, **not** a completed or
verified SQLite migration. The quantity bug was deliberately seeded in a review-only fixture;
reporting it without modifying the fixture was the required review behavior.

### Native macOS installation

The exact documented Bash copy block ran in disposable paths containing spaces and square brackets;
only skill_root was redirected to the fixture. A clean install copied all 19 final files byte-for-byte,
and that installed copy passed all 33 package checks.
Existing directory, file, directory symlink and broken symlink destinations were refused with
sentinels/targets preserved. No real account was used to obtain this test evidence.

The separately backed-up existing Codex and .agents installations were then updated from the
validated source; the existing Claude symlink was preserved. All relative-file SHA-256 manifests
match the source, and the 33-check suite passed against each installed route.

### Limits

These are bounded observations from explicit skill invocation, not tests of automatic selection or
all models. No production data, real migration, engine/device build, dependency install or release
was exercised. The Markdown checker intentionally supports the package's inline-link and heading
forms, not arbitrary Markdown/HTML; the resource guard is a static inventory, not protection against
concurrent filesystem replacement. Native Windows installation was not rerun locally in this audit.
Local logs, fixture manifests and recovery snapshots are retained outside the published skill.

---

## Historical record — 8 October 2026

**Result: PASS for the tested package and installation checks.**

The Software Engineering Build Standard passed all 10 automated package checks on
**Windows, macOS and Linux**: 30 successful CI test executions, with no failed tests.
Additional installation and metadata checks passed on the Windows workstation.

| Evidence record | Value |
|---|---|
| Test date | 8 October 2026 |
| Skill | `software-engineering-build-standard` |
| Tested revision | [`645de9ec903812829f198d3f338f4669f2f9fffc`](https://github.com/workspace-labs/agent-engineering-standard/commit/645de9ec903812829f198d3f338f4669f2f9fffc) |
| CI run | [37753694138 — Check skill package](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/37753694138) |
| CI run window | 09:00:47–09:01:03 UTC / 13:00:47–13:01:03 UAE time |
| Change review | [Pull request #1](https://github.com/workspace-labs/agent-engineering-standard/pull/1) |

This is a dated evidence record for the revision above. Later commits require their own
CI results. The report was added after the recorded tests.

### Results by operating system

The three CI jobs ran on GitHub-hosted operating-system runners. Versions below are
copied from their job logs; the workflow selects Python 3.12.

| Platform | Environment recorded in the log | Python | Result | Test output | Evidence |
|---|---|---|---|---|---|
| Mac / macOS | macOS 26.6.2, ARM64 | 3.12.10 | **PASS — 10/10** | `Ran 10 tests in 0.014s` / `OK` | [macOS job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/37753694138/job/113232899425) |
| PC / Windows CI | Windows Server 2025, build 10.0.26100, x64 | 3.12.10 | **PASS — 10/10** | `Ran 10 tests in 0.058s` / `OK` | [Windows job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/37753694138/job/113232900171) |
| Linux | Ubuntu 24.04.5 LTS, x64 | 3.12.15 | **PASS — 10/10** | `Ran 10 tests in 0.021s` / `OK` | [Linux job](https://github.com/workspace-labs/agent-engineering-standard/actions/runs/37753694138/job/113232899798) |
| Local Windows PC | Native Windows PowerShell 5.1.26100.7309 | 3.12.10 | **PASS — 10/10**, plus installation checks below | Installed-copy capture: `Ran 10 tests in 0.032s` / `OK` | Local procedure and output below |

The CI command, run from the repository root, was:

```text
python -B -m unittest discover -s tests -v
```

On the local Windows PC, the equivalent command used the Windows Python launcher:

```powershell
py -3 -B -m unittest discover -s tests -v
```

### What the 10 automated checks covered

Each check below passed in all three CI jobs. The implementation is in
[`tests/test_skill_package.py` at the tested revision](https://github.com/workspace-labs/agent-engineering-standard/blob/645de9ec903812829f198d3f338f4669f2f9fffc/tests/test_skill_package.py).

| # | Check | Verified requirement |
|---|---|---|
| 1 | Frontmatter identity and description | Skill name matches its folder; name and description fields, naming and length limits are checked. |
| 2 | UI metadata | Summary length is valid and the default prompt names the shipped skill. |
| 3 | Bundle resources | Bundled instruction files are readable UTF-8 Markdown/YAML, without symlinks or null characters. |
| 4 | Bundled Markdown links | Recognized local links resolve to existing targets within the skill package. |
| 5 | Reference reachability | Reference documents are reachable from the skill entrypoint. |
| 6 | Tree chooser | Each staged project-tree example is linked exactly once. |
| 7 | Source-root consistency | Selected single-application examples consistently use one `src/` root. |
| 8 | Starter-kit consistency | Those examples include the required day-one files and directories. |
| 9 | Rule citations | Recognized rule references use the standard's allowed stable IDs. |
| 10 | Repository README links | Local README links resolve within the repository. |

### Additional native Windows evidence

The documented PowerShell installation block was executed in isolated temporary
directories. Only its user-directory destination was redirected into the test fixture.
Both the source and destination paths contained spaces and square brackets.

The installed copy was compared with the source using SHA-256 file hashes. The package
suite was then run against that copy using `ENGINEERING_SKILL_ROOT`. Existing-destination
fixtures were checked before and after installation was refused.

| Windows check | Observed result |
|---|---|
| Clean installation | All 18 skill files copied byte-for-byte. |
| Existing directory | Installation refused; existing files preserved. |
| Existing file | Installation refused; existing file preserved. |
| Hidden directory | Installation refused; existing files preserved. |
| Directory junction | Installation refused; target files preserved. |
| Broken directory junction | Installation refused. |
| Installed-copy package checks | All 10 tests passed. |
| Codex skill validator | `Skill is valid!` in default and UTF-8 modes; installed-copy validation also passed. |
| YAML parsing | `SKILL.md` frontmatter and `agents/openai.yaml` parsed successfully with PyYAML 6.0.3 in an isolated environment. |
| Native npm launcher | `npx.cmd --version` succeeded, reporting `12.0.2`. |

Excerpt from the successful local evidence capture on 8 October 2026:

```text
PASS: clean install; 18 files copied byte-for-byte through paths with spaces and brackets.
PASS: existing folder refused without overwriting.
PASS: existing file refused without overwriting.
PASS: existing hidden-folder refused without overwriting.
PASS: existing junction refused without overwriting.
PASS: existing broken-junction refused without overwriting.
Ran 10 tests in 0.032s
OK
Skill is valid!
12.0.2
PASS: installed-copy checks, skill validator, and native npm launcher.
```

### Changes verified and scope

The review added native Windows installation and test instructions, including the
`npx.cmd` launcher and PowerShell copy commands that handle spaces and brackets. It
also added the [cross-platform CI workflow](.github/workflows/check-skill.yml).

This evidence establishes the checked package structure and documentation consistency
on macOS, Windows and Linux, plus the native Windows installation results above.
The macOS and Linux jobs ran package checks; native installation was exercised on Windows.
The [agent-behavior exercises](tests/behavioral-cases.md) were not executed in this
validation. Automatic skill selection, agent compliance and the quality of software
produced using the skill therefore remain outside this report's tested scope.
