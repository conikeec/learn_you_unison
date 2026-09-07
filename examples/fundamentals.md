# Check pure functions in an isolated codebase

This transcript uses only builtins. Run it with `ucm transcript examples/fundamentals.md`.
The runner creates a temporary codebase and an output Markdown file.

```ucm
scratch/main> builtins.merge
```

The tests check a boundary value, a polymorphic function, and a forced delayed computation.

```unison
boundedIncrement : Nat -> Nat -> Nat
boundedIncrement ceiling value =
  if value < ceiling then value Nat.+ 1 else ceiling

keep : a -> a
keep value = value

later : 'Nat
later = do boundedIncrement 10 3

test> below =
  if boundedIncrement 10 3 == 4 then [Ok "below ceiling"]
  else [Fail "below ceiling"]

test> boundary =
  if boundedIncrement 10 10 == 10 then [Ok "at ceiling"]
  else [Fail "at ceiling"]

test> polymorphic =
  if keep "agent" == "agent" then [Ok "identity"]
  else [Fail "identity"]

test> delayed =
  if later() == 4 then [Ok "forced"]
  else [Fail "forced"]
```

Persist the definitions, then run the stored tests.

```ucm
scratch/main> update
scratch/main> test
```
