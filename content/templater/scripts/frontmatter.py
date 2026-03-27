#!/usr/bin/env python3
"""
Adds front matter to markdown files based on their parent folder name.
Files in a 'sessions' folder get extended front matter with parsed filename fields.

Usage:
    python add_frontmatter.py <root_directory> [--skip] [--dry-run]

Flags:
    --skip      Skip files that already have front matter (default: override)
    --dry-run   Preview changes without modifying any files

Session filename format: ###_<anything>_YYYYMMDD.md
    e.g. 001_the_first_session_20240327.md
"""

import os
import sys
from datetime import datetime


def has_front_matter(content: str) -> bool:
    return content.startswith("---")


def strip_front_matter(content: str) -> str:
    """Remove existing front matter block if present."""
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    if end == -1:
        return content  # malformed, leave as-is
    return content[end + 3:].lstrip("\n")


def parse_session_filename(filename: str) -> dict:
    """
    Parse session number and date from filename.
    Expects first 3 chars to be session number (e.g. '001')
    and last 8 chars before .md to be date in YYYYMMDD format.
    """
    stem = filename[:-3]  # strip .md

    # Session number from first 3 chars
    session_no = stem[:3] if stem[:3].isdigit() else ""

    # Date from last 8 chars
    date_str = stem[-8:]
    try:
        parsed_date = datetime.strptime(date_str, "%d%m%Y").strftime("%Y-%m-%d")
    except ValueError:
        parsed_date = ""

    return {"session_no": session_no, "date": parsed_date}


def make_front_matter(tag: str, filename: str = "") -> str:
    if tag.lower() == "sessions":
        parsed = parse_session_filename(filename)
        return (
            f"---\n"
            f"tags:\n  - {tag}\n"
            f"session: {parsed['session_no']}\n"
            f"date: {parsed['date']}\n"
            f"chapter: \n"
            f"location: \n"
            f"characters: \n"
            f"description: \n"
            f"publish: true\n"
            f"---\n\n"
        )
    return f"---\ntags:\n  - {tag}\npublish: true\n---\n\n"


def process_file(filepath: str, tag: str, skip: bool = False, dry_run: bool = False) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_front_matter(content):
        if skip:
            return "skipped"
        body = strip_front_matter(content)
    else:
        body = content

    filename = os.path.basename(filepath)
    new_content = make_front_matter(tag, filename) + body

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return "updated"


def process_directory(root: str, skip: bool = False, dry_run: bool = False):
    updated = []
    skipped = []
    errors = []

    for dirpath, dirnames, filenames in os.walk(root):
        tag = os.path.basename(dirpath)

        for filename in filenames:
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(dirpath, filename)
            try:
                result = process_file(filepath, tag, skip=skip, dry_run=dry_run)
                if result == "skipped":
                    skipped.append(filepath)
                else:
                    updated.append(filepath)
            except Exception as e:
                errors.append((filepath, str(e)))

    return updated, skipped, errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python add_frontmatter.py <root_directory> [--skip] [--dry-run]")
        sys.exit(1)

    root = sys.argv[1]
    skip = "--skip" in sys.argv
    dry_run = "--dry-run" in sys.argv

    if not os.path.isdir(root):
        print(f"Error: '{root}' is not a valid directory.")
        sys.exit(1)

    if dry_run:
        print("--- DRY RUN — no files will be modified ---\n")

    print(f"Mode: {'skip existing' if skip else 'override existing'}\n")

    updated, skipped, errors = process_directory(root, skip=skip, dry_run=dry_run)

    print(f"Updated : {len(updated)}")
    for f in updated:
        print(f"  + {f}")

    if skipped:
        print(f"\nSkipped : {len(skipped)} (already had front matter)")
        for f in skipped:
            print(f"  - {f}")

    if errors:
        print(f"\nErrors  : {len(errors)}")
        for f, e in errors:
            print(f"  ! {f} — {e}")


if __name__ == "__main__":
    main()