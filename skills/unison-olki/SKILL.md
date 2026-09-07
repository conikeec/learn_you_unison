---
name: unison-olki
description: Apply Unison to Olki's typed circuits, grants, reasoning stages, journals, and harness tools. Use for Olki architecture or implementation work that needs a precise mapping to Unison capabilities.
---

# Implement Olki's rules explicitly

Read [the design map](references/design-map.md) and the relevant Olki specification before choosing a representation.
The original request named `~/tulving/olki_docs`; research found the documents at `~/tulving/olki-docs`.
Locate the current checkout instead of requiring that machine-specific path.

The docs describe intended behavior and their README labels the design as such.
A neighboring implementation can exist without proving every requirement. Inspect code and tests for the requested slice.

## Trace each guarantee to an implementation

1. Select the circuit, checker, runtime, or protocol requirement being implemented.
2. Record its specification section and observable acceptance case.
3. Choose a Unison data representation and explicit ability boundary.
4. Identify enforcement supplied by Unison and enforcement that Olki must implement itself.
5. Implement the narrow slice with rejection tests and runtime behavior tests.
6. State which evidence proves the requirement and what remains a proposal.

## Keep the two MCP roles distinct

UCM MCP helps a coding agent inspect and modify Unison code.
Olki's proposed MCP surface exposes catalog/check/run/answer/journal behavior for agent operations.
Enabling UCM MCP does not implement Olki's tools, grant filter, or suspended reasoning loop.

For `via self`, model the run/stage correlation and validate the answer before resumption.
Treat replayed, stale, mismatched, and malformed answers as explicit cases.
Pass external data in structured slots and enforce the specification's instruction/data boundary in the runtime.

Completion evidence: requirement-to-code mapping, types and effects, rejection tests, runtime tests, and a list of unresolved guarantees.
