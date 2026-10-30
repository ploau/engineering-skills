---
name: git-plan
description: Plans the branch, commits, and exclusions for the current change. A release version bump is one commit in that plan and is carried out by /create-release. Use when the user names /git-plan or asks for a commit plan. Does not commit or push unless the user asks.
disable-model-invocation: true
---

## User language

Chat replies, and the prose of any report this skill writes, use the user's language. Infer that language from the conversation, or from the text after the command. Keep each paragraph of that output in one language. When this skill names a heading that another skill has to find, keep that heading text as specified and write the body in the user's language. The instructions in this file stay in English.

# Git Plan

Plan the git work for the current change. The text after the command is also a language signal. This skill plans. It does not commit, push, switch branches, or edit git config unless the user asks for that action. Never force-push.

Read the current branch, status, and diff in the repo that owns the change. Propose a feature branch when `HEAD` is the default branch. If a feature branch is already checked out, keep it.

## Commits

List commits in the order the domains were built. One domain per commit. Title only, no long body. Technical English. At most 72 characters.

```text
<type>(<scope>): <short message>
```

Types: `feat`, `fix`, `refactor`, `perf`, `chore`, `docs`, `test`.

Scope is required. Take it from a domain in this change (a route, a module, a package). Do not reuse a scope list from another project.

## Stays out

Name the paths that stay out of these commits: secrets, unrelated dirty files, and any path the user excluded. Say why each one stays out.

## Checklist

Before any commit the user later asks for, confirm the scope matches the diff, the type matches the change, the title is technical English within 72 characters, the order follows how the change was built, and each domain is its own commit.

Write the plan in chat unless the project already has a place for it. Do not invent a path.

## Release

When the change includes a release, list one commit for the version bump: type `chore`, scope `release`, title `chore(release): version X.Y.Z`. That commit stays on the branch being released. Do not propose a feature branch for it.

Name what stays out of that commit, same as any other domain. Do not apply `.changeset/` notes, create the tag, or push the release from this skill. Follow [create-release](../create-release/SKILL.md) for those steps when the user invokes `/create-release`.
