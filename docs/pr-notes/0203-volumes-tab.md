# Change note 0203: add a volumes tab to the pack template

**Changed:** 2026-05-19. **Author:** Lucia Ferreira. **Reviewer:** none.

## What changed

The pack template gained a third sheet breaking tickets down by product area, with a total row.

## Why

Two accounts asked where their volume was coming from and the pack could not answer.

## How it was done

Added by hand to the template workbook, then each account's next pack was started from the new
template rather than from last month's file.

## Notes

The total row is a `SUM` formula. Every other number on the sheet is pasted in from the volumes
export.

There is no check that the pasted areas match the eight the product uses, so a renamed area
would appear as a new row and the total would still add up.
