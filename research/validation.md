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

All seven orientation diagrams passed the Mermaid 11 parser. Their rendered layout has not been visually checked.

## Research has explicit limits

The DevTools.fm publisher transcript was retrieved and read. Audio was not independently verified.
The Strange Loop recording fetch failed, and individual Forall talk transcripts were not retrieved.
Historical lessons use the sources identified in [the talk notes](../skills/unison-research/references/talks.md).

No Cloud deployment, HTTP integration execution, FFI call, dependency upgrade, or unique-type migration was executed.
The Olki mapping reflects design documents and identifies implementation responsibilities; it is not an audit of the neighboring implementation.
Multi-harness behavioral evaluation remains unrun. [Fourteen scenarios](../evals/scenarios.md) define observable criteria for that work.

## Editorial review preserves the technical distinctions

Desk route: row 4, documentation. The two orientation guides use explanation form for readers familiar with Git.
Skill workflows use how-to form; detailed mechanics and source records use reference form.
The README's target questions are how to orient a coding agent and how to verify Unison work.
The bundle uses its own Unison/Olki scope; Modiqo/Rote marketing claims do not apply.

The deterministic lint output, warning dispositions, and skim extracts are recorded in [the editorial review](editorial-review.json).
Skim verdict: pass. The entrypoints state the next operation and verification evidence before conditional detail.
Conservation: the orientation guides and their transcript are new; existing README and skill guidance retain their facts and gain navigation links.
Source-derived claims retain links and verification qualifiers. The source catalog and test results now include the orientation example.

GEO extraction: the bundle supplies task-specific Unison guidance, executable verification, and a distinct Olki design mapping.
Those three attributes match the README and references. Plain Markdown makes them available without JavaScript rendering.
SPECULATIVE: the routing and tests may reduce API guessing. This is a single-model assessment, not measured productivity evidence.
