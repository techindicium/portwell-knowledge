# INCIDENT-04: a July pack went out with a first-cut figure

**Written:** 2026-08-24, by the service delivery manager.
**Severity:** a wrong figure reached an Enterprise account. Not disputed, and not corrected.

## What happened

The July pack for Nordkai Logistics was assembled on 3 August from the figures analytics sent
on 1 August. A batch of late July tickets landed after that cut. Analytics re-ran and sent
corrected figures on 6 August.

The pack was updated with the corrected inputs and sent. The percentages in it were not
recomputed, so the file went out with the corrected ticket counts and the first-cut
percentages.

Attainment was reported as 37.4 per cent. On the corrected figures it is 36.8 per cent.
Self-service was reported as 37.4 per cent. It is 38.9 per cent.

## How it was found

By accident, three weeks later, while checking something else.

## Why nobody saw it

The workbook holds a formula and the result the formula produced the last time anything
recalculated it. Opening the file shows the stored result. The formula and the stored result
disagreed, and nothing displays that disagreement.

The account did not query it. Both figures are plausible and the direction of travel is the
same either way.

## What would have caught it

Any of these, none of which exist:

- A check that every percentage in a pack agrees with its own formula.
- A record of which export each pack was built from, so a superseded export is visible.
- A figure that carries its source and version, which `POLICY-13` already requires.

## What was done

Nothing. The pack was not reissued, on the grounds that the difference is under two points and
reissuing draws attention to it.

That decision was made in a corridor and is recorded here only because this write-up exists.

## Open

Whether to reissue. Whether the same problem is in the other two July packs. Nobody has checked.
