# Stress-it log patterns

Generic signals first. Discover paths from the project that is open.

## Console

Do not assume a host scanner component. If the page exposes a scanner API, the skill may enable logging for the run and restore it afterward. If the API is missing, the console wrap still keeps lines that match the filters in `SKILL.md`.

Keep versus drop:

- Keep: maximum update depth, too many re-renders, uncaught errors, and scanner lines that name an application component during idle or one gesture.
- Drop as a product bug: a notice that a scanner dependency is outdated. That is a pin, unless it coincides with a loop.

## Debug or session logs

Discover the newest ingest or session log in the current project. List by mtime. Read only that file. Tail it. If none exist, say so.

Common layouts are signals, not requirements:

- a project debug directory of structured logs
- another ingest path the project already documents

Loop smells, whatever the logger calls them:

- the same message or dedupe key with an exploding deduped count
- tick, camera, fit, rehydrate, or overlay messages with no following idle
- counts that never stabilize

Do not open older log files. Do not ingest an editor debug log wholesale.

## Maximum update depth and source

Minified UI runtimes often look like an animation-frame coalesced state update:

```js
flag.current || (flag.current = requestAnimationFrame(() => {
  flag.current = 0, setN((n) => n + 1);
}));
```

Search the package that owns the UI under test for an animation frame plus an increment (overlays, transform listeners, layout bumps). A transform or scroll event that fires on every paint is a usual cause.

Search with line numbers, then read with a limit. Do not dump hub files whole.
