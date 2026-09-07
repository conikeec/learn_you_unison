# Select a runtime and inspect its libraries

| Target | Verify before implementation |
|---|---|
| Local command | Entry signature, argv handling, working directory, exit/failure behavior |
| Runtime bytecode | `compile` output, matching runtime, dependencies, and deployment machine |
| Ordinary HTTP service | Server handler, bind/listen API, routing, shutdown, request size limits |
| Unison Cloud HTTP | Environment, credentials, current deployment signature, service naming |
| Unison Cloud native service | Input/output type identity and call/deployment API |
| Host-language bridge | Actual available FFI or process/HTTP mechanism in the installed release |

The [running-program guide](https://www.unison-lang.org/docs/usage-topics/running-programs/) and local `ucm --help` distinguish runtime execution modes.
`compile entry output` inside UCM can produce an `.uc` artifact for `ucm run.compiled`.
Do not label `.uc` as a standalone native binary. Check native compilation support separately when that is required.
The [1.0 overview](https://www.unison-lang.org/unison-1-0/) describes deployment outside managed Cloud.

## Treat external data and concurrency as contracts

Inspect the library's URL and request types. Parse URLs and JSON with library functions, then validate the domain input.
Explicitly handle unexpected status, malformed bodies, and transport failure.
For writes, decide retry eligibility and idempotency from the operation's semantics.

Search installed concurrency APIs by signature. Identify whether they manage cancellation and child lifetime or only start a thread.
Use bounded concurrency for unbounded input. Confirm acquisition/release behavior through tests.
Do not assume an API named `fork` supplies the structured concurrency rules required by Olki.

For persistence, distinguish Unison codebase storage from application data storage.
Content-addressed code does not automatically journal external inputs or make application transactions durable.
Keep schema migration and replay assumptions explicit.

## Deploy Cloud code against a verified template

The [HTTP learning module](https://www.unison.cloud/learn/http-hello-world/) supplies a project and deployment example.
Inspect its current release and dependency aliases before reusing it.
Its workflow handles Cloud operations, deploys the HTTP function, and optionally assigns a stable service name.
Assignment changes a remote mapping; record the previous mapping when rollback matters.

Verify the returned endpoint with a representative request and inspect service logs when behavior differs from the local test.
Credentials, environment selection, and remote service state are separate from code hashes.
Do not copy credentials into a skill, transcript, source definition, or shared artifact.
