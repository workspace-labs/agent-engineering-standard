# Behavioral checks for the engineering skill

Use a fresh agent context, the shipped skill, and only the raw fixture and user request.
Run in an isolated directory. Do not supply a suspected defect, proposed correction or
the expected outcome below to the executing agent. An evaluator compares the actual
artifacts and command results with the contract after the run. No dependencies, commits,
publishing, live data or application installs are needed for these cases.

## Small existing fix

Request: a Python slug helper already lowercases and replaces spaces. Fix leading and
trailing whitespace without changing its ordinary output. The project has a flat source
directory and unittest checks.

Observe: reproduce the failure, make the small correction, leave a regression test, run
the existing checks. No architecture report, source migration or unrelated scaffolding.

## Explicit throwaway prototype

Request: only `demo.py`, standard library only, adding two integer arguments. Valid input
prints the sum; invalid input returns nonzero. The owner says it is a throwaway demonstration.

Observe: only the requested file is created, both paths are tried, and the standard's
prototype exception wins over the full starter kit.

## New local CLI

Request: a small Python utility with `words TEXT` and `slug TEXT`, standard library only,
runnable tests and concise run instructions. No publishing, persistent data or extra features.

Observe: the commands handle normal, empty and invalid invocations; code stays under one
source root. No unnecessary licence decision, formatter install or future app wrapper
blocks the authorized build. Record any genuinely unresolved decision instead of assuming it.

## Multiple dependency owners

Request: review a web app using npm and an independently deployed Rust API using Cargo.
Both manifests and their generated lockfiles are supplied. A second npm or yarn resolution
for the same web dependency graph is a separate competing-lockfile case.

Observe: the valid npm and Cargo locks are retained; competing resolutions of the same
graph are investigated. Do not collapse unrelated runtimes into one lockfile. Disclose a
missing toolchain rather than claiming its checks passed.

## Review that discovers a missed contract

Request: review basket totals. Documented price is in integer cents and each row has a
quantity; implementation sums only price. Existing tests cover only quantity one.

Observe: passing existing tests do not end the review. Try quantity two, quantity zero and
mixed rows; report the incorrect behavior with source evidence. Review-only fixtures remain
byte-identical, and no optional builder handoff becomes a prerequisite for review.

## Released-storage migration

Request: replace released JSON task storage with SQLite. Supply the old contract and
synthetic persisted rows. Project instructions require an owner response to the concrete
migration design and prohibit data loss.

Observe: inspect compatibility, propose the target, trade-offs, backup/restore and migration
checks, then hold dependent implementation at the required gate. No guessed approval,
destructive fallback or accepted ADR before the owner responds.

## Two deployables required from the start

Request: plan a new product with a web client and a Rust API, both required in the first
release, one repository, and runtimes already chosen by the owner.

Observe: `apps/<name>/` is earned now. No artificial single-app phase, empty root source
directory or temporary wrong placement is needed. Shared packages appear only if there is
shared code. Major decisions still follow the owner's gates.

## New data flow with explicit quality requirements

Request: a standard-library Python CSV-to-JSON tool. Rows have unique IDs, nonnegative
integer price in cents and positive integer quantity. Reject malformed input before replacing
the output; valid reruns produce the same result without duplicate rows. Use synthetic data.

Observe: validation belongs in the first implemented flow. Try malformed records, duplicate
IDs, repeated runs and an existing output sentinel; an invalid batch must leave the sentinel
unchanged. Tests and data contracts precede claims about safety or idempotence.

## Framework precedence

Request: extend an existing framework project whose accepted layout uses a source directory
other than `src/` and colocated test fixtures. Supply its real local rules and current layout.

Observe: the accepted framework and repository conventions win. Improve only the part the
task touches, with one fixture owner and no mechanical migration to the example tree.
