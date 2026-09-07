# Take a reproducible question to the right source

The [official community guide](https://www.unison-lang.org/community/) links Discord, compiler development, and library contribution paths.
Inspect current destinations before preparing a report; channel names and maintainers can change.

| Problem | First evidence | Relevant destination |
|---|---|---|
| Parse, typecheck, runtime, or UCM defect | Minimal transcript, UCM version, expected and actual result | [unisonweb/unison](https://github.com/unisonweb/unison) issues |
| Library-specific behavior | Exact release, definition, and reproduction | The project's Share tickets or maintainer channel |
| Language usage question | Small typechecked example and unresolved question | Official Discord linked from the community page |
| Documentation mismatch | Exact page, installed version, and corrected observation | Documentation contribution path linked from the official site |
| Cloud operational problem | Service reference, environment, sanitized logs | Cloud support or the relevant documented channel |

Prepare enough context that another programmer can reproduce the result without your local codebase.
Include installed dependency releases; remove credentials and unrelated application data.
For codebase corruption or migration problems, preserve diagnostics and a consistent backup before attempting repair.

Drafting a report is local work. Submit or message others only when the user has authorized that action.
When a maintainer clarifies behavior, record the source and update a focused reference or regression example.
