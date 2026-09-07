# Validation and remaining limits

Validation date: 2026-09-06. Machine: macOS arm64. UCM: release/1.4.0, built 2026-08-19.

## Executable examples pass in disposable codebases

| Check | Result |
|---|---|
| Pure functions, boundary value, polymorphism, delayed computation | Passed |
| Ability handler with two resumed requests | Passed |
| Saved dependency update propagates to its stored caller | Passed |
| Equal definition references despite different names; rename preserves caller behavior | Passed |
| Alias removal enables replacement; bonus branch changes behavior while main retains it | Passed |
| Intentional failing test produces a failure exit and named failed test | Passed |

Run `python3 scripts/run_examples.py` to reproduce these checks.
It creates a separate temporary codebase for every example and the negative control.
The process logs and output transcripts remain under ignored `.validation/` paths.

The first drafts exposed incorrect builtin qualification and a missing `cases` in the inline handler.
The corrected examples passed after UCM diagnostics identified the errors.

The orientation example also exposed two UCM details: `termLink` needs a stored definition, and a remaining alias can retain callers on the old definition.
The final transcript saves definitions before comparing references and removes its extra teaching alias before replacement.

## The expanded walkthrough starts with a real TypeScript failure

`python3 scripts/check_orientation.py --tsc /path/to/tsc` executes the TypeScript blocks extracted from the first guide.
The compiler must be installed separately; the README supplies the tested installation command.
Checks used TypeScript 5.9.3, Node 22.23.1, and UCM 1.4.0.

| Check | Result |
|---|---|
| Original and cloned TypeScript repositories compute 12 | Passed |
| Declaration-only rename fails with the missing `addStar` export diagnostic | Passed |
| Repaired import/calls compile and reach the clone through push/pull | Passed |
| UCM loads a named scratch file, persists definitions, and runs the entry point | Passed |
| Rename leaves the caller working; `edit` reconstructs current source | Passed |
| Fresh UCM processes compute main=12, bonus=14, and merged branch=14 | Passed |
| Map/reduce function typechecks against Cloud 27.2.0 and local handler returns 222 | Passed |

See [machine-readable comparison results](orientation-results.json).
The Git remote was a disposable local bare repository; no sample project was published to GitHub or Share.
The UCM comparison fetched base, then used fresh local processes to verify persisted behavior.

The Cloud check cloned `@unison/cloud-start` and inspected installed signatures.
Its current branch used Cloud 27.2.0, including `Remote.fork : Location g -> ...` and `Remote.await : Task a ->{Remote} a`.
The example starts three tasks before awaiting their results; task count does not establish physical worker count.
Only `Cloud.main.local` ran. The `Cloud.main` entry point typechecked but was not executed.
Remote transport, placement, credentials, deployment, and failure handling remain untested.

## The MCP contract was discovered from a running server

`python3 scripts/probe_ucm.py` initialized an isolated UCM MCP process and retrieved 29 tool schemas.
See [the retained JSON](ucm-1.4.0-mcp.json).
The probe bootstraps its codebase through a transcript before starting MCP.
This avoids initial codebase-creation messages sharing stdout with the MCP JSON response on the tested version.

Optional Share lookups retrieved metadata and READMEs for base, HTTP, JSON, and Cloud without installing those libraries.
See [release observations and README fingerprints](share-observations.json).
No source mutation tools were called through MCP during this check.

## Structural checks cover packaging and references

`python3 scripts/validate.py` checks skill names, descriptions, relative links, source records, and repository discovery symlinks.
The skill-creator validator checks all nine skill entrypoints independently of that script.
These checks validate structure; they do not demonstrate an agent's productivity.

All eight orientation diagrams passed the Mermaid 11 parser. Their rendered layout has not been visually checked.

## Research has explicit limits

The DevTools.fm publisher transcript was retrieved and read. Audio was not independently verified.
The Strange Loop recording fetch failed, and individual Forall talk transcripts were not retrieved.
Historical lessons use the sources identified in [the talk notes](../skills/unison-research/references/talks.md).

No Cloud deployment, HTTP integration execution, FFI call, dependency upgrade, or unique-type migration was executed.
The Olki mapping reflects design documents and identifies implementation responsibilities; it is not an audit of the neighboring implementation.
Multi-harness behavioral evaluation remains unrun. [Fourteen scenarios](../evals/scenarios.md) define observable criteria for that work.

## Editorial review preserves the technical distinctions

Desk route: row 4, documentation. The two orientation guides use worked explanations for readers familiar with TypeScript and Git.
The user explicitly requested commands alongside explanation; that request takes precedence over Desk's preference for separate tutorial and explanation pages.
Skill workflows use how-to form; detailed mechanics and source records use reference form.
The README's target questions are how to orient a coding agent and how to verify Unison work.
The bundle uses its own Unison/Olki scope; Modiqo/Rote marketing claims do not apply.

The deterministic lint output, warning dispositions, and skim extracts are recorded in [the editorial review](editorial-review.json).
Skim verdict: pass. The entrypoints state the next operation and verification evidence before conditional detail.
Conservation: the rewritten guides retain definition identity, alias behavior, unique-type limits, codebase organization, history, and sharing distinctions.
They expand the original game into a TypeScript comparison and local/remote computation example; existing skill workflows remain intact.
Source-derived claims retain links and verification qualifiers. The source catalog and test results now include the orientation example.

GEO extraction: the bundle supplies task-specific Unison guidance, executable verification, and a distinct Olki design mapping.
Those three attributes match the README and references. Plain Markdown makes them available without JavaScript rendering.
SPECULATIVE: the routing and tests may reduce API guessing. This is a single-model assessment, not measured productivity evidence.
