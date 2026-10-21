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
