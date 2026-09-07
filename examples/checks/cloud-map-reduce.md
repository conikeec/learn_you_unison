# Map/reduce through the local Cloud handler

This optional transcript downloads a large public starter project and runs its Cloud handler locally.
It typechecks the remote entry point but never calls `auth.login` or `run cloudScore`.
The inspected starter project used Cloud 27.2.0; its main branch can change.

Run `ucm transcript examples/checks/cloud-map-reduce.md` from the repository root.
The result of `run localScore` must be `222`. Remote infrastructure behavior is not tested here.

```ucm
scratch/main> clone @unison/cloud-start cloud-star-game/main
```

```unison cloud-game.u
giveStar : Nat -> Nat
giveStar score = score Nat.+ 1

celebrate : Nat -> Nat
celebrate score = giveStar (giveStar score)

batchTotal : [Nat] -> Nat
batchTotal scores = List.foldLeft (Nat.+) 0 (List.map celebrate scores)

parallelTotal : '{Remote} Nat
parallelTotal = do
  pool = Remote.region!
  first = Remote.fork pool do batchTotal [10, 20]
  second = Remote.fork pool do batchTotal [30, 40]
  third = Remote.fork pool do batchTotal [50, 60]
  (Remote.await first) Nat.+ (Remote.await second) Nat.+ (Remote.await third)

cloudScore : '{IO, Exception} Nat
cloudScore = Cloud.main do
  Cloud.submit !Environment.default parallelTotal

localScore : '{IO, Exception} Nat
localScore = Cloud.main.local do
  Cloud.submit !Environment.default parallelTotal

> batchTotal [10, 20, 30, 40, 50, 60]
```
```ucm
cloud-star-game/main> load cloud-game.u
cloud-star-game/main> update
cloud-star-game/main> run localScore
```
