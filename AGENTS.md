# Working on agent-engineering-standard

Read [the scope](docs/scope.md) and [the boundaries](docs/architecture/boundaries.md) before changing the package.

## Source and checks

The installed product is `skills/software-engineering-build-standard/`. This is an instruction package,
not a runtime application: do not create an empty `src/`, dependency manifest or generated scaffold.
Tests and exercise contracts live in `tests/`; repository documentation lives in `docs/` and the root.

Run the offline checks with Python 3.9 or newer, standard library only:

```sh
python3 -B -m unittest discover -s tests -v
```

On Windows, use `py -3` or `python`. The CI workflow runs the same checks on Windows, macOS and Linux.
See [verification and publication](docs/operations/verification.md) for package, installation and behavioral proof.

## Change rules

- Keep the skill model-neutral, framework-aware and proportional to the actual project.
- Tree examples show earned responsibilities, not mandatory empty folders. Owner and accepted framework
  conventions take precedence. Keep explicit due triggers consistent with the layout map.
- New references must be reachable from SKILL.md, and each tree example must be linked once by its chooser.
- Leave tests, local evidence, machine paths, credentials and generated output outside the installed skill.
- Back up installed copies before updates. Never merge divergent copies or overwrite an existing install silently.
- Record changes in CHANGELOG.md and actual test scope in TEST-EVIDENCE.md. Preserve historical evidence.
- Commit, push, release and owner approval require the owner's authorization; passing tests is not that approval.
