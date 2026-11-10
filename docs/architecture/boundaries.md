# Responsibility boundaries

- `skills/software-engineering-build-standard/` owns the shipped instruction contract. SKILL.md routes
  to focused guidance; the tree chooser routes to each staged example once. It has no executable runtime.
- `tests/` owns offline package validation and behavioral exercise contracts. Package tests read the
  package without executing its instructions. Agent exercises run separately in disposable fixtures.
- `.github/workflows/` runs the existing package tests; it does not certify agent compliance or install
  a skill into a real user account.
- Root Markdown and `docs/` own install guidance, scope, architecture and dated evidence. They may link
  into the package; the installed package must not depend on files outside its own folder.
- Local logs, snapshots, generated ZIP files and backups are external evidence. They do not become
  package resources or public user-data fixtures.

Guidance is authored in one place. Do not duplicate a reference into different roots or move source
into a generic src/ merely to resemble an application tree. New artifact responsibilities are added
when real work earns them, following the same proportionality the skill teaches.

The platform-services reference owns §91–§104: the services a product grows around its code, each with a due-at trigger; it names homes the layout map already lists and never mandates a provider or a service.

The architecture reference also owns §105 (business rules and edge cases), beside §8 where the rules live; the backend reference also owns §106 (overload and traffic spikes), beside §67 reliability. New rules join the guide whose subject they extend and take the next free ID; IDs are never renumbered.

The coverage-and-evidence reference owns §87–§90. It consumes approved project planning; it does not generate another PRD/TRD workflow. Behavioral exercises and evidence remain outside the installed package.
