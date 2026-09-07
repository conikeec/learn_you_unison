# Discover the installed MCP contract

UCM provides a stdio MCP server through `ucm mcp`.
Its [setup guide](https://www.unison-lang.org/docs/usage-topics/mcp-setup/) also describes an HTTP connection to running UCM.
Prefer stdio for harness-managed processes unless the project requires attachment to an existing UCM process.

Configure an executable and arguments using the harness's current configuration mechanism.
For an existing codebase, the UCM process argument vector can be:

```json
{"command": "/absolute/path/to/ucm", "args": ["-c", "/absolute/path/to/codebase", "mcp"]}
```

This is a server specification fragment, not a complete harness configuration file.
Verify the harness's current schema before placing it. Do not overwrite unrelated servers.
Use `-C` only when creation is intended; `-c` targets an existing codebase.

On connection, discover `tools/list` and available prompts/resources.
Read the server's advertised Unison guide when available; the observed 1.4.0 server advertises `file://unison-guide`.
Inspect each selected tool's current `inputSchema`, description, and side effects.
Read project context before calls whose default target is the current project.
Use explicit project/branch arguments where the tool supports them.

## Map intent to discovered tools

The official setup page lists these names; your installed server may differ.

| Intent | Names to look for |
|---|---|
| Establish context | `get-current-project-context`, `list-local-projects`, `list-project-branches` |
| Inspect dependencies | `list-project-libraries`, `list-library-definitions` |
| Find an operation | `search-by-type`, `search-definitions-by-name` |
| Read selected code | `view-definitions`, `docs` |
| Assess change impact | `list-definition-dependencies`, `list-definition-dependents` |
| Discover remote libraries | `share-project-search`, `share-project-readme` |
| Install and typecheck | `lib-install`, `typecheck-code` |

## The local 1.4.0 probe exposes additional operations

On 2026-09-06, the disposable probe returned 29 tools.
These include `update-definitions`, `diff-update`, `run-tests`, `create-branch`, `history`, and `reflog`.
Inspect [the captured contract](../../../research/ucm-1.4.0-mcp.json) only when you need those exact schemas.
It is an observed baseline, not a substitute for discovery on another installation.

For this version, a file-backed `typecheck-code` call takes this argument shape:

```json
{
  "projectContext": {"projectName": "my-project", "branchName": "main"},
  "code": {"filePath": "/absolute/path/to/change.u"}
}
```

Replace the example context with the discovered target. `update-definitions` uses the same `code` union.
`diff-update` accepts `code.filePath` or `code.text`; its inline-text key differs from `typecheck-code`'s `sourceCode`.
`share-project-readme` splits the owner and project into `projectOwnerHandle` and `projectName`.
These concrete differences make schema discovery necessary.

Do not hardcode argument names from a remembered call. A file path and source text are different inputs.
Prefer file-backed typechecking when the schema supports it; retain the file for later edits and review.
Inspect whether typechecking evaluates watches. An effectful watch can execute during a seemingly diagnostic operation.

## Recover from missing tools or wrong context

If a server lacks persistence or branch commands, use UCM's CLI workflow for those operations.
Do not pretend a typecheck stored code.
If the connection points at the wrong codebase, correct the process target before applying changes.
If simultaneous agents contend over codebase state, isolate branches and scratch files; use separate codebases when branch isolation is insufficient.

The repository includes [a disposable contract probe](../../../scripts/probe_ucm.py).
It initializes MCP and lists tools; it does not prove that a harness connection or a tool's full behavior works.
