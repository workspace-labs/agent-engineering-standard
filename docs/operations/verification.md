# Verification and publication

## Offline package checks

From the repository root, with Python 3.9 or newer and no added dependencies:

```sh
python3 -B -m unittest discover -s tests -v
```

Windows uses `py -3 -B -m unittest discover -s tests -v`, or `python` when the launcher is unavailable.
Use an already available Agent Skills frontmatter validator for metadata changes; the repository's
simple-field reader is not a general YAML parser.

## Behavioral checks

Follow [the exercise contracts](../../tests/behavioral-cases.md). Give a fresh agent the skill, raw
fixture and user request, without the evaluator's expected outcome. Run only inside an isolated
fixture and inspect actual files, test output, refusal behavior and approval boundaries afterward.
Record model/environment limits and failed observations. Never turn static checks into a claim of
universal agent compliance.

## Install/update proof

Use [the documented installation procedure](../../README.md). Compare complete relative-file manifests
and SHA-256 hashes. Try refusal cases in disposable destinations. Preserve backups and never merge
unreviewed installed differences. Do not execute install commands against a real user account just
to obtain test evidence; actual user-authorized updates are a separate step.

## Publication

Keep tests, reports and temporary fixtures out of the installable folder. Review the final diff,
update CHANGELOG.md and TEST-EVIDENCE.md, run relevant checks and obtain owner authorization before
committing or pushing. CI results apply to their exact revision; preserve earlier records as history.
