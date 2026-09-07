#!/usr/bin/env python3
"""Run each UCM transcript in isolation and check that a failing test is rejected."""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def execute(executable, name, source, evidence):
    with tempfile.TemporaryDirectory(prefix="unison-skill-test-") as directory:
        transcript = Path(directory) / (name + ".md")
        transcript.write_text(source)
        result = subprocess.run(
            [executable, "transcript", "-S", str(Path(directory) / "codebase"), str(transcript)],
            capture_output=True, text=True, timeout=60,
        )
        output = transcript.with_suffix(".output.md")
        rendered = output.read_text() if output.exists() else ""
        (evidence / (name + ".log")).write_text(result.stdout + result.stderr)
        (evidence / (name + ".output.md")).write_text(rendered)
        return result.returncode, rendered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ucm", default="ucm")
    args = parser.parse_args()
    executable = shutil.which(args.ucm)
    if not executable:
        parser.error(f"UCM not found: {args.ucm}")
    evidence = ROOT / ".validation"
    evidence.mkdir(exist_ok=True)
    results = []
    for path in sorted((ROOT / "examples").glob("*.md")):
        if path.name.endswith(".output.md"):
            continue
        status, rendered = execute(executable, path.stem, path.read_text(), evidence)
        passed = status == 0 and bool(rendered)
        results.append({"example": path.name, "passed": passed, "exit_code": status})
        print(f"{'PASS' if passed else 'FAIL'} {path.name}")
    negative = '''```ucm
scratch/main> builtins.merge
```
```unison
test> rejectionProbe = [Fail "intentional-negative-probe"]
```
```ucm
scratch/main> update
scratch/main> test
```
'''
    status, rendered = execute(executable, "negative-control", negative, evidence)
    # Require the explicit test diagnostic, not just an arbitrary parse/tool failure.
    passed = status != 0 and bool(re.search(r"rejectionProbe\s+✗ intentional-negative-probe", rendered))
    results.append({"example": "negative-control", "passed": passed, "exit_code": status})
    print(f"{'PASS' if passed else 'FAIL'} failing-test detection")
    version = subprocess.check_output([executable, "--version"], text=True).strip()
    (evidence / "examples.json").write_text(json.dumps({"version": version, "results": results}, indent=2) + "\n")
    raise SystemExit(0 if all(row["passed"] for row in results) else 1)


if __name__ == "__main__":
    main()
