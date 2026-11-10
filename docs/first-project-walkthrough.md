# Your first project: an appointment website

**This is an example conversation, not a script or folder template to copy.**
The checks and results described are illustrative; this page does not record an executed build.
Your agent should adapt to your answers and the tools your project already uses.

**Person:** "I'm new to coding. Make me a small website where people can book an appointment."

**Agent:** "This is a new project, so I'll establish its small starting structure first.
Who will use it? Will it collect names, phone numbers or other personal information?
Where should the first version run?"

**Person:** "Eventually customers will book appointments. For this first step, only I will
try it on my laptop with made-up times. Don't collect anyone's details yet.
Our chosen tools are a browser and JavaScript, with Node.js already available to run checks."

**Agent:** "I propose a local practice page: choose an available time and see your selection.
It will not reserve a real appointment or share bookings between people. That remains the
goal for a later agreed step, when we choose how to run the shared service and keep bookings.
JavaScript is the language that makes the page respond; Node.js runs checks outside the browser.
This first step needs no extra code packages or code-conversion step. Is that first step right?"

**Person:** "Yes, build that practice page with those tools. After the checks pass, make
the first local commit, but don't publish anything."

**Agent:** "I'll use the [webapp example](../skills/software-engineering-build-standard/references/trees/webapp.md)
from the [project chooser](../skills/software-engineering-build-standard/references/trees/README.md).
It fits because people interact with the page, rather than only read it. It can start as one
browser app; a separate service is not needed for our agreed practice page."

**Agent:** "The [day-one map](../skills/software-engineering-build-standard/references/layout-map.md#day-one)
starts with exactly these six pieces. Each has a job now:"

```text
appointments/
  README.md        what this project does and how to run it
  CHANGELOG.md     what changed in each version
  .gitignore       what Git must leave out, including private settings and files tools make
  docs/scope.md    what we will build, what we will leave out and how we will check it
  src/             the website's code
  tests/           checks that show whether the code behaves as intended
```

**Agent:** "Git keeps a history of the project's files. A commit is a named saved point
in that history. I'll keep personal information out of it."

**Agent:** "Now the first feature earns a few additions; these are not extra day-one pieces:"

- `src/app/bootstrap/` starts the first screen, so it is needed when that screen arrives.
- `src/features/appointments/` owns appointment selection now that the feature has several files.
- `docs/design.md` records the first screen's agreed layout, readable text and visible keyboard focus.
- `AGENTS.md` records run and check instructions now that this has grown past the starting kit.
- `docs/architecture/boundaries.md` says where each responsibility lives, also due past the kit.
- `docs/architecture/overview.md` explains how the screen and selection code talk to each other.
- `tests/fixtures/` holds the made-up appointment times needed by the checks.
- `scripts/test/` holds the command that runs the code checks, now that there is one to run.
- `tests/e2e/` holds a browser check of the complete selection flow, now that a person can finish it.

**Agent:** "'e2e' means checking a whole flow from beginning to end. The selection rule stays
outside the screen-starting code, so a check can exercise it directly. We need no extra app,
shared code folder or stored booking records for this step."

**Person:** "What happens when we ask for customers' names and phone numbers?"

**Agent:** "Before we collect or process those details, I must add `docs/privacy.md`
under [the personal-data rule](../skills/software-engineering-build-standard/references/team-and-lifecycle.md#80-privacy-and-the-data-lifecycle).
It will say what we collect and why, who can read it, how long it stays and how to delete it.
Our practice page has no contact fields or real customer records, so that file is not due yet."

**Agent:** "I'll write the selection rules in `docs/scope.md` as plain sentences: only an available time can be selected, and an empty selection cannot continue."

**Agent:** "Two people choosing the same time is another case to consider, but it cannot happen on this practice page because nothing is saved or shared. There is nothing to build or test for that case yet."

**Agent:** "When we plan the shared booking service, I'll raise that case with you and ask what we promise a customer."

**Agent:** "I'll first check the selection rule with made-up times: an available time works,
an unavailable time is rejected, and an empty selection cannot continue. The first check
fails before the rule exists; then I write the rule and run the checks again."

**Agent:** "The rule checks now pass. I connected the page and tried the complete flow:
choose a time, see the same time in the result, then choose another. The result says
'Practice selection only — no appointment reserved.' Refreshing clears it because this
step does not save bookings. I also tried no selection and no available times."

**Agent:** "The controls work by keyboard with a visible focus mark, and each control has a
clear label. I checked the page with an accessibility tool too, to look for barriers to use.
This page asks no other computer for data, so it needs no waiting or connection-error screen."

**Person:** "Can I show this to customers as the booking website?"

**Agent:** "It is ready to review as the practice step you approved. Customers still cannot
make a real reservation. A shared booking service needs an agreed plan for storage, access
and protecting their details before we build that next part."

**Agent:** "The README now shows how to run it and where the existing parts live:"

```markdown
# Appointment-selection practice
A local page for trying the booking interaction; it does not reserve real appointments.

## Run it
1. Open src/app/bootstrap/index.html in your browser.
2. Choose a made-up time; the result is a practice selection, not a reservation.

## Project map
- Browser screens: src/app/bootstrap/
- Appointment selection: src/features/appointments/
- Checks: tests/; the whole-flow browser check is in tests/e2e/
- Instructions and design notes: docs/

## Settings
No settings are read in this first slice. Add .env.example and describe each setting here
when the code first reads one. Never write a real private value into these instructions.

See CHANGELOG.md for changes; docs/design.md and docs/architecture/boundaries.md explain
the current screen and code organization. Add docs/adr/ decision records when a major choice earns them.
```

**Agent:** "I updated the run instructions, the limits in `docs/scope.md` and the change
record. I checked the changed files for private details and unintended additions, ran the
checks, and made the local commit you authorized: 'Add local appointment-selection practice'.
Nothing was published."

**Agent — What I set up and why**

- A small appointment-selection page, so you can review the interaction before a shared service.
- Direct rule checks and a whole-flow browser check, so mistakes are easier to catch as it grows.
- Run instructions, responsibility notes and a saved history point, so the next change has a clear start.
- An explicit practice-only limit, so nobody mistakes a demonstration for a real booking.

Next, you review this first step and decide whether to proceed with real booking.
