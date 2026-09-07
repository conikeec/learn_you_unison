#!/usr/bin/env python3
"""Inspect the installed UCM MCP contract in a disposable codebase."""
import argparse
import json
import os
import selectors
import shutil
import subprocess
import tempfile
import time
from pathlib import Path


def probe(executable, share_projects=()):
    version = subprocess.check_output([executable, "--version"], text=True).strip()
    with tempfile.TemporaryDirectory(prefix="unison-mcp-probe-") as directory:
        bootstrap = Path(directory) / "bootstrap.md"
        bootstrap.write_text("```ucm\nscratch/main> builtins.merge\n```\n")
        codebase = Path(directory) / "codebase"
        subprocess.run(
            [executable, "transcript", "-S", str(codebase), str(bootstrap)],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45,
        )
        with tempfile.TemporaryFile(mode="w+") as errors:
            proc = subprocess.Popen(
                [executable, "-c", str(codebase), "mcp"], stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=errors, bufsize=0,
            )
            selector = selectors.DefaultSelector()
            selector.register(proc.stdout, selectors.EVENT_READ)

            def send(message):
                proc.stdin.write((json.dumps(message) + "\n").encode())
                proc.stdin.flush()

            def request(number, method, params):
                send({"jsonrpc": "2.0", "id": number, "method": method, "params": params})
                deadline = time.monotonic() + 45
                buffer = b""
                observed = []
                while time.monotonic() < deadline:
                    if not selector.select(timeout=1):
                        if proc.poll() is not None:
                            break
                        continue
                    chunk = os.read(proc.stdout.fileno(), 65536)
                    if not chunk:
                        break
                    buffer += chunk
                    while b"\n" in buffer:
                        line, buffer = buffer.split(b"\n", 1)
                        observed.append(line.decode(errors="replace"))
                        try:
                            reply = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        if reply.get("id") == number:
                            if "error" in reply:
                                raise RuntimeError(str(reply["error"]))
                            return reply["result"]
                errors.seek(0)
                raise RuntimeError(f"No response to {method}: {errors.read()[-1000:]} {observed[-4:]} {buffer[-1000:]!r}")

            try:
                initialized = request(1, "initialize", {
                    "protocolVersion": "2024-11-05", "capabilities": {},
                    "clientInfo": {"name": "unison-skills-contract-probe", "version": "1.0"},
                })
                send({"jsonrpc": "2.0", "method": "notifications/initialized"})
                tool_list = request(2, "tools/list", {})
                all_tools = list(tool_list.get("tools", []))
                number = 3
                while tool_list.get("nextCursor"):
                    tool_list = request(number, "tools/list", {"cursor": tool_list["nextCursor"]})
                    all_tools.extend(tool_list.get("tools", []))
                    number += 1
                share = []
                for project in share_projects:
                    owner, name = project.removeprefix("@").split("/", 1)
                    info = request(number, "tools/call", {
                        "name": "share-project-info", "arguments": {"projectName": project},
                    })
                    readme = request(number + 1, "tools/call", {
                        "name": "share-project-readme", "arguments": {
                            "projectName": name, "projectOwnerHandle": owner,
                        },
                    })
                    share.append({"project": project, "info": info, "readme": readme})
                    number += 2
                result = {"ucm_version": version, "initialize": initialized, "tools": all_tools}
                if share:
                    result["share"] = share
                return result
            finally:
                selector.close()
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ucm", default="ucm")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--share-project", action="append", default=[], help="Optional read-only Share lookup, e.g. @unison/base; requires network")
    args = parser.parse_args()
    executable = shutil.which(args.ucm)
    if not executable:
        parser.error(f"UCM executable not found: {args.ucm}")
    for project in args.share_project:
        if not project.startswith("@") or project.count("/") != 1:
            parser.error("--share-project requires @owner/project")
    result = probe(executable, args.share_project)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(result["ucm_version"])
    for tool in result["tools"]:
        print(tool["name"])
    for project in result.get("share", []):
        print(project["project"], "read-only metadata and README retrieved; inspect output for tool errors")


if __name__ == "__main__":
    main()
