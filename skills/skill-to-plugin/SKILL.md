---
name: skill-to-plugin
description: Generates a harness plugin from a skill using the local templates in this repo. Use when the user names /skill-to-plugin or asks to package a skill as a plugin for a coding-agent harness.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Skill to plugin

Package a skill as a plugin. The contract is the templates in this repo. Read [templates/README.md](../../templates/README.md) and the matching note in `templates/harness/` before writing files. Copy those templates. Do not invent another manifest layout.

Skill text stays harness-agnostic. The manifest is where a harness differs. Do not put a required agent, model, browser, or product stack into the skill.

## Parse

Accept `/skill-to-plugin` plus a skill directory, and an optional harness name. The text after the command is also a language signal.

- The skill directory must contain `SKILL.md` with `name` and `description`.
- If the user names a harness, generate that harness. Known names are the files in `templates/harness/`.
- If the user does not name a harness, generate every template under `templates/plugin/`.
- If a harness note says to reuse another note in `templates/harness/`, copy that note's files. Do not add a manifest directory the note does not list.
- Ask for an output directory when the user did not name one. Do not overwrite the source skill. Do not invent a publish URL.

## Generate

From this repository:

```bash
node scripts/skill-to-plugin.mjs \
  --skill /absolute/path/to/skill \
  --out /absolute/path/to/plugin \
  --name plugin-name \
  --description "Short description."
```

`--version` is optional. When it is omitted, the script uses `version` from the root `package.json`. Changesets bumps that field and writes `CHANGELOG.md`.

Add `--harness <name>` to limit the copy. Repeat the flag for more than one.

The script copies `templates/plugin/` and fills these tokens: `{{pluginName}}`, `{{displayName}}`, `{{version}}`, and `{{pluginDescription}}`.

To refresh manifests in a checkout that already has `skills/`, pass `--skills-dir` and `--manifests-only`.

## After generation

1. Confirm `package.json` `name` is the plugin name.
2. Confirm each written manifest matches its note in `templates/harness/`.
3. Confirm the skill file was copied and not rewritten.
4. Report the output path and the harness notes you applied.

Do not commit or push unless the user asks.
