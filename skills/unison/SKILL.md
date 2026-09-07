---
name: unison
description: Orient and route work on the Unison programming language, UCM codebases, and Unison Share. Use when starting an unfamiliar Unison task or coordinating several Unison workflows.
---

# Establish context before writing Unison

For a first introduction, read [content-addressed code](../../docs/01-code-that-knows-its-own-name.md), then [working without source folders](../../docs/02-your-codebase-is-not-a-folder.md).
Skip these guides when you already know the model and need a specific operation.

Unison identifies stored definitions by content hash. Names are editable references to those definitions.
The UCM codebase holds definitions, names, and history; scratch files provide an editing surface.
Filesystem search can find exported source, but cannot establish everything stored in UCM.
See [the language overview](https://www.unison-lang.org/unison-1-0/) for this model.

## Select the next useful operation

1. Read the project's instructions and intended outcome. Establish whether it uses UCM directly or an additional source-file build process.
2. Record `ucm --version`, the codebase path, project/branch, scratch directory, and installed dependency names.
3. If a UCM MCP connection exists, inspect its tools and obtain current project context. Match that context to the user's target.
4. Load only the specialist needed now from the table below.
5. Inspect relevant type signatures, implement a small slice, and typecheck it. Follow diagnostics instead of guessing APIs.
6. Verify behavior and persistence separately. Report the resulting project/branch and what actually ran.

| Task | Read |
|---|---|
| Write functions or resolve syntax/type errors | [Language](../unison-language/SKILL.md) |
| Design or handle effects | [Abilities](../unison-abilities/SKILL.md) |
| Configure MCP, edit stored code, update, merge, or recover | [UCM](../unison-ucm/SKILL.md) |
| Find, install, upgrade, or publish a library | [Libraries](../unison-libraries/SKILL.md) |
| Add tests, reproduce a bug, or automate checks | [Testing](../unison-testing/SKILL.md) |
| Build a service or deploy a program | [Services](../unison-services/SKILL.md) |
| Implement Olki circuits, grants, or harness integration | [Olki](../unison-olki/SKILL.md) |
| Resolve stale guidance or investigate talks | [Research](../unison-research/SKILL.md) |

## Keep inspection proportional to the task

Read the project README, relevant signatures, and selected bodies. Avoid dumping an entire base library into context.
Search by input/output type when naming is uncertain. Record dependency versions and definition references worth reusing.
After two unsuccessful repairs using the same assumption, inspect the actual definition, schema, or command help.

Maintain a compact handoff for multi-turn work:

```text
UCM version and executable:
Codebase path; project/branch:
Scratch file and load status:
Relevant libraries and resolved versions:
Target signatures/definition references:
Changes persisted in UCM:
Tests run and remaining failure:
Next operation:
```

This is a suggested working note, not a required extra artifact for small edits.
Never infer execution, publication, or migration success from generated code alone.
