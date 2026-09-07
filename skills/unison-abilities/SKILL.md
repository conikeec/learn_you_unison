---
name: unison-abilities
description: Design Unison abilities and implement or debug handlers, effect polymorphism, and continuations. Use when separating domain operations from their interpreters or resolving ability errors.
---

# Separate an operation from its handler

An ability describes requests. A handler chooses their interpretation.
The function signature exposes required abilities; it does not describe host allowlists, token budgets, or OS isolation.
[The mental model](https://www.unison-lang.org/docs/fundamentals/abilities/) introduces this separation.

## Implement one request through two interpreters

1. Define the smallest operation contract needed by the domain. Keep vendor details in the interpreter when possible.
2. Inspect existing abilities before introducing a new one.
3. Write the calling computation with an explicit effect signature.
4. Implement a pure test handler first, including the normal return case.
5. Implement the external handler using the actual IO/library functions. Account for its remaining effects.
6. Check repeated requests, failure behavior, and cleanup. Verify each handler's inferred type.

Use [handler mechanics](references/handlers.md) for continuation behavior and effect rows.
Run [the executable handler example](../../examples/abilities.md) to see two requests handled without IO.

## Preserve the contract when changing effects

For a handler of an ability `A`, inspect whether it removes `A`, introduces another effect, or changes the result type.
An effect variable such as `g` can preserve caller effects. Use the actual inferred signature as the check.
Do not call every handler “pure”: a handler that translates requests into IO still requires IO.

For Olki grants or taint, read [the Olki skill](../unison-olki/SKILL.md).
Those application requirements need explicit enforcement beyond an ordinary ability declaration.

Completion evidence: declarations, caller and handler signatures, tested request paths, and the final remaining effect requirements.
