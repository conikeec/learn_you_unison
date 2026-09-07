---
name: unison-ucm
description: Operate Unison Codebase Manager and its MCP server for inspection, scratch-file edits, persisted updates, project branches, merges, and recovery. Use for UCM workflow or agent-tool integration tasks.
---

# Keep codebase state explicit

Start with the executable version, codebase path, project/branch, and installed libraries.
A shell working directory does not determine the UCM project.
For MCP setup or schemas, read [agent integration](references/mcp.md).
For command sequences and recovery, read [edit workflows](references/workflows.md).

## Use the smallest inspect-edit-verify cycle

1. Inspect current context and relevant definitions. Check dependents before changing a public type or function signature.
2. Create or select an appropriate working branch through UCM when isolation is needed.
3. Retrieve existing definitions into a scratch file. Preserve unique type/ability identity annotations.
4. Change the file and explicitly load/typecheck it when the watcher is unavailable or disabled.
5. Inspect `diff.update` when supported, then apply `update` within the authorized task.
6. Resolve any temporary update branch using UCM's diagnostics. Recheck context after it completes.
7. Inspect stored definitions and run the relevant tests.

The [current update guide](https://www.unison-lang.org/docs/usage-topics/workflow-how-tos/update-code/) describes dependent repair and temporary branches.
Older patch-based tutorials can describe a different workflow.

## Distinguish three kinds of evidence

| Evidence | What it establishes |
|---|---|
| File typechecked | The loaded definitions typecheck in that context |
| `update` succeeded and stored definition matches | The codebase contains the change |
| Tests or program executed | Those behaviors ran under the stated interpreter and environment |

None of these establishes remote publication. Verify Share state separately when publishing was requested.
When a command fails, preserve the original project, branch, file, and diagnostics before choosing recovery.
