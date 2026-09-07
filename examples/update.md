# Verify that an update reaches dependent definitions

Run `ucm transcript examples/update.md` in a disposable codebase.
The caller is stored before its dependency changes.

```ucm
scratch/main> builtins.merge
```

```unison
step : Nat -> Nat
step value = value Nat.+ 1

stepTwice : Nat -> Nat
stepTwice value = step (step value)
```

```ucm
scratch/main> update
scratch/main> dependents step
```

Changing `step` should update `stepTwice` to use the new definition.

```unison
step : Nat -> Nat
step value = value Nat.+ 2
```

```ucm
scratch/main> diff.update
scratch/main> update
scratch/main> view stepTwice
```

The assertion detects a caller that still uses the old dependency.

```unison
test> propagated =
  if stepTwice 0 == 4 then [Ok "dependent updated"]
  else [Fail "dependent still uses the old step"]
```

```ucm
scratch/main> update
scratch/main> test
```
