# Evaluate observable agent behavior

These scenarios are evaluation prompts, not claims that multiple harnesses have passed them.
Give a fresh agent the relevant skill path and fixture. Use a disposable codebase for mutations.
The evaluator should inspect tool calls, diagnostics, stored definitions, and test output.

| Scenario | Prompt and fixture | Observable pass condition |
|---|---|---|
| 1. Find the real project | “Inspect this Unison project before editing it.” Give a scratch directory and a UCM codebase with different names. | Records codebase/project/branch; does not infer the UCM target from cwd. |
| 2. Implement a pure function | “Write a bounded increment and test its boundary.” Supply builtins or a pinned base. | Inspects available operators; typechecks and passes meaningful boundary tests. |
| 3. Force the right computation | “Fix a function/value mismatch in `!(f x)`.” Supply a delayed-return signature. | Explains and fixes the delay/application boundary; checks the resulting value. |
| 4. Repair an ability handler | “Make this handler support two requests.” Supply the ability example with handler reinstallation removed. | Handles normal completion and repeated requests; test fails before the repair and passes afterward. |
| 5. Preserve type identity | “Add a field to this existing unique type.” Supply a stored type and dependent definitions. | Retrieves the declaration from UCM, preserves identity annotations, and repairs actual dependents. |
| 6. Distinguish typecheck from save | “Save this definition.” Expose both typecheck and update tools. | Uses persistence, then retrieves the stored result; does not claim success after only typechecking. |
| 7. Discover a package | “Find a JSON decoder with useful failures.” Expose Share tools and an existing unrelated JSON library. | Compares real signatures and errors; records a release/alias and typechecks a minimal call. |
| 8. Diagnose a wrong MCP target | “My function is missing after a successful update.” Set two codebases. | Checks context before overwriting names or reinstalling libraries. |
| 9. Reproduce an update | “Prove that this dependency update changes the caller.” Use the update example. | Executes an isolated transcript and tests the stored dependent's behavior. |
| 10. Reject a false guarantee | “Does `{Http}` enforce my grant for one host?” | Separates an ability interface from Olki's scope checker and runtime enforcement. |
| 11. Validate an external boundary | “Handle an HTTP 500 and malformed JSON.” Use fake responses. | Tests status handling and decoding separately; does not infer success from a returned response. |
| 12. Reconcile an old talk | “This interview says codebase APIs are future work. Can my agent inspect code?” | Labels the historical remark and checks the installed MCP contract. |
| 13. Package an executable | “Give me a standalone command from this program.” | Distinguishes `.uc` plus runtime from native output and tests the selected entrypoint. |
| 14. Resume an Olki hole | “Design the `via self` answer path.” Supply sections 08 and 10. | Includes schema validation, correlation, duplicate/stale answers, and journal state; labels unimplemented parts. |

Record a pass only when all conditions hold. Mark missing tool or account prerequisites as blocked, not passed.
Track attempted API guesses, typecheck/repair turns, inspected definitions, and completion time to compare harness behavior.
These are proposed measurements; this repository makes no measured productivity claim.

For a comparative run, use the same version, dependencies, prompt, fixture, and time allowance with and without these skills.
Keep evaluator expectations separate from the tested agent's prompt.
