# Handle requests with explicit continuation behavior

An inline handler uses `handle computation() with cases`.
`{ result } -> result` handles normal completion.
A request pattern such as `{ Setting.read -> resume }` binds `resume` to the continuation of the computation.
Calling `resume value` supplies the request's result and continues execution.
See [writing abilities](https://www.unison-lang.org/docs/fundamentals/abilities/writing-abilities/).

The continuation may issue more requests. Reinstall the handler around its resumed computation when that is the intended behavior.
The repository's `Setting.run value do resume value` example tests this explicitly.
For state, the recursive handler passes updated state to the resumed computation.

## Continuations do not imply exactly one execution

A handler can discard a continuation, resume it once, or resume it multiple times.
Discarding suits abort behavior; multiple resumptions can implement search.
Repeated resumptions can repeat external actions. Audit this before using such handlers around writes.

Handler nesting determines which interpreter receives a request and where other effects remain.
Test both normal completion and a request made after another request resumes.
For resource handlers, test release after normal return, exceptions, cancellation, and abandoned continuations as relevant.
Do not infer linear resource use from ordinary Unison value types.

## Choose data errors or effect errors intentionally

Return a sum when callers must inspect expected outcomes as values.
Use an error ability when callers benefit from handling failures across a larger computation.
Handler order can affect the result when state, exceptions, or nondeterminism interact.
Confirm that interaction with a small test rather than importing monad-transformer assumptions.
[Ability FAQs](https://www.unison-lang.org/docs/fundamentals/abilities/faqs/) discusses error representation and handler behavior.

In a production review, record which requests can touch the world, which handler implements them, and which effects escape.
Test-handler success establishes domain behavior under that interpreter. It does not verify a network implementation.
