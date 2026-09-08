# How the reporting work gets done today

Written by whoever was asked to write it, at some point, and not revised since. It is the only
written description of the process, and `docs/interviews/` contradicts parts of it.

> **A note for the reader.** This is not a specification. Where it disagrees with the
> interviews or with what is actually in `data/packs/`, the interviews and the files are the
> record and this is the aspiration.

## The monthly service review pack

Every Enterprise account is owed one within five business days of month end. Three accounts
qualify: `ACCOUNT-1001`, `ACCOUNT-1003` and `ACCOUNT-1008`.

1. The month closes.
2. Analytics sends the figures, usually as a CSV in the shared folder, sometimes pasted into a
   message. Nothing states which version of a metric definition produced them.
3. Last month's workbook is copied, renamed, and the input cells are typed over. The
   percentages recalculate.
4. The volumes tab is pasted in from a second file.
5. The narrative is written in a separate document. It says what moved and, where the author
   happens to know, why.
6. Both files go to the account.

Steps 2 and 5 are where the judgment is, and neither leaves a record.

## What is written down

| Thing | Where | Kept current? |
| :- | :- | :- |
| The packs that were sent | `data/packs/<month>/` | Yes, they are the artifact |
| The figures they were built from | `data/figures/` | Partly. Filenames carry the date; nothing inside does. |
| Which export a given pack used | Nowhere | No |
| Which metric version a figure came from | Nowhere | No |
| Who reviewed a pack before it went out | Nowhere | No |
| Why a number moved | In the narrative, when the author knew | No |
| The help articles | `data/articles/` | Partly. See `POLICY-04`. |

## The deadline

Five business days after month end, in the Enterprise contracts. Missed twice in the last year,
both times because a person was on leave. Nothing chased on either occasion.

A late pack is a contractual breach. A wrong pack is worse and is much harder to notice, which
is the trade-off the process does not currently make anyone confront.

## The judgment calls nobody wrote down

- Whether the figures received are current enough for the period being reported.
- Whether a number is fit to put in front of a paying customer.
- Whether a change in a figure is real or a change in how it was measured.
- Whether a pack needs a second reader. `POLICY-14` says always. Practice is: when it feels
  sensitive.
- What to write when the author does not know why something moved.

## The help articles

The same person maintains the customer-facing help articles. `project/index-build.py` produces
the `article-index` handoff that the help portal retrieves from.

There is no schedule for reviewing an article. `POLICY-04` asks for re-verification past 180 days
and nothing measures article age.

## What people say

> "I do not know a number is right. I know it is what Declan sent me."
> Lucia Ferreira, 2026-08-14.

> "A late pack announces itself. A wrong number sits in my model until somebody notices."
> Henrik Sole, 2026-08-21.
