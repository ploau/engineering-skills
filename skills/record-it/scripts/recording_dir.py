#!/usr/bin/env python3
"""Pick the folder for one /record-it capture and print its absolute path.

Layout (repo root, not under .tasks/):

    .recordings/
      001-first-flow/
        report.md
        session.webm
        screenshots/

Numbering lives only inside `.recordings/`. The first capture is 001. A
slug that already has a folder is reused. A new slug is (highest NNN) + 1.

Usage:
    recording_dir.py [--root DIR] [--print-only] [NNN-slug | kebab-slug]

Env:
    RECORD_IT_ROOT   repo root when --root is omitted
    RECORD_IT_SLUG   name when no positional argument is given
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

# Parent of every capture: <repo>/.recordings/
RECORDING_ROOT_NAME = ".recordings"

# "019-hero-five-properties" — three digits, hyphen, kebab-case slug
NUMBERED_FOLDER_PATTERN = re.compile(
    r"^(?P<number>\d{3})-(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)

# "hero-five-properties" — slug only, we assign the next number
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve .recordings/NNN-slug/ for a /record-it run."
    )
    parser.add_argument(
        "--root",
        default=os.environ.get("RECORD_IT_ROOT", ""),
        help="Git/repo root. Default: RECORD_IT_ROOT, else git toplevel, else cwd.",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print the path but do not create the capture folder or screenshots/.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default=os.environ.get("RECORD_IT_SLUG", ""),
        help="Existing NNN-slug, or a kebab slug to allocate/reuse.",
    )
    return parser.parse_args(argv)


def find_repo_root(explicit_root: str) -> Path:
    """Prefer an explicit root, then `git rev-parse --show-toplevel`, then cwd."""
    if explicit_root:
        return Path(explicit_root).expanduser().resolve()

    git = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    if git.returncode == 0:
        return Path(git.stdout.strip())

    return Path.cwd().resolve()


def list_numbered_captures(recording_root: Path) -> dict[str, int]:
    """Map folder name -> NNN for each existing `.recordings/NNN-slug/` child."""
    captures: dict[str, int] = {}
    if not recording_root.is_dir():
        return captures

    for child in recording_root.iterdir():
        if not child.is_dir():
            continue
        match = NUMBERED_FOLDER_PATTERN.match(child.name)
        if match:
            captures[child.name] = int(match.group("number"))
    return captures


def slug_from_numbered_folder(folder_name: str) -> str:
    """'001-hero-five-properties' -> 'hero-five-properties'."""
    return folder_name.split("-", 1)[1]


def next_capture_number(existing_captures: dict[str, int]) -> int:
    if not existing_captures:
        return 1
    return max(existing_captures.values()) + 1


def resolve_capture_folder_name(requested_name: str, existing_captures: dict[str, int]) -> str:
    """Turn a user/agent name into `NNN-slug`."""
    numbered_match = NUMBERED_FOLDER_PATTERN.match(requested_name)
    if numbered_match:
        return requested_name

    if not SLUG_PATTERN.match(requested_name):
        raise SystemExit(
            "recording-dir: name must be kebab-case (hero-five-properties) "
            f"or NNN-slug (001-hero-five-properties), got {requested_name!r}"
        )

    folders_for_this_slug = sorted(
        folder_name
        for folder_name in existing_captures
        if slug_from_numbered_folder(folder_name) == requested_name
    )
    if folders_for_this_slug:
        # Recapture: keep the same number so takes overwrite in place.
        return folders_for_this_slug[-1]

    number = next_capture_number(existing_captures)
    return f"{number:03d}-{requested_name}"


def ensure_recording_layout(capture_dir: Path, *, print_only: bool) -> None:
    """Create `.recordings/` always; create the capture + screenshots unless print-only."""
    recording_root = capture_dir.parent
    recording_root.mkdir(parents=True, exist_ok=True)
    if print_only:
        return
    (capture_dir / "screenshots").mkdir(parents=True, exist_ok=True)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    requested_name = args.name.strip().strip("/")
    if not requested_name:
        print(
            "recording-dir: pass NNN-slug, a kebab slug, or set RECORD_IT_SLUG",
            file=sys.stderr,
        )
        return 2

    repo_root = find_repo_root(args.root)
    recording_root = repo_root / RECORDING_ROOT_NAME
    existing_captures = list_numbered_captures(recording_root)
    capture_folder_name = resolve_capture_folder_name(requested_name, existing_captures)
    capture_dir = recording_root / capture_folder_name

    ensure_recording_layout(capture_dir, print_only=args.print_only)
    print(capture_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
