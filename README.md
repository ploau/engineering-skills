# engineering-skills

Harness-agnostic skills for the project that is open and the harness that is already running. Skill files describe the outcome and the evidence. They do not require a named agent, model, browser, or product stack.

The file map is [templates/README.md](templates/README.md).

## Layout

```text
skills/<name>/SKILL.md
templates/plugin/          filled manifests
templates/harness/         one note per harness
scripts/skill-to-plugin.mjs
```

`package.json` `name` is `engineering-skills`. Per-harness manifests use the same name and point at `skills/`.

## Skills

| Skill | Invocation |
| --- | --- |
| auto-task | plan and finish every task under `.tasks/` on the feature branch |
| improve | evidence battery on this plan, then apply no-risk polish |
| test-it | `/test-it` exercises the UI in the harness browser |
| record-it | `/record-it` records with the harness recorder |
| stress-it | `/stress-it` provokes UI failures and writes `.stress/` |
| writing-review | `/writing-review` reviews prose in the language of the text |
| skill-to-plugin | `/skill-to-plugin` builds a plugin from a skill |

Chat output follows the user's language. The instruction files stay in English, except the labeled Portuguese and English sections in `writing-review`.

## Package a skill

```bash
node scripts/skill-to-plugin.mjs --skill skills/test-it --out /path/to/plugin
```

Harness notes that have no directory of their own say which files in `templates/harness/` to copy. Do not add a manifest directory that those notes do not list.
