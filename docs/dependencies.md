# Dependencies

What this team consumes, what it publishes, and what it verifies about either.

## Consumed

| From | What | How it arrives | What this team verifies |
| :- | :- | :- | :- |
| Analytics | Monthly figures per account | A CSV in a shared folder, or numbers pasted into a message | That the accounts are the expected three. Nothing about the period, the extract date, or the metric version. |
| Analytics | Ticket volumes by area | A second CSV | Nothing |
| Support | Open escalations and their ages | Verbally, or from the desk | Nothing |

The figures carry no metric version. `POLICY-13` requires the pack to state one, so the pack states
something the source never supplied.

There is no record of which export a given pack was built from. `data/figures/` holds three
exports for two months and the filenames are the only clue.

## Published

| To | What | Contract | What breaks when it slips |
| :- | :- | :- | :- |
| Enterprise accounts | The service review pack | Five business days after month end, contractual | A contractual breach, or a wrong figure in front of a customer |
| Finance | The same pack, read for three cells | None | The renewal model silently takes the wrong cells |
| Portal engineering | `article-index.json` | Article identifiers, status, source, reviewer | The service retrieves articles it should not, or misses ones it should |

## The article index

`project/index-build.py` reads `data/articles/` and writes the index the help portal
consumes. The build does not check `POLICY-02`, so an article with no source and no reviewer is
published into the index and retrieved.

Nothing on either side verifies the index against the schema after it is written.

## What nobody owns

The gap both interviews independently identified: a figure that carries its definition and
version from the warehouse through to the pack. Analytics does not attach it, this team does
not request it, and `POLICY-13` says it must be there.
