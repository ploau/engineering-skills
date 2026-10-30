---
name: create-release
description: Plans the release commits, writes Changesets notes, applies them to the changelog and version, creates the git tag, and pushes that commit and tag. Use when the user names /create-release or asks to release this repo. Does not publish a package.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Create release

Release this repository. The text after the command is also a language signal. Invoking `/create-release` authorizes the commits below, one git tag, and the push of those commits and that tag. It does not authorize a force push, a git config change, or a package publish.

Run from the git root that contains `.changeset/config.json`. If that file is missing, stop. Stay on the branch being released. Do not open a feature branch for the version commit.

Follow [git-plan](../git-plan/SKILL.md) for every commit. Pass the author and committer with `git -c` on each commit. Do not write git config. One domain per commit. Title only, technical English, at most 72 characters. Do not hand-edit `version` in `package.json`.

## Plan

List the commits in this order. Product commits come first and must not touch `version` or `CHANGELOG.md`. The note commit contains only new `.changeset/*.md` files. The version commit contains only what `npm run version` changed.

```text
<type>(<scope>): <short message>
chore(changeset): note <what shipped>
chore(release): version X.Y.Z
```

Secrets, lockfiles that the version command did not change, and unrelated dirty files stay out. Say why.

## Notes

Pending notes are the `.md` files in `.changeset/` other than `README.md`. If none describe what is about to ship, write one. The package name is `name` in the root `package.json`. Pick patch, minor, or major from what shipped since the last `CHANGELOG.md` section. The body is the release note, not a copy of `git log`.

Commit only those new note files:

```text
chore(changeset): note <what shipped>
```

## Version

1. Run `npm run version` from the repo root. It consumes the pending notes, updates `CHANGELOG.md`, and sets `version` in `package.json`.
2. Read the new version. The tag is `v` plus that version.
3. You may polish the generated changelog prose. Do not edit `version` by hand.
4. Commit only the files that command changed:

```text
chore(release): version X.Y.Z
```

## Tag

Run `npx changeset git-tag`. Confirm `vX.Y.Z` exists locally. If the package is already tagged, stop and do not push.

```bash
git push origin HEAD
git push origin vX.Y.Z
```

Do not use `--force` or `--tags`. Do not run `changeset publish`.

## After

Report the version, the commit hashes, the tag, and the remote branch. If the push fails, leave the local commit and tag in place and quote the error.
