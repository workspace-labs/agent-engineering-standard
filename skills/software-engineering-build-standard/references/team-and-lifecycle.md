# Team workflow and project lifecycle

Apply each responsibility only when its **due at** trigger is met (§22). A solo or tiny
project does not earn team ceremony by existing. Accepted project workflows — AGENTS.md,
CONTRIBUTING, branch policy, ADR format and release process — take precedence (§61).

## Contents

- §74 Test levels
- §75 CI quality gates
- §76 Branches, pull requests and code review
- §77 ADR format and lifecycle
- §78 Releasing a project
- §79 Environments and feature flags
- §80 Privacy and the data lifecycle
- §81 Dependency health over time
- §82 Incidents
- §83 Code ownership

## §74 Test levels

**Due at:** the first behavior that needs verification; use the existing
[test folders and their triggers](layout-map.md#tests), not a new scaffold (§15).

- Unit tests prove one rule or function in isolation. Integration tests prove two real
  parts together, such as code and a real database. Contract tests prove an interface both
  sides own (§39). End-to-end tests prove one flow a person completes.
- Put most checks at the fastest level that proves the behavior; keep a few end-to-end
  checks for the flows that matter most.
- A flaky test is a defect: find its cause or quarantine it with an owner and a note.
  Never hide it with automatic retries or silently delete it. Quarantine that weakens a
  gate needs the owner's recorded decision under §75.
- Coverage is a signal, not a target; never add assertion-free tests to raise it. Use
  synthetic test data (§27).

## §75 CI quality gates

**Due at:** the first check that should run without being asked — the existing CI trigger.

- CI runs the same commands developers run locally, documented in README/AGENTS.md:
  format check, lint, type check where the language has one, tests and build, as applicable
  to the project. Add the secret scan (§69) and dependency audit (§68) when each is due.
- Main stays green: merge a change only when its gates pass. Never weaken a gate to get
  green by deleting tests, skipping checks, adding blanket suppressions or lowering a
  threshold without the owner's explicit decision, recorded in the change.

## §76 Branches, pull requests and code review

**Due at:** the second person or agent changing the same repository, or the owner asking
for review before merge. A solo project keeps §55 commit hygiene; PRs are optional.

- Use short-lived branches from main with one intent per pull request, small enough to
  review in one sitting; preserve truthful Git state and coherent commits (§18, §55).
- A PR description says what changed and why, how it was tested with commands and
  results, risks, rollback and any Human Gate needed.
- The author reviews their own diff first; the reviewer applies §52. Nobody merges a PR
  with failing gates (§75). Protect main where the platform allows.

## §77 ADR format and lifecycle

**Due at:** an important decision earns an ADR under §36; its timing stays there.

- Use the project's own ADR format when one exists. Otherwise use
  `docs/adr/NNNN-short-title.md`, numbered in order, never reusing a number.
- Sections: Status, Date, Context, Decision, Alternatives considered, Consequences.
- Status values: Proposed, Accepted, Rejected, Deprecated, Superseded by NNNN. An agent
  writes Proposed; it becomes Accepted only after the owner's answer at the Human Gate
  (§30). A proposal may instead be Rejected; an accepted decision may later be Deprecated
  or Superseded.
- Never edit an Accepted ADR to change its decision: a new ADR supersedes it, and the old
  one names its successor (§36).
- **`docs/adr/README.md` is due at the second ADR:** an index of number, title and status.

## §78 Releasing a project

**Due at:** the first release someone else installs, deploys or depends on.

- Use semantic versioning for things others depend on: libraries, APIs, CLIs and skills.
  An app may use the version scheme its platform or owner requires.
- Every release bumps the version once, has a dated CHANGELOG entry (§19), a tag and
  release notes for users, and is built reproducibly (§26), ideally from CI.
- A rollback plan exists **before release**: what to roll back to and how. Data migrations
  state whether they can be reversed (§43, §44).
- Publishing is the owner's action unless the project grants that authority.

## §79 Environments and feature flags

**Due at:** the first environment actually used; flags have their separate trigger below.

- Keep only environments that exist: development, test, staging, production. Each has its
  own configuration (§49) and keys (§69); `config/<environment>/` follows the
  [existing settings trigger](layout-map.md#settings-commands-tools-published-files), not an earlier split.
- Keep environments as similar as practical. Production data never goes to development
  or test environments; use synthetic data (§27).
- **A feature flag is due at the first unfinished feature that must merge to main, or the
  first staged rollout.** Every flag has an owner and a removal condition; remove it after
  full rollout (§25). Never use flags as permanent configuration.

## §80 Privacy and the data lifecycle

**Due at:** the first personal data stored or processed — names, email, phone, IDs,
location, device identifiers or anything that identifies a person.

- Keep a data inventory in `docs/privacy.md`: what is collected, why, where it is stored,
  who can access it, how long it is kept and how it is deleted.
- Collect the minimum. Every stored category has a retention period and a working deletion
  path, including backups where practical. Log access by people when the data is sensitive,
  without exposing the personal records in those logs (§27).
- Laws differ by country; UAE PDPL and EU GDPR are examples. Name likely obligations for
  the owner, but never claim the product is legally compliant: that decision belongs to
  the owner and their legal adviser.

## §81 Dependency health over time

**Due at:** the first deployed or published release; extends §25 and §47.

- Lockfiles stay authoritative. Use an automated update tool or a scheduled review to
  keep dependencies current. Triage vulnerability alerts by severity; fix them or record
  them as accepted debt (§57).
- A major-version dependency upgrade is its own change with its tests run, never mixed
  into a feature (§55).
- When deprecating an API, option or feature, announce it, give a migration path and a
  timeline, and keep it working until the next major version. Removal still needs the
  deliberate, documented approval required by §44; a version number is not permission.

## §82 Incidents

**Due at:** the first deployment someone depends on. A runbook in `docs/operations/`
says how to check health, roll back and restore.
After an incident, write a short blameless review: what happened, impact, cause, fix and
prevention. Add a regression test for the cause, following the
[existing test folders and triggers](layout-map.md#tests).

## §83 Code ownership

**Due at:** different people or teams own different parts of the repository.
Use CODEOWNERS or the platform's equivalent to record that ownership.
CONTRIBUTING keeps its [existing layout-map trigger](layout-map.md#root-files-and-documentation).
