# Example tree — web application (SPA + backend)

A web app with its own server. Snapshots of one project as it grows, worked examples of the
*due at* rule — **never a template to scaffold**. Create only what the product has already
earned (§22). The folder names below are one vocabulary; the responsibilities are the rule,
and a framework's own conventions win (§61).

## Stage 1 — day one

```
myapp/
  README.md
  CHANGELOG.md
  .gitignore
  docs/scope.md
  src/                    the frontend — plain src/ while it is the only app
  tests/
```

## Stage 2 — the first real feature

```
  src/
    app/bootstrap/        earned by: the first screen — where the app starts
    app/routing/          earned by: the second page
    features/<feature>/   earned by: the first feature that owns more than one file
                          (only the subfolders it really has: components, state, tests…)
  docs/architecture/boundaries.md   earned by: past the kit — the one-home rule lives here
  one lockfile            earned by: the first dependency — never two
```

The feature's home is chosen once and written down in `boundaries.md` — every later feature
follows it.

## Stage 3 — a server appears (the second deployable thing)

One app keeps plain `src/`; two deployables earn `apps/` — never an `apps/` folder with a
single child.

```
  apps/frontend/src/
    services/             earned by: the first server call — ONE API client owning
                          addresses, headers and error handling
    state/                earned by: the first state two features share
    validation/           earned by: the first response checked before it is trusted
  apps/backend/src/
    server/               earned by: day one of the server
    api/routes/           earned by: the first endpoint
    api/schemas/          earned by: the first input from outside — the contract, checked
                          at the edge (§39)
    domain/entities/      earned by: the first thing the product has rules about
    infrastructure/database/  earned by: the first stored row
    config/               earned by: the first server setting — an example file, no real values
  docs/architecture/overview.md   earned by: the second part that talks to another
```

## Stage 4 — the contract between the two

```
  packages/contracts/     earned by: the first type the app and the server both import
  data/migrations/        earned by: the first change to a table that has shipped (§43)
  tests/contract/         earned by: the first interface both sides of the repo own (§39)
  tests/e2e/              earned by: the first flow a person completes end to end
  docs/api/               earned by: the first endpoint something else calls
  docs/security.md        earned by: the first sign-in, stored data or secret
```

Later stages add `application/use-cases/` (first multi-step operation), `packages/domain/`
(product rules both apps share) and `docs/adr/` (first real decision, §36) — each on the day
it is earned, never earlier.
