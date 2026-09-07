# Load, persist, run, rename, and branch the game

This transcript installs base from Share and runs locally. It does not deploy anything.
Use `python3 scripts/check_orientation.py --tsc /path/to/tsc` for the full comparison, including a fresh-process persistence check.

```ucm
scratch/main> project.create star-game
```

```unison game.u
addStar : Nat -> Nat
addStar score = score Nat.+ 1

celebrate : Nat -> Nat
celebrate score = addStar (addStar score)

> celebrate 10
```

```ucm
star-game/main> load game.u
star-game/main> update
```

```unison game.u
addStar : Nat -> Nat
addStar score = score Nat.+ 1

celebrate : Nat -> Nat
celebrate score = addStar (addStar score)

> celebrate 10

main : '{IO, Exception} ()
main = do printLine (Nat.toText (celebrate 10))
```

```ucm
star-game/main> load game.u
star-game/main> update
star-game/main> run main
star-game/main> move.term addStar giveStar
star-game/main> view celebrate
star-game/main> run main
```

An empty working file permits `edit` to reconstruct the saved definitions without stale duplicate declarations.

```unison game.u
-- Stored definitions are safe in the codebase.
```

```ucm
star-game/main> load game.u
star-game/main> edit main celebrate giveStar
star-game/main> load game.u
star-game/main> branch bonus
```

```unison game.u
giveStar : Nat -> Nat
giveStar score = score Nat.+ 2
```

```ucm
star-game/bonus> load game.u
star-game/bonus> update
star-game/bonus> run main
star-game/bonus> switch /main
star-game/main> run main
star-game/main> history
```

Check a merge on a separate branch, leaving the main/bonus comparison available for the persistence check.

```ucm
star-game/main> branch merge-check
star-game/merge-check> merge /bonus
star-game/merge-check> run main
star-game/merge-check> switch /main
```
