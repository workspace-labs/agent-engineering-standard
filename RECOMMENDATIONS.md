# Recommendations: how WorkSpace Labs' three engineering skills should fit together

> Prepared 2026-11-04 (Dubai, UTC+4) for review. **Read-only analysis**: nothing was committed, pushed or opened as a PR.
> Each recommendation has an ID (R1, R2, …) so a reviewer can answer item by item: *agree / disagree / modify*, with a reason.

---

## 1. Purpose and context

Three public repositories in the `workspace-labs` org cover one project's life:

| Phase | Repo | What it does | Analyzed at |
|---|---|---|---|
| **Before building** | [workspace-labs/project-docs](https://github.com/workspace-labs/project-docs) | Agent skill that writes six approved documents with the person: `docs/prd.md`, `docs/trd.md`, `DESIGN.md`, `docs/data.md`, `docs/security.md`, `docs/plan.md`. Stamps (`> vN · Draft/Approved <date>`), locked choices with dated `Changed` lines, honest `TBD`s, English/Arabic. | commit `a206d4d` (2026-11-04 10:12 +04), version **0.2.4**, no tags |
| **While building** | [workspace-labs/agent-engineering-standard](https://github.com/workspace-labs/agent-engineering-standard) | Agent skill `software-engineering-build-standard`: work sizing, Human Gate, rules §1–§86, a layout map in which every folder has a *due at* trigger, 11 staged example trees, team/lifecycle guidance. | commit `3ee51a1` (2026-11-02 21:18 +04), standard **1.2.1**; tags v1.0.0, v1.1.0, v1.2.0 exist, **v1.2.1 is not tagged** |
| **After building** | [workspace-labs/vibe-to-engineering](https://github.com/workspace-labs/vibe-to-engineering) | Diagnoses whether an existing project needs restructuring and migrates it in approved phases with recovery checkpoints. Judges structure with its own criteria **C1–C16** (`skills/vibe-to-engineering/references/engineering-standard.md`). macOS-only development version. | commit `bd8133f` (2026-10-19 04:02 +04), no tags |

The ideas are consistent and complementary. The problem: **file locations and "what good structure is" are defined in three places**, and some of those definitions now contradict each other (section 3).

What is already strong and should be kept (research agrees): proportional structure that grows only when earned ("due at"), framework conventions winning, one home per feature recorded in `docs/architecture/boundaries.md`, Human Gates for architecture, ADR lifecycle, `.env.example` and the secrets rules, CI running the same commands as local, and the "ten-year handover" README test. This matches the Go team's official layout guidance, Russ Cox's criticism of over-prescriptive layouts, Turborepo's `apps/` + `packages/`, and the colocation and vertical-slice arguments (see Sources).

---

## 2. Core recommendation

**R1. Make `agent-engineering-standard` the one source of truth for *where* files live and *when* each becomes due.**
- **project-docs** owns the *content* of its six documents (questions, fixed headings, stamps, locks), but their *locations and triggers* are declared in the standard's layout map. project-docs cites the standard instead of redefining paths.
- **vibe-to-engineering** judges projects against the standard's rule IDs (§5–§10, §15, §22, §37, §38, §49, §50, …). Its C1–C16 either become a mapping table to §-IDs, or an ADR records why it keeps an independent rubric (for example, because it must judge projects not built under the standard).
- Each skill names the others in its workflow (R12, R20), so an agent moves naturally: project-docs → build under the standard → vibe-to-engineering for legacy code.

---

## 3. Conflicts to resolve

| ID | Topic | project-docs says | Standard says | Proposed resolution |
|---|---|---|---|---|
| **R2** | Scope vs PRD | ADR 0002: when `docs/prd.md` exists it *is* the scope. The ADR says the standard's wording would change separately ("plan step 15"). | Day-one kit requires `docs/scope.md`. The standard never mentions a PRD. | Day-one kit item becomes **"`docs/scope.md` *or* `docs/prd.md`"**: if `docs/prd.md` exists it is the scope, and `scope.md` is optional or legacy. Update `layout-map.md`, `trees/*`, the `SKILL.md` new-project workflow, the tests that check the starter kit, and §85/§86 wording. This closes project-docs ADR 0002's open step. |
| **R3** | Design reference | `DESIGN.md` at the project root (ADR 0002) | Layout map: "a written design or style reference" at the first screen. `docs/first-project-walkthrough.md` uses `docs/design.md`. | Adopt **`DESIGN.md` at the root** as the canonical name in the layout map and walkthrough (a common convention, and already what project-docs writes). Replace `docs/design.md` mentions. |
| **R4** | Plan vs roadmap | `docs/plan.md`: small steps, each with a check, ticked only by the person | `docs/roadmap.md`, due at "the second planned piece of work" | Canonical **`docs/plan.md`**. Roadmap content (later, unscheduled work) becomes a section of the plan, or `docs/roadmap.md` stays only for long-horizon items. Pick one; I recommend plan.md only, for one place. |
| **R5** | `docs/security.md` shape | Seven fixed headings: Who can get in · How it's protected · Secrets · Personal data · Outside services · Work rules · If something goes wrong | Same path, due at the first stored data, sign-in, network call or secret; no structure defined | The standard adopts project-docs' headings as the **default structure** of `docs/security.md` (a project's own accepted format still wins, §61). The standard's §27/§68/§69 rules map onto those headings. |
| **R6** | Test placement | TRD default: "tests beside the code" | Default: a separate `tests/` tree with typed subfolders | New rule: **the ecosystem's convention wins.** Go `*_test.go` and Rust unit tests sit beside the code; Rust integration tests go in `tests/`; JS/TS may colocate `*.test.ts`. A separate `tests/` stays the fallback and the home for cross-app suites (contract, e2e, architecture). project-docs' TRD default then says "the language's usual test location". |
| **R7** | Where stack decisions live | `docs/trd.md` records and locks stack choices | Nothing; stack choices are handled through ADRs and the Human Gate | Add **`docs/trd.md`** to the layout map (due: before the first dependency or stack choice). State the relationship: the TRD is the current locked stack; an ADR is written when a TRD choice is *changed* or is important enough to need alternatives recorded. The standard's "outside the accepted stack" Human Gate rule refers to the TRD. |
| **R8** | Data | `docs/data.md`: tables, columns, personal or secret fields marked, a ready block | `data/schemas/`, `data/migrations/` (code) | Not a contradiction, but link them: `docs/data.md` is the human contract; `data/schemas/` and migrations implement it. Add a row to the layout map and a §43 note: a migration that changes a shipped table also updates `docs/data.md`. |

---

## 4. Changes per repo

### 4.1 agent-engineering-standard

**High**
- **R9. `references/ecosystems.md`** (new, linked from `SKILL.md` and `layout-map.md`): one short block per ecosystem with source root, manifest, lockfile, test location, version file and the community gotcha.
  - **Python:** `pyproject.toml`, src layout `src/<pkg>/` (PyPA's reasons), `uv.lock` or `poetry.lock`, `.python-version`.
  - **Go:** `go.mod`/`go.sum`, start flat, `internal/` early, `cmd/<app>/` only for mixed or multi-binary repos, no `pkg/` or `src/` (Go docs, Russ Cox).
  - **Rust:** `Cargo.toml`/`Cargo.lock`, `src/lib.rs`, `src/bin/`, `tests/`, `benches/`, `examples/`.
  - **Node/TS:** `package.json` `exports` instead of barrel files, a `pnpm-workspace.yaml` per Turborepo guidance, no `../` imports across packages.
  - JVM, .NET and Swift optional.
  - Clarify: "the ecosystem's convention wins over the generic map" (ties to R6).
- **R10. Boundary enforcement by tools.** In `layout-map.md` (`tooling/architecture-checks/`) and `architecture-and-boundaries.md` §9, name examples: Python `import-linter` (layers and independence contracts), TS/JS `dependency-cruiser` or `eslint-plugin-boundaries`, Go `internal/`, JVM ArchUnit. Trigger: the second time the same boundary is broken, it becomes a CI rule.
- **R11. Agent instruction files.** Extend the root-files table:
  - `AGENTS.md` at the root, plus **nested `AGENTS.md` per package in monorepos** (the nearest file wins, per agents.md).
  - `CLAUDE.md` containing `@AGENTS.md` plus Claude-only notes. Not a symlink, which breaks on Windows. Claude Code reads AGENTS.md only when no CLAUDE.md exists.
  - Path-scoped rules: `.claude/rules/*.md` and `.cursor/rules/*.mdc` (Cursor ignores `.md` there; `.cursorrules` is legacy), and `.github/copilot-instructions.md`, each due when one area has conventions the root file shouldn't carry.
  - A size budget (Claude docs: under ~200 lines per file).
  - The principle "instructions are not enforcement": anything that must always happen becomes a hook or a CI check.
- **R12. Link project-docs in the new-project workflow.** In `SKILL.md` §3: "If no approved `docs/prd.md` or `docs/trd.md` exists and the `project-docs` skill is installed, offer it before ARCHITECTURE; otherwise follow the minimal `docs/scope.md` path." Never require it.
- **R13. Single task-runner entry point.** Add a row: `Makefile` / `justfile` / `Taskfile.yml` / `package.json` scripts, due at **the second command a person must remember**. README, AGENTS.md and CI all call the same targets (`test`, `lint`, `build`). This makes §75 ("CI runs the same commands") concrete.
- **R14. CI supply-chain hygiene** (in §75/§81 and for the repo's own workflow):
  - Pin actions to full commit SHAs with a version comment, or adopt GitHub's workflow lockfile (`.github/workflows/actions.lock`).
  - Add `.github/dependabot.yml` including the `github-actions` ecosystem.
  - Per-job least-privilege `permissions:`.
  - Avoid `pull_request_target`.
  - Current repo state: `actions/checkout@v7` and `actions/setup-python@v7` are pinned by tag; `permissions: contents: read` is already set (good).

**Medium**
- **R15. Monorepo tooling trigger** in `trees/monorepo.md`:
  - A build orchestrator (Turborepo, Nx, Bazel/Pants, Cargo/Go/uv workspaces) is due when CI time or wasted rebuilds become measurable.
  - List the minimum files: workspace file, root lockfile, shared tsconfig package.
  - Name the polyrepo vs monorepo trade-off and keep it under the Human Gate (already §30).
- **R16. Vertical-slice option for backends.** `trees/api-backend.md` is layer-first only. Add the slice or hybrid alternative `features/<feature>/{api,domain,infra}`, chosen once in `boundaries.md`, so agents don't default to Clean Architecture for every API.
- **R17. Developer environment rows:**
  - Name the version files (`.nvmrc`, `.python-version`, `.tool-versions`/`mise.toml`, `rust-toolchain.toml`).
  - `.devcontainer/devcontainer.json`, due at the second contributor or the first native dependency.
  - `.pre-commit-config.yaml` (or lefthook) as the local mirror of CI gates, due with the linter or the first secret.
- **R18. `infra/` or `deploy/`** (Terraform, Helm, k8s) row: due at the first infrastructure defined as code. It is reviewed and CI-checked like app code, and secrets stay out.
- **R19. Release automation and commit convention** (§78): optional Conventional Commits plus release-please / changesets / semantic-release, due at the second release someone depends on. Keep a Changelog format as a suggestion for `CHANGELOG.md`.
- **R20. Docs taxonomy:** once `docs/` passes about 5 how-to/reference files, organize by Diátaxis (tutorials / how-to / reference / explanation). Optional.

**Low**
- **R21. Skill size.** `SKILL.md` is about 3,000 words (21 KB), near the Agent Skills spec's recommended body limit (under 5,000 tokens). Consider moving the §73 closure template and the Human Gate long form into references. `references/trees/` is two levels deep against the spec's "one level" advice; the repo already accepts this in `docs/risks-and-debt.md`.
- **R22. Small additions:** `examples/` for libraries and CLIs, `benches/` beside `tests/performance/`, an observability row (metrics/tracing) beside `logging/`, a pointer to github/gitignore templates.

### 4.2 project-docs

- **R23 (High). Add CI**: `.github/workflows/test.yml` running `node --test` on Linux, macOS and Windows, with SHA-pinned actions. This is already listed as debt in `docs/risks-and-debt.md` ("No CI").
- **R24 (High). Take locations from the standard** (after R2–R7 land): add a line to `docs/architecture/boundaries.md` and the `SKILL.md` Start section saying document locations follow software-engineering-build-standard's layout map. Change the TRD default "tests beside the code" to "the language's usual test location" (R6).
- **R25 (Medium). Tags and releases:** start tagging (`v0.2.4`), following its own `docs/operations/release.md`. This is listed as debt.
- **R26 (Medium). Version in one place:** the version and test count currently live in README, CHANGELOG and TESTING (listed as debt). Either a test that checks they agree, or keep the version only in CHANGELOG and reference it.
- **R27 (Low). Regenerate `docs/workflow/project-docs-workflow.json`** (stuck at 0.1, listed as debt).
- **R28 (Low).** At the end of the Plan, offer: "build under the engineering standard" (mirror of R12).

### 4.3 vibe-to-engineering

- **R29 (High). Link the criteria to the standard:** add a mapping table C1–C16 → §-IDs in `references/engineering-standard.md` (e.g. C1→§6, C2→§10, C6→§9, C7→§5, C8→§50, C9→§49, C10→§15, C12→§7, C16→§22), or an ADR explaining why the rubric is independent. Either way, state precedence when they disagree.
- **R30 (Medium). Recognize project-docs files as accepted decisions** when diagnosing: an approved `docs/trd.md`, `DESIGN.md` and `docs/prd.md` count as owner decisions (like accepted ADRs) and are not findings.
- **R31 (Medium). Same CI hygiene as R14**: `.github/workflows/validate.yml` pins `actions/checkout@v7`, `setup-python@v7`, `setup-node@v6` and `upload-artifact@v7` by tag.

### 4.4 Shared housekeeping (all three repos)

- **R32 (Medium).** `.gitattributes` (`* text=auto eol=lf`; binaries marked) in agent-engineering-standard and vibe-to-engineering. project-docs already has it, as of 0.2.4. The standard's CI runs on Windows, and a recent fix was about path casing.
- **R33 (Low).** `.editorconfig` in all three.
- **R34 (Medium).** `SECURITY.md` and `CONTRIBUTING.md` in all three public repos, or once in an org-level `workspace-labs/.github` repo (GitHub applies default community health files from there). By the standard's own trigger these are optional until outside contributions arrive; they are cheap.
- **R35 (Low).** `.github/ISSUE_TEMPLATE/` and `PULL_REQUEST_TEMPLATE.md`, ideally in the org `.github` repo.
- **R36 (Low).** GitHub topics on agent-engineering-standard and project-docs (e.g. `agent-skills`, `claude-code`, `software-architecture`, `project-structure`, `prd`). deckcraft already uses topics.
- **R37 (Medium). Fix the stale README text and the missing tag in the standard.** The README says "After the owner publishes the `v1.0.0` tag … The local 1.0.0 candidate does not create that tag", but v1.0.0, v1.1.0 and v1.2.0 exist. Update it to "pin a released tag, e.g. `v1.2.1`", and publish the **v1.2.1** tag that matches the current `CHANGELOG.md`.

---

## 5. Proposed v1.3.0 plan for the standard (ordered)

Each step is one coherent change with its own CHANGELOG line and tests. The owner approves before commit and push, per the repo's AGENTS.md.

1. **R37**: fix the README pinning text; tag v1.2.1 on the current commit (owner action).
2. **R2, R3, R4, R5, R7, R8**: reconcile with project-docs in `layout-map.md`, `trees/*`, `SKILL.md`, `first-project-walkthrough.md` and `new-developer-guide.md`. Update `tests/test_skill_package.py` and `test_package_regressions.py` where they assert the six-piece starter kit. Add an ADR in `docs/adr/0002-…` recording "project-docs owns document content; the standard owns locations".
3. **R6 + R9**: add `references/ecosystems.md` and the "ecosystem convention wins" test-placement rule. Add it to the reference router and the reachability tests.
4. **R11**: agent-files rows and guidance.
5. **R10, R13**: boundary-enforcement tool examples and the task-runner row.
6. **R14 + R32 + R33**: harden the repo's own CI (SHA pins or actions lockfile, dependabot.yml), add `.gitattributes` and `.editorconfig`.
7. **R12**: the project-docs hand-off in the new-project workflow; add a behavioral case in `tests/behavioral-cases.md` ("new project with no PRD").
8. **R15–R20**: the medium-priority additions (each can slip to 1.4.0).
9. **R21**: size review of `SKILL.md`; move long sections into references if over budget.
10. Bump to **1.3.0** (a minor version: rules added, none removed or redefined, so semver holds; R2 widens a rule rather than breaking it), update the CHANGELOG and TEST-EVIDENCE, run the package checks on 3 operating systems, and the owner tags it.

---

## 6. Recommended reference tree

A **map of possible homes, not a scaffold**. Each entry appears only when its trigger in the layout map is met.

```
project/
├── README.md  CHANGELOG.md  LICENSE  .gitignore  .gitattributes  .editorconfig
├── AGENTS.md                  # one source for all agents (nested per package in monorepos)
├── CLAUDE.md                  # "@AGENTS.md" + Claude-only notes
├── .claude/rules/  .cursor/rules/*.mdc   # path-scoped agent rules, when earned
├── DESIGN.md                  # the look (project-docs), first screen
├── Makefile | justfile        # one command surface for README, AGENTS.md and CI
├── .tool-versions | mise.toml | .nvmrc | .python-version
├── pyproject.toml+uv.lock | package.json+pnpm-lock.yaml | go.mod/go.sum | Cargo.toml/Cargo.lock
├── .pre-commit-config.yaml    # local mirror of CI gates + secret scan
├── .env.example               # names + purpose + where to get each value, no values
├── .devcontainer/devcontainer.json
├── .github/
│   ├── workflows/ci.yml (+ actions.lock or SHA-pinned actions, per-job permissions)
│   ├── dependabot.yml         # includes the github-actions ecosystem
│   ├── CODEOWNERS  PULL_REQUEST_TEMPLATE.md  ISSUE_TEMPLATE/
│   └── copilot-instructions.md
├── SECURITY.md  CONTRIBUTING.md          # public repos (or org .github repo)
├── docs/
│   ├── prd.md  (or scope.md)  trd.md  data.md  security.md  plan.md   # project-docs content
│   ├── architecture/{overview,boundaries,dependencies}.md
│   ├── adr/{README.md,0001-*.md}
│   ├── api/  operations/  deployment/
│   ├── risks-and-debt.md  privacy.md  glossary.md
│   └── (Diátaxis when large: tutorials/ how-to/ reference/ explanation/)
├── src/<pkg>/                 # Python src layout; Go: cmd/<app>/ + internal/; Rust: src/lib.rs, src/bin/
│   └── features/<feature>/    # one home per feature, recorded in boundaries.md
├── apps/<name>/  packages/  platform/    # only with 2+ deployables (+ workspace file, turbo.json)
├── tests/{unit,integration,contract,e2e,architecture,regression,fixtures}/   # Go/Rust/JS may colocate unit tests
├── data/{schemas,migrations,seeds}/   (data/backups/ gitignored)
├── infra/ | deploy/           # IaC, when deployed
├── scripts/                   # what a person runs
└── tooling/                   # what runs by itself: import-linter / dependency-cruiser configs, codegen
```

---

## 7. Open questions: where a reviewer might reasonably disagree

1. **Tool neutrality vs naming tools (R9, R10, R13, R14, R19).** The standard deliberately says "tool-agnostic." Naming tools risks dating it and looking prescriptive. My view: name them as *examples* in a separate reference file, keep the rule itself neutral, and review the file yearly. A reviewer may prefer to keep everything out of the core skill.
2. **Is project-docs part of the standard or a separate optional skill? (R1, R12).** Merging would give one source of truth but a heavier skill. Keeping them separate needs the cross-references in R2–R8 to stay synchronized, perhaps via a shared test. I chose separate skills with the standard owning paths.
3. **`docs/plan.md` vs `docs/roadmap.md` (R4).** Some teams want both: a short execution plan and a long-horizon roadmap. Folding them into one is a simplicity preference, not a correctness issue.
4. **`DESIGN.md` at the root (R3).** Root files compete for attention; `docs/design.md` keeps the root clean. I chose the root because project-docs already ships it and agents find root files more reliably. Either is defensible if recorded once.
5. **Tests beside the code vs `tests/` (R6).** Colocation (Dodds, Go, Rust) vs a clear separate tree (easy packaging exclusion, mirrors the standard's typed folders). "Ecosystem wins" is a compromise that leaves JS/TS ambiguous; the project should still decide once in `boundaries.md`.
6. **Layered vs vertical slice (R16).** Bogard argues slices scale better and layered architecture invites needless abstraction. Others value strict dependency direction. Offering both with a recorded choice adds a decision for beginners.
7. **Skill size (R21) vs completeness.** Every addition here grows the package. The Agent Skills spec recommends under 500 lines and under 5,000 tokens for `SKILL.md`, and references one level deep. Additions should go into reference files, not `SKILL.md`, and some medium items may not be worth their context cost.
8. **Community files "due at" (R34).** The standard's own rule says SECURITY.md and CONTRIBUTING.md are due only when a contribution or reporting workflow actually needs them. Recommending them now slightly contradicts the "nothing before earned" philosophy. The counter-argument: these are public repos with followers, and the cost is minimal.
9. **SHA pinning vs readability (R14, R31).** SHA pins plus Dependabot add update noise. GitHub's newer workflow lockfile avoids the noise but is newer and less widely adopted.
10. **vibe-to-engineering independence (R29).** It may need its own rubric to judge projects never built under the standard. A mapping table keeps both while preventing silent drift.

---

## 8. Sources

**Fetched and checked during this analysis (2026-11-04):**
- PyPA, src layout vs flat layout: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- Go, Organizing a Go module: https://go.dev/doc/modules/layout
- Russ Cox, "this is not a standard Go project layout": https://github.com/golang-standards/project-layout/issues/117
- Cargo package layout: https://doc.rust-lang.org/cargo/guide/project-layout.html
- Turborepo, structuring a repository: https://turborepo.com/docs/crafting-your-repository/structuring-a-repository
- Kent C. Dodds, Colocation: https://kentcdodds.com/blog/colocation
- Jimmy Bogard, Vertical Slice Architecture: https://www.jimmybogard.com/vertical-slice-architecture/
- AGENTS.md (nested files, nearest wins): https://agents.md/
- Claude Code memory (CLAUDE.md / AGENTS.md / `.claude/rules`, size guidance): https://docs.anthropic.com/en/docs/claude-code/memory
- Cursor rules (`.cursor/rules/*.mdc`, `.cursorrules` legacy): https://cursor.com/docs/rules
- Agent Skills specification (size and nesting guidance): https://agentskills.io/specification
- GitHub Actions secure use (SHA pinning, workflow lockfile): https://docs.github.com/en/actions/reference/security/secure-use
- GitHub workflow dependency lockfiles: https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles
- GitHub Well-Architected, Actions security (Dependabot, least privilege): https://learn.github.com/well-architected/library/application-security/recommendations/actions-security/
- import-linter layers contract: https://import-linter.readthedocs.io/en/stable/contract_types/layers/
- eslint-plugin-boundaries: https://github.com/javierbrea/eslint-plugin-boundaries

**Cited from memory, not re-fetched in this session** (well-known, stable pages; verify if a claim depends on them):
- Bulletproof React (feature-based frontend): https://github.com/alan2207/bulletproof-react (its `docs/project-structure.md` fetch returned empty)
- dependency-cruiser: https://github.com/sverweij/dependency-cruiser
- pnpm workspaces: https://pnpm.io/workspaces
- monorepo.tools: https://monorepo.tools
- Google, "Why Google Stores Billions of Lines of Code in a Single Repository" (CACM 2016): https://cacm.acm.org/research/why-google-stores-billions-of-lines-of-code-in-a-single-repository/
- Uncle Bob, Screaming Architecture: https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html
- The Twelve-Factor App, Config: https://12factor.net/config
- ADRs: https://adr.github.io/ and Michael Nygard, "Documenting Architecture Decisions": https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Keep a Changelog: https://keepachangelog.com · SemVer: https://semver.org · Conventional Commits: https://www.conventionalcommits.org
- Diátaxis: https://diataxis.fr
- EditorConfig: https://editorconfig.org · pre-commit: https://pre-commit.com · Dev Containers: https://containers.dev
- GitHub, default community health files (org `.github` repo): https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- GitHub, line endings and `.gitattributes`: https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings
- github/gitignore templates: https://github.com/github/gitignore

**Repository facts** were read directly from clones at the commits in section 1: file contents, tags via `git ls-remote`, and workflow `uses:` lines.
