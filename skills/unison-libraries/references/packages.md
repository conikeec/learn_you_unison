# Inspect candidates before pinning a dependency

These are discovery starting points, not a claim that any particular release was executed.
The initial web fetch saw Share's JavaScript shell. A subsequent UCM MCP lookup retrieved all four project READMEs and release metadata.

| Need | Starting point | Evidence to retrieve |
|---|---|---|
| Collections, IO, common abilities, tests | [@unison/base](https://share.unison-lang.org/@unison/base) | Installed release, actual namespaces, test functions |
| HTTP clients and servers | [@unison/http](https://share.unison-lang.org/@unison/http) | Request/response types, handler, exception and resource behavior |
| JSON parsing and encoding | [@unison/json](https://share.unison-lang.org/@unison/json) | Codec/parser types, malformed-input behavior |
| Cloud deployment and storage | [@unison/cloud](https://share.unison-lang.org/@unison/cloud) | Current environment, deployment, and storage APIs |
| A worked Cloud project | [Cloud hello-world](https://www.unison.cloud/learn/http-hello-world/) | Template release and its own pinned dependencies |
| Other parsers, databases, protocols | [Share](https://share.unison-lang.org/) | Type search, README, release, tests, and examples |

Observed `latestRelease` values on 2026-09-06: base **7.19.2**, HTTP **16.1.0**, JSON **1.4.2**, Cloud **27.3.1**.
These are dated metadata observations. The README tool does not select a release, so do not assume its text is release-pinned.
See [the compact observations](../../../research/share-observations.json).

The HTTP README describes clients, servers, and WebSockets. Its client examples use `Threads.run` around `Http.run`.
It explicitly leaves non-success HTTP status handling to the caller; receiving a response does not imply application success.
The JSON README presents composable decoders and structured decoding failures.
The base README now lists C FFI support; the old roadmap's FFI status must not override current package evidence.
Inspect the installed symbols and runtime support before relying on that FFI entry.

Avoid installing a broad toolkit only because its name resembles the task.
For a parser, confirm whether it consumes `Text`, bytes, tokens, or a domain stream.
For a protocol library, inspect transport and schema support separately.

## Record a reproducible choice

Use a dependency note or the project's established manifest convention:

```text
Task and required signature:
Share owner/project:
Resolved release or branch reference:
Local lib alias:
Relevant definition names/hashes:
License and maintenance evidence:
Minimal call tested; UCM version:
Reason selected; unresolved limitation:
```

`latest` and default installation are useful for exploration, but moving targets are insufficient evidence for reproducible examples.
Record the release actually resolved. Recheck exact names before reproducing an old example.

The current [UCM reference](https://www.unison-lang.org/docs/ucm-commands/) distinguishes dependency installation from project cloning.
`lib.install @unison/base` selects a release as a dependency; `clone` brings a project locally for development.
Use a release-qualified reference after confirming that release exists.

## Documentation belongs beside the public API

Unison documentation is stored as definitions, conventionally `name.doc`, using documentation literals.
Include linked types and functions, runnable examples, expected errors, and effect requirements.
Use the actual project's conventions for its README and author/license metadata.
[Documenting code](https://www.unison-lang.org/docs/usage-topics/documentation/) describes `{{ ... }}` literals and definition links.
