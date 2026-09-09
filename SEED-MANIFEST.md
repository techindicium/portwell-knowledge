# Seed manifest

**Delete this file before handover.** It describes what was placed in this repository and why,
which is teaching-team information. A group that reads it has been told where to look.

## What this repository is

The article index and the service review packs. Help articles with front matter, an index built from them, and a monthly pack per account assembled in a spreadsheet.

## What was placed here

| Path | What it is |
| :- | :- |
| `data/articles/` | Article bodies and their front matter |
| `data/article-index.json` | The handoff the portal answers from |
| `data/packs/` | The monthly service review packs |
| `data/figures/` | The numbers the packs quote |
| `data/sources/` | Where article content came from, where anyone recorded it |
| `docs/interviews/` | How the packs get made, in the manager's words |

## Where the data comes from

Every seeded fixture in the mock systems is generated from `course-shared/canon/data/` by
`course-shared/tools/seed_mocks.py`. The files in this repository are authored rather than
generated, but they are reconciled against the same canon: account identifiers, people, product
areas and policy numbers all resolve there.

Changing a value here without changing the canon puts this repository out of step with the four
mock systems. `seed_mocks.py --check` does not cover authored files, so nothing will tell you.

## What is deliberately wrong

One pack carries cached formula values that disagree with what the formulas would compute. Two articles answer the same question differently and one supersedes the other without saying so at the point of retrieval.

The full register is `course-shared/heldout/seeded-defects.md`, and the contradictions this
repository takes part in are in `course-shared/canon/conflicts.md`. Both are held out.

## Identifier ranges

This repository's reserved ranges are in `course-shared/canon/identifiers.md`. Identifiers
outside its own range are references to another track's material and must resolve.
