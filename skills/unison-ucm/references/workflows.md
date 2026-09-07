# Run UCM commands in the intended context

Shell launch flags come from `ucm --help`; interactive commands come from `help` inside UCM.
The [command reference](https://www.unison-lang.org/docs/ucm-commands/) is a lookup aid; installed help resolves version differences.

## Inspect before loading an edit

The following are UCM prompt commands. Replace the example definition with one from the target project.
They list names, search, and display dependencies without changing a definition.

```text
ls
find myFunction
view myFunction
dependencies myFunction
dependents myFunction
help edit
help load
help update
```

`edit` can write to a scratch file. Inspect its destination before replacing another agent's active scratch file.
`load path/to/change.u` explicitly loads a file when file watching does not apply.
`diff.update` previews the pending change on supporting versions; `update` applies it.
Check the response for dependent repair instructions and verify the resulting stored definition with `view`.

## Branches belong to UCM

Use `help branch`, `help switch`, `help merge`, and `help history` to confirm local syntax.
The [project workflow guide](https://www.unison-lang.org/docs/tooling/project-workflows/) covers cloning, branches, and contributions.
A Git branch containing scratch files does not automatically create a UCM branch.

Before a breaking update, record the source project/branch and history position.
Let UCM create its repair branch when necessary. Fix the definitions it presents, then rerun `update`.
Do not manually delete a temporary branch before confirming that the update completed or was deliberately abandoned.

## Recover the smallest state that is wrong

| Problem | Recovery |
|---|---|
| Saved `.u` file is invisible | Check scratch directory, watcher, explicit `load`, and MCP target |
| Unknown library name | Inspect `lib` and the actual installed alias |
| New definitions replace unintended names | Stop persistence; inspect context and pending diff |
| Update leaves dependent errors | Read the generated scratch content and complete the repair branch |
| Need to undo a saved update | Inspect history and local `help undo`/reset commands before changing state |
| Codebase lock error | Identify the owning UCM process and its target; coordinate access instead of deleting locks |
| Old codebase needs migration | Read release guidance and preserve a consistent backup before opening with a newer UCM |

Use UCM operations for its database. Do not edit its SQLite tables or copy a live database without its consistency requirements.
For a bug report, prefer a disposable executable transcript reproducing only the failing behavior.
