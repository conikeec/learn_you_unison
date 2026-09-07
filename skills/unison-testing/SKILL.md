---
name: unison-testing
description: Verify Unison behavior with test watches, pure handlers, IO tests, and executable UCM transcripts. Use for regressions, reproducible bugs, and CI checks.
---

# Test the behavior and the persistence workflow

Choose tests that can fail for the defect or requirement in question.
Typechecking alone does not establish a correct result.
Read [test and transcript decisions](references/testing.md) when choosing a test form.

## Build the smallest meaningful check

1. For pure code, use `test>` watches with assertions producing test results. Include the relevant boundary or failure case.
2. For ability-based logic, use a deterministic handler and exercise repeated requests or failure paths.
3. For external behavior, use an IO test or executable entrypoint supported by the installed version and library.
4. Persist intended tests, run them from the codebase, and inspect failures and cached results.
5. For a UCM workflow or compiler bug, create a transcript using a fresh codebase and explicit prerequisites.

Run [the supplied examples](../../examples/fundamentals.md) through [the repository runner](../../scripts/run_examples.py).
The runner also checks that an intentionally failing test causes failure; a green process must mean something.

## Make CI reproduce the relevant environment

Pin UCM and library releases through the project's build convention.
Run transcripts in disposable codebases unless the test specifically requires an existing codebase.
Keep `.output.md` and diagnostics as CI artifacts; check exit status and semantic failures.
Do not use `transcript.in-place` against a developer codebase as a default test command.

Completion evidence includes the test names, UCM/library context, result, and any external paths left untested.
