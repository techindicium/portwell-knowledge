# Seed manifest, KDLC track

**Status:** the shell is in place. The track ships the legacy starting condition only, with no
lifecycle, no controls, and no process verification, because building those is the four modules'
work. The track's domain material is not seeded yet. This file is the specification for that work.

**Audience:** teaching team. Delete this file before handing the repository to participants.

Follow `track-sdlc/` as the worked reference.

## What the track builds

An agentic knowledge-development system for capture, provenance, synthesis, review,
publication, freshness checks, and retirement. Its primary artifact is a sourced, reviewed,
published, and maintained knowledge artifact.

## Files to seed

| Path | Content | Notes |
| :- | :- | :- |
| `fixtures/articles/KB-01xx/*.md` | Twenty to thirty article files with front matter | The nine in `track-sdlc/fixtures/articles/article-index.json` must appear here with the same IDs, titles, areas, statuses, sources, reviewers, and bodies |
| `fixtures/sources/` | The raw material articles were written from: product docs, three meeting notes, two support threads | At least one article with no source in this directory at all |
| `fixtures/sources/meeting-notes/` | Notes that contradict a published article | The adjudication case |
| `project/index-build.py` | The script that produces the `article-index` handoff | This track owns that contract |
| `project/schema/article.schema.json` | Front-matter schema: id, title, area, status, source, reviewer, reviewed_at | Publishing without source and reviewer must be possible today, so `POL-02` has somewhere to be enforced later |
| `docs/policies.md` | `POL-02`, `POL-04`, `POL-03`, plus the review rule that is bypassed by reclassification | Copy verbatim from `course-shared/canon/company.md` |
| `docs/identifiers.md` | Owned: article. Consumed: account, policy, person, product area, ticket | Reserved range `KB-0400`+ |
| `docs/dependencies.md` | The `article-index` contract this track publishes, and who breaks when it slips | The SDLC track is the consumer |
| `docs/backlog.md` | Eight to twelve items, one of which does not apply here | |
| `docs/architecture-rules.md` | Append KDLC rules and the blast-radius table | High-radius: billing and integrations article changes |
| `legacy/tracker.csv` | What is in flight, with inconsistent statuses and missing owners | The Module 1 trace starts here |
| `legacy/incidents/` | `INC-01` and `INC-02` as this track saw them | Each traceable to a control that does not exist |

## Seeded problems, one per family

| Family | Seed | Why it survives a green suite |
| :- | :- | :- |
| Stale context | `KB-0117` still `published` with `superseded_by: KB-0142`, and `KB-0139` reviewed 237 days ago | The schema requires the fields, not their consistency |
| Missing provenance | `KB-0131` published with no `source` and no `reviewer` | `POL-02` exists only in prose |
| Specification gaming | An article reclassified from `billing` to `reporting` so it skips domain review | The review rule keys on the classification the author supplies |
| Weak routing | A billing article edit merged without the solution consultant's review | There is no review gate in the project |
| Recovery failure | Two sources contradicting each other, and the build loops without an adjudicator | The loop terminates on attempt count and publishes the last version tried |

The first two are already fixed by the SDLC track's copy of the index and must match exactly.

## Cross-track consistency

`track-sdlc/fixtures/articles/article-index.json` is a handoff this track produces. Its nine
articles, their statuses, their missing fields, and their bodies are already fixed. Seed this
track so that `project/index-build.py` run over `fixtures/articles/` reproduces that file
byte-for-byte in content, or update both together.

## Acceptance

- `make test` passes on a clean clone, or reports that the track has no tests yet.
- `project/index-build.py` produces an index that matches the SDLC track's copy.
- Every visible scenario names a real article and states what it detects.
- The five seeded problems are recorded in `course-shared/heldout/seeded-defects.md`.
