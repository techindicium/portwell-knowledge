# Seed manifest, portwell-knowledge (Reporting, KDLC track)

**Status:** the template is in place. The team's own material is not seeded yet. This file is
the specification for that work.

**Audience:** teaching team. Delete this file before handing the repository over.

Follow `portwell-assist/` as the worked reference. Nothing seeded here may mention the course;
`course-shared/scripts/check-course-blind.py` enforces it.

## The business process this team runs

**The monthly service review pack.** Every Enterprise account is contractually owed one within
five business days of month end (`POL-12`). Three accounts qualify: `ACC-1001` Nordkai
Logistics, `ACC-1003` Halden Cold Chain, and `ACC-1008` Sunder Retail Supply.

A pack contains, for the month just closed:

- SLA attainment against the account's tier commitments, first response and resolution.
- Ticket volume by product area, against the prior month.
- Deflection rate, where Assist was active on the account.
- Open escalations and their age.
- A short written summary from the service delivery manager.

The figures come from the analytics warehouse. The pack is assembled in a spreadsheet, the
narrative is written in a document, and both go to the account.

The team also maintains the customer-facing help articles. At this size one person does both,
and that is why the two sit in one repository.

## Why this is the fixture

It is the clearest business process in the company: a hard cadence, a contractual deadline, a
named owner, a customer on the other end, and figures that come from someone else's system. A
wrong figure in a pack is worse than a late pack, which gives a group a real trade-off to
model rather than a synthetic one.

## What an agentic system would do here

Assemble the pack: pull each figure with its lineage, compare against last month, draft the
narrative, flag what moved and why, and prepare it for review. What it must not do is decide
whether a figure is fit to send to a paying customer.

## Files to seed

| Path | Content | Notes |
| :- | :- | :- |
| `data/packs/2026-07/ACC-1001.xlsx` | Last month's delivered pack, three sheets: figures, volumes, escalations | Contains formulas and cached values. See the seeded problems. |
| `data/packs/2026-07/ACC-1003.xlsx` | As above | |
| `data/packs/2026-07/ACC-1008.xlsx` | As above | |
| `data/packs/2026-07/*.docx` | The narrative that accompanied each pack | One references a figure that is not in its own spreadsheet |
| `data/packs/2026-08/` | The month currently being assembled, incomplete | This is the live work |
| `data/packs/pack-template.xlsx` | The template everyone copies | Its formulas are the origin of one seeded problem |
| `data/warehouse-extract-2026-08.csv` | The figures pulled from analytics, by hand, on a date | The extract date is in the filename and nowhere else |
| `data/articles/KB-01xx/*.md` | Twenty to thirty help articles with front matter | The nine already in `portwell-assist/data/articles/article-index.json` must appear with identical IDs, statuses, sources, reviewers and bodies |
| `data/sources/` | Product docs and meeting notes the articles were written from | At least one article with no source here at all |
| `project/index-build.py` | Produces the `article-index` handoff | This team owns that contract |
| `project/schema/article.schema.json` | Front matter: id, title, area, status, source, reviewer, reviewed_at | Publishing without source and reviewer must remain possible |
| `docs/how-we-work-today.md` | The pack process as practised, including the parts nobody wrote down | Who reviews, and what happens when a figure looks wrong |
| `docs/policies.md` | `POL-12` to `POL-15`, plus `POL-02`, `POL-04`, `POL-03` | Verbatim from canon |
| `docs/identifiers.md` | Owned: article, pack. Consumed: account, metric, ticket, policy | Reserved ranges `KB-0400`+, `PACK-`+ |
| `docs/dependencies.md` | The metric definitions consumed from analytics, the `article-index` published to Assist engineering | The third column is where the gaps live |
| `docs/backlog.md` | Eight to twelve items, one of which does not apply here | |
| `docs/incidents/` | `INC-01` and `INC-02` as this team saw them, plus one pack incident | The pack incident is this team's own |
| `docs/pr-notes/` | Two change notes, of the many never written | |
| `data/tracker.csv` | What is in flight, inconsistent statuses, missing owners | |

## Seeded problems

Six, one per family plus one for the pack specifically.

| Family | Seed | Why it survives |
| :- | :- | :- |
| Stale context | `ACC-1003`'s July pack quotes a resolution figure computed under `POL-10`, superseded on 2026-07-01 by `POL-11` | Nothing checks a policy citation against the policy's status |
| Missing provenance | `KB-0131` published with no `source` and no `reviewer` | `POL-02` exists only in prose |
| Missing provenance | A figure in `ACC-1008`'s pack appears in no warehouse extract and nobody can say where it came from | `POL-13` exists only in prose |
| Specification gaming | An article reclassified from `billing` to `reporting` so it skips domain review | The review rule keys on the classification the author supplies |
| Weak routing | A billing article edit merged without the solution consultant's review | There is no review gate |
| Recovery failure | Two sources contradict; the build loops and publishes the last version tried | The loop terminates on attempt count, not on resolution |

### The pack defect, which is the one worth getting right

`pack-template.xlsx` computes deflection as a formula. `ACC-1001`'s July pack was last saved by
a person, so it carries **cached values** alongside its formulas, and the cached deflection
figure is from June. The formula is correct. The number that was sent is not.

This is invisible in a diff, invisible on a casual read, and only visible to a reader that
decides between the formula and the cached value. That decision is a provenance decision, not a
parsing one, and it is exactly what a Module 2 tool has to get right.

## Cross-team consistency

`portwell-assist/data/articles/article-index.json` is a handoff this team produces. Its nine
articles are already fixed. Seed so that `project/index-build.py` reproduces that file's content,
or update both together.

Pack figures must reconcile with the analytics warehouse for the same month on the ten canon
accounts.

## Acceptance

- `make test` passes on a clean clone, or reports that there are no tests yet.
- `check-course-blind.py` reports clean.
- `project/index-build.py` reproduces the index Assist engineering already has.
- The six seeded problems are recorded in `course-shared/heldout/seeded-defects.md`.
