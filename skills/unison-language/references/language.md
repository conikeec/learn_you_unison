# Read Unison syntax by its meaning

## Functions are curried and values evaluate eagerly

`f : a -> b -> c` accepts one argument and returns a function accepting the next.
Application uses whitespace; parentheses group expressions. Lambdas use `x -> expression`.
`use Namespace name1 name2` changes name resolution within its scope; it does not install a dependency.
Prefer qualified names while resolving ambiguity, then add narrow `use` clauses.
[Functions and types](https://www.unison-lang.org/docs/) provide the basic notation.

`Nat` represents nonnegative integers. `Int` literals use a sign, such as `+3` or `-3`.
Do not assume subtraction on naturals behaves like signed subtraction.
Lists have one element type; tuples combine different types. An empty list often needs context for inference.

## A delay is a function awaiting unit

`'a` abbreviates `() -> a`. `'{IO, Exception} a` delays a computation requiring those abilities.
`do expression` delays the entire expression; `thunk()` or `!thunk` forces it.
For an applied function, use `!(f x)` or `f x ()`.
`do` does not import Haskell's monadic bind syntax, and Unison is not lazy by default.
[Delayed computations](https://www.unison-lang.org/docs/fundamentals/values-and-functions/delayed-computations/) explains the precedence rules.

## Data declarations choose identity as well as shape

`structural type Outcome a = Good a | Bad Text` makes identity depend on structure.
Use explicit `unique type` for domains whose separate identity matters.
UCM preserves a unique declaration's identity when presenting it for editing; retain the identity annotation it supplies.
Recreating a unique declaration from remembered text can produce an incompatible type.

Pattern matching uses `match value with` or `cases` for a function defined by cases.
Handle each constructor, including expected failures. Use `Optional` for absence and an appropriate sum for failure details.
Inspect the real `Either` or domain result declaration before choosing constructor names.

Named records supply fields and generated operations, but are not unrestricted structural row types.
Check current record syntax against local UCM and the existing project style.
Olki notation such as `Text<trusted>` is not Unison syntax.
[Data type identity](https://www.unison-lang.org/docs/fundamentals/data-types/unique-and-structural-types/) explains structural and unique declarations.

## Transfer concepts without importing unsupported features

| Familiar concept | Unison decision |
|---|---|
| Haskell laziness | Delay explicitly where required |
| Type classes or Rust traits | Inspect the library's explicit dictionaries, records, or abilities |
| Monad transformer stack | Consider ability requirements and handlers |
| Class with mutable fields | Use data values and an explicit state effect where mutation belongs |
| Package import | Install the library separately; resolve names in scope |
| Dynamic exception everywhere | Choose data errors or an ability according to the caller's recovery needs |

The [general FAQ](https://www.unison-lang.org/docs/usage-topics/general-faqs/) documents differences from Haskell.
Treat language features under development as unverified until the installed version accepts a minimal example.
