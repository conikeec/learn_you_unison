# Sources and verification boundaries

Research date: 2026-09-06. The catalog records inspected sources, access limits, and the skills they support.
Use the installed UCM contract and package definitions to resolve operational differences.
The local baseline is UCM release/1.4.0, built 2026-08-19.

## Primary sources support the operational guidance

| ID | Source | Evidence status | Used by |
|---|---|---|---|
| home | [Unison language homepage](https://www.unison-lang.org/) | read | unison |
| docs | [Official documentation index](https://www.unison-lang.org/docs/) | read | unison-language, unison-research |
| overview | [Unison 1.0 overview](https://www.unison-lang.org/unison-1-0/) | read | unison, unison-services |
| community | [Official community guide](https://www.unison-lang.org/community/) | read | unison-research, unison-libraries |
| mcp | [UCM MCP setup](https://www.unison-lang.org/docs/usage-topics/mcp-setup/) | read; cross-checked against installed schemas | unison-ucm |
| commands | [UCM command reference](https://www.unison-lang.org/docs/ucm-commands/) | read; selected commands executed | unison-ucm, unison-libraries |
| tour | [A tour of Unison](https://www.unison-lang.org/docs/tour/) | read | unison |
| delay | [Delayed computations](https://www.unison-lang.org/docs/fundamentals/values-and-functions/delayed-computations/) | read; example executed | unison-language |
| types | [Unique and structural types](https://www.unison-lang.org/docs/fundamentals/data-types/unique-and-structural-types/) | read | unison-language |
| records | [Record types](https://www.unison-lang.org/docs/fundamentals/data-types/record-types/) | read | unison-language |
| ability-model | [Abilities mental model](https://www.unison-lang.org/docs/fundamentals/abilities/) | read | unison-abilities |
| ability-writing | [Writing abilities](https://www.unison-lang.org/docs/fundamentals/abilities/writing-abilities/) | read; original handler example executed | unison-abilities |
| ability-handler | [Language reference: handlers](https://www.unison-lang.org/docs/language-reference/ability-handlers/) | read | unison-abilities |
| ability-faq | [Ability FAQs](https://www.unison-lang.org/docs/fundamentals/abilities/faqs/) | read | unison-abilities |
| language-faq | [General language FAQs](https://www.unison-lang.org/docs/usage-topics/general-faqs/) | read | unison-language |
| updates | [Updating code and dependencies](https://www.unison-lang.org/docs/usage-topics/workflow-how-tos/update-code/) | read; compatible update example executed | unison-ucm, unison-libraries |
| projects | [Project workflows](https://www.unison-lang.org/docs/tooling/project-workflows/) | read | unison-ucm, unison-libraries |
| tests | [Testing guide](https://www.unison-lang.org/docs/usage-topics/testing/) | read; pure tests executed | unison-testing |
| transcripts | [Executable UCM transcripts](https://www.unison-lang.org/docs/tooling/transcripts/) | read; three transcripts executed | unison-testing |
| documentation | [Documenting Unison code](https://www.unison-lang.org/docs/usage-topics/documentation/) | read | unison-libraries |
| running | [Running programs](https://www.unison-lang.org/docs/usage-topics/running-programs/) | read | unison-services |
| release | [UCM release 1.4.0](https://github.com/unisonweb/unison/releases/tag/release%2F1.4.0) | read; local version confirmed | unison-ucm, unison-testing, unison-research |
| upstream-agent | [Upstream agent instructions](https://github.com/unisoncomputing/unison-llm-support/blob/main/instructions.md) | read; workflow source, not adopted as policy | unison, unison-ucm |
| upstream-language | [Upstream language guide](https://raw.githubusercontent.com/unisoncomputing/unison-llm-support/main/unison-language-guide.md) | introductory sections inspected | unison-language, unison-research |
| cloud-http | [Cloud HTTP learning module](https://www.unison.cloud/learn/http-hello-world/) | read; no deployment executed | unison-services |
| cloud-native | [Native service calls](https://www.unison.cloud/learn/native-services/) | read; no deployment executed | unison-services |
| roadmap | [Unison roadmap](https://www.unison-lang.org/roadmap/) | read; intent only, may lag releases | unison-research |
| share | [Unison Share](https://share.unison-lang.org/) | web shell only; selected projects read using MCP | unison-libraries |
| base | [Base library](https://share.unison-lang.org/@unison/base) | README and latestRelease retrieved through UCM MCP; not executed | unison-libraries, unison-services |
| http | [HTTP library](https://share.unison-lang.org/@unison/http) | README and latestRelease retrieved through UCM MCP; not executed | unison-libraries, unison-services |
| json | [JSON library](https://share.unison-lang.org/@unison/json) | README and latestRelease retrieved through UCM MCP; not executed | unison-libraries, unison-services |
| cloud | [Cloud client library](https://share.unison-lang.org/@unison/cloud) | README and latestRelease retrieved through UCM MCP; not executed | unison-libraries, unison-services |
| devtools | [DevTools.fm episode 45, Runar Bjarnason](https://www.devtools.fm/episode/45) | publisher transcript read from public HTML payload; audio not checked | unison-research, unison-abilities, unison-libraries |
| strangeloop | [Strange Loop 2019 conference talk](https://thestrangeloop.com/2019/unison-a-new-distributed-programming-language.html) | conference description located; recording fetch failed; no transcript | unison-research |
| talk-writeup | [Author companion post for Strange Loop](https://www.unison-lang.org/blog/heres-whats-been-happening-with-unison/) | read; historical 2019-10-16 | unison-research |
| forall | [Unison Forall 2024](https://www.unison-lang.org/unison-forall-2024/) | event page read; individual transcripts not retrieved | unison-research |
| wrapped | [Unison 2024 recap](https://www.unison-lang.org/wrapped2024/) | read; recording discovery lead | unison-research |

## Local evidence strengthens the documentation

- [MCP contract](ucm-1.4.0-mcp.json): 29 tools returned by a disposable UCM process.
- [Share observations](share-observations.json): retrieved release metadata and README fingerprints for four projects.
- [Executable examples](../examples/fundamentals.md): original code checked against the installed runtime.
- [Talk notes](../skills/unison-research/references/talks.md): derived lessons and exact transcript access status.

The Share README tool does not pin a release. Its response and a project's latest-release metadata are separate observations.
No Cloud deployment, external service mutation, or library compatibility matrix was tested.

## Olki supplies requirements, not Unison language facts

The requested `~/tulving/olki_docs` path was absent. The local source was `~/tulving/olki-docs`.
The mapping uses its README and sections 02, 03, 04, 07, 08, 09, 10, 21, 22, 23, and 24.
See [local document fingerprints](olki-sources.json) for the exact files and review scope.
The independent mapping lives in [the Olki reference](../skills/unison-olki/references/design-map.md).

## Maintain a dated claim instead of a copied manual

Retain concise paraphrases and source links. Do not vendor third-party transcripts or whole language manuals.
Refresh an affected reference when UCM schemas, package releases, or observed behavior change.
A roadmap is evidence of intent; local schemas, release notes, and executed examples establish narrower operational facts.

Upstream agent instructions informed signature inspection and incremental typechecking.
Their repeated user-confirmation rules were not adopted: these skills preserve the harness's existing authorization and the user's task scope.
