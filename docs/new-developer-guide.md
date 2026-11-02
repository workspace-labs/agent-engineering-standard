# New to building software? Start here

You do not need to choose the folders before you know what your project needs.
This skill gives your coding agent instructions for building carefully and explaining the important choices.

## Use it with your agent

[Install the skill using the README's “Use it” instructions](../README.md#use-it), then describe what you want.
Tell the agent you are new. It picks a suitable project structure and explains why each part is needed.
For example: “I'm new to coding. Make me a small website where people can book an appointment.”
Answer the few questions that affect the build, such as who will use it and what information it must save.

## A few words your agent may use

- **API:** an agreed way for one program to ask another program for information or an action.
- **Backend:** the part running on a server, a computer serving requests rather than the visitor's device.
- **Frontend:** the screens and controls people use, such as the part of a website running in their browser.
- **.env:** a local settings file; private values belong outside the shared project history and browser code.
- **Commit:** a named checkpoint of selected project changes saved with Git, a tool that keeps change history.
- **Test:** a repeatable check that compares what the software does with what it should do.
- **Migration:** a planned change to the way existing saved information is arranged or stored.
- **ADR:** an architecture decision record, a short note explaining an important design choice and its trade-offs.

## The 10 mistakes that hurt new projects most

### 1. Putting an API key inside the app or website

What goes wrong: a key is like a password for a service; people can extract one included in the files they receive.
Instead: your agent keeps the project's key on the server and sends requests there from the app.
It keeps private settings out of shared history and explains where the key lives. [§69]

### 2. Putting everything in one giant file

What goes wrong: unrelated jobs become tangled, so changing one thing can break another.
Instead: your agent gives different responsibilities clear homes; it does not split a file just to make it shorter. [§7]

### 3. Building without tests

What goes wrong: a change can silently break something that used to work.
Instead: your agent adds repeatable checks as it builds, organized around the behavior they prove.
It uses small, fast checks where enough and checks whole user journeys where needed. [§15, §74]

### 4. Keeping no history, or saving everything in one huge commit

What goes wrong: nobody can tell which change caused a problem or recover a known working starting point.
Instead: your agent keeps the real project in Git and saves focused checkpoints when commits are authorized.
Each commit explains one coherent change; passwords and personal records stay out of history. [§18, §55]

### 5. Changing saved information with no plan or recovery copy

What goes wrong: an update works on a new install but damages information people already saved.
Instead: your agent checks the existing information, plans the change and preserves a way to recover it.
It tests normal and broken records and repeated runs before claiming the change is safe. [§43]

### 6. Collecting personal information carelessly

What goes wrong: names, email addresses or phone numbers are saved without a clear need or a way to delete them.
Instead: your agent collects only what is needed and writes down why, where it is kept and who can see it.
It defines how long to keep it and provides a working deletion path, considering backup copies too. [§80]

### 7. Leaving screens blank while loading or after a failure

What goes wrong: people cannot tell whether the app is busy, has nothing to show or has stopped working.
Instead: your agent handles waiting, empty results, failure and success for information fetched from a server.
When something fails, the screen explains what the person can do next. [§71]

### 8. Adding libraries without thinking

What goes wrong: borrowed code, called a library, can add maintenance work and security risks without enough benefit.
Instead: your agent checks whether existing tools are enough and weighs upkeep, safety, size and removal costs.
It uses outside code when justified, especially instead of inventing sensitive security code. [§47]

### 9. Building too much too early

What goes wrong: unused folders, services and features make a small project hard to understand.
Instead: your agent creates only the parts needed for the work you have actually agreed to build.
New structure arrives when it solves a real problem. [§22]

### 10. No README map or settings list, so nobody can take the project over

What goes wrong: a new person cannot find the code or learn which settings are needed without the original builder.
Instead: your agent grows the README, the project's starting guide, with run steps, a map of the real code and a settings list.
The list points to `.env.example`, an example settings file, and explains each setting and where to get its value, never the value itself. [§19, §85]

## Taking over someone else's project

Before adding features, your agent reads the code and repairs the README map and run steps.
It lists needed settings and asks you for real values; it never guesses passwords or copies them from old records or other machines.
It records gaps and known problems honestly, without making up past changes.
A confusing folder layout earns a finding and a proposed small, approved repair, not an automatic rebuild. [§86]

## See a first project take shape

Read the [first-project walkthrough](first-project-walkthrough.md) for an example conversation.
It shows the questions, first files, a tested feature and a short explanation of what was set up and why.
