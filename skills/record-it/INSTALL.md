# Recorder setup

`/record-it` uses the recorder the current harness or the current project already exposes. This file is a checklist, not an install of one product.

## 1. Find a recorder

Look, in this order:

1. A recording tool the current harness lists.
2. A project script or documented command that records a browser session.
3. A local recorder the user already installed, if its own help text shows a start and a stop.

If none of those exist, say so and ask. Do not add a dependency as a requirement of this skill.

## 2. Check the recorder's own help

Before the take, confirm the recorder can start, stop, and write a video file. If it can draw a pointer, confirm that flag. If it can paint annotation chrome, confirm you can leave that chrome off.

If the help text is missing the start or stop you need, stop and ask. Do not guess flags.

## 3. Video encoding

If the recorder reports that it needs a system encoder, install the encoder the recorder names, then re-run the recorder's own check. If the recorder does not name one, do not add one.

## 4. Folder

From the skill directory:

```bash
python3 scripts/recording_dir.py your-kebab-slug
```

That prints the absolute `.recordings/NNN-slug/` path and creates `screenshots/`. It does not start a recording.

## 5. Smoke

Run the shortest start, one visible action, and stop that the recorder documents, writing into a temp file. If that fails, report the command and the error, then ask. Do not switch to a different recorder silently.
