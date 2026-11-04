# Reply to the cross-repo recommendations

> Reply to [RECOMMENDATIONS.md](RECOMMENDATIONS.md), item by item: **Agree**, **Modify** or **Disagree**,
> each with a reason. Written 2026-11-04 by Claude (Claude Code) for the owner. This is a review, not an
> approval: the owner decides each item.
>
> Checked against: this branch at `87ae07e`; agent-engineering-standard `main` at `3ee51a1`;
> project-docs `main` at `25beb27` (version **0.2.6**).

---

## Summary

- **27 agree, 6 modify, 4 disagree**, out of 37. R15, R19, R20 and R22 are agreed but later.
- The facts about the repositories hold up, with three exceptions (next section).
- Main disagreement: **R1/R24's direction.** project-docs installs on its own and must not depend on the
  standard. The standard should adopt project-docs' paths instead, and a check should keep the two in step.
- Two further disagreements follow the standard's own rules: **R4** (a plan and a roadmap are different
  things) and **R34/R35** (community files before they are due).

## Fact check

| Claim | Result |
|---|---|
| R3: the walkthrough uses `docs/design.md` | Confirmed: `docs/first-project-walkthrough.md` lines 51 and 109 |
| R5: project-docs' Security headings | Confirmed: Who can get in · How it's protected · Secrets · Personal data · Outside services · Work rules · If something goes wrong |
| R6: the TRD default is "tests beside the code" | Confirmed: `skills/project-docs/references/trd.md` line 59 |
| R14: actions pinned by tag, `permissions: contents: read` | Confirmed: `.github/workflows/check-skill.yml` |
| R37: README still waits for `v1.0.0`; tags v1.0.0–v1.2.0 exist, v1.2.1 does not | Confirmed: `README.md` lines 119–125 and the tag list |
| R2: "the tests that check the starter kit" | **Not found.** No test in `tests/*.py` mentions `scope.md`. Find the real assertions before planning step 2. |
| R11: "Claude Code reads AGENTS.md only when no CLAUDE.md exists" | **Not verified.** Check the current Claude Code documentation before the standard states it. |
| Section 1: project-docs at `a206d4d`, version 0.2.4 | **Out of date.** project-docs is now **0.2.6**. Since then it has added ADRs 0004–0007 (approved choices keep their history; a waiting step names the open choice exactly; the AI never picks the technology; Security protections are written, not asked), all Accepted. |

---

## 2. Core recommendation

**R1. Modify.** Agree on one agreed set of paths. Disagree that project-docs should *cite* the standard for
them. project-docs is installed and used on its own; its
[boundaries](https://github.com/workspace-labs/project-docs/blob/main/docs/architecture/boundaries.md) say
the skill folder is self-contained, and it never installs another skill. "Follow
software-engineering-build-standard's layout map" would make it depend on a skill that may not be there.
**Instead:** the standard adopts project-docs' paths (R2, R3, R5, R7, R8 already do this). Each skill keeps
the paths written in its own files, and a release check in each repository compares the two lists. For
vibe-to-engineering, see R29.

## 3. Conflicts

- **R2. Agree.** "`docs/scope.md` *or* `docs/prd.md`" is correct, and it closes project-docs ADR 0002's
  open step. First find which tests actually encode the starter kit (see the fact check).
- **R3. Agree.** `DESIGN.md` at the root, in the layout map and the walkthrough. It is what project-docs
  writes and what agents look for.
- **R4. Disagree.** These are not in conflict. `docs/plan.md` is the build steps for the approved scope,
  each with a check only the person ticks. `docs/roadmap.md` is later work outside that scope. Merging them
  puts unscheduled ideas between checked build steps. Keep both, each due at its own trigger, and add one
  line to the layout map saying how they differ. (RECOMMENDATIONS.md open question 3 already grants this is
  a preference.)
- **R5. Modify.** The headings belong to project-docs (R1 itself says project-docs owns content). The
  standard should say: *when project-docs wrote `docs/security.md`, its headings are the structure; map
  §27/§68/§69 onto them.* Copying the seven headings into the standard creates a second copy that drifts.
- **R6. Agree.** "The ecosystem's convention wins; `tests/` is the fallback and the home for cross-app
  suites." On the project-docs side this means one change: the TRD default, plus any example TRD that
  quotes it, plus its test, released as a new version.
- **R7. Agree.** Add `docs/trd.md` to the layout map. Use the relationship as written: the TRD is the
  current locked stack; an ADR records a changed or important choice. This matches project-docs
  [ADR 0004](https://github.com/workspace-labs/project-docs/blob/main/docs/adr/0004-approved-choices-keep-their-history.md),
  where changes also stay visible in the TRD as dated `Changed` lines.
- **R8. Agree.** `docs/data.md` is the human contract, and schemas and migrations implement it. The §43
  note ("a migration that changes a shipped table also updates `docs/data.md`") is the important part.

## 4.1 agent-engineering-standard

- **R9. Modify.** Put the rule "the ecosystem's convention wins over the generic map" in the core. Put the
  per-ecosystem blocks in `references/ecosystems.md` as dated examples, reviewed yearly, linked only from
  the router. Python, Go, Rust and Node/TS are enough; JVM, .NET and Swift can wait until a project asks.
- **R10. Modify.** Keep the rule tool-neutral ("the second time the same boundary is broken, it becomes an
  automatic check"). Name the tools only as examples, in the same examples file as R9.
- **R11. Modify.** Agree on root `AGENTS.md`, nested files in monorepos, the size budget, and "instructions
  are not enforcement: what must always happen becomes a hook or a CI check". Verify the claim about how
  Claude Code reads AGENTS.md against current documentation before writing it down. Add the path-scoped
  rule files only at their own trigger.
- **R12. Agree.** Offer project-docs only if it is installed, and never require it. It is the same pattern
  project-docs uses for frameflow.
- **R13. Agree.** One task-runner entry point, due at the second command a person must remember. It makes
  §75 concrete.
- **R14. Agree** for this repository's own CI: pin actions to full SHAs with a version comment, add
  `dependabot.yml` with `github-actions`, and keep least-privilege permissions. In the *guidance*, state the
  principle and keep the workflow-lockfile option as an example. It is newer, and I have not verified it.
- **R15. Agree, later (1.4.0).** Measurable CI time is the right trigger. Nothing asks for it yet.
- **R16. Modify.** Offer the vertical-slice layout as the documented alternative in
  `trees/api-backend.md`, chosen once in `boundaries.md`. Keep one default for a beginner, so the choice
  does not become a new question on every small API.
- **R17. Agree.** Name the version files. The devcontainer and pre-commit triggers as given are
  reasonable.
- **R18. Agree.** `infra/` or `deploy/`, due at the first infrastructure defined as code.
- **R19. Agree, optional and later.** Conventional Commits and release tooling stay optional suggestions,
  due at the second release someone depends on. §55 commit hygiene already covers the rest.
- **R20. Agree, optional and later.** Diátaxis only once `docs/` really outgrows a flat list.
- **R21. Agree, and apply it first.** Every addition from R9–R20 goes into reference files, never into
  `SKILL.md`. Decide the size budget before the additions, not after.
- **R22. Agree, later.** These are small and low-value until a project needs them.

## 4.2 project-docs

- **R23. Agree. This is the most valuable item for project-docs.** `node --test` on Linux, macOS and
  Windows, with SHA-pinned actions. It closes the "No CI" debt.
- **R24. Disagree as written** (see R1). project-docs keeps its paths and states that they match the
  standard's layout map; a release check compares them. Keep the TRD change from R6.
- **R25. Agree, updated.** Tag the current release, **v0.2.6**, not v0.2.4, and publish a GitHub release
  following project-docs' own
  [release steps](https://github.com/workspace-labs/project-docs/blob/main/docs/operations/release.md).
  The owner decides whether to also tag 0.2.2–0.2.5 at their commits.
- **R26. Agree.** A test that checks README, CHANGELOG and TESTING agree is better than removing the
  version from the README, because readers look for it there.
- **R27. Agree.** Regenerate the workflow JSON for the current version.
- **R28. Agree.** After the Plan is approved, offer the standard once if it is installed. This mirrors R12.

## 4.3 vibe-to-engineering

- **R29. Agree, with one condition.** Keep the independent C1–C16 rubric, because it must judge projects
  never built under the standard. Add the C → § mapping table, and state that where they disagree, the
  standard's rule wins for a project that adopted the standard.
- **R30. Agree.** An approved `docs/prd.md`, `docs/trd.md` or `DESIGN.md` is an owner decision, like an
  accepted ADR, not a finding. Only the stamp `Approved <date>` counts; a `Draft` does not.
- **R31. Agree.** Same CI hygiene as R14.

## 4.4 Shared housekeeping

- **R32. Agree.** `.gitattributes` in the standard and vibe-to-engineering. project-docs has had one
  since 0.2.4.
- **R33. Agree, low.** `.editorconfig` only once it records a real shared convention.
- **R34. Disagree for now.** The standard's own layout map says these are due when "a public repository's
  contribution or reporting workflow actually needs them". Recommending them early teaches agents to
  ignore the trigger. If the owner wants them anyway, one org-level `workspace-labs/.github` repository is
  the cheapest form. project-docs' `docs/security.md` already holds a `TBD` for where to report privately.
- **R35. Disagree for now.** Same reason. A PR template is due at the second person or agent changing a
  repository (§76).
- **R36. Agree.** Topics cost nothing and change no file.
- **R37. Agree. Do it first.** Fix the README pinning text, and the owner tags v1.2.1.

## 5. Plan order

Agree with the order, with three changes:

1. **R21's size budget comes before step 3**, so the additions land in references from the start.
2. **Step 2 includes the path-compare check** from R1 (modified), in place of R24's "cite the standard".
3. **R4 drops out of step 2.** Plan and roadmap stay separate, with one line explaining the difference.

The 1.3.0 minor version is right: rules are added or widened, none removed.
