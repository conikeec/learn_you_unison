# Handle a request and resume its computation

Run `ucm transcript examples/abilities.md` to test a handler without network access or a base installation.

```ucm
scratch/main> builtins.merge
```

The handler supplies a value, then reinstalls itself when resuming the continuation.
The second request checks that repeated requests remain handled.

```unison
unique ability Setting where
  read : {Setting} Nat

Setting.run : Nat -> '{Setting} a -> a
Setting.run value computation =
  handle computation() with cases
    { result } -> result
    { Setting.read -> resume } ->
      Setting.run value do resume value

twice : '{Setting} Nat
twice = do
  first = Setting.read
  second = Setting.read
  first Nat.+ second

test> handled =
  if Setting.run 7 twice == 14 then [Ok "two requests"]
  else [Fail "two requests"]
```

```ucm
scratch/main> update
scratch/main> test
```
