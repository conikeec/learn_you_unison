#!/usr/bin/env python3
"""Validate this bundle's skill frontmatter, routing links, and discovery links."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    names = set()
    for path in skills:
        content = path.read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not frontmatter:
            errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            continue
        fields = dict(re.findall(r"^([a-z-]+): (.+)$", frontmatter[1], re.M))
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name != path.parent.name:
            errors.append(f"{path}: name does not match directory")
        if name in names:
            errors.append(f"duplicate skill name: {name}")
        names.add(name)
        if not fields.get("description", "").strip():
            errors.append(f"{name}: missing description")
        if len(content.splitlines()) > 250:
            errors.append(f"{name}: move conditional detail into references")
        discovery = ROOT / ".agents" / "skills" / name
        if not discovery.is_symlink() or discovery.resolve() != path.parent:
            errors.append(f"{name}: missing or incorrect repository discovery link")
    files = [ROOT / "README.md", ROOT / "AGENTS.md"]
    for folder in ("skills", "docs", "research", "evals", "examples"):
        files.extend((ROOT / folder).rglob("*.md"))
    for path in files:
        if path.name.endswith(".output.md"):
            continue
        text = path.read_text()
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            link = link.strip("<>")
            parsed = urlsplit(link)
            if parsed.scheme or not parsed.path:
                continue
            target = path.parent / unquote(parsed.path)
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {link}")
    manifest = ROOT / "research" / "sources.json"
    if manifest.exists():
        sources = json.loads(manifest.read_text())
        ids = set()
        for row in sources:
            if row["id"] in ids:
                errors.append(f"duplicate source: {row['id']}")
            ids.add(row["id"])
            for required in ("id", "title", "url", "accessed", "status", "used_by"):
                if not row.get(required):
                    errors.append(f"source {row.get('id')}: missing {required}")
            for user in row.get("used_by", []):
                if user not in names:
                    errors.append(f"source {row['id']}: unknown skill {user}")
    else:
        errors.append("missing research/sources.json")
    for error in errors:
        print("FAIL", error)
    print(f"Checked {len(skills)} skills and {len(files)} Markdown files; {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
