# Recorder references

The source of truth for flags is the recorder that is actually available in this session.

1. Read the help text or docs that the harness tool, the project script, or the installed recorder provides.
2. Follow that recorder's start, stop, pointer, and viewport rules.
3. If two recorders are available, use the one the user named. If the user did not name one, use the one the harness exposes, and say which one you used.

Do not treat a screenshot tool as a recorder. Do not copy a recorder's helper scripts into `.recordings/`.

The folder allocator is `scripts/recording_dir.py`. It only chooses `.recordings/NNN-slug/`.
