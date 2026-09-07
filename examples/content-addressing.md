# Check identity independently of names

Run `ucm transcript examples/content-addressing.md` for the code behind the orientation guides.
The runner uses a disposable codebase. The tests compare definition references, not just returned values.

```ucm
scratch/main> builtins.merge
```

Changing the function name and argument name leaves this definition's identity unchanged.

```unison
addStar : Nat -> Nat
addStar score = score Nat.+ 1

awardPoint : Nat -> Nat
awardPoint points = points Nat.+ 1

celebrate : Nat -> Nat
celebrate score = addStar (addStar score)
```

```ucm
scratch/main> update
```

```unison
test> sameDefinition =
  if termLink addStar == termLink awardPoint then [Ok "same definition, different names"]
  else [Fail "names changed identity"]

test> firstScore =
  if celebrate 10 == 12 then [Ok "two stars"]
else [Fail "unexpected score"]
```

Save the tests, then remove the extra teaching alias before renaming and replacing the definition.
Keeping another name for the old definition can keep callers attached to it during an update.

```ucm
scratch/main> update
scratch/main> delete.term awardPoint
scratch/main> move.term addStar giveStar
scratch/main> view celebrate
scratch/main> test
```

Keep a baseline branch before changing behavior on the current branch.

```ucm
scratch/main> branch bonus
```

```unison
giveStar : Nat -> Nat
giveStar score = score Nat.+ 2
```

The update changes dependent definitions. Replace the old score assertion to reflect the deliberate new behavior.

```ucm
scratch/bonus> update
```

```unison
test> firstScore =
  if celebrate 10 == 14 then [Ok "four stars"]
  else [Fail "caller not updated"]
```

```ucm
scratch/bonus> update
scratch/bonus> test
scratch/bonus> switch /main
scratch/main> test
scratch/main> view giveStar
scratch/main> view celebrate
```
