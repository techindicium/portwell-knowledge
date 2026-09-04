# Data

What this team works with.

| Path | Is |
| :- | :- |
| `packs/2026-07/` | The July packs, all three sent |
| `packs/2026-08/` | August. One pack in progress, two not started. |
| `figures/` | What analytics sent. The date is in the filename and nowhere inside. |
| `articles/` | The help articles, one file each, front matter plus body |
| `article-index.json` | Generated from `articles/` by `project/index-build.py`. Read by the support assistant. |
| `tracker.csv` | What is in flight |

## The figures

Three exports for two months. `warehouse-export-2026-08-01.csv` is the first cut of July;
`warehouse-export-2026-08-06.csv` is July again after a late batch of tickets landed. Nothing
records which export a given pack was built from.

## The packs

Each is a workbook and a document. The workbook holds the figures, the volumes and the open
escalations. The document holds the narrative.

The workbook carries formulas for the percentages and stored results from whenever it last
recalculated. Those two can disagree. `docs/incidents/INCIDENT-04.md` is what happened when they did.

## Reading a workbook

A reader that wants the stored number and a reader that wants the formula are asking different
questions, and in at least one file here they get different answers.
