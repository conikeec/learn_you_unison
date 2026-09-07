# Work with Unison through its codebase

Read [skills/unison/SKILL.md](skills/unison/SKILL.md) for Unison language tasks.
It routes to the smallest relevant specialist. Read further references only when needed.

This repository contains agent skills, research notes, and executable UCM examples.
It does not contain the Unison compiler or an Olki implementation.

Before editing Unison definitions, establish the UCM version, codebase path, project, branch, and installed libraries.
Use the connected UCM MCP server when available. Discover its current schemas; tool names and parameters can change.
Otherwise use explicit UCM commands or disposable transcripts. Keep shell commands distinct from commands entered at the UCM prompt.

Treat `.u` files as editing inputs. Verify persistence in UCM before claiming that a definition was saved.
Preserve unique type identities when editing existing declarations.

When changing this skill set, run `python3 scripts/validate.py` and `python3 scripts/run_examples.py`.
Keep source dates, local verification evidence, and proposed Olki design separate.
Do not promote a roadmap item or an old conference demo to a current capability without verification.
