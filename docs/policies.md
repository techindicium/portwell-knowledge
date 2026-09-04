# Policies

The company's rules that reach this team, as written and circulated. Ownership sits with the
named person.

Nothing in this repository enforces any of them.

| ID | Policy | Owner | Status |
| :- | :- | :- | :- |
| `POLICY-02` | Published knowledge articles cite a source and name a reviewer. Articles without both are not eligible for retrieval. | Ana Fialho | current |
| `POLICY-03` | Customer data leaving the EU region requires a documented transfer basis. | Tomas Silva | current |
| `POLICY-04` | A knowledge article older than 180 days is re-verified before it is used to answer a ticket. | Ana Fialho | current |
| `POLICY-12` | A service review pack is delivered within five business days of month end. | Lucia Ferreira | current, contractual |
| `POLICY-13` | Every figure in a customer-facing pack names the metric definition and version it was computed from. | Sofia Marques | current |
| `POLICY-14` | A pack is reviewed by someone other than the person who assembled it before it is sent. | Lucia Ferreira | current |
| `POLICY-15` | A figure that cannot be sourced is omitted with a note, never estimated or carried forward. | Henrik Sole | draft |

## Where each one stands

| Policy | What would have to be true to enforce it | What exists today |
| :- | :- | :- |
| `POLICY-02` | The index build refusing an article missing source or reviewer | It publishes them. `ARTICLE-0131` is one. |
| `POLICY-04` | Article age measured against the 180 day line | Nothing measures article age |
| `POLICY-12` | A deadline anyone is reminded of | A date in a contract nobody on this team has open |
| `POLICY-13` | Figures carrying their definition and version out of the warehouse | Bare numbers arrive in a CSV |
| `POLICY-14` | Somewhere to record that a second person read a pack | Nowhere. See the 2026-08-14 interview. |
| `POLICY-15` | A convention for an unsourceable figure | The August narrative for `ACCOUNT-1008` quotes one anyway |

`POLICY-14` has been unenforceable since it was written, because there is no field anywhere that
records a review. The person it applies to had not heard of it.

## Rules that exist only as habit

- The pack is built from the most recent export in the shared folder. Which one that is depends
  on when somebody looks.
- Last month's file is the template. So a formatting mistake persists until someone notices.
- If a figure looks wrong, ask analytics to re-run rather than investigating it here.
