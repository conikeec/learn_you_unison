---
name: unison-libraries
description: Discover and inspect libraries on Unison Share, select dependencies, upgrade installed libraries, and prepare Unison project releases or contributions.
---

# Select libraries by their actual contract

Search the current project and installed dependencies first.
For remote discovery, use UCM MCP's discovered Share tools or the [Share interface](https://share.unison-lang.org/).
A JavaScript-required page response does not mean a library is empty or absent.

## Find a dependency and prove its fit

1. Express the needed input/output type and effects, then search by type and task keywords.
2. Inspect a small set of candidates: README, exact definitions, release identity, license, and relevant activity or maintenance evidence.
3. Record why the selected API fits and what failure handling it needs.
4. Install within the intended project using the current `lib.install` command or MCP schema.
5. Inspect the resulting local alias and signatures. Typecheck a minimal call before building around it.

Read [library selection and release notes](references/packages.md) for discovery starting points and a dependency record.

## Upgrade through dependent repair

Record the previous release and local alias. Inspect current `help lib.upgrade` before issuing an upgrade.
Follow UCM's repair workflow, review changed types, and test affected callers.
Content-addressed definitions allow versions to coexist; they do not make different type identities interchangeable.
The [update guide](https://www.unison-lang.org/docs/usage-topics/workflow-how-tos/update-code/) covers library upgrades.

## Publish a reviewable project

When publication is requested, prepare public signatures, documentation, tests, license, and dependency references first.
Confirm the intended owner, project, branch/release, and visibility from task context.
Use current UCM/Share commands and verify the resulting remote definitions.
Do not infer publication authority from successful authentication or from a request to install a dependency.
