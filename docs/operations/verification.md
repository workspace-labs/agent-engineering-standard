# Verification and publication

## Offline package checks

From the repository root, with Python 3.9 or newer and no added dependencies:

```sh
python3 -B -m unittest discover -s tests -v
```

Windows PowerShell uses `py -3 -B -m unittest discover -s tests -v`. If the launcher (`py`)
is unavailable or reports "No installed Python found!", check `python --version` and use
`python -B -m unittest discover -s tests -v` with Python 3.9 or newer instead.
No Bash or WSL is required. [CI](../../.github/workflows/check-skill.yml) runs the same
package checks on Windows, macOS and Linux.

The checks cover metadata limits, local links and heading fragments across repository
Markdown, reference reachability, the tree chooser, starter-kit and source-root consistency,
and rule citations. Adversarial fixtures check missing targets and refusal of links,
Windows reparse points and special filesystem nodes before content reads or descent.
They use only the standard library and do not install or execute the skill. The Markdown
checker supports this package's inline links and heading forms; it is not a general renderer.
The metadata checks cover simple YAML string fields; the simple-field reader is not a
general YAML parser. Use an already available Agent Skills YAML frontmatter validator
as well if you change that representation.

See [the test evidence](../../TEST-EVIDENCE.md) for dated local results and verification
limits, the October 21 repair, and historical Windows, macOS and Linux results with native
Windows installation checks. Each record applies only to its stated revision.

## Behavioral checks

Instruction quality also needs [realistic agent exercises](../../tests/behavioral-cases.md).
Give a fresh agent the skill, raw fixture and user request, without the evaluator's expected
outcome. Run only inside an isolated fixture and inspect actual files, test output, command
results, refusal behavior and approval boundaries afterward. Record model/environment limits
and failed observations, distinguishing tested behavior from anything the environment could
not verify. Never turn static checks into a claim of universal agent compliance: package
checks passing alone do not prove that every agent will select or follow the skill correctly.

## Install/update proof

Use [the documented installation procedure](../../README.md). Compare complete relative-file manifests
and SHA-256 hashes. Try refusal cases in disposable destinations. Preserve backups and never merge
unreviewed installed differences. Do not execute install commands against a real user account just
to obtain test evidence; actual user-authorized updates are a separate step.

## Publication

Keep tests, reports and temporary fixtures out of the installable folder. Review the final diff,
update CHANGELOG.md and TEST-EVIDENCE.md, run relevant checks and obtain owner authorization before
committing or pushing. CI results apply to their exact revision; preserve earlier records as history.
