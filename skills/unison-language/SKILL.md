---
name: unison-language
description: Write and debug Unison functions, type signatures, data types, pattern matches, and delayed computations. Use for language implementation work rather than UCM administration.
---

# Write against the types in the target codebase

Inspect imported functions and constructors before using them. Similar names from Haskell, Scala, Rust, or Python do not establish a Unison API.
Read [syntax and modeling decisions](references/language.md) for unfamiliar constructs.

## Implement a typechecked slice

1. State the input, output, and effects. Choose explicit signatures for public definitions and effect boundaries.
2. Search local definitions and installed libraries for the needed operations. Inspect argument order and failure representation.
3. For an existing type, use UCM to retrieve its declaration and preserve its unique identity.
4. Write a small `.u` file or edit the project's existing source input. Typecheck in the intended project/branch.
5. Add a normal watch for exploration or a `test>` assertion for a regression. Confirm the value, not just compilation.
6. Use the project's persistence workflow and inspect the resulting stored definition.

## Diagnose the first cause

| Symptom | Next check |
|---|---|
| Unknown name | Installed library, namespace, spelling, then `use` scope |
| Unexpected function where a value belongs | Partial application or an unforced delayed computation |
| Ability mismatch | Exact effect row and handler boundary; read [Abilities](../unison-abilities/SKILL.md) |
| Constructor mismatch after an edit | Unique identity and old/new dependent types |
| Numeric mismatch | `Nat`, signed `Int`, or `Float`; inspect conversion signatures |
| Parse error around a handler | `handle expression with handler`; inline handlers use `with cases` |
| Record syntax rejected | Installed version and existing declaration syntax, rather than a roadmap example |

Do not clear a type error by broadening everything to `IO` or replacing structured data with `Text`.
Report a needed API change explicitly when it changes the user's contract.

Executable examples live in [fundamentals](../../examples/fundamentals.md) and [abilities](../../examples/abilities.md).
These examples intentionally use builtins; application code should reuse appropriate base definitions.
