# Learn You Unison

This skill set helps coding agents inspect, write, test, and maintain Unison programs.
Start by asking your agent to read [the Unison entry skill](skills/unison/SKILL.md) and complete a concrete task.

For example: “Read `skills/unison/SKILL.md`, inspect my UCM project, and implement a tested pure function.”
The agent loads the relevant specialist, checks real signatures, and verifies the result through UCM.

## New to Unison? Start with Git

1. **[From Git files to Unison functions](docs/01-code-that-knows-its-own-name.md)** — build a TypeScript game, break an import, then load, run, and rename the same game in UCM.
2. **[From a saved function to a distributed program](docs/02-your-codebase-is-not-a-folder.md)** — branches and Share, remote runtimes, a map/reduce example, and the community.

Both guides follow one scoring example with diagrams, commands, and expected results. Start with basic TypeScript and Git knowledge; learn Unison as you go.

## Load the skills where your harness can find them

The canonical skills live under `skills/`. Each directory contains standard `SKILL.md` frontmatter and task instructions.
The repository's `.agents/skills/` links expose these same files to harnesses that support that discovery path.
`AGENTS.md` provides an explicit entrypoint for repository work.

For a different harness, add this instruction to its project rules: “For Unison tasks, read `skills/unison/SKILL.md`.”
Keep the bundle's `skills/`, `docs/`, `examples/`, `scripts/`, and `research/` paths together; references link across these directories.
Automatic discovery depends on the harness; this repository does not modify user-wide configuration.

## Choose the skill that matches the task

| Skill | Use it for |
|---|---|
| [unison](skills/unison/SKILL.md) | Orientation, choosing tools, and preserving project context |
| [unison-language](skills/unison-language/SKILL.md) | Functions, data types, syntax, and type errors |
| [unison-abilities](skills/unison-abilities/SKILL.md) | Effect interfaces, handlers, and continuations |
| [unison-ucm](skills/unison-ucm/SKILL.md) | MCP, scratch files, updates, branches, and recovery |
| [unison-libraries](skills/unison-libraries/SKILL.md) | Share discovery, dependency selection, upgrades, and publication |
| [unison-testing](skills/unison-testing/SKILL.md) | Pure tests, effectful tests, executable transcripts, and CI |
| [unison-services](skills/unison-services/SKILL.md) | HTTP, serialization, concurrency, runtime packaging, and Cloud |
| [unison-olki](skills/unison-olki/SKILL.md) | Mapping Olki's design to Unison without inventing guarantees |
| [unison-research](skills/unison-research/SKILL.md) | Checking releases, reading talks, and maintaining source evidence |

## Verify the examples on your machine

Use Python 3.9 or newer and UCM. These checks use disposable codebases and leave your working codebase alone.
The runner reports failures and retains output under `.validation/` for inspection.

```sh
python3 scripts/validate.py
python3 scripts/run_examples.py
```

For the Git-to-Unison walkthrough, install its TypeScript compiler locally and run the comparison check:

```sh
npm install --prefix .validation/typescript-check --no-audit --no-fund --ignore-scripts typescript@5.9.3
python3 scripts/check_orientation.py --tsc .validation/typescript-check/node_modules/.bin/tsc
```

This checks the broken/repaired TypeScript build, a local Git remote, and fresh-process UCM behavior.
It downloads base from Share. The optional [Cloud transcript](examples/checks/cloud-map-reduce.md) downloads a larger starter project and runs only its local handler.

To inspect your installed MCP contract, run this probe. It lists tools without calling definition-changing tools.

```sh
python3 scripts/probe_ucm.py --output .validation/ucm-mcp.json
```

## Read the evidence behind the guidance

Research date: **2026-09-06**. Local test baseline: **UCM release/1.4.0**, built 2026-08-19.
This baseline records what was installed; it is not a claim about the latest available release.

- [Source catalog](research/sources.md): primary documentation, Share, upstream agent guidance, talks, and access limitations.
- [Validation report](research/validation.md): checks executed and their limits.
- [Evaluation tasks](evals/scenarios.md): realistic prompts and observable success criteria for another harness.
- [Olki mapping](skills/unison-olki/references/design-map.md): requirements from the neighboring `olki-docs` directory.

The Olki documents were found at `~/tulving/olki-docs`; the requested underscore path did not exist.
The mapping records design requirements. It does not certify the separate Olki implementation.
