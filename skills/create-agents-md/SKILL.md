---
name: create-agents-md
description: Writes or updates the short harness agent guide for the open project, capped at 15 concepts. Use when the user names /create-agents-md, or when the user states a request or decision that changes how the agent should work in this project.
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Agent guide

Write the harness agent file for the open project. The file is a basic agent guide, not a second spec. Keep it short. Cap it at 15 concepts. Use clear, objective sentences aimed at the agent. Do not copy the chat into the file.

## Which file

- When the harness uses `CLAUDE.md`, write that.
- When the harness uses `AGENTS.md`, write that.
- When the project already has one of those files, update that file.
- When the harness and the project do not determine the name, ask once. Recommend `AGENTS.md`.

Use the question tool the current harness exposes. If that tool is missing, ask in chat.

## Stack patterns

Read the stack that is actually in the project. Add a few patterns that prevent slop in that stack. Do not force a stack the project does not use.

These lines are examples of the style, not a required stack. In a project that already uses React, say to avoid ternary hell. In a project that already uses Tailwind, say not to create constants of class strings unless a constant is actually needed. When the project uses neither, write the equivalent rule for the stack you found.

## Auto-improve

When the user states a request or a decision that changes how the agent should work in this project, update this file. Before adding a concept, remove or merge an older one so the file stays at or under 15 concepts. Prefer editing an existing line over appending.
