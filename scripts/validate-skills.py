#!/usr/bin/env python3
"""Validate the repository's skill packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
MUTABLE_CONFIG_FILES = {"MODEL_INVENTORY.md"}


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(frontmatter)
    if match is None:
        return None

    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def metadata_value(metadata: str, key: str) -> str | None:
    pattern = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(metadata)
    if match is None:
        return None

    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def metadata_references(metadata: str) -> list[str]:
    references: list[str] = []
    in_references = False

    for line in metadata.splitlines():
        if re.match(r"^\S", line):
            in_references = line.strip() == "references:"
            continue

        if not in_references:
            continue

        match = re.match(r"^\s+-\s*(.+?)\s*$", line)
        if match is None:
            if line.strip():
                in_references = False
            continue

        value = match.group(1).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        references.append(value)

    return references


def validate_agents_openai(skill_dir: Path, metadata: str) -> list[str]:
    errors: list[str] = []

    if re.search(r"^interface:\s*$", metadata, re.MULTILINE) is None:
        errors.append("agents/openai.yaml missing top-level interface")

    for key in ("display_name", "short_description", "default_prompt"):
        if re.search(rf"^\s+{key}:\s*.+$", metadata, re.MULTILINE) is None:
            errors.append(f"agents/openai.yaml missing interface.{key}")

    entry = metadata_value(metadata, "entry")
    if entry != "SKILL.md":
        errors.append('agents/openai.yaml entry must be "SKILL.md"')

    references = metadata_references(metadata)
    for reference in references:
        if reference in MUTABLE_CONFIG_FILES:
            errors.append(f"agents/openai.yaml references mutable config {reference!r}")
            continue

        reference_path = Path(reference)
        if reference_path.is_absolute() or ".." in reference_path.parts:
            errors.append(f"agents/openai.yaml reference {reference!r} must be a relative path inside the skill")
            continue

        target = skill_dir / reference_path
        if not target.is_file():
            errors.append(f"agents/openai.yaml reference {reference!r} must point to an existing file")

    if skill_dir.name == "sounder" and "references/model-inventory.md" not in references:
        errors.append("agents/openai.yaml must reference references/model-inventory.md")

    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    license_file = skill_dir / "LICENSE.txt"
    agents_openai = skill_dir / "agents" / "openai.yaml"

    if not SKILL_NAME_RE.fullmatch(skill_dir.name):
        errors.append("directory name must be lowercase letters, digits, or hyphens")

    if not skill_md.is_file():
        errors.append("missing SKILL.md")
        return errors

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append("SKILL.md frontmatter must end with ---")
        else:
            frontmatter = text[4:end]
            name = frontmatter_value(frontmatter, "name")
            description = frontmatter_value(frontmatter, "description")

            if not name:
                errors.append("SKILL.md frontmatter missing name")
            elif name != skill_dir.name:
                errors.append(f"SKILL.md name {name!r} must match directory {skill_dir.name!r}")
            elif not SKILL_NAME_RE.fullmatch(name):
                errors.append("SKILL.md name must be lowercase letters, digits, or hyphens")

            if not description:
                errors.append("SKILL.md frontmatter missing description")

    if not license_file.is_file():
        errors.append("missing LICENSE.txt")

    if agents_openai.exists():
        metadata = agents_openai.read_text(encoding="utf-8")
        errors.extend(validate_agents_openai(skill_dir, metadata))

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    skills_dir = repo_root / "skills"

    if not skills_dir.is_dir():
        print("No skills/ directory found", file=sys.stderr)
        return 1

    failures: list[tuple[Path, list[str]]] = []
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        errors = validate_skill(skill_dir)
        if errors:
            failures.append((skill_dir, errors))

    if failures:
        for skill_dir, errors in failures:
            print(f"{skill_dir.relative_to(repo_root)}:", file=sys.stderr)
            for error in errors:
                print(f"  - {error}", file=sys.stderr)
        return 1

    print("All skills are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
