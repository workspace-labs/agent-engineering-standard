# An engineering standard for AI agents

**AI agents can build software that works today and is painful to change next month. A better prompt doesn't fix that. A standard the agent follows from the first file does.**

This is that standard, packaged as an Agent Skill. It makes structure, clear ownership, tests, documentation and Git hygiene part of the build instead of a clean-up job for later — and it scales down, so a small project stays small.

It is tool-agnostic. Nothing here depends on a particular model, CLI, or framework.

The skill is in this repo — [`skills/`](skills).

---

## In practice

![How a builder agent works under the standard: the board around it, its eight steps, the folder it leaves behind, and the rules it keeps](media/how-i-build-a-new-project.png)

*The standard at work on the author's own board. One agent plans, one writes the exam and reviews the code, one builds — and a person holds every gate.*

---

## What it asks of an agent

- **Size the work first.** A typo gets the smallest safe change. A new project gets its requirements, a map of its parts, a data model and a test plan before the first feature.
- **Give every job one home.** No god files. Product rules stay out of the screens and the storage.
- **Build the tests and the docs with the code**, not after it.
- **Don't over-engineer.** No layer, interface, framework or folder without a real problem it solves.
- **Leave the big calls to the owner.** Replacing the architecture, changing how data is stored, or anything that could lose data waits for a person.

---

## Use it

One line, for every project on your machine:

```bash
npx skills add workspace-labs/agent-engineering-standard -g
```

Or clone it and copy the whole skill folder by hand:

```bash
git clone https://github.com/workspace-labs/agent-engineering-standard.git
```

Choose the user skill location for your agent, following its current documentation. For
Codex, the documented user location is `~/.agents/skills/`; Claude uses `~/.claude/skills/`:

```bash
skill_root="$HOME/.agents/skills"        # Codex
# skill_root="$HOME/.claude/skills"      # Claude: use this instead
```

Then copy into a new destination. This refuses an existing folder or symlink, so an update
cannot silently mix old and new reference files. Back up an existing installation before
replacing it through your normal update workflow.

```bash
skill_source="agent-engineering-standard/skills/software-engineering-build-standard"
skill_target="$skill_root/software-engineering-build-standard"
if [ -e "$skill_target" ] || [ -L "$skill_target" ]; then
  printf '%s\n' "Already exists: $skill_target. Back it up before updating." >&2
  false
else
  mkdir -p "$skill_root" && cp -R "$skill_source" "$skill_target"
fi
```

The bundled `agents/openai.yaml` supplies optional interface metadata; it is not required
for skill discovery. See [the official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
for discovery locations and metadata.

Agents can choose it when they build, extend, restructure or review software, or you can
invoke it explicitly as `$software-engineering-build-standard`. The entry point is
[`SKILL.md`](skills/software-engineering-build-standard/SKILL.md), with five main reference
guides and [staged examples for ten project types](skills/software-engineering-build-standard/references/trees/README.md).
The [layout map](skills/software-engineering-build-standard/references/layout-map.md) gives
each piece's *due at* trigger, so nothing is created before the product earns it. A project's
own rules, recorded decisions and the owner's instructions always come first.

## Test it

From the repository root, run the offline package checks with Python 3.9 or newer:

```bash
python3 -B -m unittest discover -s tests -v
```

The checks cover metadata limits, all bundled links, reference reachability, the tree
chooser, starter-kit and source-root consistency, and rule citations. They use only the
standard library and do not install or execute the skill. The metadata checks cover this
package's simple YAML string fields; use an Agent Skills YAML validator as well if you
change that representation.

Instruction quality also needs [realistic agent exercises](tests/behavioral-cases.md).
Run those in isolated fixtures, inspect the actual files and command results, and distinguish
tested behavior from anything the environment could not verify. Package checks passing
alone do not prove that every agent will select or follow the skill correctly.

---

## What it costs

- **Slower first steps.** A new project spends its opening on a map, a data model and a test plan instead of features.
- **More questions for the owner.** Big decisions wait for a person, and some of those waits will feel slow.
- **It can't rescue a bad idea.** A standard shapes how something is built, not whether it was worth building.

**Worth it when:** the software has to outlive the week, or more than one agent or person will change it.

**Not worth it when:** it's a throwaway prototype. The standard itself says to keep those minimal.

---

## The shortest version

> Never build first and organize later. Give every piece a home, a check and a note from the first file — and keep it no more complicated than the product needs.

---

<sub>by Workspace Labs · Drawn from a working system, not a thought experiment — see <a href="https://github.com/workspace-labs/workspace">a showcase of it running</a>, and the patterns beside it: <a href="https://github.com/workspace-labs/agent-builder-handoff">a builder handoff for AI agents</a>, <a href="https://github.com/workspace-labs/agent-health-checks">health checks for AI agents</a> and <a href="https://github.com/workspace-labs/agent-separation-of-duties">separation of duties for AI agents</a>.</sub>
