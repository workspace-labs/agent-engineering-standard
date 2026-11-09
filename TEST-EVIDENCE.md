# Test evidence

The dated records below distinguish executed checks from behavioral exercises and simulations.
Each record remains evidence for its original revision; earlier cross-platform results do not
certify the current local release candidate.

## 1.4.0 local candidate — 2026-11-09

Branch `release/1.4.0` from `fd8ab67` (1.3.0), in `~/Desktop/Projects/agent-engineering-standard`.
Not pushed, not tagged, not installed: the six user skill copies stay at 1.3.0.

### Executed package checks

On macOS 27.2 arm64, Python 3:

- `python3 -B -m unittest discover -s tests`: **41/41** passed, no skips. `git diff --check` clean.
- Fail-first, three ways, each restored afterwards: a stray `§105` citation fails
  `test_rule_citations_use_existing_stable_ids`; removing the `## §99 Search` heading fails
  the heading count; removing `references/platform-services.md` fails the link checks from
  SKILL.md, so the old 1.3.0 package does not pass the new suite.
- This is package protection only. No agent exercise was run against §91–§104.

### Fix round 1 — 2026-11-09

Independent Codex review of 45d44cb returned F01–F05 (review file kept outside the
repository). Corrections applied to platform-services.md §96, §98, §99, §103, the layout
map's `locales/`, `payments/` and `email/notifications/` rows and the API backend tree;
four scenarios added to tests/behavioral-cases.md. `python3 -B -m unittest discover -s
tests`: **41/41** passed, no skips; `git diff --check` clean. The scenarios were written,
not executed; no agent exercise was run.

### Fix round 2 — 2026-11-09

Codex round 2 closed F01–F05 and raised F06 (Low): the hero image's "Team & lifecycle"
tile read "DUE the second person", gating the whole guide on collaboration. The image was
re-rendered from its HTML source with four due labels corrected (lifecycle, platform
services, data, backend) and opened to confirm the text, the ten rule sets and the font.
Image-only change plus this record and the changelog; `python3 -B -m unittest discover
-s tests`: **41/41**, `git diff --check` clean.

## 1.3.0 coordinated local candidate — 2026-11-05

The engineering candidate starts from `3ee51a147ceb77114c46d644a324bf6205d0b806`
(1.2.1), in an isolated clone. The companion project-docs candidate starts from
`25beb27c376af95728386be330376987ed077aa2` (0.2.6) and becomes 0.3.0. Original
source repositories and all six existing user skill copies remain preserved.
No candidate was committed, pushed, published or installed for real use.

### Executed package checks

On macOS 27.2 arm64, Python 3.15.2 and Node.js 22.14.0:

- Engineering baseline: `python3 -B -m unittest discover -s tests -v`, **40/40** passed.
  Candidate: the same command passed **41/41**, no skips. The new routing test fails
  against the exact baseline package because its coverage guide is absent, then passes
  against this candidate. This is package protection, not proof an agent obeys the prose.
- The engineering suite also passed **41/41** against a disposable staged package selected
  by `ENGINEERING_SKILL_ROOT`. This is the same suite repeated, not 41 additional tests.
- Project-docs baseline `node --test`: **110/110**; candidate: **113/113** passed.
  The new checks protect bundled reference reachability and boundary integrity.
- Both `git diff --check` commands passed. The static audit found **0 structural errors**:
  project-docs has no findings; engineering retains its **12 pre-existing deep-reference
  review warnings** for the nested tree examples. No new static warning remains.
- The skill-creator general YAML validator was attempted for both packages but could not
  start because this Python lacks PyYAML. No dependency was installed. Existing package
  metadata checks and the static audit passed; the unavailable validator is not a pass.

### Five fresh isolated exercises

One fresh executor context per case received an ordinary raw request, its synthetic
workspace and manually supplied candidate skill paths, without the private rubric.
A separate agent authored the fixtures/probes before seeing solutions, then independently
graded actual artifacts in disposable copies. A separate source reviewer reran all five
fixture suites. The observed outcomes passed for these scopes:

- **Tiny typo:** only the intended heading changed, no new files or scaffold; **1** existing
  test passed independently. Browser rendering remains unverified.
- **Approved notes build:** accepted stack, documents and requirement IDs reused;
  persistent owned deletion, cross-owner refusal and unchanged denied data verified with
  unpredictable records and a fresh load. **10** retained tests passed. The prior checked
  step remains checked; the new step waits for the owner's check.
- **Restore repair:** supplied and randomized native SQLite snapshots restore usable
  records; corrupt/missing/wrong-schema failures return nonzero and preserve useful target
  data. **16** tests passed. Independent old-code controls prove the retained tests detect
  the original missing deletion and false-success restore behaviors.
- **Changed approved decision:** current seven-day drafts preserve original decisions,
  checked history and the old run as history; affected work is not started. Code remains
  at its original thirty-day checkpoint; its **1** test passed independently. This is a
  document-only outcome, not an implemented policy change.
- **Release assessment:** accurately leaves a Mac App Store source slice unready and
  identifies missing app, identity, signing, sandbox, privacy, artifact and current-rule
  evidence. Only documentation changed; its **1** source test passed independently.

These are **29 distinct fixture test methods**, separate from the package suites.
Private probes also checked resulting artifacts; their counts are not added to that total.
One raw restore grading guard remains red: it incorrectly required the operating document
to stay byte-identical. Both independent reviewers accepted the expanded documentation
after verifying the accepted SQLite/schema/CLI contract. The raw false positive is
retained as EVAL-01; no rubric was silently changed and no candidate defect was hidden.

### Identity, evidence and limits

The review-only packages contain **23 engineering files** and **60 project-docs files**.
Source/staged content, modes and entry types matched the final staging manifests; both
review agents independently confirmed current source/staged equality. An earlier manifest
predates the guide's Contents addition, made before executor launches; it is explicitly
marked intermediate. Exact hashes at each executor read were not captured.

Raw requests, pristine fixtures, responses, package logs, snapshot notes, manifests,
independent probes and assessments are retained outside these repositories in the local
coordinated update workspace's `evidence/` directory. The candidate changes are not installed
by those tests. All six current installations matched their recovery copies afterward.

Complete executor tool transcripts were unavailable: actual artifacts and independent
reruns are evidence, while each builder's claimed command history or absence of external
actions is not independently attested. Exact model-build identifiers were not captured.
Automatic selection, repeated-agent reliability and causal improvement were not tested;
there was no prior-skill/no-skill agent comparison. The pristine-code controls test the
retained regression tests, not skill effectiveness.

Current Apple rules, real signing/submission, legal or assurance conformance, production
data/recovery, concurrent writers, power loss, other platforms and Arabic live handoff
were not established. These five small cases do not certify the 91 research duties or
all examples in §§87–90. Final owner acceptance precedes any real installation.

### Subsequent owner acceptance and installed-copy verification

The owner accepted both candidates on 2026-11-05 and explicitly authorized committing
and pushing them. The pre-acceptance candidate record above is preserved as history.
The accepted 23-file engineering and 60-file project-docs packages were then installed
across six logical user skill paths. Four physical directories were replaced; the two
existing Claude symlink aliases were preserved. Fresh verified recovery copies and the
original directories were retained before switching.

All six installed paths matched the accepted content/mode manifests. The engineering
suite passed **41/41** with `ENGINEERING_SKILL_ROOT` selecting the real Codex installation.
Hash/mode-identical snapshots of both installed packages passed the static re-audit with
**0 structural errors**, the same **12 engineering nested-tree review warnings**, and no
project-docs findings. This adds installed-copy proof, not new behavioral/platform results.
The existing PyYAML, automatic-selection and other limits above remain. No real rollback
drill, version tag, GitHub Release or app-store submission was performed for this record.

The first staged whitespace check caught one extra blank line at the new coverage guide's
end; the earlier unstaged check had not included that untracked file. Exactly one final LF
was removed in the source, staged and installed copies. Instruction text/meaning and modes
are unchanged. The original manifests and pre-correction copies are retained separately
from the final publication manifests; the staged check was rerun after this correction.

## 1.2.1 native Windows verification — 2026-11-02

Started from a clean clone of `main` at `afe373cf5cdefe8f4afdeaf71daa625c45ad7c32`
(standard 1.2.0), on native Windows with **Windows PowerShell 5.1.26100.7309** and
**Python 3.12.10**. No Bash or WSL was used. Before editing, the working tree was clean
and `python -B -m unittest discover -s tests -v` passed all **39 tests**, with no skips.
This record describes a local 1.2.1 candidate, not a published release.

### Confirmed problems and repairs

1. **Incorrectly capitalized links passed on Windows.** With an actual file named
   `Guides/Guide.md`, the checker accepted both `Guides/guide.md` and `guides/Guide.md`
   on the native case-insensitive filesystem. These links are not portable to a
   case-sensitive host. One new regression method covers both errors and a correctly
   spelled positive control. Before the repair, **40 methods ran with two failing
   subcases** (`AssertionError not raised`); afterward all **40 passed**, with no skips.
   Component spelling is now checked against directory entries after the existing
   link/reparse/type guards. Native junction, boundary and selected-root-alias controls
   continue to pass. Repeated runs and subcases do not increase the method count.
2. **The email exercise missed required settings explanations.** The original skill
   executor produced working mail behavior and listed settings/defaults, but did not
   explain every setting's purpose. It reported that it had not loaded §85. The
   entrypoint's reference chooser did not name settings/handover as a reason to read
   that guide, and the completion checklist only asked generally for documentation.
   The repair adds explicit routing and a completion check for setting names, purposes
   and value sources. It clarifies the existing §85 requirement; rule IDs and the rule's
   meaning are unchanged. The standard version and changelog are now 1.2.1.
3. **The installed `py` launcher could not locate Python.** `py -3` reported
   `No installed Python found!` (exit 112), although `python --version` found Python
   3.12.10 and the tests ran successfully. README, contributor instructions and
   verification instructions now cover an unusable launcher as well as a missing one.
   This is an environment problem with a documented command fallback, not a Python fix.

### Executed behavior: original skill and no-skill baseline

Three isolated synthetic fixtures were executed with the original 1.2.0 skill and
without it. Both executors received the same requests and raw files, without evaluator
expectations. One executor per configuration handled all three fixtures; these were
separate projects, **not a fresh agent context per case**. A different grader inspected
the files, reran tests and probed the contracts independently.

| Exercise | Original skill | Without skill | Observed result |
|---|---:|---:|---|
| Tiny home-page typo | 3/3 assertions | 3/3 assertions | Only the heading changed; existing check passed; no lesson or scaffold. |
| Read-only basket review | 3/3 assertions | 3/3 assertions | Both found ignored quantities despite the passing old test; file paths and bytes stayed unchanged. |
| Email after booking | 3/4 assertions | 3/4 assertions | Local transport, exactly-once send and invalid-input checks passed; per-setting purposes were missing. |

Each configuration therefore passed **9/10 assertions**. The email projects passed
seven implementation tests with the skill and six without it; the grader also ran the
two original tests against each implementation. Passing code tests did not erase the
documentation failure. The missed check and original outputs remain preserved.

The basket review with the skill also made an overbroad prose claim about every quantity
other than one: a zero-price row is a counterexample. The grader recorded that limitation;
the actual reported quantity bug and reproductions were valid.

### Fresh-agent retest after the routing repair

The email request and pristine project were rerun with **one fresh executor per
configuration**: the saved original 1.2.0 skill and revised 1.2.1. Neither executor
received the grader's assertions. The same independent grader reran the original tests,
the new checks and separate send/configuration probes, without modifying project bytes.

- Revised skill: **4/4 assertions passed**, all **8 implementation tests** and both
  original tests passed. Its settings documentation explains every name, purpose and
  where to choose the synthetic local value.
- Original skill, fresh repeat: **4/4 assertions passed**, all **7 implementation tests**
  and both original tests passed. This run supplied a purpose table and explained safe
  defaults, process-environment values and shell overrides. The same grading threshold
  was applied to both runs; explanatory detail may be supplied across the README and
  example settings file.

Both preserved `book(name, slot)` and its confirmation result, sent exactly once through
the unchanged local transport, rejected invalid bookings before sending, honored all four
environment overrides, and propagated transport failures. No real service was contacted.
The revised documentation was more explicit about per-setting value selection, but this
fresh comparison shows **no assertion-score improvement**. One earlier original run
missed the documentation requirement and its fresh repeat satisfied it; neither that
variation nor one revised success proves reliability. The patch improves routing to an
existing requirement, not a demonstrated guarantee of compliance. All eight executor
runs (six initial, two fresh repeats) and their failures remain separately recorded.

### Native PowerShell installation and relocation

The README PowerShell manual-copy procedure was executed in disposable destinations,
with only its source and destination redirected into the fixture. All **six cases passed**:

- Fresh destination containing spaces: complete relative-file/SHA-256 manifests matched
  for all **22 files**.
- Existing directory, hidden directory, existing file, native junction and dangling
  junction: all five destinations were refused and their prior contents or link targets
  were preserved.

The same controls passed for the original bundle and were repeated for revised 1.2.1;
these are six distinct cases, not twelve. The final installed copy also passed the full
**40-test suite**, using `ENGINEERING_SKILL_ROOT` to select it. The fixture script used
a process-only PowerShell execution-policy override because this PC blocks `.ps1` files;
the documented inline copy commands were unchanged. No machine execution policy or real
user skill installation was changed.

### Commands, artifacts and limits

From the repository root, in PowerShell:

```powershell
python --version
python -B -m unittest discover -s tests -v
git diff --check
```

Raw fail-first logs, baseline state, manifests, synthetic projects, command records,
independent grades and review pages are retained in the sibling local
`agent-engineering-standard-workspace/`, outside the repository and installable skill.
Historical records below are preserved.

- The optional general YAML frontmatter validator could not run: its existing local
  Python environment lacks `yaml`/PyYAML. No dependency was installed. The package's
  simple-field metadata checks passed; frontmatter representation was unchanged.
- These are native local Windows results. macOS, Linux and hosted CI were not rerun.
- The email transport only appends synthetic messages in memory. No real emails,
  services, credentials, deployment, persistence migration or production data were used.
- Manual skill loading was tested. Automatic skill selection and universal agent
  compliance are not established. Token counts were unavailable; none are invented.
- The test run performed no commit, push, tag, GitHub Release or real user installation.
  The owner subsequently authorized committing and pushing this candidate; that does
  not publish a version tag or GitHub Release or change a real user installation.

## 1.2.0 local candidate — 2026-11-02

Work began on a clean `release/1.1.1` at `25f3bc676c519f6e813ad33776ca42acd0e8eaa0`,
then branched locally to `release/1.2.0`. Before any edit, on macOS/Python 3.15.2:

```text
python3 -B -m unittest discover -s tests -v
Ran 39 tests in 0.059s
OK
```

### Package checks and fail-first proof

The candidate package command passed all **39 tests**, with no failures, errors or skips
(0.059s), including rule citations, exact heading counts, starter-kit consistency, repository
and bundle links, reference reachability and standard-version/changelog agreement.
No test method was added: allowed rule IDs now span §1–§86 and the existing heading test
also requires exactly one heading for each of §84–§86. Existing §66–§72 and §74–§83 checks remain.

The heading test was extended before its rule was added: §84 first failed with one intended
assertion failure, then passed after implementation. When the owner added Part B mid-build,
extending the same test through §86 first failed for the missing §85 and §86 headings, then passed.

The final candidate was also copied into a disposable skill fixture. For each new rule,
only its heading was removed, the focused test run, then the heading restored and the
same test rerun. `ENGINEERING_SKILL_ROOT` selected the copy; source files were not changed
by the controls. The command for each run was:

```text
python3 -B -m unittest discover -s tests -p test_skill_package.py -k test_backend_frontend_rules_and_release_version -v
```

Observed for each of §84, §85 and §86 when its heading was removed:

```text
AssertionError: 0 != 1 : Rule §84 needs exactly one heading
AssertionError: 0 != 1 : Rule §85 needs exactly one heading
AssertionError: 0 != 1 : Rule §86 needs exactly one heading
```

These were three separate runs, each `Ran 1 test` / `FAILED (failures=1)` and exit 1,
without an error. Removal runs took 0.003s, 0.003s and 0.004s respectively.
Each restoration returned `Ran 1 test in 0.003s` / `OK` and exit 0.
Repeated controls do not add unique test methods to the count.

### Content checks and limits

The 95-line human guide has ten mistakes with verified rule meanings and eight glossary
entries. The 125-line example walkthrough starts with exactly the layout map's six day-one
paths; later additions name their actual triggers. Its final README shows Project map and
Settings sections, with no invented settings or premature `.env.example`. Personal-data
documentation is required before collecting names or phone numbers; the approved first
slice uses made-up times without contact fields and does not reserve real appointments.

All 22 existing behavioral cases and their introduction remain byte-identical to the base;
four new Request/Observe cases cover a first project, a tiny typo, takeover and new settings.
Their Request text matches the brief and a Request-only hint search found no forbidden words.
Rules §1–§83 remain unchanged. The only layout-map change is the owner-authorized README
description; the six starter paths and all tree guides are unchanged. The former 1.1.1
changelog bullets remain in the single 1.2.0 entry; all older changelog/evidence entries remain.

The skill-creator validator reported `Skill is valid!`. The read-only skill audit reports
zero structural errors and twelve existing `deep-reference` warnings for unchanged staged
tree resources; trigger, safety, portability and Claude/Codex compatibility axes pass.
These are static checks, not behavioral certification.

The four new cases were **written, not executed**, with or without the skill. The walkthrough
is an illustrative conversation, not evidence of an app build or test run. Agent compliance,
live services, app builds, native Windows/Linux and hosted CI were not tested for this
candidate. No push, tag, release or installation was performed. The owner added §85–§86
and related handover requirements during this same unreleased 1.2.0 build; the delivery
records that addition explicitly. Historical 1.1.1 evidence below is retained.

## 1.1.1 local candidate — 2026-11-02

This is a test-wording patch on local branch `release/1.1.1`, not a published release.
Work began on a clean `main` at `de4be07b2ca7593493ac2b3ae42f0869fb855597`.
`git pull --ff-only origin main` reported Already up to date. On local macOS with
Python 3.15.2, before any edit:

```text
python3 -B -m unittest discover -s tests -v
Ran 39 tests in 0.050s
OK
```

After the case and version edits, the same package command passed all **39 tests** with
zero failures, errors or skips (0.050s), including the standard-version/changelog check.
No automated test method was added or changed. The eleven existing beginner requests
were rewritten and one new API-key-placement case was added: **12 beginner cases**.

Request-only checks found no forbidden hint words, and the word "key" appears only in
the chat-website and key-placement requests. All twelve requests match the owner's brief.
The ten older cases are byte-identical to the starting commit (5,377 bytes;
SHA-256 `7405f398a23e062f9c4f424168bd7b2de0bfb38c99343b575f825bdbc3c3fb7d`).
The required introductory paragraph is the only change before those cases. SKILL.md
changes only its version line; older changelog entries remain byte-identical.

The skill-creator validator reported `Skill is valid!` with system Python 3.9.6. A read-only
skill audit reported zero structural errors and twelve existing `deep-reference` review
warnings for the unchanged tree chooser and eleven staged guides; trigger, safety,
portability and both compatibility profiles passed. These are static package results.

The twelve beginner behavioral cases were **written, not executed**. Neither with-skill
nor without-skill baseline exercises were run; their results must be recorded separately
when run. Agent compliance, live providers, app/container builds, native Windows/Linux and
hosted CI were not tested for this patch. No push, tag, release or installation was performed.
The rules, references, layout map, trees and README remain unchanged.



## 1.1.0 local candidate — 2026-11-02

This instruction-package candidate extends the standard with §74–§83; it is not a published
release. Work began on a clean `main` at `af003c3c631be07125540795beb3a6cfa2ee92fa`.
`git pull --ff-only origin main` reported Already up to date. Before edits, on local macOS
with Python 3.15.2, the package baseline was:

```text
python3 -B -m unittest discover -s tests -v
Ran 39 tests in 0.047s
OK
```

### Package and fail-first checks

After the guide, wiring and documentation changes, the same command passed all **39 tests**
with zero failures, errors or skips (0.053s). No new test method was added: the existing
heading/version method now checks §66–§72 and §74–§83, and allowed citations span §1–§83.
The suite also verifies reference reachability, repository/bundle links, metadata, tree
consistency and its existing adversarial boundary controls. These are package checks.

For fail-first proof, a disposable copy of the candidate had the §74 heading removed.
The focused command below failed at the intended assertion, without an error:

```text
python3 -B -m unittest discover -s tests -p test_skill_package.py -k test_backend_frontend_rules_and_release_version -v
Ran 1 test in 0.004s
FAILED (failures=1)
AssertionError: 0 != 1 : Rule §74 needs exactly one heading
```

Restoring the fixture returned `Ran 1 test in 0.003s` / `OK`. The test used
`ENGINEERING_SKILL_ROOT` to select the disposable copy; no source or installed copy was
mutated for the fault control. Repeated controls do not add unique methods to the count.

### Verification limits

The five new Request/Observe cases were **written, not executed**. No agent-built team PR,
ADR workflow, customer-data implementation, flaky-test repair or solo-script exercise was
run. Native Windows/Linux and hosted CI were not run for this candidate. Static package
results do not prove automatic selection, agent compliance, legal compliance or production
behavior. Earlier evidence below applies only to its recorded revision.

The owner clarified that the historical 1.0.0 changelog entry stays unchanged, including its
old gate note; the new 1.1.0 entry contains release changes only. No push, tag, release,
GitHub topic change or installation was performed; the separate v1.0.0 clone was untouched.

---

## 1.0.0 local candidate — 2026-11-02

This is a local instruction-package candidate on `release/1.0.0`, not a published release.
The starting tree was clean. `git pull --ff-only origin main` fast-forwarded from
`e5ecba3` to `e7060cb420d1a992510c5dd37cec454336729e32` before any edit.

### Baseline and package checks

Before editing, on macOS with Python 3.15.2:

```text
python3 -B -m unittest discover -s tests -v
Ran 38 tests in 0.044s
OK
```

The release suite contains **39 tests: the original 38 plus one new test method**.
All 39 passed with no failures, errors or skips on local Python 3.15.2 and 3.9.6:

```text
python3 -B -m unittest discover -s tests -v
Ran 39 tests in 0.053s
OK

/usr/bin/python3 -B -m unittest discover -s tests -v
Ran 39 tests in 0.048s
OK
```

The new method checks exactly one reference heading for each of §66–§72 and agreement
between the entrypoint's standard version and the newest versioned changelog heading.
The suite also checks bundled and repository Markdown links, reference reachability,
metadata, allowed rule citations and the existing adversarial package boundaries.

### Fail-first and negative controls

Before the guides and version line were added, this focused command ran one test method
and failed with eight expected assertion failures: seven missing headings and the missing
standard version line. These subcases are not eight extra test methods.

```text
python3 -B -m unittest discover -s tests -p test_skill_package.py -k test_backend_frontend_rules_and_release_version -v
Ran 1 test in 0.004s
FAILED (failures=8)
```

After implementation it passed. Four additional runs against disposable skill fixtures
removed §66, duplicated §66, mismatched the standard version and removed its version line.
Each exited 1 at the intended assertion, without an error. Restoring the fixture returned
one passing test. No source was mutated for these fault controls, and no skill was installed.

### Static validation and preservation

The available skill-creator frontmatter validator reported `Skill is valid!` using system
Python 3.9.6 with its existing PyYAML 6.0.3. The default Python lacked PyYAML; nothing was
installed to resolve it. A read-only audit of this repository's skill collection found
zero structural errors and twelve `deep-reference` review warnings for the existing tree
chooser and eleven staged guides. Reachability checks pass; these nesting warnings remain
visible and are not a warning-free result. Trigger, safety, portability and compatibility
axes passed the static audit. This is static evidence, not agent-behavior certification.

The October 21 record below was appended verbatim: all 13,617 original bytes match the
record from `e7060cb`, confirmed by byte comparison and `diff -u` with no output (exit 0).
The earlier October 19 and October 8 records remain unchanged apart from the top-level
introductory evidence link being replaced by a consolidated-record explanation.

### Not verified and gates

The five new behavioral cases were **written, not executed**. No live provider, application,
container build, deployment, accessibility tool/keyboard exercise or real RTL screen was
tested by this instruction-package change. Historical executed scenarios above/below apply
only to their stated revisions. Automatic selection and agent compliance remain unverified.

The 1.0.0 suite was not run on native Windows or Linux or in hosted CI. No installation,
push, tag, GitHub Release or topic change was performed. Claude's independent review and
the owner's publication decisions follow this local delivery.

### Fix round 1 — 2026-11-02

F1: widen §69 from browser secrets to project keys in all shipped clients, including mobile,
desktop and published CLI apps; retain the user-supplied runtime-key exception. The three
tree guides now cite §69. Version remains 1.0.0; frontend.md is unchanged.

On local macOS/Python 3.15.2, `python3 -B -m unittest discover -s tests -v` passed all
**39 tests**, with no failures, errors or skips, both before this repair (0.046s) and after
the instruction changes (0.045s). The heading/version test still passes. No test method
was added or changed. The new Android Request/Observe case was **written, not executed**.
Agent compliance, Android/desktop/CLI builds, package inspection, live model calls and
native Windows/Linux/hosted CI were not run. No push, tag, release or installation occurred.

---

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


---

## Local repair record merged verbatim — 2026-10-21

# Test evidence — 21 October 2026

The current local repair passes **38 package tests and 4 tests in an executed example project:
42 automated test methods in total**, plus **12 independent direct controls**.
Separately, **11 instruction scenarios were simulated**.
Repeated runs and failing subcases are not counted as additional unique tests.

## What was checked

The target is the Software Engineering Build Standard from
[workspace-labs/agent-engineering-standard](https://github.com/workspace-labs/agent-engineering-standard).
The baseline was a clean checkout of `0da1cb5808e0003eae8fead936de53d9eab393de`.
These results were captured against the local repair on top of that baseline, before publication.
The owner subsequently authorized committing and pushing the repair with this evidence file.

Environment: macOS 27.0.1, Python 3.9.6. The package tests use only Python's standard library.
The source was backed up before edits; before/after manifests and logs are retained outside the
repository. The previous checkout and installed Codex/Agent Skills copies remain unchanged.
No dependency installation, commit, push or release was performed during the test phase.

## Test counts and results

- **Baseline package suite: 33/33 passed**, with zero failures, errors or skips before repairs.
- **Final package suite: 38/38 passed**, with zero failures, errors or skips. Five test methods
  were added; the original 33 remain in the suite.
- **Executed skill-use example: 4/4 passed**, with zero failures, errors or skips. A separate
  fresh-context agent used the skill to repair a small existing Python project; the main agent
  inspected its artifacts and reran its tests independently of the fixture implementation.
- **Independent direct controls: 12/12 passed**. A reviewer who did not author the patch
  checked three valid relative routes, four decoded absolute-path forms, three native linked
  routes under skipped metadata (including a linked path followed by `..`), one simulated
  reparse-directory traversal, and one explicitly selected root alias. Its repeated run of
  the 38-test suite is not counted again.
- **Instruction simulations: 11/11 produced the expected scope/approval decisions**: eight
  baseline scenarios and three fresh-context approval scenarios after clarification. These
  were written decisions, not executed applications or migrations.
- **Skill frontmatter validator: valid**, both before and after the changes.
- **Static skill audit: 0 errors, 12 review warnings**, both before and after. All twelve are
  existing `deep-reference` observations about the intentional tree chooser and its guides.
  Their links and reachability pass; the auditor's status remains `Needs review`, not warning-free.
- **Git diff whitespace check: passed.**

## Confirmed checker bugs and fail-first proof

1. **Nonportable absolute links were accepted.** A local absolute link to a file inside the
   checkout passed validation but failed after an identical package was copied elsewhere.
   The checker now rejects absolute paths, including percent-encoded absolute paths, before
   resolving them. Valid relative parent links remain supported.
2. **Linked resources in skipped metadata could be followed.** The repository inventory skips
   `.git`, but a Markdown link could reach a symlink or Windows reparse resource inside it.
   The checker now inspects path components below the selected root before descent or content
   reads. The explicitly selected installation root may still be an alias; its child resources
   are checked. This preserves the previously supported installed-skill route.

With the five new methods and the old checker, **38 methods ran and 5 subcases failed across
3 methods**: two absolute-path forms, one native linked-directory route, and two simulated
Windows reparse resource routes. The valid relative-link and selected-root-alias controls
already passed. After the repair, all 38 methods passed. The failed run is retained as
`validator-red.txt`; the passing run is retained as `validator-green.txt` outside the repository.

The five added regression/control methods are:

- `test_absolute_paths_inside_boundary_are_not_portable_links`
- `test_relative_parent_links_inside_boundary_remain_valid`
- `test_explicit_root_alias_remains_supported`
- `test_native_link_under_skipped_git_is_refused_before_read`
- `test_skipped_reparse_file_and_directory_readme_are_refused_before_read`

An existing linked-directory-README test now expects refusal at the earlier symlink/reparse
check, rather than after following the link and detecting an escaped boundary.

## Executed example project: one small bug fix

The fresh-context request was to trim leading and trailing whitespace in an existing Python
slug helper while preserving ordinary output and keeping the standard library only.

- Before changes, the example's two existing tests passed.
- After adding regression cases, the original implementation failed three whitespace subcases.
- The agent added `strip()` to the existing expression and changed only the implementation and
  its test file. No architecture scaffold, new dependency or unrelated change was introduced.
- The final four test methods passed. The main agent reran them and also ran the same tests
  against a separate copy containing the original implementation: three subcases failed again.

The four methods cover ordinary words, empty input, boundary whitespace (spaces, tabs, newlines
and whitespace-only input), and preservation of internal repeated spaces and tabs.
These artifacts and `behavioral-red.txt` / `behavioral-green.txt` remain in the isolated evidence
fixture, outside the installable skill. The fixture had no Git repository; no Git baseline was claimed.

## Eleven instruction simulations

Baseline scenarios:

1. Mechanical Python documentation spelling correction: no engineering ceremony.
2. Small Flask empty-query-field bug: narrow fix and regression coverage.
3. Small Rust CLI: keep Cargo conventions and proportional structure.
4. Existing Next.js preference: preserve accepted app and colocated-test layout.
5. Previously approved SQLite migration: proceed within existing approval.
6. Read-only engineering review: report findings without editing the project.
7. pnpm plus independent Rust services: retain each dependency graph's own lockfile.
8. Owner-stopped restructuring: report incomplete approved scope and remaining debt.

Fresh-context approval scenarios after the wording change:

9. Add a flag using the accepted Node/Zod stack: proceed without a new technology gate.
10. Implement the same concrete migration design already approved by the owner: proceed.
11. Replace released storage without any proposal/approval yet: inspect and propose, then hold
    implementation for the design decision.

The instruction repair clarifies two textual inconsistencies: the general workflow now puts
required design approval before implementation, and reuse of accepted technology or an earlier
approval does not create a duplicate gate. The baseline simulations did not demonstrate an actual
approval bypass; these are clarity corrections, not a claim of a reproduced dangerous agent action.
The reusable exercise contracts are in [tests/behavioral-cases.md](tests/behavioral-cases.md).

## Commands

From the repository root:

```sh
python3 -B -m unittest discover -s tests -v
git diff --check
```

The isolated example project uses the same unittest command, run from its own directory.
The installed validation tools were also run:

```sh
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/software-engineering-build-standard
node "$HOME/.codex/skills/audit-agent-skills/scripts/audit-skills.js" --root "repo=$PWD/skills" --json
```

These tool paths describe the existing local validation tools; the repository does not require
or install them. Its 38-test package suite remains standard-library only.

## Package identity and integrity

Static auditor bundle digests:

- Before: `1c7b81ed9c3d3dcb80c22ab10724deb02ec4c86fe7ff33b466a9d70d72455237`
- After: `682780f341a68aece03f61fa8f993d3738e53a37ca3004f39b87a5de1c337e62`

Only the entrypoint instructions changed inside the installable skill; checker code and reports
stay outside it. Source and backup manifests matched before editing. Existing installed copies
were compared with their initial SHA-256 manifests and remained unchanged.

## Limits

- This repair was executed locally on macOS. Native Windows and Linux checks were **not rerun**;
  earlier CI evidence in [TEST-EVIDENCE.md](TEST-EVIDENCE.md) applies only to its recorded revisions.
- Native POSIX links were exercised. Windows reparse metadata was simulated; the new native
  Windows junction branches still need a Windows run.
- Eleven simulations are not eleven implemented products. No real migration, production data,
  application deployment, signing, or automatic skill selection was exercised.
- The checker supports this package's inline Markdown links and headings, not arbitrary Markdown
  or HTML. Filesystem checks are static and do not protect against concurrent path replacement.
- The broad state-model sizing label and audit-closure wording remain nonblocking observations;
  explicit scope/accepted-project precedence supplied safe decisions in the scenarios tested.
- This session authored the repairs, so its own checks are builder verification. A separate
  read-only reviewer found no source-repair blocker in the inspected diff, the 38-test suite
  or its twelve independent controls. Its exact probe record is retained outside the repository.

## All 38 package test methods

The list below names unique unittest methods. Parameterized subcases and reruns do not increase
this count. Ten are package integrity checks and twenty-eight are regression/control methods.

```text
test_package_regressions.MarkdownLinkRegressions.test_missing_path_fragment_is_refused
test_package_regressions.MarkdownLinkRegressions.test_missing_pure_fragment_is_refused
test_package_regressions.MarkdownLinkRegressions.test_directory_link_without_readme_is_refused
test_package_regressions.MarkdownLinkRegressions.test_directory_readme_and_fragment_are_resolved
test_package_regressions.MarkdownLinkRegressions.test_encoded_path_and_non_ascii_duplicate_headings
test_package_regressions.MarkdownLinkRegressions.test_valid_same_document_atx_and_setext_headings
test_package_regressions.MarkdownLinkRegressions.test_fenced_example_heading_is_not_a_fragment
test_package_regressions.MarkdownLinkRegressions.test_existing_files_and_external_links_remain_valid
test_package_regressions.MarkdownLinkRegressions.test_fenced_and_inline_code_links_are_examples
test_package_regressions.MarkdownLinkRegressions.test_local_file_urls_are_not_portable_external_links
test_package_regressions.MarkdownLinkRegressions.test_absolute_paths_inside_boundary_are_not_portable_links
test_package_regressions.MarkdownLinkRegressions.test_relative_parent_links_inside_boundary_remain_valid
test_package_regressions.MarkdownLinkRegressions.test_explicit_root_alias_remains_supported
test_package_regressions.MarkdownLinkRegressions.test_non_markdown_fragment_is_explicitly_unsupported
test_package_regressions.MarkdownLinkRegressions.test_directory_readme_link_cannot_escape_the_boundary
test_package_regressions.MarkdownLinkRegressions.test_documents_beyond_the_repository_readme_are_checked
test_package_regressions.MarkdownLinkRegressions.test_repository_inventory_finishes_before_reading_any_markdown
test_package_regressions.MarkdownLinkRegressions.test_fragment_target_must_be_regular_before_reading_it
test_package_regressions.MarkdownLinkRegressions.test_fragment_under_skipped_git_directory_is_checked_before_read
test_package_regressions.MarkdownLinkRegressions.test_native_link_under_skipped_git_is_refused_before_read
test_package_regressions.MarkdownLinkRegressions.test_skipped_reparse_file_and_directory_readme_are_refused_before_read
test_package_regressions.MarkdownLinkRegressions.test_missing_file_and_encoded_escape_are_refused
test_package_regressions.ResourceBoundaryRegressions.test_windows_junction_metadata_is_refused_portably
test_package_regressions.ResourceBoundaryRegressions.test_nonregular_node_is_refused_without_reading_it
test_package_regressions.ResourceBoundaryRegressions.test_junction_is_refused_before_enumerating_its_children
test_package_regressions.ResourceBoundaryRegressions.test_rule_checks_do_not_read_a_linked_external_child
test_package_regressions.ResourceBoundaryRegressions.test_native_entrypoint_link_is_refused_before_any_text_read
test_package_regressions.ResourceBoundaryRegressions.test_native_directory_link_is_refused_and_target_preserved
test_skill_package.SkillPackageTests.test_frontmatter_identity_and_description
test_skill_package.SkillPackageTests.test_ui_metadata_mentions_the_shipped_skill
test_skill_package.SkillPackageTests.test_bundle_contains_only_readable_instruction_resources
test_skill_package.SkillPackageTests.test_all_bundled_markdown_links_resolve_inside_the_skill
test_skill_package.SkillPackageTests.test_all_references_are_reachable_from_the_entrypoint
test_skill_package.SkillPackageTests.test_tree_chooser_links_each_example_once
test_skill_package.SkillPackageTests.test_single_app_snapshots_keep_a_consistent_source_root
test_skill_package.SkillPackageTests.test_single_app_day_one_examples_include_the_starter_kit
test_skill_package.SkillPackageTests.test_rule_citations_use_existing_stable_ids
test_skill_package.SkillPackageTests.test_all_repository_markdown_links_resolve
```
