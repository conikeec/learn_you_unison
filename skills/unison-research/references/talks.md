# Use talks to explain design, then verify current behavior

## DevTools.fm episode 45 has a publisher transcript

Source: [Rúnar Bjarnason — Unison](https://www.devtools.fm/episode/45).
Video: [publisher-linked recording](https://www.youtube.com/watch?v=zHTp9-LJSQA).
Retrieved 2026-09-06 from the publisher's public page payload; the plain web extractor returned no text.
The payload contains a `TRANSCRIPT` section. The transcript was read; audio was not independently checked.
Publication date was not confirmed during this pass.

The publisher lists chapter starts at **00:01:45** (what Unison is), **00:09:19** (UCM), and **00:29:55** (content addressability).
These are chapter markers, not precise timestamps for the following lessons.

Derived lessons:

- References identify particular definitions, which permits different dependency versions to coexist.
- Coexistence does not make incompatible type versions interchangeable; composition can still produce a type error.
- Abilities transfer control to a handler with a continuation that can resume the calling computation.

The interview also discusses future codebase manipulation and browser possibilities.
Treat those as historical remarks. Current UCM MCP already exposes codebase operations; inspect today's tools before repeating older limitations.

No full transcript is redistributed here. These notes paraphrase the retrieved publisher text.

## Strange Loop 2019 explains the content-addressing motivation

Source: [Paul Chiusano's conference page](https://thestrangeloop.com/2019/unison-a-new-distributed-programming-language.html).
Recording: [Unison: a new distributed programming language](https://www.youtube.com/watch?v=gCWtkvDQ2ZI).
Companion source: [the author's post](https://www.unison-lang.org/blog/heres-whats-been-happening-with-unison/), published 2019-10-16.

The author's post connects content addressing to rename behavior, cached tests, and distributed code movement.
Use it for rationale. It predates projects, modern Share releases, and the current update workflow.
The recording fetch failed during this research pass; no captions or transcript were retrieved for it.

## Unison Forall 2024 supplies further research leads

The [official conference page](https://www.unison-lang.org/unison-forall-2024/) advertises web development, distributed systems, and algebraic effects.
It dates the event to 2024-09-20. No individual talk transcript was verified in this pass.
The [2024 recap](https://www.unison-lang.org/wrapped2024/) links the conference recordings.
Use these links to find a talk on a specific gap; do not treat the event description as evidence about a library API.

## Keep transcript provenance next to each new lesson

Record the publisher, speaker, URL, date, text acquisition method, available timestamp, and current verification.
When captions misrender code, retrieve the speaker's source or reproduce a minimal example through UCM.
A useful addition changes an agent's decision and points to evidence; a catalog of unviewed videos does neither.
