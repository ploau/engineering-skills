---
name: create-plan
description: Interviews the user and writes an implementation plan for the current request. Use when the user names /create-plan or asks for an implementation plan of this feature.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Create Plan

Interview the user until the answers support an implementation plan for the current request. The text after the command is also a language signal.

State what the plan will do, in clear language. The plan has two parts, both in the user's language: a product summary a non-engineer can read, and an engineering summary for execution.

Scope the plan to this feature only. Other dirty files in the repo are not the plan.

Use the question tool the current harness exposes. If that tool is missing, ask in chat. Keep asking until a missing answer would no longer change the plan.

## Where the plan goes

Look for a plan file or a plans directory the project already uses. If one exists, write the plan there. If none exists, ask where to put it. Do not invent a path.

## Proof before done

Before calling the plan done, run the same proof `/improve` runs on the packages this feature touches:

- The typecheck command the project already defines, when it has one.
- Tests, when the project already has them.
- Package exports, prebuild, and build output that the host imports, when this feature ships those.
- A search for symbols this feature deletes or renames.
- The host process the project already uses to serve the feature. Quote compile failures and missing-module errors.

A plan that treats a local URL as ready while that host is failing is incomplete. Do not skip the host because page files are absent from the feature diff. If the project has no command for a row, record that and do not invent one.
