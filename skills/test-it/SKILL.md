---
name: test-it
description: Creates and executes a real UI test for the current task in the browser the current harness exposes. Persists results under .tests/ on the feature branch that owns the work, pushes that folder, and never merges .tests/ into main. Use when the user names test-it, /test-it, asks to test a task in a browser, or wants evidence that a requested flow works.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Test It

Create a test from the task being delivered or from the user's explicit test request. Exercise the actual UI the way a user would: navigate, click, type, submit, and confirm behavior. A screenshot alone is not proof.

Use the browser, tab list, and page tools the current harness already exposes. If the harness has no browser, or the browser cannot open the page, say which capability is missing and ask the user how to proceed. Do not invent a second browser, a model, or a product URL.

If the user also names `/record-it`, a recording, or a video of the flow, follow the `record-it` skill for that run. Evidence for a recording goes in `.recordings/NNN-slug/` (`report.md` and the video file), numbered only inside `.recordings/`. Persist that capture with the same branch-local archive rule. Never land it on `main`.

## Parse

Accept `/test-it` plus an optional URL, route, or other instruction. The text after the command is also a language signal.

- If the argument is a URL or route, that is the target.
- If it is empty, test the current project's primary local URL when that URL is already known from the project or a running process. Otherwise ask. Do not invent a URL.
- Derive the test case from the task context: expected UI, actions, assertions, affected routes, and relevant empty or error states.
- If `.tasks/README.md` exists, read it **once** for the default host, viewports, and any stress preservation contract. Do not reread it per case. That file is the auto-task archive, not this skill's evidence folder.
- If `.tasks/` exists, prefer each task folder's `report.md` `## Test cases` checklist as the run list. Run every item (Goal, Task, Passes when). Do not invent extra pages or drop a listed item. If there is no `## Test cases` section, derive cases from the task objective and acceptance criteria.
- After the run, write the test report and screenshots under `.tests/NNN-slug/`. Do not write them into `.tasks/`.

Do not stop after planning. Perform the first concrete browser step in the same turn when a browser is available.

## Start

1. Restate the Goal, Task, and Passes when checklist from `.tasks/NNN-slug/report.md` when that task record exists. Create `.tests/NNN-slug/screenshots/` if it is missing.
2. Discover the browser tools the current harness exposes. If none exist, stop and ask. Name the missing capability.
3. List live tabs before acting. That list is the only authoritative tab source. Ignore a tab id that appears only in conversation context and is absent from the list.
4. If the harness can lock a tab, lock the existing project tab before interacting. Do not spawn an extra tab when one already shows the site. If you must open a tab, open it, then lock it if locking exists, then exercise the flow.
5. Read the page structure with the harness snapshot or accessibility tool, then interact. Confirm behavior, not just appearance.
6. Release the lock only when all browser work for this run is done, and only if a lock was taken.
7. If the same browser action fails, retry it once only when you have new evidence. If it still fails, stop and ask. Do not switch to an unnamed browser.

## Evidence folder

`/test-it` writes `.tests/NNN-slug/report.md` and `.tests/NNN-slug/screenshots/`. The folder README is `.tests/README.md`. Locate the matching task by the current task, the user's argument, or the URL recorded in `.tasks/NNN-slug/report.md`. Do not leave screenshots only in a tool temp directory. Do not copy the test report into `.tasks/`.

1. Read `.tasks/NNN-slug/report.md` when it exists and treat `## Test cases` as the run list.
2. For each item, navigate and interact. Take a screenshot that shows the asserted UI when the harness can capture one.
3. Copy every screenshot into `.tests/NNN-slug/screenshots/` with a kebab-case name that matches the item. If the tool writes to a temp directory, copy that file into the evidence folder before finishing.
4. Write `.tests/NNN-slug/report.md` with the same checklist shape:
   - `[x]` on pass. Leave `[ ]` on fail or skip.
   - Result: `pass`, `fail`, or `skipped`, plus the evidence (URL, observed text, or missing control). Name the browser source the harness actually used.
   - Screenshot: relative path, or empty when the case was skipped or the task has no UI.
5. Include `## Test results` for the latest run: date, source, passed / failed / skipped counts, and a short note.

Do not modify project source from `/test-it`. Only `.tests/` may change. After those writes, follow **Context index** and **Branch-local archive**.

## Context index

The first time this skill creates `.tests/`, before writing any ignore entry, ask in the user's language whether this folder should be indexed in context. Offer two options, recommended first: do not index (recommended), and index. If `.tests/README.md` already records `index`, do not ask again.

Create `.tests/README.md` if it is missing. YAML front-matter includes `index: true` or `index: false`, and `created` as a date. Write the body in the user's language. Include a table of links to each report this skill wrote, with columns Path, Title, and Date. Each later run updates that table. Do not copy a report into the README.

If the user declines indexing (`index: false`), exclude the folder from context indexing only. When the harness is Cursor, add `.tests/` to `.cursorindexingignore` at the git repo root. Create that file if it is missing. Do not add the folder to `.cursorignore`. `.cursorindexingignore` keeps the folder out of the semantic index and automatic context. The agent can still read and update the files by path. `.cursorignore` blocks agent reads. That would break the next run, which must open `.tests/README.md` and the reports by path. Never ignore the whole repo. Only `.tests/`.

This run does not need the index. You just wrote the files and still have that content in the conversation. Write the report anyway. Later runs open the README and the report by path. Do not skip the report because the folder is unindexed.

If the user approves indexing (`index: true`), do not add an ignore entry. The front-matter records the approval. If a previous ignore entry for `.tests/` exists, remove only that entry.

If the harness is not Cursor, ask which index-ignore file the project already uses. Do not invent a second ignore mechanism. If the user declined indexing and no such file exists, record `index: false` and tell the user no index-ignore file was found, so nothing was excluded. Do not create `.cursorignore`.

## Branch-local archive (required)

`.tests/` results live **on the branch where the work happens**. They are not product source. Never land `.tests/` or `.recordings/` on `main` or `master`.

1. Resolve the git repo that owns the work. All `.tests/` paths are relative to that repo. Prefer the matching folder on the current feature branch. Do not drain another branch's queue.
2. If `HEAD` is `main` or `master`, do not commit there. Create or check out a feature branch first (`feat/…`, `fix/…`, `improve/…`). If the user already named a branch, use it.
3. After writing `.tests/NNN-slug/report.md` and copying screenshots, stay on that branch, `git add .tests/`, commit `chore(tests): test NNN-slug`, and push (`git push -u origin HEAD`) when a remote exists. Leave `origin/<branch>` in place. If no remote exists, say so and do not invent one.
4. Do not mix screenshots into a product commit unless the user asked for a single commit. Do not commit secrets or unrelated dirty product files.
5. When landing the feature, stage product paths only. Unstage `.tests/` and `.recordings/` if they sneak into the index. After the land, delete the local feature branch only. Keep the remote so the test record stays inspectable.

`main` may show untracked `.tests/`. Leave it untracked or check it out on the feature branch. Never `git add .tests/` on `main`.

## Guidelines

- Keep the full test objective intact across turns. Release a lock only when the session is finished, not between every click.
- Temporary rough edges in the site are findings, not reasons to abandon the test.
- An attached view id from conversation context is not authoritative. The harness tab list is the source of truth.
- If layout changed, check representative desktop and mobile viewports when the browser tools allow it.
- If verification finds a product bug, record it. Do not redefine success as "the screenshot loaded."
- Exercise the main affected flow end to end. Check related routes that share state. Probe empty and error states when the change could affect them.
- Prefer a short poll of the page over a single long wait. Do not get stuck in wait-action-wait loops.
- Do not run a request-only probe as a substitute for the requested UI test when the harness has a browser.

## When the browser is missing or blind

Stop and ask, in the user's language. Say which tool you looked for and what you found. Ask the user to open the page in the browser surface this harness controls and keep it active. If that surface already shows the page and the tool still cannot see it, ask them to restart the harness session. Do not claim the flow passed.

## Completion audit

Treat completion as unproven until interaction evidence from the harness browser proves it. Name that source.

- For every checklist item, identify what rendered behavior would prove it, then inspect the page and perform the interaction.
- Write the outcome back into that item: checkbox, Result, and Screenshot path.
- A screenshot alone is not verification. The file in `screenshots/` supports the Result. It does not replace the click, submit, or navigation.
- Intent, partial navigation, or a successful lock is not proof the UI works.

Mark the test complete when every requested flow was exercised, every checklist item has a Result in `.tests/NNN-slug/report.md`, screenshots for executed UI cases are in `.tests/NNN-slug/screenshots/`, the evidence source is named, and the updated `.tests/` folder is committed on the feature branch. Push when a remote exists. If the browser cannot run the flow, stop and ask instead of claiming completion.
