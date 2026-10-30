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

Version and release notes use Changesets. Add a note with `npm run changeset`, then run `npm run version` to update `CHANGELOG.md` and `package.json` `version`. The license is MIT.

Install the skills from this repo:

```bash
npx skills add ploau/engineering-skills
```

`skills.sh.json` only groups the page at [skills.sh/ploau/engineering-skills](https://skills.sh/ploau/engineering-skills). The page appears after an install with telemetry enabled.

## Skills

| Folder | Invocation | Description |
| --- | --- | --- |
| `skills/auto-task/` | `/auto-task` | Turns incoming requests into durable, independently scoped implementation tasks and keeps working until every queued task is complete. |
| `skills/create-agents-md/` | `/create-agents-md` | Writes or updates the short harness agent guide for the open project, capped at 15 concepts. |
| `skills/create-dx/` | `/create-dx` | Organizes the open project so it is easier to read, trace, maintain, and scale. |
| `skills/create-feature/` | `/create-feature` | Builds the feature the user named in the open project, after the project organization step. |
| `skills/create-plan/` | `/create-plan` | Interviews the user and writes an implementation plan for the current request. |
| `skills/git-plan/` | `/git-plan` | Plans the branch, commits, and exclusions for the current change. |
| `skills/improve/` | `/improve` | One-pass analysis of the current plan's feature diff. |
| `skills/record-it/` | `/record-it` | Records a UI flow with the recorder the current harness exposes, into `.recordings/NNN-slug/` (`report.md` plus a video file) on the feature branch that owns the work. |
| `skills/skill-to-plugin/` | `/skill-to-plugin` | Generates a harness plugin from a skill using the local templates in this repo. |
| `skills/stress-it/` | `/stress-it` | Stress-tests the current project's UI in the browser the current harness exposes, then mines the console and the newest project debug or session logs for render loops and runtime errors. |
| `skills/test-it/` | `/test-it` | Creates and executes a real UI test for the current task in the browser the current harness exposes. |
| `skills/writing-review/` | `/writing-review` | Reviews or rewrites technical prose in the language of that prose. |

Chat output follows the user's language. The instruction files stay in English, except the labeled Portuguese and English sections in `writing-review`.

## Package a skill

```bash
node scripts/skill-to-plugin.mjs --skill skills/test-it --out /path/to/plugin
```

Harness notes that have no directory of their own say which files in `templates/harness/` to copy. Do not add a manifest directory that those notes do not list.
