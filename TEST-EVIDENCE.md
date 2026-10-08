# Cross-platform test evidence

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

## Results by operating system

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

## What the 10 automated checks covered

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

## Additional native Windows evidence

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

## Changes verified and scope

The review added native Windows installation and test instructions, including the
`npx.cmd` launcher and PowerShell copy commands that handle spaces and brackets. It
also added the [cross-platform CI workflow](.github/workflows/check-skill.yml).

This evidence establishes the checked package structure and documentation consistency
on macOS, Windows and Linux, plus the native Windows installation results above.
The macOS and Linux jobs ran package checks; native installation was exercised on Windows.
The [agent-behavior exercises](tests/behavioral-cases.md) were not executed in this
validation. Automatic skill selection, agent compliance and the quality of software
produced using the skill therefore remain outside this report's tested scope.
