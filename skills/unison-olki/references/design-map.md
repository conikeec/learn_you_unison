# Map Olki requirements to Unison mechanisms

This is an implementation analysis of the local Olki documents, reviewed 2026-09-06.
It proposes boundaries; it does not assert that the separate Olki implementation satisfies them.
Paths below are relative to an `olki-docs` checkout.

| Olki requirement | Unison mechanism to consider | Work Olki still owns | Local source |
|---|---|---|---|
| Typed ops and circuits | ADTs, functions, explicit signatures | Runtime validation of dynamically composed graphs | `01-core-concepts.md`, `03-type-system.md` |
| Content-addressed IR | Immutable data, hashing library | Canonical encoding, BLAKE3 rule, labels, signed records | `02-ir-spec.md` |
| Scoped effects and grants | Abilities and interpreters | Scope comparison, identity, budgets, publisher admission | `04-effects-and-grants.md` |
| Failure arms | Sum types and pattern matching | Circuit exhaustiveness, transient classification, retry rules | `03-type-system.md`, `07-runtime.md` |
| Taint and quoting | Dedicated value types and checked constructors | Propagation, sink checks, runtime schema validation | `03-type-system.md` |
| Consumed-once resources | Scoped handlers and resource bookkeeping | Linear-use checking and release on every exit path | `03-type-system.md` |
| `reason via self` | Explicit request/result state and interpreter | Durable suspension, answer correlation, schema checking | `08-reason-and-crystallization.md`, `10-harness-integration.md` |
| Crystallization | Pure replacement functions and test handlers | Compatibility relation, coverage, evidence, guarded fallback | `08-reason-and-crystallization.md`, `09-trust-ledger.md` |
| Journal and replay | Data values and storage APIs | Observations, retries, idempotency, external-state preconditions | `07-runtime.md` |
| Export/import manifest | Serializable domain records | Dependency closure, signatures, tool schemas, grant checks | `21-circuit-manifest.md` |
| Nested circuit calls | Function composition or interpreted graph nodes | Scope, arm/effect propagation, cycles, manifests | `23-circuit-composition.md` |

## Code identity and circuit identity are different contracts

Olki section 02 specifies BLAKE3 over a normalized canonical serialization.
Unison identifies definitions according to its own hashing and reference representation.
Do not substitute a UCM definition hash for an Olki record hash merely because both are content addresses.
Keep an explicit mapping if a circuit record references an implementation stored in Unison.
Test normalization with rename invariance, changed literals, dependency changes, and serialization ordering.

## An ability row does not enforce a scoped grant

A Unison ability can separate HTTP operations from their handler.
It does not automatically enforce Olki's value-level host scopes or its grant-specific reasoner ordering.
Implement these comparisons in the circuit checker and enforce actual operations in runtime interpreters.
Keep declared effects and observed operations distinct in tests.

The specification's `Text<trusted>`, `Session<host>`, and linearity annotations are Olki notation.
Do not present them as accepted Unison syntax or compiler guarantees.
Represent their meaning explicitly and test the relevant rejected compositions.

## A dynamic circuit needs a dynamic checker

If agents submit pipe text or JSON graphs, the Unison compiler cannot typecheck each future graph at compile time.
Represent the IR with Unison data types, then implement Olki's checking rules over that representation.
The interpreter should consume a checked form or another explicit evidence of successful checking.
Choose how that evidence resists invalid construction within the implementation; a type name alone is insufficient proof.

For a vertical slice, consider `parse → check → interpret → journal → resume` with one narrow effect.
Exercise a valid circuit, a type mismatch, a denied host, a malformed answer, and a duplicated answer.
This is a proposed implementation slice. Preserve section 22's requirement dependencies where the project already uses them.
That document proposes Rust crates and Cargo checks. Translate its implementation choices to the current Unison project; keep its acceptance criteria.

Sections 03 and 23 need interpretation together: the former rejects unhandled terminal failures, while the latter discusses callee failure propagation.
Before implementing that boundary, determine how a circuit declares exported failure arms and how callers discharge them.
Record the chosen interpretation with tests instead of silently choosing whichever rule makes an example compile.

## Preserve requirements that code hashes cannot prove

Matching a crystallized stage's type does not prove matching behavior.
Require the specified coverage, guard, provenance, and fallback checks.
Changing a model to a cheaper reasoner requires Olki's explicit ordering; Unison does not infer that policy.

Hash identity also does not prove authorization, runtime environment compatibility, secret availability, or exactly-once external writes.
Keep each claim tied to the checker, handler, manifest, or journal evidence that supports it.
