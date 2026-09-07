# Match the test form to the failure

| Form | Establishes | Does not establish |
|---|---|---|
| `>` watch | An observed exploratory value | A persisted assertion or failure gate |
| `test>` watch | A test result from a pure computation | Real network behavior |
| Pure ability handler | Logic under the chosen interpreter | Production interpreter correctness |
| IO test or explicit program run | Behavior in that environment | A timeless cached result |
| UCM transcript | A sequence of codebase interactions | The same behavior on every UCM version |

The [testing guide](https://www.unison-lang.org/docs/usage-topics/testing/) describes test results, test helpers, and property testing.
Inspect the installed base definitions before choosing `test.verify`, assertion helpers, or generators.
Builtins-only transcripts have a smaller naming environment than an application with base installed.

Pure test results can be cached by definition identity. Changed external state is not part of that identity.
Use fresh IO execution for external conditions and use cache clearing only for a stated diagnostic reason.
UCM 1.4.0 introduces `run>` watches; read the local behavior before loading code containing them.
See [the 1.4.0 release](https://github.com/unisonweb/unison/releases/tag/release%2F1.4.0).

## Executable transcripts are Markdown programs

A `unison` fence introduces code. A `ucm` fence contains prompt-prefixed commands, such as `scratch/main> update`.
Stanzas execute in order. Start with `builtins.merge` for builtins-only examples, or explicitly install a pinned base release.
Fresh transcripts do not implicitly provide an application's base library.
[Transcript documentation](https://www.unison-lang.org/docs/tooling/transcripts/) describes stanzas and expected errors.

The shell command `ucm transcript file.md` creates an isolated codebase and writes `file.output.md`.
`transcript.fork` and `transcript.in-place` have different persistence behavior. Inspect their help before using them.
An expected-error stanza should contain only the failure being asserted, so an unrelated parse error cannot pass the test accidentally.

## Preserve evidence that distinguishes failures

Check typechecking, persistence, and behavioral execution independently.
For property tests, record generator boundaries and reproducible seeds where the API permits them.
For services, check status codes and decoded bodies, cancellation, and resource cleanup.
For retrying writes, exercise duplicate attempts and confirm the chosen idempotency contract.
